# Generated by Django 3.2.16 on 2022-10-27 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geoapps', '0006_geoapp_blob_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonSpatialDataset',
            fields=[
                ('geoapp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geoapps.geoapp')),
                ('url', models.URLField(help_text='Link to the dataset', max_length=2000)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('geoapps.geoapp',),
        ),
    ]
