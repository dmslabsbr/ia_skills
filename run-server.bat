@echo off
REM Run IA Skills MCP server locally (Windows).
REM Execute from the ia_skills repo root. Server listens on http://0.0.0.0:8001/sse

set "REPO_ROOT=%~dp0"
set "MCP_DIR=%REPO_ROOT%mcp-server"
cd /d "%REPO_ROOT%"

REM Prefer venv in repo root, then mcp-server folder
if exist "%REPO_ROOT%.venv\Scripts\python.exe" (
    set "PY=%REPO_ROOT%.venv\Scripts\python.exe"
) else if exist "%MCP_DIR%\.venv\Scripts\python.exe" (
    set "PY=%MCP_DIR%\.venv\Scripts\python.exe"
) else (
    set "PY=python"
)

echo Starting IA Skills MCP server at http://localhost:8001/sse
echo Press Ctrl+C to stop.
"%PY%" "%MCP_DIR%\main.py"
