# Generated by Django 2.2.5 on 2019-12-06 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruits', '0004_auto_20191125_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruits.Question'),
        ),
    ]
