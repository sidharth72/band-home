# Generated by Django 4.2.1 on 2023-05-22 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venue', '__first__'),
        ('booking', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('members', models.ManyToManyField(blank=True, related_name='shift_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='booking.booking')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='shift.group')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('my_view_shift', 'View shift'),),
            },
        ),
        migrations.CreateModel(
            name='DefaultShiftSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shiftsets', to='venue.venue')),
            ],
        ),
        migrations.CreateModel(
            name='DefaultShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='default_shifts', to='shift.group')),
                ('shiftset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='shift.defaultshiftset')),
            ],
        ),
    ]
