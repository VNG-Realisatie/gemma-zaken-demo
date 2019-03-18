# Generated by Django 2.1.3 on 2019-03-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_merge_20190122_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otherztc',
            options={'verbose_name': 'Overige ZTC', 'verbose_name_plural': "Overige ZTC's"},
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='callback_client_id',
            field=models.CharField(blank=True, help_text='De Client ID van de webhook API van deze demo applicatie', max_length=255, verbose_name='Callback Client ID'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='callback_secret',
            field=models.CharField(blank=True, help_text='De Secret van de webhook API van deze demo applicatie', max_length=512, verbose_name='Callback Secret'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='callback_url',
            field=models.URLField(blank=True, help_text='De URL van deze demo applicatie waar het NC berichten naar toe kan sturen.', verbose_name='Callback URL'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='nc_amqp_host',
            field=models.CharField(blank=True, help_text='Verbind direct met AMQP-server via deze host.', max_length=255, verbose_name='AMQP-host'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='nc_amqp_port',
            field=models.CharField(blank=True, default='', help_text='Verbind direct met AMQP-server via deze port.', max_length=255, verbose_name='AMQP-port'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='nc_base_url',
            field=models.CharField(blank=True, default='http://localhost:8004/api/v1/', help_text='Notificatie API van het Notificatie component', max_length=255, verbose_name='NC basis URL'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='nc_client_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='Client ID'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='nc_method',
            field=models.CharField(default='webhook', max_length=20, verbose_name='Notificatie methode'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='nc_secret',
            field=models.CharField(blank=True, max_length=512, verbose_name='Secret'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='vrl_base_url',
            field=models.CharField(blank=True, default='https://ref.tst.vng.cloud/referentielijsten/api/v1/', help_text='VNG Referentielijsten API: Typisch de landelijke API URL en niet een eigen installatie.', max_length=255, verbose_name='VRL basis URL'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='google_maps_api_key',
            field=models.CharField(blank=True, max_length=255, verbose_name='Google maps API-key'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='google_maps_lat',
            field=models.DecimalField(blank=True, decimal_places=6, default='52.369918', max_digits=9, verbose_name='Google maps latitude'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='google_maps_long',
            field=models.DecimalField(blank=True, decimal_places=6, default='4.897787', help_text='Deze coördinaten worden standaard op de kaart weergegeven', max_digits=9, verbose_name='Google maps longitude'),
        ),
    ]
