# Generated by Django 4.2.4 on 2023-10-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Elective_FD",
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
                    "Elective_ID",
                    models.CharField(max_length=20, verbose_name="Elective_ID"),
                ),
                (
                    "ELective_name",
                    models.CharField(max_length=50, verbose_name="Elective_name"),
                ),
                (
                    "Elective_Department",
                    models.CharField(
                        choices=[
                            ("Chemical", "Chemical"),
                            ("Mechanical", "Mechanical"),
                            ("Electrical", "Electrical"),
                            ("Computer Science", "Computer Science"),
                            ("Physics", "Physics"),
                            ("Biology", "Biology"),
                            ("Chemistry", "Chemistry"),
                            ("Mathematics", "Mathematics"),
                        ],
                        max_length=100,
                        verbose_name="Elective_Department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Elective_HD",
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
                    "Elective_HD_ID",
                    models.CharField(max_length=20, verbose_name="Elective_ID"),
                ),
                (
                    "Elective_HD_name",
                    models.CharField(max_length=50, verbose_name="Elective_name"),
                ),
                (
                    "Elective_HD_Department",
                    models.CharField(
                        choices=[
                            ("Chemical", "Chemical"),
                            ("Mechanical", "Mechanical"),
                            ("Electrical", "Electrical"),
                            ("Computer Science", "Computer Science"),
                            ("Physics", "Physics"),
                            ("Biology", "Biology"),
                            ("Chemistry", "Chemistry"),
                            ("Mathematics", "Mathematics"),
                        ],
                        max_length=100,
                        verbose_name="Elective_Department",
                    ),
                ),
            ],
        ),
    ]
