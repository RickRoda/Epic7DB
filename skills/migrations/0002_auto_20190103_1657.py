# Generated by Django 2.1.4 on 2019-01-03 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belongs_to_character', to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
