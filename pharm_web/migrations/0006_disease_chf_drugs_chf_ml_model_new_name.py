# Generated by Django 4.2.1 on 2024-11-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharm_web', '0005_alter_adverse_effects_medscape_adverse_effects_name_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='disease_chf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='drugs_chf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='ml_model',
            name='New_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]