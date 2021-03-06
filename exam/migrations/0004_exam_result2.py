# Generated by Django 3.0.8 on 2020-09-15 12:36

from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('exam', '0003_remove_exam_result_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_result2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=None)),
                ('course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='student.Courses')),
                ('student', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('subject', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='student.Subject')),
            ],
        ),
    ]
