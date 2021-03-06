# Generated by Django 3.2.4 on 2021-06-24 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0007_auto_20210623_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_title', models.CharField(max_length=100)),
                ('t_body', models.TextField()),
                ('t_date', models.DateTimeField(auto_now_add=True)),
                ('t_file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('t_audio_file', models.FileField(blank=True, help_text='upload audio recordings', null=True, upload_to='audio/')),
                ('t_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
