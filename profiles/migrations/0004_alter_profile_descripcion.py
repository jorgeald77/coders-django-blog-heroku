# Generated by Django 4.0.5 on 2022-06-26 02:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_foto_alter_profile_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bio'),
        ),
    ]
