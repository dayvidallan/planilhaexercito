# Generated by Django 3.0.4 on 2022-12-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20201119_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('DENTISTA', 'Dentista'), ('TÉCNICO', 'Técnico')], default='TÉCNICO', help_text='* Campos obrigatórios', max_length=15, verbose_name='Tipo do usuário *'),
        ),
    ]
