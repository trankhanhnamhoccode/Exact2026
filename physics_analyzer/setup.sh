#!/bin/bash

# Cập nhật hệ thống
sudo apt-get update

# Cài đặt zstd để giải nén
sudo apt-get install -y zstd

# Cài đặt Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Cài đặt Python packages
pip install -r requirements.txt

echo "✅ Setup completed!"