# Generated by Django 5.0.2 on 2024-04-27 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceData',
            fields=[
                ('roll_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('face_embeddings', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='facial_data',
        ),
    ]
