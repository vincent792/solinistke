# Generated by Django 4.2.5 on 2023-10-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('username', models.CharField(max_length=255)),
            ],
        ),
    ]
