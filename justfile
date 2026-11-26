# List the recipes
default:
    @just --list

# Link this host's skills into ~/.claude/skills and ~/.agents/skills (pass --dry-run, --check, --host NAME, ...)
link-skills *args:
    scripts/link_skills.py {{args}}
