# Generated by Django 4.1.1 on 2023-01-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_item',
            name='picture',
            field=models.FileField(null=True, upload_to='About_item'),
        ),
        migrations.AlterField(
            model_name='sertificat',
            name='file',
            field=models.FileField(null=True, upload_to='Sertificat'),
        ),
    ]
