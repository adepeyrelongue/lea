# Generated by Django 2.2.2 on 2019-06-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190625_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstpage',
            name='html_meta',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='firstpage',
            name='html_title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='html_meta',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='html_title',
            field=models.CharField(default='', max_length=500),
        ),
    ]
