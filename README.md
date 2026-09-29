# Bethel Hall's website

Source for [bethelhall.tech](https://bethelhall.tech/), Bethel Hall's academic website with research, publications, news, and professional service.

The site is static HTML, CSS, and JavaScript. Edit `index.html` for page content and styling. The `CNAME` file configures the custom domain for GitHub Pages.

## Local preview

From this directory, run:

```sh
python3 -m http.server 8000
```

Open [localhost:8000](http://localhost:8000/) in a browser. Check both desktop and mobile layouts before publishing.

## Research figures

Full-resolution figures live in `images/web_fig/`. Smaller WebP previews live in `images/web_fig/thumbs/`; the image viewer uses the original files for enlarged views.

The homepage uses five of these previews plus a vector chart for CloudFix repair rates. The older CloudFix raster chart is retained as a source asset but is not displayed.

To regenerate the raster previews, install the WebP command-line tools and run:

```sh
sh scripts/generate-thumbnails.sh
```

The script preserves the originals and creates 1,200-pixel-wide previews with lossless WebP encoding. When changing a figure, regenerate its preview and update the image's `width`, `height`, alternative text, and caption in `index.html` as needed.

The CloudFix repair-rate chart uses the complete-repair percentages from [Table III of the paper](https://arxiv.org/html/2512.09957v2#S5.T3). Regenerate it with `python3 scripts/generate-cloudfix-chart.py`.

Use concise copy without em dashes. Keep the visible footer update date aligned with substantive content changes.

The current CV is `data/resume_bethel.pdf`. Keep its link in `sitemap.xml` aligned with the homepage and update the sitemap's modification date when publishing content changes.

## Attribution

This website was originally adapted from [Jon Barron's academic website template](https://jonbarron.info/). The unrelated example project pages have been removed.
