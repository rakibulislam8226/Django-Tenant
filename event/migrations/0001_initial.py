# Generated by Django 4.1.5 on 2023-01-24 13:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_tenants.postgresql_backend.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_alter_client_options_remove_client_created_on_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(db_index=True, max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('redirected', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('event_name', models.CharField(max_length=255)),
                ('event_description', models.TextField(blank=True, null=True)),
                ('launched', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('registration_deadline', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('event_start', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('event_end', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('archive_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('event_code', models.CharField(blank=True, max_length=11, null=True)),
                ('event_status', models.CharField(choices=[('A', 'Active'), ('P', 'Pending'), ('C', 'Completed')], default='P', max_length=1)),
                ('event_type', models.CharField(choices=[('R', 'Registration'), ('P', 'Presentation Management'), ('M', 'Registration + Presentation Management')], default='R', max_length=1)),
                ('event_category', models.CharField(choices=[('1', 'Conference'), ('2', 'Meeting'), ('3', 'Seminar'), ('4', 'Training Session'), ('5', 'Trade Show'), ('6', 'Webinar'), ('7', 'Incentive Trip'), ('8', 'Other / General'), ('9', 'Sport Event'), ('10', 'Reunion'), ('11', 'Holiday'), ('12', 'Celebration'), ('13', 'Save The Date'), ('14', 'Fundraiser / Benefit'), ('15', 'Forum'), ('16', 'Political Event'), ('17', 'Dinner')], default='8', max_length=2)),
                ('internal_note', models.TextField(blank=True, max_length=300, null=True)),
                ('language', models.CharField(blank=True, max_length=30, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('event_passcode', models.CharField(blank=True, max_length=255, null=True)),
                ('display_policy', models.BooleanField(default=False)),
                ('cookie_notification', models.BooleanField(default=False)),
                ('domain_name', models.CharField(blank=True, max_length=253, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='events', to='client.client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(db_index=True, default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='event.event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]