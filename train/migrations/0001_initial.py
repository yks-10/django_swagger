# Generated by Django 4.0.1 on 2022-01-21 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=40)),
                ('train_no', models.CharField(max_length=6, unique=True)),
                ('starting_at', models.CharField(max_length=30)),
                ('ending_at', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('d_date', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passanger_name', models.CharField(max_length=100, unique=True)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='train.train')),
            ],
        ),
        migrations.CreateModel(
            name='Bookedby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Train', to='train.book')),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.train')),
            ],
            options={
                'unique_together': {('train', 'booked_by')},
            },
        ),
    ]