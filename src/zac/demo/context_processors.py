from django.conf import settings as django_settings


def settings(request):
    public_settings = ('GOOGLE_ANALYTICS_ID', 'GOOGLE_API_KEY', 'ENVIRONMENT',
                       'SHOW_ALERT', 'PROJECT_NAME', 'FORCE_SCRIPT_NAME', 'IS_HTTPS')

    context = {
        'settings': dict([
            (k, getattr(django_settings, k, None)) for k in public_settings
        ]),
    }

    if hasattr(django_settings, 'RAVEN_CONFIG'):
        context.update(dsn=django_settings.RAVEN_CONFIG.get('public_dsn', ''))

    return context
