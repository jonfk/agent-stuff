import { loadConfigOrDefault } from "@richardgill/pi-config";
import { DEFAULT_OPTIONS, type PresetOptions, preset } from "@richardgill/pi-preset";
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { z } from "zod";

const ThinkingLevelSchema = z.enum(["off", "minimal", "low", "medium", "high", "xhigh"]);

const PresetSchema = z.object({
  provider: z.string().optional(),
  model: z.string().optional(),
  thinkingLevel: ThinkingLevelSchema.optional(),
  tools: z.array(z.string()).optional(),
  instructions: z.string().optional(),
});

const ConfigSchema = z.object({
  presets: z.record(z.string(), PresetSchema).optional(),
  commandName: z.string().optional(),
  flagName: z.string().optional(),
  cycleShortcut: z.union([z.string(), z.literal(false)]).optional(),
  defaultTools: z.array(z.string()).optional(),
  persistState: z.boolean().optional(),
});

const ProjectConfigSchema = z.object({
  presets: z.record(z.string(), PresetSchema).optional(),
}).strict();

const stripJsoncComments = (input: string): string => {
  let output = "";
  let inString = false;
  let escaped = false;

  for (let index = 0; index < input.length; index += 1) {
    const char = input[index];
    const next = input[index + 1];

    if (inString) {
      output += char;
      if (escaped) {
        escaped = false;
      } else if (char === "\\") {
        escaped = true;
      } else if (char === '"') {
        inString = false;
      }
      continue;
    }

    if (char === '"') {
      inString = true;
      output += char;
      continue;
    }

    if (char === "/" && next === "/") {
      while (index < input.length && input[index] !== "\n") index += 1;
      output += "\n";
      continue;
    }

    if (char === "/" && next === "*") {
      index += 2;
      while (index < input.length && !(input[index] === "*" && input[index + 1] === "/")) {
        output += input[index] === "\n" ? "\n" : " ";
        index += 1;
      }
      index += 1;
      continue;
    }

    output += char;
  }

  return output;
};

const stripJsoncTrailingCommas = (input: string): string => {
  let output = "";
  let inString = false;
  let escaped = false;

  for (let index = 0; index < input.length; index += 1) {
    const char = input[index];

    if (inString) {
      output += char;
      if (escaped) {
        escaped = false;
      } else if (char === "\\") {
        escaped = true;
      } else if (char === '"') {
        inString = false;
      }
      continue;
    }

    if (char === '"') {
      inString = true;
      output += char;
      continue;
    }

    if (char === ",") {
      let nextIndex = index + 1;
      while (/\s/.test(input[nextIndex] ?? "")) nextIndex += 1;
      if (input[nextIndex] === "}" || input[nextIndex] === "]") continue;
    }

    output += char;
  }

  return output;
};

const parseJsonc = (input: string): unknown =>
  JSON.parse(stripJsoncTrailingCommas(stripJsoncComments(input)));

const parseProjectConfig = (path: string): Pick<PresetOptions, "presets"> => {
  try {
    const content = readFileSync(path, "utf8");
    return ProjectConfigSchema.parse(parseJsonc(content));
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    throw new Error(`Invalid project preset config at ${path}: ${message}`);
  }
};

const loadProjectConfig = (): Pick<PresetOptions, "presets"> => {
  const path = join(process.cwd(), ".pi", "preset.jsonc");
  if (!existsSync(path)) return {};
  return parseProjectConfig(path);
};

const mergeConfig = (
  globalConfig: PresetOptions,
  projectConfig: Pick<PresetOptions, "presets">,
): PresetOptions => ({
  ...globalConfig,
  presets: {
    ...globalConfig.presets,
    ...projectConfig.presets,
  },
});

const globalConfig = loadConfigOrDefault({
  filename: "preset.jsonc",
  schema: ConfigSchema,
  defaults: DEFAULT_OPTIONS,
});

const config = mergeConfig(globalConfig as PresetOptions, loadProjectConfig());

export default preset(config as PresetOptions);
