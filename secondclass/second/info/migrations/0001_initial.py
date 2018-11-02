# Generated by Django 2.1.2 on 2018-11-01 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('population', models.IntegerField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('population', models.IntegerField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='div',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Division'),
        ),
    ]
