# Generated by Django 4.1.2 on 2022-11-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_info", "0009_blood_remove_appointment_dept"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ambulance",
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
                ("type", models.CharField(max_length=50)),
                ("source", models.CharField(max_length=50)),
                ("to", models.CharField(max_length=50)),
                ("dep", models.DateField()),
                ("nop", models.IntegerField()),
                ("contactno", models.IntegerField()),
                ("dtime", models.TimeField()),
                ("dadd", models.CharField(max_length=50)),
                ("oxygen", models.CharField(max_length=50)),
            ],
        ),
    ]
