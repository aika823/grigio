# Generated by Django 3.2.6 on 2021-08-24 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0004_merge_0003_auto_20190323_0543_0003_auto_20200923_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.RemoveField(
            model_name='fcuser',
            name='useremail',
        ),
        migrations.RemoveField(
            model_name='fcuser',
            name='username',
        ),
    ]
