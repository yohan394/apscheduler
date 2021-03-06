# Generated by Django 3.1.7 on 2021-04-14 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_status', models.CharField(choices=[('A', 'ACTIVE'), ('I', 'INACTIVE')], default='A', max_length=1)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('bank_type', models.CharField(max_length=30, null=True)),
                ('account_number', models.CharField(max_length=70, null=True)),
                ('age', models.IntegerField(null=True)),
                ('reg_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TestFlowModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
