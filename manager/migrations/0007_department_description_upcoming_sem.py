# Generated by Django 4.2.4 on 2023-11-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0006_alter_cdc_fd_cdc_department_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="department_description",
            name="Upcoming_Sem",
            field=models.CharField(
                choices=[("Sem 1", "Sem 1"), ("Sem 2", "Sem 2")],
                max_length=50,
                null=True,
                verbose_name="Upcoming Semester",
            ),
        ),
    ]
