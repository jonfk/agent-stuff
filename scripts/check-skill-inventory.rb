#!/usr/bin/env ruby
# frozen_string_literal: true

require "pathname"
require "yaml"

ROOT = Pathname.new(__dir__).join("..").expand_path
README = ROOT.join("README.md")
GROUPS = {
  "Shared skill inventory" => ROOT.join("skills", "*", "SKILL.md"),
  "Opt-in skill packs" => ROOT.join("skill-packs", "*", "*", "SKILL.md")
}.freeze

errors = []
readme = README.read
frontmatter_by_directory = {}

manifests_by_directory = GROUPS.values.flat_map { |pattern| Dir.glob(pattern.to_s) }
  .sort
  .to_h do |manifest_path|
    manifest = Pathname.new(manifest_path)
    directory = manifest.dirname.relative_path_from(ROOT).to_s
    text = manifest.read
    match = text.match(/\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\z)/m)

    unless match
      errors << "#{manifest.relative_path_from(ROOT)}: missing YAML frontmatter"
      next [directory, nil]
    end

    begin
      frontmatter = YAML.safe_load(
        match[1], permitted_classes: [], permitted_symbols: [], aliases: false
      )
      unless frontmatter.is_a?(Hash)
        errors << "#{manifest.relative_path_from(ROOT)}: frontmatter must be a mapping"
        next [directory, nil]
      end

      name = frontmatter["name"]
      errors << "#{manifest.relative_path_from(ROOT)}: frontmatter name must be a non-empty string" unless name.is_a?(String) && !name.empty?
      frontmatter_by_directory[directory] = frontmatter
      [directory, name]
    rescue Psych::Exception => error
      errors << "#{manifest.relative_path_from(ROOT)}: invalid YAML frontmatter (#{error.message.lines.first.strip})"
      [directory, nil]
    end
  end

Dir.glob(GROUPS.fetch("Shared skill inventory").to_s).sort.each do |manifest_path|
  manifest = Pathname.new(manifest_path)
  directory = manifest.dirname.relative_path_from(ROOT).to_s
  frontmatter = frontmatter_by_directory[directory]
  next unless frontmatter

  claude_manual_only = frontmatter["disable-model-invocation"] == true
  openai_manifest = manifest.dirname.join("agents", "openai.yaml")
  codex_manual_only = false

  if openai_manifest.file?
    begin
      openai_config = YAML.safe_load(
        openai_manifest.read, permitted_classes: [], permitted_symbols: [], aliases: false
      )
      unless openai_config.is_a?(Hash)
        errors << "#{openai_manifest.relative_path_from(ROOT)}: configuration must be a mapping"
        next
      end
      codex_manual_only = openai_config.dig("policy", "allow_implicit_invocation") == false
    rescue Psych::Exception => error
      errors << "#{openai_manifest.relative_path_from(ROOT)}: invalid YAML (#{error.message.lines.first.strip})"
      next
    end
  end

  next if claude_manual_only == codex_manual_only

  errors << "#{directory}: manual-only invocation must set both " \
            "SKILL.md disable-model-invocation: true and " \
            "agents/openai.yaml policy.allow_implicit_invocation: false"
end

documented_by_directory = {}

GROUPS.each do |heading, pattern|
  heading_line = readme.lines.index { |line| line.chomp == "### #{heading}" }
  unless heading_line
    errors << "README.md: missing #{heading.inspect} section"
    next
  end

  section_lines = readme.lines[(heading_line + 1)..]
  section_lines = section_lines.take_while { |line| !line.start_with?("### ") }
  entries = section_lines.each_with_index.map do |line, offset|
    match = line.match(/^\|\s*\[`([^`]+)`\]\(([^)]+)\)\s*\|/)
    [match[1], match[2], heading_line + offset + 2] if match
  end.compact

  expected_directories = Dir.glob(pattern.to_s).sort.map do |manifest_path|
    Pathname.new(manifest_path).dirname.relative_path_from(ROOT).to_s
  end
  documented_directories = entries.map { |_, directory, _| directory }

  (expected_directories - documented_directories).each do |directory|
    errors << "README.md: #{heading} does not document #{directory}"
  end
  (documented_directories - expected_directories).each do |directory|
    errors << "README.md: #{heading} links missing skill #{directory}"
  end

  entries.each do |documented_name, directory, line_number|
    if documented_by_directory.key?(directory)
      errors << "README.md:#{line_number}: duplicate inventory link for #{directory}"
    else
      documented_by_directory[directory] = documented_name
    end

    manifest_name = manifests_by_directory[directory]
    next unless manifest_name && documented_name != manifest_name

    errors << "README.md:#{line_number}: documents #{documented_name.inspect}, but #{directory}/SKILL.md is named #{manifest_name.inspect}"
  end
end

shared_count = Dir.glob(GROUPS.fetch("Shared skill inventory").to_s).length
pack_count = Dir.glob(GROUPS.fetch("Opt-in skill packs").to_s).length
count_match = readme.match(/contains (\d+) tracked skills: (\d+) broadly useful skills.*?and (\d+) opt-in fiction skills/m)

if count_match
  documented_counts = count_match.captures.map(&:to_i)
  actual_counts = [shared_count + pack_count, shared_count, pack_count]
  if documented_counts != actual_counts
    errors << "README.md: documents skill totals #{documented_counts.join("/")}, expected #{actual_counts.join("/")}"
  end
else
  errors << "README.md: missing tracked/shared/fiction skill totals"
end

if errors.empty?
  puts "Skill inventory is current: #{shared_count + pack_count} skills (#{shared_count} shared, #{pack_count} opt-in)."
else
  warn errors.map { |error| "- #{error}" }.join("\n")
  exit 1
end
