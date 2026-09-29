#!/bin/sh
set -eu

if ! command -v cwebp >/dev/null 2>&1; then
  echo "cwebp is required. Install the WebP command-line tools first." >&2
  exit 1
fi

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
site_dir=$(dirname -- "$script_dir")
figure_dir="$site_dir/images/web_fig"
thumbnail_dir="$figure_dir/thumbs"
mkdir -p "$thumbnail_dir"

for filename in method_verimed.png verimed_res.png method_cloudfix.jpg method_pol.png pol_res.png; do
  stem=${filename%.*}
  cwebp -quiet -lossless -m 6 -resize 1200 0 "$figure_dir/$filename" -o "$thumbnail_dir/$stem.webp"
done
