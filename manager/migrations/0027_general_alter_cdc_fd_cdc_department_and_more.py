# Generated by Django 4.2.9 on 2024-03-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0026_alter_faculty_list_department_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="General",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "General_ID",
                    models.CharField(max_length=20, verbose_name="General_ID"),
                ),
                (
                    "General_name",
                    models.CharField(max_length=50, verbose_name="General_name"),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="cdc_fd",
            name="CDC_Department",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH ", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("Computer Science", " Computer Science"),
                    ("PHY", " Physics"),
                    ("BIO", " Biology"),
                    ("CHEM", "Chemistry"),
                    ("MATH", "Mathematics"),
                    ("ECON", "Economics"),
                    ("HUM", "Humanities"),
                ],
                max_length=50,
                verbose_name="Department name",
            ),
        ),
        migrations.AlterField(
            model_name="cdc_hd",
            name="CDC_HD_Department",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH ", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("Computer Science", " Computer Science"),
                    ("PHY", " Physics"),
                    ("BIO", " Biology"),
                    ("CHEM", "Chemistry"),
                    ("MATH", "Mathematics"),
                    ("ECON", "Economics"),
                    ("HUM", "Humanities"),
                ],
                max_length=50,
                verbose_name="Department name",
            ),
        ),
        migrations.AlterField(
            model_name="elective_fd",
            name="Elective_Department",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH ", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("Computer Science", " Computer Science"),
                    ("PHY", " Physics"),
                    ("BIO", " Biology"),
                    ("CHEM", "Chemistry"),
                    ("MATH", "Mathematics"),
                    ("ECON", "Economics"),
                    ("HUM", "Humanities"),
                ],
                max_length=50,
                verbose_name="Department name",
            ),
        ),
        migrations.AlterField(
            model_name="elective_hd",
            name="Elective_HD_Department",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH ", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("Computer Science", " Computer Science"),
                    ("PHY", " Physics"),
                    ("BIO", " Biology"),
                    ("CHEM", "Chemistry"),
                    ("MATH", "Mathematics"),
                    ("ECON", "Economics"),
                    ("HUM", "Humanities"),
                ],
                max_length=50,
                verbose_name="Department name",
            ),
        ),
        migrations.AlterField(
            model_name="files",
            name="department",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH ", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("Computer Science", " Computer Science"),
                    ("PHY", " Physics"),
                    ("BIO", " Biology"),
                    ("CHEM", "Chemistry"),
                    ("MATH", "Mathematics"),
                    ("ECON", "Economics"),
                    ("HUM", "Humanities"),
                ],
                max_length=50,
                verbose_name="Department name",
            ),
        ),
        migrations.AlterField(
            model_name="wilp",
            name="WILP_Department",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH ", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("Computer Science", " Computer Science"),
                    ("PHY", " Physics"),
                    ("BIO", " Biology"),
                    ("CHEM", "Chemistry"),
                    ("MATH", "Mathematics"),
                    ("ECON", "Economics"),
                    ("HUM", "Humanities"),
                ],
                max_length=50,
                verbose_name="Department name",
            ),
        ),
    ]
