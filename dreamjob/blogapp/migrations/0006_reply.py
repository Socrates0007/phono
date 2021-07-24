# Generated by Django 3.2.4 on 2021-06-23 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_comment_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_user', models.CharField(max_length=50)),
                ('reply', models.TextField()),
                ('datef', models.DateTimeField(auto_now_add=True)),
                ('repl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blogapp.comment')),
            ],
        ),
    ]
