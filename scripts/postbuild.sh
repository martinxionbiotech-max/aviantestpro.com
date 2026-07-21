#!/bin/bash
# Copy _redirects and _headers into site/ after mkdocs build
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
if [ -f "$PROJECT_DIR/_redirects" ]; then
  cp "$PROJECT_DIR/_redirects" "$PROJECT_DIR/site/_redirects"
  echo "✅ _redirects copied to site/"
fi
if [ -f "$PROJECT_DIR/_headers" ]; then
  cp "$PROJECT_DIR/_headers" "$PROJECT_DIR/site/_headers"
  echo "✅ _headers copied to site/"
fi
