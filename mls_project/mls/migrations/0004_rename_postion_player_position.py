# Generated by Django 4.1 on 2022-08-31 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mls', '0003_player_age_player_goals_player_injured_player_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='postion',
            new_name='position',
        ),
    ]