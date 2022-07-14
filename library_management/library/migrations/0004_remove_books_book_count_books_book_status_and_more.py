# Generated by Django 4.0.6 on 2022-07-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_count',
        ),
        migrations.AddField(
            model_name='books',
            name='book_status',
            field=models.PositiveIntegerField(choices=[(0, 'BORROWED'), (1, 'AVAILABLE')], default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='borrwed_books',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
