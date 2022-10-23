# Generated by Django 3.2.2 on 2022-10-22 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto', '0011_remove_proyecto_materiales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion_Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material', to='materiales.material')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto+', to='proyecto.proyecto')),
            ],
        ),
    ]
