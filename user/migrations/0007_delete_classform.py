# Generated by Django 4.2.4 on 2023-10-15 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_alter_classform_faculty_in_charge_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="classform",
        ),
    ]
