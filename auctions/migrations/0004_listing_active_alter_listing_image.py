# Generated by Django 5.0.7 on 2024-08-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_category_title_alter_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.CharField(max_length=256),
        ),
    ]
