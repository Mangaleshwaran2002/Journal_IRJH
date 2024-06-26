# Generated by Django 4.2.7 on 2024-02-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='editor title')),
                ('name', models.CharField(max_length=150, verbose_name='editor name')),
                ('bio', models.TextField(verbose_name='editor bio')),
                ('location', models.CharField(blank=True, max_length=250, null=True, verbose_name='editor location')),
                ('email', models.EmailField(max_length=254, verbose_name='editor email')),
            ],
        ),
    ]
