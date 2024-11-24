# Generated by Django 3.1.12 on 2024-11-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('crp', models.FloatField()),
                ('hgb', models.FloatField()),
                ('mcv', models.FloatField()),
                ('plt', models.FloatField()),
                ('rbc', models.FloatField()),
                ('wbc', models.FloatField()),
                ('diagnosis', models.CharField(max_length=255)),
            ],
        ),
    ]
