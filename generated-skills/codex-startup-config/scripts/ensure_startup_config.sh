#!/usr/bin/env bash
set -euo pipefail

config_path="${CODEX_CONFIG_PATH:-$HOME/.codex/config.toml}"
config_dir="$(dirname "$config_path")"

mkdir -p "$config_dir"
touch "$config_path"

tmp_file="$(mktemp)"

awk '
function current_section(line, sec) {
  sec = line
  sub(/^[ \t]*\[/, "", sec)
  sub(/\][ \t]*$/, "", sec)
  gsub(/[ \t]/, "", sec)
  return sec
}
function emit_missing_key() {
  if (section == "sandbox_workspace_write" && !sandbox_key) {
    print "network_access = true"
    sandbox_key = 1
  }
  if (section == "features" && !features_key) {
    print "web_search_request = true"
    features_key = 1
  }
}
BEGIN {
  section = ""
  sandbox_section = 0
  sandbox_key = 0
  features_section = 0
  features_key = 0
}
{
  if ($0 ~ /^[ \t]*\[[^\]]+\][ \t]*$/) {
    emit_missing_key()
    section = current_section($0)
    if (section == "sandbox_workspace_write") sandbox_section = 1
    if (section == "features") features_section = 1
    print $0
    next
  }
  if (section == "sandbox_workspace_write" && $0 ~ /^[ \t]*network_access[ \t]*=/) {
    print "network_access = true"
    sandbox_key = 1
    next
  }
  if (section == "features" && $0 ~ /^[ \t]*web_search_request[ \t]*=/) {
    print "web_search_request = true"
    features_key = 1
    next
  }
  print $0
}
END {
  emit_missing_key()
  if (!sandbox_section) {
    print ""
    print "[sandbox_workspace_write]"
    print "network_access = true"
  }
  if (!features_section) {
    print ""
    print "[features]"
    print "web_search_request = true"
  }
}
' "$config_path" > "$tmp_file"

mv "$tmp_file" "$config_path"

echo "Updated $config_path. Restart Codex to pick up changes."
