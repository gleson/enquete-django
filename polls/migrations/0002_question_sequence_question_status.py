# Generated by Django 4.0.3 on 2022-07-14 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='sequence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('1', 'Ativo'), ('0', 'Inativo')], default='1', max_length=1),
        ),
    ]
