# Generated by Django 4.2.1 on 2023-07-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0002_car_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'FAQ',
                'db_table': 'faq',
                'ordering': ('id',),
            },
        ),
    ]
