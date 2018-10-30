# Generated by Django 2.1.1 on 2018-10-30 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('para1', models.CharField(max_length=200)),
                ('para2', models.CharField(max_length=200)),
                ('para3', models.CharField(max_length=200)),
                ('para4', models.CharField(max_length=200)),
                ('para5', models.CharField(max_length=200)),
                ('para6', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('para1', models.CharField(max_length=200)),
                ('para2', models.CharField(max_length=200)),
                ('para3', models.CharField(max_length=200)),
                ('para4', models.CharField(max_length=200)),
                ('para5', models.CharField(max_length=200)),
                ('para6', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PoolMux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='machine.Miner')),
                ('pool', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='machine.Pool')),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]
