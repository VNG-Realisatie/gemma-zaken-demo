# Generated by Django 2.1.3 on 2019-07-29 16:08

from django.db import migrations
from django.db.models import Value, F
from django.db.models.functions import Replace


def forward(apps, schema_editor):
    Subscription = apps.get_model("notifications", "Subscription")

    old_val = 'https://ref.tst.vng.cloud/nrc/'
    new_val = 'https://notificaties-api.vng.cloud/'

    Subscription.objects.filter(
        _subscription__startswith='https://ref.tst.vng.cloud/nrc/'
    ).update(
        _subscription=Replace(F('_subscription'), Value(old_val), Value(new_val)),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_auto_20190704_0924'),
        ('vng_api_common', '0005_auto_20190614_1346'),
    ]

    operations = [
        migrations.RunPython(forward, migrations.RunPython.noop)
    ]
