# Generated by Django 4.0.4 on 2022-05-26 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_programs_program_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_head',
            fields=[
                ('course_id', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=200, primary_key='True', serialize=False)),
                ('program_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.programs')),
            ],
        ),
        migrations.DeleteModel(
            name='courses_header',
        ),
    ]
