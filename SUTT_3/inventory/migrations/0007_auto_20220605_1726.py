# Generated by Django 3.2.5 on 2022-06-05 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20220605_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='issue_details',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.issueitem'),
        ),
        migrations.DeleteModel(
            name='Issue',
        ),
    ]
