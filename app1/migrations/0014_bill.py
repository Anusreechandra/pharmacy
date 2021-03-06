# Generated by Django 4.0.3 on 2022-04-13 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_medicine_purchace_price_medicine_selling_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.medicine')),
            ],
            options={
                'db_table': 'bill',
            },
        ),
    ]
