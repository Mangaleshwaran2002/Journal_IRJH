# Generated by Django 4.2.7 on 2024-02-14 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manuscript', '0003_manuscript_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuscript',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Author', to=settings.AUTH_USER_MODEL, verbose_name='Manuscript author'),
        ),
    ]
