# Generated by Django 4.2 on 2023-04-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate_app', '0007_alter_contract_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='closing',
            name='createDate',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='contract',
            name='AddDate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='contract',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='contractaction',
            name='AddDate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='contractaction',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='closing',
            name='closeDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contractDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='contractaction',
            name='actionDueDate',
            field=models.DateField(null=True),
        ),
    ]
