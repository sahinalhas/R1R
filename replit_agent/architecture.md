# Architecture Overview

## 1. Overview

This repository contains a Flask-based web application designed for tracking and managing student progress for the YKS (Higher Education Institutions Examination) in Turkey. The system serves as a comprehensive tool for guidance counselors, teachers, and students to track academic progress, create study schedules, analyze performance data, and generate reports.

The application employs a modular architecture using Flask Blueprints to organize functionality into separate components, with a relational database backend (supporting both SQLite for development and PostgreSQL for production), and a modern front-end using Bootstrap, DataTables, FullCalendar, and custom JavaScript components.

## 2. System Architecture

The application follows a traditional multi-tier web application architecture:

- **Presentation Layer**: HTML templates with Bootstrap, custom CSS, and JavaScript
- **Controller Layer**: Flask routes organized in blueprints
- **Service Layer**: Business logic encapsulated in service classes
- **Data Access Layer**: SQLAlchemy ORM models for database interaction
- **Utility Layer**: Helper functions for common tasks

```
+-----------------+       +----------------+        +------------------+
|                 |       |                |        |                  |
|  Presentation   |       |   Controller   |        |    Services      |
|     Layer       +------>+     Layer      +------->+     Layer        |
|                 |       |                |        |                  |
+-----------------+       +----------------+        +------------------+
|                 |       |                |        |                  |
| - Templates     |       | - Blueprints   |        | - OgrenciService |
| - Static Files  |       | - Routes       |        | - DersService    |
| - JavaScript    |       | - View Funcs   |        | - ProgramService |
| - CSS           |       | - Forms        |        | - RaporService   |
|                 |       |                |        |                  |
+-----------------+       +----------------+        +------------------+
                                                            |
                                                            |
                                                            v
                              +----------------+    +------------------+
                              |                |    |                  |
                              |    Models      |    |     Utilities    |
                              |     Layer      |    |                  |
                              |                |    |                  |
                              +----------------+    +------------------+
                              |                |    |                  |
                              | - Ogrenci      |    | - Auth           |
                              | - Ders         |    | - Session        |
                              | - Konu         |    | - Program        |
                              | - DersProgrami |    | - Report         |
                              | - KonuTakip    |    | - Filters        |
                              |                |    |                  |
                              +----------------+    +------------------+
```

## 3. Key Components

### 3.1 Backend Framework

**Flask** is used as the primary web framework due to its lightweight nature and flexibility. The application leverages Flask's Blueprint system to modularize the codebase by functional domains.

Key blueprints include:
- **ana_sayfa**: Main dashboard and landing pages
- **ogrenci_yonetimi**: Student management functionality
- **calisma_programi**: Study schedule management
- **ders_konu_yonetimi**: Subject and topic management
- **deneme_sinavlari**: Mock exam management and tracking
- **rapor_yonetimi**: Report generation and management
- **yapay_zeka_asistan**: AI assistant for data analysis and guidance

### 3.2 Database Architecture

The application uses **SQLAlchemy** as the ORM (Object-Relational Mapper) with a relational database backend. It supports two database systems:

- **PostgreSQL** for production environments
- **SQLite** for development environments

The database configuration is determined at runtime based on the presence of a `DATABASE_URL` environment variable, providing flexibility across different deployment scenarios.

Main database models include:
- Student information (Ogrenci)
- Subjects and topics (Ders, Konu)
- Study schedules (DersProgrami)
- Progress tracking (DersIlerleme, KonuTakip)
- Exam results (DenemeSonuc)
- Reports (FaaliyetRaporu, IstatistikRaporu)
- AI models and analysis results (YapayZekaModel, YapayZekaAnaliz)

### 3.3 Frontend Architecture

The frontend is built with:
- **Bootstrap 5** for responsive UI components and layout
- **DataTables** for interactive data tables
- **FullCalendar** for schedule visualization and management
- **Chart.js** for data visualization
- **Font Awesome** for icons
- **Custom JavaScript modules** for specific functionality

The application uses a component-based approach for frontend organization, with reusable templates and modular JavaScript files that handle specific functionality like calendar management, charting, and student search.

### 3.4 Authentication & Authorization

The application implements a custom session-based authentication system:
- Session tracking for active students
- Function decorators for access control (`session_required`, `ogrenci_required`, `admin_required`)
- No traditional user login system, instead focusing on student selection and session management

This approach indicates that the system is designed for internal use within a counseling office where multiple counselors might work with different students throughout the day.

### 3.5 AI Assistant Integration

The application includes a machine learning component (`yapay_zeka_asistan`) for advanced analytics:
- Risk assessment models for academic performance
- Text sentiment analysis for student communications
- Recommendation engines for study plans
- Integration with scikit-learn for model training and prediction

## 4. Data Flow

### 4.1 Main Application Flow

1. **Initialization**: The application starts in `main.py`, which imports the Flask app factory from `app/__init__.py`
2. **App Configuration**: Database connections, blueprints, and template filters are registered during application initialization
3. **Request Handling**: Flask routes in various blueprints manage HTTP requests
4. **Data Access**: Routes use SQLAlchemy models to interact with the database
5. **Template Rendering**: Jinja2 templates are rendered with data from the database
6. **Client Interaction**: JavaScript in the browser handles user interactions and dynamic updates

### 4.2 Key Processes

#### Student Management
- Create, view, update student records
- Track student progress across subjects
- Generate performance reports

#### Study Planning
- Create and manage weekly study schedules
- Track topic-by-topic progress
- Visualize study plans in calendar and report formats

#### Reporting
- Generate PDF reports using WeasyPrint
- Export data to Excel
- Produce visualizations for progress tracking
- Create standardized reports for educational authorities

#### AI Analysis
- Train models on student performance data
- Generate predictions and recommendations
- Perform sentiment analysis on student writings

## 5. External Dependencies

### 5.1 Core Dependencies

- **Flask**: Web framework
- **SQLAlchemy**: ORM for database access
- **Gunicorn**: WSGI server for production deployment
- **Psycopg2**: PostgreSQL adapter
- **WeasyPrint**: HTML to PDF conversion
- **Pandas/NumPy**: Data manipulation and analysis
- **Scikit-learn**: Machine learning functionality
- **Joblib**: Model serialization and parallel processing
- **OpenPyXL**: Excel file handling

### 5.2 Frontend Dependencies (CDN-loaded)

- **Bootstrap 5**: UI framework
- **DataTables**: Enhanced tables
- **Chart.js**: Data visualization
- **FullCalendar**: Calendar interface
- **Font Awesome**: Icon library
- **Toastr**: Notification system

## 6. Deployment Strategy

The application is configured for deployment on cloud platforms like Replit or potentially Heroku, as evident from:

- **Gunicorn configuration** in .replit file for production server
- **Replit Nix** package specifications
- **Environment variable handling** for database configuration
- **Port configuration** for both development and production

The deployment process includes:
1. Setting up a PostgreSQL database
2. Configuring environment variables
3. Installing dependencies
4. Running the application through Gunicorn

The system supports both development mode (using Flask's built-in server with debug enabled) and production mode (using Gunicorn with multiple workers).

## 7. Future Architectural Considerations

The codebase shows signs of planned or ongoing development in several areas:

1. **Enhanced AI functionality**: The yapay_zeka_asistan blueprint suggests plans for more advanced AI features
2. **MEB integration**: The report generation module includes references to MEB (Ministry of National Education) standards
3. **Mobile optimization**: Frontend styles indicate consideration for mobile device support
4. **Authentication expansion**: The authorization system could be expanded to include more traditional user authentication

These areas represent potential evolution paths for the architecture as the application matures.