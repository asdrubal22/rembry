# Generated by Django 3.2.2 on 2022-10-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0005_auto_20221021_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=100)),
            ],
        ),
    ]
