# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 19:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiveawayEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=1, verbose_name='auth.User')),
                ('giveaway', models.PositiveIntegerField(default=1, verbose_name='Giveaway')),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
                ('updated', models.DateField(default=django.utils.timezone.now)),
                ('total_points', models.IntegerField(default=0)),
                ('facebook_share_count', models.IntegerField(default=0)),
                ('twitter_share_count', models.IntegerField(default=0)),
                ('google_plus_share_count', models.IntegerField(default=0)),
                ('stumble_share_count', models.IntegerField(default=0)),
                ('linked_share_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='giveaway',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='description',
            field=models.TextField(default='No description avaiable'),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='ending_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='entries',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='g_name',
            field=models.CharField(default='my giveaway', max_length=55),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='image',
            field=models.ImageField(null=True, upload_to='giveaways/Img/'),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='p_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='price',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='updated',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='actual_price',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='software', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(null=True, upload_to='Products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='p_name',
            field=models.CharField(default='product', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='product_file',
            field=models.FileField(blank=True, null=True, upload_to='doc_files'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='product',
            name='screenshot2',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='screenshot3',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]