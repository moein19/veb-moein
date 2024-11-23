# Generated by Django 5.0.6 on 2024-07-21 13:39

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bloggers', '0001_initial'),
        ('posts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('post_id', models.IntegerField()),
                ('comment_text', models.TextField()),
                ('blogger', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='bloggers.blogger')),
                ('post_title', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='posts.post')),
            ],
        ),
    ]
