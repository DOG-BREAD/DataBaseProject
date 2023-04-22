# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Active(models.Model):
    iname = models.OneToOneField('Items', models.DO_NOTHING, db_column='IName', primary_key=True)  # Field name made lowercase.
    cooldown = models.TextField(db_column='Cooldown', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'active'


class AffixBuffs(models.Model):
    internal_name = models.OneToOneField('StatusEffects', models.DO_NOTHING, db_column='Internal_name', primary_key=True)  # Field name made lowercase.
    power_of_elite = models.CharField(db_column='Power_of_elite', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'affix_buffs'


class Aiblacklist(models.Model):
    charactersname = models.OneToOneField('UnplayableCharacters', models.DO_NOTHING, db_column='charactersName', primary_key=True)  # Field name made lowercase. The composite primary key (charactersName, AIBlackList) found, that is not supported. The first column is selected.
    aiblacklist = models.CharField(db_column='AIBlackList', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aiblacklist'
        unique_together = (('charactersname', 'aiblacklist'),)


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


class Buffs(models.Model):
    internal_name = models.OneToOneField('StatusEffects', models.DO_NOTHING, db_column='internal_name', primary_key=True)
    helps_character = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buffs'


class Characters(models.Model):
    armor = models.IntegerField(db_column='Armor', blank=True, null=True)  # Field name made lowercase.
    basedamage = models.FloatField(db_column='BaseDamage', blank=True, null=True)  # Field name made lowercase.
    basehealth = models.IntegerField(db_column='BaseHealth', blank=True, null=True)  # Field name made lowercase.
    charactersname = models.CharField(db_column='charactersName', primary_key=True, max_length=80)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    health_regen = models.FloatField(db_column='Health_Regen', blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    icon = models.TextField(db_column='Icon', blank=True, null=True)  # Field name made lowercase.
    mvmtspeed = models.FloatField(db_column='MvmtSpeed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'characters'


class CooldownBuffs(models.Model):
    internal_name = models.OneToOneField('StatusEffects', models.DO_NOTHING, db_column='internal_name', primary_key=True)
    has_cool_down = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cooldown_buffs'


class Debuffs(models.Model):
    internal_name = models.OneToOneField('StatusEffects', models.DO_NOTHING, db_column='internal_name', primary_key=True)
    helps_enemy = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debuffs'


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


class Drone(models.Model):
    abilities = models.CharField(max_length=80, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    charactersname = models.OneToOneField('UnplayableCharacters', models.DO_NOTHING, db_column='charactersName', primary_key=True)  # Field name made lowercase.
    charname = models.ForeignKey('PlayableCharacters', models.DO_NOTHING, db_column='charName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drone'


class Enemies(models.Model):
    charactersname = models.OneToOneField('UnplayableCharacters', models.DO_NOTHING, db_column='charactersName', primary_key=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=80, blank=True, null=True)  # Field name made lowercase.
    sb_flag = models.IntegerField(db_column='SB_Flag', blank=True, null=True)  # Field name made lowercase.
    map_spawn_requirements = models.CharField(db_column='MAP_SPAWN_REQUIREMENTS', max_length=80, blank=True, null=True)  # Field name made lowercase.
    sm_flag = models.IntegerField(db_column='SM_Flag', blank=True, null=True)  # Field name made lowercase.
    special_spawn_requirements = models.CharField(max_length=80, blank=True, null=True)
    om_flag = models.CharField(db_column='OM_Flag', max_length=80, blank=True, null=True)  # Field name made lowercase.
    survivar_ally = models.CharField(max_length=80, blank=True, null=True)
    e_flag = models.CharField(db_column='E_flag', max_length=80, blank=True, null=True)  # Field name made lowercase.
    effect = models.CharField(db_column='Effect', max_length=80, blank=True, null=True)  # Field name made lowercase.
    damage_boost = models.CharField(max_length=80, blank=True, null=True)
    health_boost = models.CharField(max_length=80, blank=True, null=True)
    chance_to_drop_buff = models.CharField(db_column='Chance_to_drop_buff', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enemies'


class Environment(models.Model):
    envname = models.CharField(db_column='EnvName', primary_key=True, max_length=80)  # Field name made lowercase.
    stage = models.CharField(db_column='Stage', max_length=80, blank=True, null=True)  # Field name made lowercase.
    soundtrack = models.TextField(db_column='Soundtrack', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    lunar_seer_quotes = models.CharField(db_column='Lunar_Seer_Quotes', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'environment'


class Generates(models.Model):
    unplayable_char = models.OneToOneField('UnplayableCharacters', models.DO_NOTHING, db_column='Unplayable_char', primary_key=True)  # Field name made lowercase. The composite primary key (Unplayable_char, EnvName) found, that is not supported. The first column is selected.
    envname = models.ForeignKey(Environment, models.DO_NOTHING, db_column='EnvName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'generates'
        unique_together = (('unplayable_char', 'envname'),)


class Gives(models.Model):
    iname = models.OneToOneField('Items', models.DO_NOTHING, db_column='iname', primary_key=True)  # The composite primary key (iname, status_effect_name) found, that is not supported. The first column is selected.
    status_effect_name = models.ForeignKey('StatusEffects', models.DO_NOTHING, db_column='status_effect_name')

    class Meta:
        managed = False
        db_table = 'gives'
        unique_together = (('iname', 'status_effect_name'),)


class Items(models.Model):
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    rarity = models.CharField(db_column='Rarity', max_length=80, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=80, blank=True, null=True)  # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True, null=True)  # Field name made lowercase.
    iname = models.CharField(db_column='IName', primary_key=True, max_length=80)  # Field name made lowercase.
    charname = models.ForeignKey(Characters, models.DO_NOTHING, db_column='charName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'items'


class Passive(models.Model):
    stack = models.CharField(db_column='Stack', max_length=80, blank=True, null=True)  # Field name made lowercase.
    iname = models.OneToOneField(Items, models.DO_NOTHING, db_column='IName', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'passive'


class PlayableCharacters(models.Model):
    charname = models.ForeignKey(Characters, models.DO_NOTHING, db_column='CharName', blank=True, null=True)  # Field name made lowercase.
    mass = models.IntegerField(db_column='Mass', blank=True, null=True)  # Field name made lowercase.
    outfit_color = models.TextField(db_column='Outfit_color', blank=True, null=True)  # Field name made lowercase.
    dmg_scalar = models.FloatField(db_column='Dmg_Scalar', blank=True, null=True)  # Field name made lowercase.
    mvmtspeed_scalar = models.FloatField(db_column='MvmtSpeed_Scalar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playable_characters'


class Skills(models.Model):
    cname = models.ForeignKey(PlayableCharacters, models.DO_NOTHING, db_column='cName', blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='sName', primary_key=True, max_length=80)  # Field name made lowercase.
    icon = models.TextField(blank=True, null=True)
    cooldown = models.TextField(db_column='Cooldown', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=80, blank=True, null=True)  # Field name made lowercase.
    proc_coefficient = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'


class Spawns(models.Model):
    env = models.OneToOneField(Environment, models.DO_NOTHING, db_column='Env', primary_key=True)  # Field name made lowercase. The composite primary key (Env, Items) found, that is not supported. The first column is selected.
    items = models.ForeignKey(Items, models.DO_NOTHING, db_column='Items')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spawns'
        unique_together = (('env', 'items'),)


class Status(models.Model):
    current_character_status = models.CharField(db_column='Current_character_status', max_length=80, blank=True, null=True)  # Field name made lowercase.
    status_name = models.ForeignKey('StatusEffects', models.DO_NOTHING, db_column='Status_Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'status'


class StatusEffects(models.Model):
    internal_name = models.CharField(db_column='Internal_name', primary_key=True, max_length=80)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True, null=True)  # Field name made lowercase.
    effect = models.CharField(db_column='Effect', max_length=80, blank=True, null=True)  # Field name made lowercase.
    charname = models.ForeignKey(Characters, models.DO_NOTHING, db_column='CharName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'status_effects'


class UnplayableCharacters(models.Model):
    constant_speed = models.FloatField(db_column='Constant_Speed', blank=True, null=True)  # Field name made lowercase.
    ai_controlled = models.CharField(db_column='AI_Controlled', max_length=80, blank=True, null=True)  # Field name made lowercase.
    additional_damage = models.FloatField(db_column='Additional_Damage', blank=True, null=True)  # Field name made lowercase.
    charactersname = models.ForeignKey(Characters, models.DO_NOTHING, db_column='charactersName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unplayable_characters'
