# Generated by Django 4.2.3 on 2023-07-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=2100)),
                ('city', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
    ]