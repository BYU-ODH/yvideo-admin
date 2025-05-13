# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthTokens(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_tokens'


class CollectionCoursesAssoc(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    collection = models.ForeignKey('Collections', models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey('Courses', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection_courses_assoc'
        unique_together = (('deleted', 'course', 'collection'),)


class Collections(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    collection_name = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('Users', models.DO_NOTHING, db_column='owner', blank=True, null=True)
    published = models.BooleanField(blank=True, null=True)
    archived = models.BooleanField(blank=True, null=True)
    public = models.BooleanField(blank=True, null=True)
    copyrighted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collections'
        unique_together = (('deleted', 'owner', 'collection_name'),)


class Contents(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content_type = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    annotations = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    allow_definitions = models.BooleanField(blank=True, null=True)
    allow_notes = models.BooleanField(blank=True, null=True)
    allow_captions = models.BooleanField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    file_version = models.TextField(blank=True, null=True)
    published = models.BooleanField(blank=True, null=True)
    words = models.TextField(blank=True, null=True)
    clips = models.TextField(blank=True, null=True)
    resource = models.ForeignKey('Resources', models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(Collections, models.DO_NOTHING, blank=True, null=True)
    file = models.ForeignKey('Files', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contents'


class Courses(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    catalog_number = models.TextField(blank=True, null=True)
    section_number = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'
        unique_together = (('deleted', 'department', 'catalog_number', 'section_number'),)


class EmailLogs(models.Model):
    id = models.UUIDField(primary_key=True)
    sender = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    sender_email = models.TextField()
    recipients = models.TextField()  # This field type is a guess.
    subject = models.TextField()
    message = models.TextField()
    sent_date = models.DateTimeField()
    deleted = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_logs'


class FileKeys(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    file = models.ForeignKey('Files', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_keys'


class Files(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    resource = models.ForeignKey('Resources', models.DO_NOTHING, blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)
    file_version = models.ForeignKey('Languages', models.DO_NOTHING, db_column='file_version', blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    aspect_ratio = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'
        unique_together = (('deleted', 'filepath'),)


class Languages(models.Model):
    id = models.TextField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Migrations(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    applied = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migrations'


class ResourceAccess(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    username = models.TextField()
    resource = models.ForeignKey('Resources', models.DO_NOTHING, blank=True, null=True)
    last_verified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_access'
        unique_together = (('deleted', 'username', 'resource'),)


class Resources(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    resource_name = models.TextField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    requester_email = models.TextField(blank=True, null=True)
    copyrighted = models.BooleanField(blank=True, null=True)
    physical_copy_exists = models.BooleanField(blank=True, null=True)
    full_video = models.BooleanField(blank=True, null=True)
    published = models.BooleanField(blank=True, null=True)
    date_validated = models.TextField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    all_file_versions = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resources'


class Subtitles(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    words = models.TextField(blank=True, null=True)
    content_0 = models.ForeignKey(Contents, models.DO_NOTHING, db_column='content_id', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'subtitles'


class UserCollectionsAssoc(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(Collections, models.DO_NOTHING, blank=True, null=True)
    account_role = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_collections_assoc'
        unique_together = (('deleted', 'username', 'collection'),)


class UserCoursesAssoc(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, blank=True, null=True)
    account_role = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_courses_assoc'
        unique_together = (('deleted', 'user', 'course'),)


class UserTypeExceptions(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    account_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_type_exceptions'
        unique_together = (('deleted', 'username'),)


class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    last_person_api = models.DateTimeField(blank=True, null=True)
    last_course_api = models.DateTimeField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    account_name = models.TextField(blank=True, null=True)
    account_type = models.IntegerField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    byu_person_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('deleted', 'username'),)


class Words(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    src_lang = models.TextField(blank=True, null=True)
    dest_lang = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'words'
        unique_together = (('deleted', 'user', 'word', 'src_lang', 'dest_lang'),)
