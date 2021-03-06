# Generated by Django 3.0.4 on 2020-12-03 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_auto_20201015_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ISBN',
            field=models.CharField(default='123', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='writer', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='publication',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=6),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(max_length=15)),
                ('profession', models.CharField(max_length=100)),
                ('interest', models.CharField(choices=[('FC', 'fiction'), ('ER', 'Engineering'), ('SC', 'Science'), ('MG', 'Managemetn'), ('LT', 'Literature'), ('AR', 'Arts'), ('SC', 'School Level'), ('RG', 'Religion'), ('LA', 'Law'), ('ET', 'Entrance Preparation'), ('GR', 'Government Jobs'), ('MI', 'Miscelleneous')], default='MI', max_length=100)),
                ('profile_image', models.ImageField(upload_to='media')),
                ('user_type', models.CharField(choices=[('IS', 'Individual Seller'), ('WS', 'Wholeseller'), ('OT', 'Other')], default='IS', max_length=100)),
                ('rating', models.CharField(max_length=50)),
                ('pradesh', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('palika', models.CharField(max_length=50)),
                ('ward_no', models.IntegerField()),
                ('local_add', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
