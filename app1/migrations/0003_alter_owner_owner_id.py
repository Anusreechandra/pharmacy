# Generated by Django 4.0.3 on 2022-04-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_medicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]