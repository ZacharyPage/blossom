# Generated by Django 2.1.3 on 2018-11-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=1000)),
                ('alcoholic', models.BooleanField(default=False)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(choices=[('Appetizer', 'Appetizer'), ('Entree', 'Entree'), ('Dessert', 'Dessert')], default='Entree', max_length=9)),
                ('item_name', models.CharField(max_length=1000)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
    ]