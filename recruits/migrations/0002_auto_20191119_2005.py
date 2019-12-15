# Generated by Django 2.2.5 on 2019-11-19 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='recruits.Question'),
        ),
        migrations.AlterField(
            model_name='recruitstatus',
            name='recruit',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recruits.Recruit'),
        ),
    ]
