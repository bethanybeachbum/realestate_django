# Generated by Django 4.2 on 2023-04-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate_app', '0006_alter_closing_closingdocumentspdf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['propertyAddress']},
        ),
        migrations.RemoveField(
            model_name='closing',
            name='propertyAddress',
        ),
        migrations.AddField(
            model_name='person',
            name='contracts',
            field=models.ManyToManyField(to='realestate_app.contract'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contractPDF',
            field=models.FileField(blank=True, help_text='Attach Contract', null=True, upload_to=''),
        ),
    ]
