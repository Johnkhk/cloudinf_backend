# Generated by Django 4.0.3 on 2022-04-02 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='summarizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(default='', max_length=50, unique=True)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]