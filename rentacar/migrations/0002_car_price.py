# Generated by Django 4.2.1 on 2023-06-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='car_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'car price',
                'db_table': 'carprice',
                'ordering': ('id',),
            },
        ),
    ]