# Generated by Django 3.0.1 on 2019-12-28 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tittle',
        ),
        migrations.AddField(
            model_name='post',
            name='collage',
            field=models.CharField(default='0', max_length=300),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='0', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='female',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='male',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='False', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='password',
            field=models.CharField(default='0', max_length=300),
        ),
        migrations.AddField(
            model_name='post',
            name='rollno',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
