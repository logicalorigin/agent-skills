---
name: codex-startup-config
description: "Ensure Codex startup config enables sandbox workspace write network access and web search request. Use when a user asks to set or enforce startup config for sandbox workspace write, network access, or web search request."
---

# Codex Startup Config

- Run `scripts/ensure_startup_config.sh` to update the Codex config idempotently.
- The script ensures these settings exist and are set to true in `~/.codex/config.toml`:
  - `[sandbox_workspace_write] network_access = true`
  - `[features] web_search_request = true`
- After applying changes, tell the user to restart Codex so the settings load on startup.
- If the config lives elsewhere, set `CODEX_CONFIG_PATH` before running the script.

## Command

```bash
bash scripts/ensure_startup_config.sh
```
