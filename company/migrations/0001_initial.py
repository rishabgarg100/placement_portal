# Generated by Django 2.2.3 on 2019-08-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('CTC', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('Profile', models.TextField(default='software')),
                ('description', models.TextField()),
            ],
        ),
    ]