# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CommentInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    username = models.CharField(db_column='userName', unique=True, max_length=20)  # Field name made lowercase.
    userscore = models.CharField(db_column='userScore', max_length=20)  # Field name made lowercase.
    time = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'comment_info'


class MovieAwards(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    awardname = models.CharField(db_column='awardName', max_length=20)  # Field name made lowercase.
    awardclass = models.CharField(db_column='awardClass', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie_awards'
        unique_together = (('name', 'awardname', 'awardclass'),)


class MovieInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=50)
    time = models.CharField(max_length=10)
    director = models.CharField(max_length=20)
    types = models.CharField(max_length=20)
    releasedate = models.DateField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(blank=True, null=True)
    sumcomment = models.IntegerField(db_column='sumComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie_info'


class MoviePlay(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    moviesite = models.CharField(db_column='movieSite', max_length=10)  # Field name made lowercase.
    movieurl = models.CharField(db_column='movieUrl', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie_play'
        unique_together = (('name', 'moviesite'),)


class MovieScore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=20)
    fivestarrate = models.FloatField(db_column='fiveStarRate', blank=True, null=True)  # Field name made lowercase.
    fourstarrate = models.FloatField(db_column='fourStarRate', blank=True, null=True)  # Field name made lowercase.
    threestarrate = models.FloatField(db_column='threeStarRate', blank=True, null=True)  # Field name made lowercase.
    twostarrate = models.FloatField(db_column='twoStarRate', blank=True, null=True)  # Field name made lowercase.
    onestarrate = models.FloatField(db_column='oneStarRate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie_score'
