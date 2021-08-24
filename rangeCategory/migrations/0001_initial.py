# Generated by Django 3.0.6 on 2021-08-24 09:06

import authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import rangeCategory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_value', models.IntegerField()),
                ('max_value', models.IntegerField()),
                ('charge_type', models.CharField(choices=[('percentage', 'Percentage'), ('quantity', 'Quantity')], default='percentage', max_length=50)),
                ('charge_amount', models.IntegerField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('in_category', models.ForeignKey(default=rangeCategory.models.Category, null=True, on_delete=django.db.models.deletion.CASCADE, to='rangeCategory.Category')),
                ('user', models.ForeignKey(default=authentication.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
