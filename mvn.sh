#!/bin/bash

# Install Homebrew if not already installed
if test ! $(which brew); then
    echo "Installing Homebrew..."
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

# Install Maven using Homebrew
echo "Installing Maven..."
brew install maven

# Print Maven version to verify installation
echo "Maven version:"
mvn -version
