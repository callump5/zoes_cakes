# Generated by Django 2.1.1 on 2018-09-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180916_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null='True', upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null='True', upload_to='uploads'),
        ),
    ]
