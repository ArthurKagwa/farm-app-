# Generated by Django 5.1.4 on 2024-12-24 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_address', models.CharField(max_length=100)),
                ('staff_phone', models.CharField(max_length=10)),
                ('staff_email', models.EmailField(max_length=254)),
                ('staff_position', models.CharField(max_length=50)),
                ('staff_nin', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('animal_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('breed', models.CharField(max_length=50)),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='father_of', to='animal.animal')),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mother_of', to='animal.animal')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.type')),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_date', models.DateField()),
                ('treatment_name', models.CharField(max_length=50)),
                ('treatment_cost', models.FloatField()),
                ('treatment_description', models.CharField(max_length=100)),
                ('animal_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('event_description', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_location', models.CharField(max_length=50)),
                ('event_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=50)),
                ('task_description', models.CharField(max_length=100)),
                ('task_day', models.DateField()),
                ('task_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Task_log',
            fields=[
                ('task_log_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('task_log_date', models.DateField()),
                ('task_log_time', models.TimeField()),
                ('task_log_description', models.CharField(max_length=100)),
                ('task_log_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.staff')),
                ('task_log_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.task')),
            ],
        ),
    ]