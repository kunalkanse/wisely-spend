# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based personal expense tracking web application called "Spendly". The project appears to be structured as a step-by-step learning exercise, with many features currently showing placeholder implementations that reference "Step X" where students will implement functionality.

## Development Setup

### Environment Setup
```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The application runs on http://localhost:5001 in debug mode by default.

### Testing
```bash
# Run tests (using pytest)
pytest

# Run specific test file
pytest test_filename.py

# Run with coverage (if coverage is added to requirements)
pytest --cov=.
```

## Architecture

### Application Structure
- **app.py**: Main Flask application with route definitions
- **database/**: Database layer (currently contains placeholder for SQLite setup)
  - **db.py**: Database connection and initialization functions (to be implemented)
- **templates/**: Jinja2 HTML templates
  - **base.html**: Base template with navigation, branding, and common layout
  - **landing.html**: Marketing homepage with hero section and feature cards
  - **login.html**: User authentication form
  - **register.html**: User registration form
- **static/**: Client-side assets
  - **css/style.css**: Complete styling system with CSS variables and component styles
  - **js/main.js**: JavaScript functionality (currently placeholder)

### Key Design Elements
- **Brand**: "Spendly" with diamond icon (◈) and tagline "Track every rupee"
- **Design System**: Uses CSS custom properties for consistent colors, typography, and spacing
- **Typography**: DM Serif Display for headings, DM Sans for body text
- **Currency**: Indian Rupees (₹) - application appears to be targeted at Indian market

### Current Route Structure
**Implemented Routes:**
- `/` - Landing page with marketing content
- `/register` - User registration form
- `/login` - User authentication form

**Placeholder Routes (return string messages about future implementation):**
- `/logout` - Coming in Step 3
- `/profile` - Coming in Step 4
- `/expenses/add` - Coming in Step 7
- `/expenses/<int:id>/edit` - Coming in Step 8
- `/expenses/<int:id>/delete` - Coming in Step 9

### Database Design (Planned)
Based on placeholder comments in `database/db.py`, the database layer should include:
- `get_db()` - SQLite connection with row_factory and foreign keys enabled
- `init_db()` - Table creation using CREATE TABLE IF NOT EXISTS
- `seed_db()` - Sample data insertion for development

## Development Notes

### Planned Feature Areas
1. **Database Setup** (Step 1)
2. **User Authentication** (Steps 2-3)
3. **User Profile Management** (Step 4)
4. **Expense Management** (Steps 7-9)

### Styling System
The CSS uses a comprehensive design system with:
- Color variables for consistent theming
- Typography scale with display and body font families
- Spacing and layout variables
- Component-based styling approach

### Dependencies
- **Flask 3.1.3**: Web framework
- **Werkzeug 3.1.6**: WSGI utilities
- **pytest 8.3.5**: Testing framework
- **pytest-flask 1.3.0**: Flask testing utilities

## Common Development Tasks

### Adding New Routes
Routes follow Flask patterns and should be added to the main routes section in app.py (lines 10-23 for implemented routes).

### Working with Templates
Templates extend the base.html template and use Jinja2 templating. The base template includes navigation, footer, and common scripts/styles.

### Database Development
When implementing database functionality, work in the `database/` package and ensure SQLite connections use row_factory and foreign keys as noted in the placeholder comments.