# Generated by Django 3.1.3 on 2020-11-29 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amigosecreto', '0003_friend_gift_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='gift_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amigosecreto.friend'),
        ),
    ]