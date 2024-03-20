# Generated by Django 4.2.9 on 2024-03-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0015_rename_pnr_no_phd_list_psm_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="cdc_fd",
            name="Upcoming_Sem_FD",
            field=models.CharField(
                choices=[("Sem 1", "Sem 1"), ("Sem 2", "Sem 2")],
                max_length=50,
                null=True,
                verbose_name="Upcoming Semester",
            ),
        ),
        migrations.AddField(
            model_name="cdc_hd",
            name="Upcoming_Sem_HD",
            field=models.CharField(
                choices=[("Sem 1", "Sem 1"), ("Sem 2", "Sem 2")],
                max_length=50,
                null=True,
                verbose_name="Upcoming Semester",
            ),
        ),
        migrations.AddField(
            model_name="elective_fd",
            name="Upcoming_Sem_El_FD",
            field=models.CharField(
                choices=[("Sem 1", "Sem 1"), ("Sem 2", "Sem 2")],
                max_length=50,
                null=True,
                verbose_name="Upcoming Semester",
            ),
        ),
        migrations.AddField(
            model_name="elective_hd",
            name="Upcoming_Sem_El_HD",
            field=models.CharField(
                choices=[("Sem 1", "Sem 1"), ("Sem 2", "Sem 2")],
                max_length=50,
                null=True,
                verbose_name="Upcoming Semester",
            ),
        ),
    ]
