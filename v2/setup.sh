# Install tauri dependencies
sudo apt install -y \
  libwebkit2gtk-4.0-dev \
  build-essential \
  curl \
  wget \
  libssl-dev \
  libgtk-3-dev \
  libayatana-appindicator3-dev \
  librsvg2-dev \
  cmake \
  pkg-config \
  libx11-dev \
  libxdo-dev

# Install rust
curl https://sh.rustup.rs -sSf | sh
source $HOME/.cargo/env
rustup target add armv7-unknown-linux-gnueabihf

# Install node & pnpm
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
npm install -g pnpm
