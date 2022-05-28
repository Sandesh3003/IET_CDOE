# Generated by Django 4.0.4 on 2022-05-26 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_course_head_delete_courses_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_type',
            fields=[
                ('type_id', models.CharField(max_length=100)),
                ('course_type', models.CharField(max_length=200, primary_key='True', serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='course_head',
            name='card_image',
            field=models.ImageField(null=True, upload_to='images/course_image/'),
        ),
        migrations.AddField(
            model_name='course_head',
            name='course_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course_type'),
        ),
    ]
