# from django.db import models
# from django.forms import ModelForm

# # Create your models here.
# class Player(models.Model):
# 	name = models.CharField(max_length=100)
# 	team_id = models.IntegerField()
# 	season_year = models.IntegerField()
# 	player_id = models.IntegerField()
# 	date_of_birth = models.DateField()
# 	position = models.CharField(max_length=50)
# 	height = models.DecimalField(max_digits=3, decimal_places=2)
# 	weight = models.DecimalField(max_digits=3, decimal_places=2)

# 	class Meta:
# 		db_table = 'website_player'


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CheckUp(models.Model):
    check_up_date = models.IntegerField(primary_key=True)
    bp = models.IntegerField()
    cholestrol = models.IntegerField()
    bpm = models.IntegerField()
    oxygen = models.IntegerField()
    injuries = models.CharField(max_length=100)
    support_id_p = models.ForeignKey('Physiotherapist', models.DO_NOTHING, db_column='support_id_p')
    support_id_d = models.ForeignKey('Dietician', models.DO_NOTHING, db_column='support_id_d')

    class Meta:
        managed = False
        db_table = 'check_up'


class Coach(models.Model):
    start_year = models.DateField()
    support = models.OneToOneField('SupportStaff', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'coach'


class Coaches(models.Model):
    support = models.ForeignKey(Coach, models.DO_NOTHING)
    team_id = models.IntegerField(primary_key=True)
    year_field = models.DateField(db_column='year_')  # Field renamed because it ended with '_'.
    player = models.ForeignKey('Player', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coaches'
        unique_together = (('team_id', 'year_field', 'support'),)


class Contract(models.Model):
    start_year = models.IntegerField(primary_key=True)
    end_year = models.IntegerField()
    fa_year = models.IntegerField()
    salary = models.IntegerField()
    aav = models.IntegerField()
    player = models.ForeignKey('Player', models.DO_NOTHING)
    approval_status = models.CharField(max_length=5)
    support = models.ForeignKey('Manager', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contract'
        unique_together = (('start_year', 'player'),)


class Dietician(models.Model):
    avail_date = models.DateField()
    support = models.OneToOneField('SupportStaff', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dietician'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GoesFor(models.Model):
    check_up_date = models.OneToOneField(CheckUp, models.DO_NOTHING, db_column='check_up_date', primary_key=True)
    player = models.ForeignKey('Player', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goes_for'
        unique_together = (('check_up_date', 'player'),)


class HasMatchStats(models.Model):
    fgm = models.IntegerField(db_column='FGM')  # Field name made lowercase.
    fga = models.IntegerField(db_column='FGA')  # Field name made lowercase.
    fg_percent = models.FloatField(db_column='FG_percent')  # Field name made lowercase.
    fg3m = models.IntegerField(db_column='FG3M')  # Field name made lowercase.
    fg3a = models.IntegerField(db_column='FG3A')  # Field name made lowercase.
    fg3_percent = models.FloatField(db_column='FG3_percent')  # Field name made lowercase.
    ftm = models.IntegerField(db_column='FTM')  # Field name made lowercase.
    fta = models.IntegerField(db_column='FTA')  # Field name made lowercase.
    ft_percent = models.FloatField(db_column='FT_percent')  # Field name made lowercase.
    offensive_rebound = models.IntegerField(db_column='Offensive_rebound')  # Field name made lowercase.
    defensive_rebounds = models.IntegerField(db_column='Defensive_rebounds')  # Field name made lowercase.
    rebounds = models.IntegerField()
    assists = models.IntegerField()
    steals = models.IntegerField()
    blocked_shots = models.IntegerField()
    turnovers = models.IntegerField()
    personal_fouls = models.IntegerField()
    points_scored = models.IntegerField()
    player = models.OneToOneField('Player', models.DO_NOTHING, primary_key=True)
    match = models.ForeignKey('Matches', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'has_match_stats'
        unique_together = (('player', 'match'),)


class Manager(models.Model):
    support = models.OneToOneField('SupportStaff', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'manager'


class Matches(models.Model):
    match_id = models.IntegerField(primary_key=True)
    match_date = models.DateField()
    home_points = models.IntegerField()
    away_points = models.IntegerField()
    season = models.IntegerField()
    opponent_team = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    arena = models.CharField(max_length=100)
    home_fg_per = models.FloatField()
    away_fg_per = models.FloatField()
    home_ft_per = models.FloatField()
    away_ft_per = models.FloatField()
    home_3_per = models.FloatField()
    away_3_per = models.FloatField()
    home_assists = models.IntegerField()
    away_assists = models.IntegerField()
    home_rebounds = models.IntegerField()
    away_rebounds = models.IntegerField()
    home_wins = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'matches'


class Physiotherapist(models.Model):
    available_dates = models.DateField()
    support = models.OneToOneField('SupportStaff', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'physiotherapist'


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=1000)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    pos = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


# class Plays(models.Model):
#     match = models.OneToOneField(Matches, models.DO_NOTHING, primary_key=True)
#     team = models.ForeignKey('Team', models.DO_NOTHING)
#     year_field = models.ForeignKey('Team', models.DO_NOTHING, db_column='year_')  # Field renamed because it ended with '_'.

#     class Meta:
#         managed = False
#         db_table = 'plays'


class Schedule(models.Model):
    schedule_id = models.IntegerField(primary_key=True)
    practice_date = models.DateField()
    practice_day = models.CharField(max_length=1)
    practice_time = models.IntegerField()
    no_of_hours = models.IntegerField()
    session_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'schedule_'


class SupportStaff(models.Model):
    support_id = models.CharField(primary_key=True, max_length=10)
    support_name = models.CharField(max_length=1000)
    employment_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'support_staff'


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=100)
    year_field = models.DateField(db_column='year_')  # Field renamed because it ended with '_'.
    player = models.ForeignKey(Player, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team'
        unique_together = (('team_id', 'year_field'),)


class Updates(models.Model):
    schedule = models.OneToOneField(Schedule, models.DO_NOTHING, primary_key=True)
    support = models.ForeignKey(Coach, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'updates'
        unique_together = (('schedule', 'support'),)


class WebsitePlayer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    team_id = models.IntegerField()
    season_year = models.IntegerField()
    player_id = models.IntegerField()
    date_of_birth = models.DateField()
    height = models.DecimalField(max_digits=3, decimal_places=2)
    position = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'website_player'
