# Generated by Django 4.0.3 on 2022-04-12 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_medicine_medicine_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='medicine_id',
            new_name='medi_id',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_image',
            field=models.ImageField(upload_to='medicine/'),
        ),
    ]
