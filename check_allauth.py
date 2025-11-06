#!/usr/bin/env python
"""Script para verificar la configuración de django-allauth con Google OAuth"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

print("=" * 60)
print("Verificación de configuración django-allauth")
print("=" * 60)

# Verificar Sites
sites = Site.objects.all()
print(f"\n📍 Sites configurados ({sites.count()}):")
for site in sites:
    print(f"   ID: {site.id} | Domain: {site.domain} | Name: {site.name}")

# Verificar SocialApps
apps = SocialApp.objects.all()
print(f"\n🔑 SocialApps configurados ({apps.count()}):")
for app in apps:
    print(f"   ID: {app.id} | Provider: {app.provider} | Name: {app.name}")
    print(f"   Client ID: {app.client_id[:20]}..." if app.client_id else "   Client ID: NO CONFIGURADO ❌")
    print(f"   Secret: {'✓ Configurado' if app.secret else '❌ NO CONFIGURADO'}")
    
    # Verificar asociación con sites
    app_sites = app.sites.all()
    print(f"   Sites asociados ({app_sites.count()}):")
    if app_sites.exists():
        for s in app_sites:
            print(f"      - Site {s.id}: {s.domain}")
    else:
        print(f"      ⚠️  NO HAY SITES ASOCIADOS - ESTE ES EL PROBLEMA")
    print()

# Diagnóstico
print("=" * 60)
print("DIAGNÓSTICO:")
print("=" * 60)

if not apps.exists():
    print("❌ ERROR: No hay SocialApp configurado para Google")
    print("   Solución: Crear SocialApp en /admin/socialaccount/socialapp/")
else:
    google_app = apps.filter(provider='google').first()
    if not google_app:
        print("❌ ERROR: No hay SocialApp con provider='google'")
    else:
        if not google_app.client_id:
            print("❌ ERROR: SocialApp no tiene Client ID configurado")
        if not google_app.secret:
            print("❌ ERROR: SocialApp no tiene Secret configurado")
        if not google_app.sites.exists():
            print("❌ ERROR CRÍTICO: SocialApp no está asociado a ningún Site")
            print(f"   Solución: Asociar el SocialApp al Site ID 1 en el admin")
        else:
            site_ids = list(google_app.sites.values_list('id', flat=True))
            if 1 not in site_ids:
                print(f"⚠️  ADVERTENCIA: SocialApp está asociado a Sites {site_ids}")
                print(f"   pero settings.py tiene SITE_ID = 1")
                print(f"   Solución: Asociar también al Site 1")
            else:
                print("✅ Configuración correcta!")
                print(f"   - SocialApp existe")
                print(f"   - Client ID configurado")
                print(f"   - Secret configurado")
                print(f"   - Asociado al Site 1")

print("\n" + "=" * 60)
print("Para arreglar la asociación Site-SocialApp, ejecuta:")
print("=" * 60)
print("python manage.py shell")
print(">>> from allauth.socialaccount.models import SocialApp")
print(">>> from django.contrib.sites.models import Site")
print(">>> app = SocialApp.objects.get(provider='google')")
print(">>> site = Site.objects.get(id=1)")
print(">>> app.sites.add(site)")
print(">>> print('✅ Site asociado correctamente!')")
print("=" * 60)
