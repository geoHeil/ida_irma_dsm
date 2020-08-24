# Generated by Django 3.0.3 on 2020-07-30 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ida_core', '0014_achievementrelation_achievement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearcherType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='accessmode',
            name='access_mode_researcher_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ida_core.ResearcherType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumer',
            name='researcher_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ida_core.ResearcherType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectgroup',
            name='access_mode_researcher_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ida_core.ResearcherType'),
            preserve_default=False,
        ),
    ]