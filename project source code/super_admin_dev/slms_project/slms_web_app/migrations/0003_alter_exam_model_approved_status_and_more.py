# Generated by Django 4.0.3 on 2022-05-10 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slms_web_app', '0002_assignment_model_approved_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='approved_status',
            field=models.CharField(choices=[('1', 'Approved'), ('2', 'Rejected'), ('3', 'Pending')], default='3', max_length=1),
        ),
        migrations.AlterField(
            model_name='exam_paper_detail',
            name='exam_end_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 14, 52, 19, 837820)),
        ),
        migrations.AlterField(
            model_name='exam_paper_detail',
            name='exam_start_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 14, 52, 19, 837820)),
        ),
    ]
