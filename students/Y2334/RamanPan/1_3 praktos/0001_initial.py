# Generated by Django 3.1.7 on 2021-03-08 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_number', models.CharField(max_length=15)),
                ('mark', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='car_owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=30)),
                ('Date_of_Birth', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='driver_license',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_license_id', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('date_of_receipt', models.DateTimeField()),
                ('car_owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.car_owner')),
            ],
        ),
        migrations.CreateModel(
            name='car_ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True)),
                ('auto_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.auto')),
                ('car_owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.car_owner')),
            ],
        ),
        migrations.AddField(
            model_name='car_owner',
            name='car_ownerships',
            field=models.ManyToManyField(through='blog.car_ownership', to='blog.auto'),
        ),
    ]
