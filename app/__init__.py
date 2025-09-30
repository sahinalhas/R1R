import os
import logging
from flask import Flask, g, request
from app.extensions import db

def create_app(config=None):
    # Configure logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Create the Flask app with templates from the app directory
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    # Configure the app
    # Secret key for session management - MUST be set in production
    secret_key = os.environ.get("SESSION_SECRET")
    if not secret_key:
        # Generate a random key for development (not for production!)
        import secrets
        secret_key = secrets.token_hex(32)
        logging.warning("SESSION_SECRET not set! Using temporary random key (development only)")
    app.secret_key = secret_key
    
    # Database configuration
    # Use PostgreSQL in production, SQLite in development
    database_url = os.environ.get("DATABASE_URL")
    if database_url and database_url.startswith("postgres://"):
        # Heroku postgres:// format -> postgresql:// for SQLAlchemy
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    else:
        # Use SQLite in instance folder (outside of source code)
        instance_path = os.path.join(os.getcwd(), 'instance')
        os.makedirs(instance_path, exist_ok=True)
        db_path = os.path.join(instance_path, 'yks_takip.db')
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Configure temporary file directory (outside of source code)
    tmp_path = os.path.join(os.getcwd(), 'instance', 'tmp')
    os.makedirs(tmp_path, exist_ok=True)
    app.config["TEMP_FOLDER"] = tmp_path
    
    # Initialize extensions
    db.init_app(app)
    
    # Register template filters
    from app.utils.filters import register_filters
    register_filters(app)
    
    with app.app_context():
        # Import route modules BEFORE registering blueprints
        # to ensure routes are registered with the blueprint
        from app.blueprints.ana_sayfa import routes, ana_sayfa_bp
        from app.blueprints.ogrenci_yonetimi import routes, ogrenci_yonetimi_bp
        from app.blueprints.ders_konu_yonetimi import routes, ders_konu_yonetimi_bp
        from app.blueprints.deneme_sinavlari import routes, deneme_sinavlari_bp
        from app.blueprints.rapor_yonetimi import routes, rapor_yonetimi_bp
        from app.blueprints.calisma_programi import routes, routes_api, calisma_programi_bp
        from app.blueprints.parametre_yonetimi import routes, parametre_yonetimi_bp
        from app.blueprints.ilk_kayit_formu import routes, ilk_kayit_formu_bp
        from app.blueprints.gorusme_defteri import routes, gorusme_defteri_bp
        from app.blueprints.etkinlik_kayit import routes, etkinlik_kayit_bp
        from app.blueprints.anket_yonetimi import routes, anket_yonetimi_bp
        from app.blueprints.yapay_zeka_asistan import routes, yapay_zeka_asistan_bp
        from app.api import routes, api_bp
        
        # Register blueprints
        app.register_blueprint(ana_sayfa_bp)
        app.register_blueprint(ogrenci_yonetimi_bp, url_prefix='/ogrenci-yonetimi')
        app.register_blueprint(ders_konu_yonetimi_bp, url_prefix='/ders-konu-yonetimi')
        app.register_blueprint(deneme_sinavlari_bp, url_prefix='/deneme-sinavlari')
        app.register_blueprint(rapor_yonetimi_bp, url_prefix='/rapor-yonetimi')
        app.register_blueprint(calisma_programi_bp, url_prefix='/calisma-programi')
        app.register_blueprint(parametre_yonetimi_bp, url_prefix='/parametre-yonetimi')
        app.register_blueprint(ilk_kayit_formu_bp, url_prefix='/ilk-kayit-formu')
        app.register_blueprint(gorusme_defteri_bp, url_prefix='/gorusme-defteri')
        app.register_blueprint(etkinlik_kayit_bp, url_prefix='/etkinlik-kayit')
        app.register_blueprint(anket_yonetimi_bp, url_prefix='/anket-yonetimi')
        app.register_blueprint(yapay_zeka_asistan_bp, url_prefix='/yapay-zeka-asistan')
        app.register_blueprint(api_bp)
        
        # Import models for database table creation
        from app.extensions import Base
        from app.blueprints.ogrenci_yonetimi.models import Ogrenci
        from app.blueprints.ders_konu_yonetimi.models import Ders, Konu
        from app.blueprints.calisma_programi.models import DersProgrami, DersIlerleme, KonuTakip
        from app.blueprints.deneme_sinavlari.models import DenemeSonuc
        from app.blueprints.parametre_yonetimi.models import OkulBilgi, DersSaati, GorusmeKonusu
        from app.blueprints.gorusme_defteri.models import GorusmeKaydi
        from app.blueprints.rapor_yonetimi.models import FaaliyetRaporu, RaporSablonu, IstatistikRaporu, RaporlananOlay
        from app.blueprints.etkinlik_kayit.models import Etkinlik
        from app.blueprints.anket_yonetimi.models import AnketTuru, CevapTuru, Anket, AnketSoru, OgrenciAnket, AnketCevap, SinifAnketSonuc
        from app.blueprints.yapay_zeka_asistan.models import YapayZekaModel, YapayZekaAnaliz, OgrenciAnaliz, OgrenciOneri, DuyguAnalizi
        
        # Create all database tables
        db.create_all()
    
    return app