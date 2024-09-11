# Generated by Django 5.1.1 on 2024-09-11 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LiveChat', '0002_client_thread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='LiveChat.client'),
        ),
    ]
