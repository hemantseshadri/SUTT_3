# Generated by Django 3.2.5 on 2022-06-04 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20220604_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='issue_details',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.issue'),
        ),
    ]