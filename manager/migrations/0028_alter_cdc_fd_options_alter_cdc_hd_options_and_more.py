# Generated by Django 4.2.9 on 2024-04-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0027_general_alter_cdc_fd_cdc_department_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cdc_fd",
            options={"ordering": ["CDC_name"]},
        ),
        migrations.AlterModelOptions(
            name="cdc_hd",
            options={"ordering": ["CDC_HD_name"]},
        ),
        migrations.AlterModelOptions(
            name="elective_fd",
            options={"ordering": ["Elective_name"]},
        ),
        migrations.AlterModelOptions(
            name="elective_hd",
            options={"ordering": ["Elective_HD_name"]},
        ),
        migrations.AlterModelOptions(
            name="faculty_list",
            options={"ordering": ["first_name"]},
        ),
        migrations.AlterModelOptions(
            name="phd_list",
            options={"ordering": ["first_name"]},
        ),
        migrations.AlterModelOptions(
            name="wilp",
            options={"ordering": ["WILP_name"]},
        ),
        migrations.AlterField(
            model_name="cdc_fd",
            name="CDC_Department",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("CS", "CS"),
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
                    ("MECH", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("CS", "CS"),
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
            model_name="department_description",
            name="Department_name",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("CS", "CS"),
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
                    ("MECH", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("CS", "CS"),
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
                    ("MECH", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("CS", "CS"),
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
            model_name="faculty_list",
            name="Department",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("CS", "CS"),
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
                    ("MECH", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("CS", "CS"),
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
            model_name="phd_list",
            name="Department",
            field=models.CharField(
                choices=[
                    ("CHE", "Chemical"),
                    ("MECH", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("CS", "CS"),
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
                    ("MECH", "Mechanical"),
                    ("EEE", "Electrical"),
                    ("CS", "CS"),
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
