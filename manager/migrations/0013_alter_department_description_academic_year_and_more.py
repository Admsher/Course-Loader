# Generated by Django 4.2.9 on 2024-02-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0012_alter_department_description_upcoming_sem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department_description",
            name="Academic_year",
            field=models.CharField(
                choices=[
                    ("2023-2024", "2023-2024"),
                    ("2022-2023", "2022-2023"),
                    ("2021-2022", "2021-2022"),
                    ("2020-2021", "2020-2021"),
                    ("2019-2020", "2019-2020"),
                    ("2018-2019", "2018-2019"),
                    ("2017-2018", "2017-2018"),
                    ("2016-2017", "2016-2017"),
                    ("2015-2016", "2015-2016"),
                    ("2014-2015", "2014-2015"),
                ],
                max_length=50,
                null=True,
                verbose_name="Academic Year",
            ),
        ),
        migrations.AlterField(
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
