# Generated by Django 3.2.4 on 2021-06-24 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_testimonies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonies',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='testimonies',
            name='t_name',
        ),
    ]