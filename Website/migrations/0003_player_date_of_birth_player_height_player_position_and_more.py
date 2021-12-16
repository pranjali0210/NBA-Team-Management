# Generated by Django 4.0 on 2021-12-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_player_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='date_of_birth',
            field=models.DateField(default='2001-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]