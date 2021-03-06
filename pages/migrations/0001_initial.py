# Generated by Django 4.0.4 on 2022-05-25 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('studentID', models.CharField(max_length=8, unique=True)),
                ('Email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=3)),
                ('department', models.CharField(choices=[('Level 1', 'Level 1'), ('Level 2', 'Level 2'), ('Level 3', 'Level3'), ('Level 4', 'Level 4')], max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50)),
            ],
            options={
                'ordering': ['status', 'studentID'],
            },
        ),
    ]
