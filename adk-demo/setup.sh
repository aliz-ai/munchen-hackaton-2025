#!/bin/bash

PYTHON_VERSION=3.12.3
INSTALL_PREFIX=/usr/local

# === Step 1: Install build dependencies ===
sudo apt-get update
sudo apt-get install -y \
    wget build-essential libssl-dev zlib1g-dev \
    libncurses-dev libreadline-dev libsqlite3-dev libffi-dev \
    libbz2-dev liblzma-dev uuid-dev tk-dev libgdbm-dev \
    libnss3-dev libgdbm-compat-dev

# === Step 2: Download and build Python ===
cd /tmp
wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
tar -xzf Python-${PYTHON_VERSION}.tgz
cd Python-${PYTHON_VERSION}

./configure --enable-optimizations --prefix=${INSTALL_PREFIX}
make -j$(nproc)
sudo make altinstall  # Use altinstall to avoid overwriting system python

export PATH=${INSTALL_PREFIX}/bin:${PATH}

# === Step 3: Set Python 3.12 as default ===
sudo ln -sf ${INSTALL_PREFIX}/bin/python3.12 ${INSTALL_PREFIX}/bin/python && \
sudo ln -sf ${INSTALL_PREFIX}/bin/python3.12 ${INSTALL_PREFIX}//bin/python3 && \
sudo ln -sf ${INSTALL_PREFIX}/bin/pip3.12 ${INSTALL_PREFIX}//bin/pip && \
sudo ln -sf ${INSTALL_PREFIX}/bin/pip3.12 ${INSTALL_PREFIX}//bin/pip3

# === Step 4: Install Poetry ===
curl -sSL https://install.python-poetry.org | python3.12 -
export PATH="$HOME/.local/bin:$PATH"

# === Step 5: Clone the repo ===
cd
git clone https://github.com/google/adk-samples.git
cd adk-samples
git reset --hard ea2288c
