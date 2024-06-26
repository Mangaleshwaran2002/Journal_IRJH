# Generated by Django 4.2.7 on 2024-02-17 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manuscript', '0005_rename_uder_review_manuscript_under_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuscript',
            name='co_authors',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Manuscript co-authors'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Author', to=settings.AUTH_USER_MODEL, verbose_name='Manuscript author'),
        ),
    ]
