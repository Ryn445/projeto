# Generated by Django 5.1.3 on 2024-12-13 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advogados', '0002_remove_advogado_email_alter_advogado_especializacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advogado',
            name='email',
            field=models.EmailField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
