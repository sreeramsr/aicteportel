# Generated by Django 5.1 on 2024-08-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstituteApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=255)),
                ('application_id', models.CharField(max_length=100)),
                ('contact_details', models.TextField()),
                ('faculty_details', models.TextField()),
                ('programme_course', models.TextField()),
                ('infrastructure_library', models.TextField()),
                ('ter_charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
    ]
