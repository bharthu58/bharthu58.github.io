#!/usr/bin/env bash
set -euo pipefail

# Ensure we are in the project root
cd "$(dirname "$0")"

echo "🚀 Starting Jekyll server..."

# Use mise to ensure the correct Ruby version is used
if command -v mise &> /dev/null; then
  exec mise exec -- bundle exec jekyll serve --livereload "$@"
else
  exec bundle exec jekyll serve --livereload "$@"
fi