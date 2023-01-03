# Generated by Django 4.1.4 on 2023-01-03 23:31

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_clearancefile_submission_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='abstract_document_file',
            field=models.FileField(blank=True, editable=False, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='clearancefile',
            name='evidence_of_payment_file',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='clearancefile',
            name='submission_file',
            field=models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='clearancefile',
            name='submission_type',
            field=models.CharField(choices=[('Manuscript', 'Manuscript'), ('Exhibition', 'Exhibition'), ('Advert', 'Advert'), ('Registration', 'Registration')], max_length=20),
        ),
    ]
