# Generated by Django 3.0.8 on 2020-09-15 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='franchiseregistration',
            name='city',
        ),
        migrations.RemoveField(
            model_name='franchiseregistration',
            name='user',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='FranchiseRegistration',
        ),
    ]