# Rehberlik Servisi (Guidance Service System)

## Overview
This is a Flask-based web application for tracking and managing student progress for the YKS (Higher Education Institutions Examination) in Turkey. The system serves as a comprehensive tool for guidance counselors to track academic progress, create study schedules, analyze performance data, and generate reports.

## Recent Changes (September 30, 2025)

### Dosya Organizasyonu İyileştirmesi (Production-Ready)
- **Database konumu değişti**: SQLite database artık `instance/yks_takip.db` içinde (kaynak kod dışında)
- **Güvenlik iyileştirmesi**: SESSION_SECRET hard-coded değer yerine environment variable kullanıyor (dev için random key + warning)
- **Geçici dosya yönetimi**: 
  - Geçici dosyalar artık `instance/tmp/` klasöründe (kaynak kod dışında)
  - Tüm PDF/Excel oluşturma fonksiyonları `current_app.config["TEMP_FOLDER"]` kullanıyor
  - `/download/<filename>` endpoint'i eklendi (güvenli PDF indirme)
- **API Blueprint**: API endpoints artık düzgün şekilde kaydedildi ve kullanıma hazır
- **Auth iyileştirmesi**: `api_auth_required` decorator eklendi (gelecekte token/key auth için hazır)

### Kod Yapısı Düzenleme ve Temizlik
- **.gitignore oluşturuldu**: Python cache, database dosyaları, temp PDF'ler, backup dosyaları ignore edildi
- **Backup dosyaları silindi**: routes.py.new, ogrenciler.html.backup kaldırıldı
- **Aktif öğrenci sistemi kaldırıldı**: 
  - Session-based aktif öğrenci takibi kaldırıldı, route'lar artık sadece URL parametresi ile çalışıyor
  - `app/utils/session.py` temizlendi (set/get/clear_aktif_ogrenci fonksiyonları kaldırıldı)
  - `app/utils/auth.py` basitleştirildi (decorator'lar minimal hale getirildi)
  - Context processor kaldırıldı (`app/__init__.py`)
  - Template'lerden aktif öğrenci referansları temizlendi
  - Tüm blueprint'lerdeki import ve kullanımlar kaldırıldı

### Önceki Değişiklikler
- Successfully imported project from GitHub
- Verified Python 3.11 environment with uv package manager
- All dependencies working: Flask 3.1, SQLAlchemy 2.0, Gunicorn 23.0, WeasyPrint 65.0, ML libraries
- Configured "Flask App" workflow running on port 5000 with webview output
- Deployment configured for autoscale target with Gunicorn
- Application fully functional with existing SQLite database
- Verified student management, homepage, and all features working

## Project Structure
- **app/**: Main application package with blueprints for different modules
  - **blueprints/**: Modular components (student management, scheduling, reports, etc.)
    - **api/**: RESTful API endpoints
  - **static/**: CSS, JavaScript, and other static files
  - **templates/**: Jinja2 HTML templates
  - **utils/**: Helper functions and utilities
- **instance/**: Application data (outside source code, gitignored)
  - **yks_takip.db**: SQLite database file
  - **tmp/**: Temporary files (PDFs, exports)
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
