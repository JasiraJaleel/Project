# Generated by Django 4.2.6 on 2023-11-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_items_alter_student_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('year', models.DateField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='pics')),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
    ]