# Generated by Django 2.2.2 on 2019-09-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190920_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='acctype',
            field=models.CharField(choices=[('company', '企業アカウント'), ('general', '一般アカウント')], default='general', max_length=100),
        ),
    ]
