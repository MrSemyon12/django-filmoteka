# Generated by Django 4.1.7 on 2023-03-21 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmoteka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('photo_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.SmallIntegerField()),
                ('poster_url', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('country', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('duration', models.SmallIntegerField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmoteka.director')),
            ],
        ),
    ]