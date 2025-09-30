# Rehberlik Servisi (Guidance Service System)

## Overview
This is a Flask-based web application for tracking and managing student progress for the YKS (Higher Education Institutions Examination) in Turkey. The system serves as a comprehensive tool for guidance counselors to track academic progress, create study schedules, analyze performance data, and generate reports.

## Recent Changes (September 30, 2025)
- Successfully imported project from GitHub
- Verified Python 3.11 environment with uv package manager
- All dependencies working: Flask 3.1, SQLAlchemy 2.0, Gunicorn 23.0, WeasyPrint 65.0, ML libraries
- Configured "Flask App" workflow running on port 5000 with webview output
- Deployment configured for autoscale target with Gunicorn
- Application fully functional with existing SQLite database
- Verified student management, homepage, and all features working
- FullCalendar errors are handled gracefully by existing error handling script

## Project Structure
- **app/**: Main application package with blueprints for different modules
  - **blueprints/**: Modular components (student management, scheduling, reports, etc.)
  - **static/**: CSS, JavaScript, and other static files
  - **templates/**: Jinja2 HTML templates
  - **database/**: SQLite database file (yks_takip.db)
  - **utils/**: Helper functions and utilities
- **main.py**: Application entry point
- **pyproject.toml**: Python dependencies configuration
- **uv.lock**: Dependency lock file

## Key Features
- Student profile management
- Study schedule planning and tracking
- Mock exam results tracking
- Report generation (PDF and Excel)
- AI-powered student analysis and recommendations
- Meeting diary and activity logging
- Parameter management for school settings

## Technology Stack
- **Backend**: Flask 3.1, SQLAlchemy 2.0
- **Database**: SQLite (development), PostgreSQL (production)
- **Server**: Gunicorn 23.0
- **PDF Generation**: WeasyPrint 65.0
- **Data Analysis**: Pandas, NumPy, Scikit-learn
- **Frontend**: Bootstrap 5, DataTables, FullCalendar, Chart.js

## Running the Application
The application runs automatically via the configured workflow on port 5000. To manually run:
```bash
uv run gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

## Deployment
Configured for autoscale deployment using Gunicorn. The app will automatically scale based on traffic.

## User Preferences
- Preferred communication style: Simple, everyday language
