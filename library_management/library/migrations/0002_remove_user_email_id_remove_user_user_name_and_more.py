# Generated by Django 4.0.6 on 2022-07-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
