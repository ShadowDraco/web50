# Generated by Django 5.0.7 on 2024-08-07 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_listing_watchlist_user_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(to='auctions.listing'),
        ),
    ]
