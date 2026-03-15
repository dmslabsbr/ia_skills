# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies if needed (none strictly required for this MCP)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY mcp-server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire skills repository (MCP server + all skills)
# Since the server needs to read SKILL.md files from parent directories,
# we copy the root of ia_skills into the container
COPY . /app/ia_skills

# Set working directory to the mcp-server folder
WORKDIR /app/ia_skills/mcp-server

# Ensure the script can find the skills directory relative to itself
ENV PYTHONUNBUFFERED=1

EXPOSE 8001

# Run the MCP server
# Note: SSE transport via uvicorn
ENTRYPOINT ["python", "main.py"]
