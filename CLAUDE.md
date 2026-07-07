# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is Oriol Barbany's personal academic website, served via GitHub Pages as a static site (no build step, no package manager, no server-side code). Every page is a hand-written HTML file linked directly against shared CSS/JS assets in the repo root.

## Development

There is no build/lint/test tooling. Changes are made directly to HTML/CSS/JS files and previewed by opening the file in a browser or serving the directory statically, e.g.:

```
python3 -m http.server 8000
```

Deploying is just committing and pushing to `main` (GitHub Pages serves straight from the repo).

## Structure

- `index.html` — the homepage (bio, publications, etc.). Uses the Bulma CSS framework plus Font Awesome and Academicons for icons.
- `css/style.css` — the single global stylesheet for the main site, built on top of Bulma v0.9.4 (vendored inline, not via a package manager). Contains the dark-mode variable overrides (see below).
- `navbar.js` — shared navbar burger-menu toggle behavior, loaded across pages.
- `fonts/`, `academicons.css`/`academicons.min.css` — icon font assets used across pages.
- `img/` — images and thumbnails referenced by the homepage and project pages.
- `music/` — standalone section with its own `index.html` and static assets, not using the project-page template below.
- `bifold/`, `fast-vc/` — individual research project pages. Each is self-contained under its own directory with its own `index.html`, `static/` (or `media/`) folder for page-specific CSS/JS/images, so edits to one project's assets never affect another's.

### Project pages (`bifold/`, `fast-vc/`, and similar)

These follow the common academic-paper "Nerfies-style" template pattern (Bulma-based, single long `index.html`, `bulma-carousel` for image/video carousels, hero/abstract/results/BibTeX sections). When adding a new project page, copy the structure of an existing one (`bifold/index.html` is the most current example) rather than starting from scratch, and keep page-specific assets inside that project's own subdirectory.

`fast-vc/deploy.py` is a one-off helper script that regenerates `fast-vc/index.html`'s audio-comparison table from `fast-vc/list.txt` + `fast-vc/header.html` + `fast-vc/footer.html`; rerun it (`python3 deploy.py` from within `fast-vc/`) after changing those inputs rather than hand-editing the generated table.

## Dark mode

Dark mode is implemented via a `dark-mode` class on `<body>` plus CSS custom properties defined in `:root` and overridden under `body.dark-mode` in `css/style.css` (e.g. `--background-color`, `--text-color`, `--link-color`). Theme preference is read from `localStorage` and `prefers-color-scheme`, and applied pre-render via an inline `<script>` in `<head>` (adds `dark-mode-preload` to `<html>`) to avoid a flash of the wrong theme. When adding new UI elements, theme them with CSS variables consistent with this pattern rather than hardcoding colors.
