# Generated by Django 5.1.3 on 2024-12-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_student_admno'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='student_images/'),
        ),
    ]
