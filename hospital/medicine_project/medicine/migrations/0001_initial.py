# Generated by Django 4.1.7 on 2023-03-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255)),
                ('recomendation', models.TextField()),
                ('code', models.CharField(max_length=255)),
                ('observations', models.TextField()),
                ('bibliography', models.TextField()),
            ],
        ),
    ]