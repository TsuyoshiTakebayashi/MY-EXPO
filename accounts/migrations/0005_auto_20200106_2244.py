# Generated by Django 2.2.2 on 2020-01-06 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200106_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_post', to='posts.Post'),
        ),
    ]
