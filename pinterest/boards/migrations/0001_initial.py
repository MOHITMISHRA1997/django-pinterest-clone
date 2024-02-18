# Generated by Django 4.2.9 on 2024-01-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover', models.ImageField(default='boards/default.png', upload_to='boards')),
                ('is_private', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
    ]