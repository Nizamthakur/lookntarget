# Generated by Django 4.2.1 on 2023-06-26 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_options_alter_blog_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('id',), 'verbose_name_plural': 'blog'},
        ),
    ]