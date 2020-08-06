# Generated by Django 3.0.3 on 2020-07-28 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ida_core', '0010_auto_20200727_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectgroup',
            name='access_mode_research_field',
        ),
        migrations.AddField(
            model_name='project',
            name='access_mode_research_field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ida_core.AccessModeResearchField'),
            preserve_default=False,
        ),
    ]
