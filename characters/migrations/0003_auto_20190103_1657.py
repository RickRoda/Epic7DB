# Generated by Django 2.1.4 on 2019-01-03 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20190103_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_skills', to='skills.Skill'),
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
