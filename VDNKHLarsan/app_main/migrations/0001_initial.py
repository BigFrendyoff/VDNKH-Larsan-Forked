# Generated by Django 4.0.4 on 2022-11-03 08:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('order', models.IntegerField(verbose_name='Порядок')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('pic_url', models.CharField(max_length=150)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('code', models.CharField(max_length=50, verbose_name='Код')),
                ('pic_url', models.URLField()),
                ('detail_pic_url', models.URLField()),
                ('places', models.ManyToManyField(related_name='route', to='app_main.place', verbose_name='Места')),
            ],
        ),
    ]
