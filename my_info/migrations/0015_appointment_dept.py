# Generated by Django 4.1.2 on 2022-11-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_info", "0014_alter_appointment_email_alter_contactus_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="dept",
            field=models.CharField(max_length=50, null=True),
        ),
    ]