# Generated by Django 4.2.4 on 2023-10-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_classform_faculty_in_charge_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classform",
            name="Number_of_Tut_Sections",
            field=models.IntegerField(
                null=True, verbose_name=" Number of Tut Sections"
            ),
        ),
    ]
