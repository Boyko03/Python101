# Generated by Django 3.0.6 on 2020-05-25 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lecture_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('lecture_name', models.CharField(max_length=255)),
                ('week', models.IntegerField()),
                ('URL', models.URLField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Course')),
            ],
        ),
    ]