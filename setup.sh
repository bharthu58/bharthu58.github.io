#!/usr/bin/env bash
set -euo pipefail

echo "🚀 Setting up bharthu58.github.io development environment..."

# Ensure we are in the project root
cd "$(dirname "$0")"

# Install project-specific tool versions if mise is present
if command -v mise &> /dev/null; then
  echo "📦 Installing project runtimes via mise..."
  mise install
fi

# Check for Ruby
if ! command -v ruby &> /dev/null; then
  echo "❌ Ruby is not installed. Please run your system bootstrap or install Ruby."
  exit 1
fi

# Install dependencies
if command -v mise &> /dev/null; then
  echo "🛠️  Ensuring Bundler is installed (via mise)..."
  mise exec -- gem install bundler
  echo "📦 Installing gems from Gemfile (via mise)..."
  mise exec -- bundle install
else
  echo "🛠️  Ensuring Bundler is installed..."
  gem install bundler
  echo "📦 Installing gems from Gemfile..."
  bundle install
fi

echo ""
echo "✅ Project setup complete."
echo "To start the server, run:"
echo "  ./run.sh"