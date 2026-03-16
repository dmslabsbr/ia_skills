#!/usr/bin/env bash
# Run IA Skills MCP server via Docker on Linux.
# Execute from the ia_skills repo root. Server listens on http://0.0.0.0:8001/sse

set -e
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

echo "Building and starting skills-mcp container..."
if command -v docker compose &>/dev/null; then
  docker compose up -d --build
elif command -v docker-compose &>/dev/null; then
  docker-compose up -d --build
else
  echo "Error: docker compose or docker-compose not found." >&2
  exit 1
fi

echo "Server should be available at http://localhost:8001/sse"
echo "Logs: docker compose logs -f skills-mcp"
