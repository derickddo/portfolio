# Generated by Django 5.1 on 2024-09-21 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_userprofile_link_to_resume_userprofile_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuingOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, help_text="Upload a picture of the organization's logo here.", null=True, upload_to='', verbose_name='Organization Logo')),
            ],
            options={
                'db_table': 'issuing_organization',
            },
        ),
        migrations.AddField(
            model_name='certification',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload a picture of your certificate here.', null=True, upload_to='', verbose_name='Certificate Image'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='issuing_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.issuingorganization'),
        ),
    ]
