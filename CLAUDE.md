# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Run development server (localhost:5001)
python app.py

# Run tests
pytest

# Install dependencies
pip install -r requirements.txt
```

## Architecture

**Spendly** is a Flask web app for personal expense tracking targeting the Indian market (₹ currency). It is structured as a step-by-step tutorial project — many backend features are intentionally left as placeholders for progressive implementation.

### Stack
- **Backend**: Flask 3.1 with Jinja2 templating, SQLite (via `database/db.py`)
- **Frontend**: Vanilla JS, custom CSS design system (no Node.js/bundler)
- **Testing**: pytest + pytest-flask

### Routing (`app.py`)
All routes render Jinja2 templates from `templates/`. Placeholder routes return text strings and are meant to be implemented incrementally:
- Implemented: `/`, `/login`, `/register`, `/terms`, `/privacy`
- Placeholders: `/logout` (Step 3), `/profile` (Step 4), `/expenses/add|edit|delete` (Steps 7–9)

### Templates
All pages extend `templates/base.html`, which provides the sticky navbar, footer, and script injection blocks. Use `{% block content %}` and `{% block scripts %}` for page-specific content.

### CSS Design System (`static/css/style.css`)
CSS custom properties define the full design language. Key variables:
- `--accent`: `#1a472a` (dark green, primary)
- `--accent-2`: `#c17f24` (orange/gold, secondary)
- Fonts: DM Serif Display (headings), DM Sans (body) — loaded from Google Fonts in base.html
- Breakpoints: 900px and 600px

### Database (`database/db.py`)
Placeholder module. The three functions to implement are `get_db()`, `init_db()`, and `seed_db()`. The SQLite file will be `expense_tracker.db` (gitignored).
