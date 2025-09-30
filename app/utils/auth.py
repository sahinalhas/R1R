"""
Yetkilendirme ve oturum yönetimi işlevleri
"""

from functools import wraps
from flask import redirect, url_for, flash
from app.blueprints.ogrenci_yonetimi.models import Ogrenci

def session_required(ogrenci_zorunlu=True):
    """
    Basitleştirilmiş decorator - artık sadece fonksiyonu olduğu gibi döndürür
    Geriye dönük uyumluluk için bırakıldı
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)
        return decorated_function
    
    if callable(ogrenci_zorunlu):
        f = ogrenci_zorunlu
        ogrenci_zorunlu = True
        return decorator(f)
    
    return decorator

def ogrenci_required(f):
    """
    Öğrenci kontrol dekoratörü - URL'den gelen öğrenci ID'sini kontrol eder
    """
    @wraps(f)
    def decorated_function(ogrenci_id=None, *args, **kwargs):
        if not ogrenci_id:
            flash('Geçersiz öğrenci ID.', 'danger')
            return redirect(url_for('ogrenci_yonetimi.liste'))
            
        ogrenci = Ogrenci.query.get_or_404(ogrenci_id)
        kwargs['ogrenci'] = ogrenci
        return f(ogrenci_id, *args, **kwargs)
    
    return decorated_function

def admin_required(f):
    """
    Admin yetki kontrolü için dekoratör (ileride kullanılacak)
    Kullanıcı admin değilse ana sayfaya yönlendirir
    
    Args:
        f: Dekorlanacak view fonksiyonu
        
    Returns:
        Wrapper fonksiyonu
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # TODO: Admin kontrolü gerçekleştir
        # Şu an için bypass ediyoruz, ileride admin sistemi geldiğinde aktif olacak
        return f(*args, **kwargs)
    
    return decorated_function

def log_activity(activity_type, description=None):
    """
    Kullanıcı aktivitelerini loglama dekoratörü (ileride kullanılacak)
    
    Args:
        activity_type: Aktivite tipi (örn: 'ogrenci_ekle', 'ders_guncelle')
        description: Aktivite açıklaması
        
    Returns:
        Dekoratör fonksiyonu
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # İşlemi gerçekleştir
            result = f(*args, **kwargs)
            
            # TODO: Aktivite logu kaydet
            # Şu an için bypass ediyoruz, ileride loglama sistemi geldiğinde aktif olacak
            
            return result
        return decorated_function
    return decorator