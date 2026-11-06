"""Reject AI attribution while permitting human co-author trailers."""
import re
import sys
from pathlib import Path

AI = r"\b(?:claude|anthropic|codex|openai|chatgpt|copilot|gemini|cursor|windsurf|aider|devin|AI|artificial intelligence)\b"
CREDIT = r"co-authored-by\s*:|signed-off-by\s*:|generated\s+(?:by|with|using)|(?:assisted|powered|written|created)\s+by|^\s*(?:credits?|attribution)\s*:"


def has_ai_credit(message):
    return any(
        re.search(AI, line, re.I) and re.search(CREDIT, line, re.I)
        for line in message.splitlines()
    )


if __name__ == "__main__":
    if has_ai_credit(Path(sys.argv[1]).read_text(encoding="utf-8")):
        print("Commit rejected: remove AI attribution or generated-by notes.", file=sys.stderr)
        sys.exit(1)
