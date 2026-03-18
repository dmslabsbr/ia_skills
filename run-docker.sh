#!/usr/bin/env bash
# Run IA Skills MCP server via Docker on Linux.
# Execute from the ia_skills repo root. Server listens on http://0.0.0.0:8001/sse

set -e
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

SKILLS_CONTAINER_NAME="skills-mcp"
COMPOSE_PROJECT_NAME="${COMPOSE_PROJECT_NAME:-$(basename "$REPO_ROOT")}"
SKILLS_SERVICE_NAME="skills-mcp"

echo "Stopping/removing existing container (if any): ${SKILLS_CONTAINER_NAME}..."
docker rm -f "${SKILLS_CONTAINER_NAME}" >/dev/null 2>&1 || true

echo "Removing previous ${SKILLS_SERVICE_NAME} image(s) built by docker compose..."
SKILLS_IMAGE_IDS="$(docker images -q \
  --filter "label=com.docker.compose.project=${COMPOSE_PROJECT_NAME}" \
  --filter "label=com.docker.compose.service=${SKILLS_SERVICE_NAME}" \
  2>/dev/null || true)"

if [ -n "${SKILLS_IMAGE_IDS}" ]; then
  # Use -f because the image might still be referenced by dangling layers.
  docker rmi -f ${SKILLS_IMAGE_IDS} >/dev/null 2>&1 || true
fi

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
