# Generated by Django 4.1.1 on 2023-01-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content_image',
            name='file',
            field=models.FileField(null=True, upload_to='Content_image'),
        ),
        migrations.AlterField(
            model_name='main_image',
            name='file',
            field=models.FileField(null=True, upload_to='Main_image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_uz',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='social_media',
            name='item',
            field=models.FileField(null=True, upload_to='Social_media'),
        ),
    ]
