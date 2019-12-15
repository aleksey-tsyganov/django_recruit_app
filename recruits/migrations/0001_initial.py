# Generated by Django 2.2.5 on 2019-11-17 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('order_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruits.Planet')),
            ],
        ),
        migrations.CreateModel(
            name='RecruitStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('master', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recruits.Master')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruits.Recruit')),
            ],
        ),
        migrations.AddField(
            model_name='master',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruits.Planet'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruits.Question')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruits.Recruit')),
            ],
        ),
    ]
