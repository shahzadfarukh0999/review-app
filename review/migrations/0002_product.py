# Generated by Django 2.1.3 on 2018-12-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1024)),
                ('product_category', models.CharField(choices=[('Desi', 'Desi'), ('FastFood', 'FastFood'), ('Pizza', 'Pizza'), ('Rice', 'Rice'), ('Chinese', 'Chinese'), ('Indian', 'Indian')], max_length=50)),
            ],
        ),
    ]
