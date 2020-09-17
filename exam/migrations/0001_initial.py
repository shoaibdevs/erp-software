# Generated by Django 3.0.8 on 2020-09-15 10:26

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChessBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', jsonfield.fields.JSONField(default={'marks': ' ', 'subject': ' '})),
            ],
        ),
        migrations.CreateModel(
            name='Exam_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('Class', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='student.Class')),
                ('course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='student.Courses')),
                ('student', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('subject', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='student.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('start_date', models.DateField()),
                ('exam_type', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.Exam_type')),
            ],
        ),
    ]
