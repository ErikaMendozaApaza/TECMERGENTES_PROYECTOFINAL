# Generated by Django 4.2.4 on 2023-09-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactPageSEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=500, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
