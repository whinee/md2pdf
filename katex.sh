set -e

rm -rf tmp/katex
mkdir -p tmp/katex

NODE_VER="16"
REL_KATEX_DIR="../../src/katex"
REL_BIN_DIR="${REL_KATEX_DIR}/bin"

KATEX_REL_LATEST_API="$(wget -qSO - "https://api.github.com/repos/KaTeX/KaTeX/releases/latest" 2>/dev/null)"
KATEX_VER="$(echo "$KATEX_REL_LATEST_API" | grep -E '"name":' | cut -d '"' -f4 | head -1)"

wget -O katex.tar.gz "$(echo "$KATEX_REL_LATEST_API" | grep -E "tarball_url" | cut -d '"' -f4)" >/dev/null
tar -xzf katex.tar.gz -C tmp/katex --strip-components=1
rm -rf katex.tar.gz

cd tmp/katex/
rm -f .yarnrc.yml
npm install --no-optional --no-lockfile --no-package-lock --no-save --omit=optional &
npm install pkg commander --no-optional --no-lockfile --no-package-lock --no-audit --no-fund --omit=optional &
wait
yarn build

rm -rf "$REL_BIN_DIR"
mkdir -p "$REL_BIN_DIR"
yarn pkg -o "${REL_BIN_DIR}/katex_${KATEX_VER}_node${NODE_VER}_x86_64-win.exe" --target "node${NODE_VER}-win-x64" cli.js
yarn pkg -o "${REL_BIN_DIR}/katex_${KATEX_VER}_node${NODE_VER}_x86_64-mac" --target "node${NODE_VER}-macos-x64" cli.js
yarn pkg -o "${REL_BIN_DIR}/katex_${KATEX_VER}_node${NODE_VER}_x86_64-linux" --target "node${NODE_VER}-linux-x64" cli.js

cp -r dist/fonts dist/katex.min.css "${REL_KATEX_DIR}"

# rm -rf tmp
