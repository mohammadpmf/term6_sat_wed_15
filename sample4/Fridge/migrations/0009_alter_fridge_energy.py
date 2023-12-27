# Generated by Django 4.0.5 on 2023-12-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fridge', '0008_alter_fridge_energy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridge',
            name='energy',
            field=models.CharField(choices=[('A+', 'خیلی عالی'), ('A', 'خیلی'), ('B', 'خوب')], max_length=4),
        ),
    ]
