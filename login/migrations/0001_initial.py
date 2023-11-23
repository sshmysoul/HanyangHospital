# Generated by Django 4.2.6 on 2023-11-23 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('doc_id', models.AutoField(max_length=15, primary_key=True, serialize=False)),
                ('doc_name', models.CharField(max_length=20)),
                ('doc_email', models.EmailField(max_length=30)),
                ('doc_pwd', models.CharField(max_length=20)),
            ],
        ),
    ]