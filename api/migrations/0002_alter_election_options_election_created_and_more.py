# Generated by Django 4.1.2 on 2023-04-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="election",
            options={"ordering": ["-created"]},
        ),
        migrations.AddField(
            model_name="election",
            name="created",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="election",
            name="running",
            field=models.BooleanField(default=True),
        ),
    ]