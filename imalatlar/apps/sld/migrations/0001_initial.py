# Generated by Django 3.2.4 on 2021-09-06 10:48

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SLD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=10, verbose_name='CRM NO')),
                ('company_name', models.CharField(max_length=150, verbose_name='Firma')),
                ('billing_address', models.CharField(max_length=80, verbose_name='Fatura Adresi')),
                ('delivery_address', models.CharField(max_length=80, verbose_name='Sevk Adresi')),
                ('delivery_date', models.DateField(verbose_name='Teslim Tarihi')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Olusturma Tarihi')),
                ('delivery_type', models.CharField(choices=[('Kapida Teslim', 'Kapida Teslim'), ('Nakliye Ambarina Sevkiyat', 'Nakliye Ambarina Sevkiyat'), ('Montaj Dahil', 'Montaj Dahil')], max_length=35, verbose_name='Teslim Sekli')),
                ('has_chest', models.BooleanField(verbose_name='Sandıklı Mı?')),
                ('notes', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Notlar')),
                ('drawing', models.CharField(max_length=200, verbose_name='Hazırlayan')),
                ('control', models.CharField(blank=True, max_length=40, null=True, verbose_name='Kontrol')),
                ('manufacturing_chief', models.CharField(blank=True, max_length=40, null=True, verbose_name='Imalat Sorumlusu')),
                ('glass', models.CharField(max_length=25, verbose_name='Cam')),
                ('color', models.CharField(max_length=20, verbose_name='Renk')),
                ('opening_direction', models.CharField(blank=True, choices=[('sag', 'SAG'), ('sol', 'SOL')], max_length=3, null=True, verbose_name='Acilis Yonu')),
                ('ustluk', models.BooleanField(default=False, verbose_name='UstlUk Var Mi?')),
                ('door_type', models.CharField(choices=[('th_standart', 'STANDART TEK HAREKETLI'), ('ts_th_standart', 'STANDART TEK SBT. + TEK HRK.'), ('ih_standart', 'STANDART IKI HAREKETLI'), ('is_ih_standart', 'STANDART IKI SBT. + IKI HRK.'), ('th_cam', 'CAM - TEK HAREKETLI'), ('ts_th_cam', 'CAM - TEK SBT. + TEK HRK.'), ('ih_cam', 'CAM - IKI HAREKETLI'), ('is_ih_cam', 'CAM - IKI SBT. + IKI HRK.'), ('ih_teleskop', 'TELESKOPIK - IKI HAREKETLI'), ('ih_ts_teleskop', 'TELESKOPIK - IKI HRK. + TEK SBT.'), ('dh_teleskop', 'TELESKOPIK - DORT HAREKETLI'), ('dh_is_teleskop', 'TELESKOPIK - DORT HRK. + IKI SBT.')], max_length=30, verbose_name='Kapi Tipi')),
                ('pass_width', models.PositiveSmallIntegerField(verbose_name='Gecis Genisligi')),
                ('pass_height', models.PositiveSmallIntegerField(verbose_name='Gecis Yüksekligi')),
                ('total_width', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Toplam Genislik')),
                ('total_height', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Toplam Yükseklik')),
                ('mechanism_width', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Mekanizma Genisligi')),
                ('options', models.CharField(blank=True, max_length=250, null=True, verbose_name='Opsiyonlar')),
                ('radar_activations', models.CharField(blank=True, max_length=250, null=True, verbose_name='RADAR ve AKTIVASYON SECENEKLERI')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SLD Kayar Kapilar',
                'verbose_name_plural': 'SLDs',
                'db_table': 'SLD',
            },
        ),
    ]
