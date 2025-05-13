from django.contrib import admin

from .models import AuthTokens
from .models import CollectionCoursesAssoc
from .models import Collections
from .models import Contents
from .models import Courses
from .models import EmailLogs
from .models import FileKeys
from .models import Files
from .models import Languages
from .models import Migrations
from .models import ResourceAccess
from .models import Resources
from .models import Subtitles
from .models import UserCollectionsAssoc
from .models import UserCoursesAssoc
from .models import UserTypeExceptions
from .models import Users
from .models import Words


@admin.register(AuthTokens)
class AuthTokensAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'updated', 'deleted')
    list_filter = ('deleted', 'created', 'updated')
    search_fields = ('id', 'user__username')


@admin.register(CollectionCoursesAssoc)
class CollectionCoursesAssocAdmin(admin.ModelAdmin):
    list_display = ('id', 'collection', 'course', 'created', 'updated', 'deleted')
    list_filter = ('deleted', 'created', 'updated')
    search_fields = ('id', 'collection__collection_name', 'course__department')


@admin.register(Collections)
class CollectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'collection_name', 'owner', 'published', 'archived', 'public', 'copyrighted')
    list_filter = ('published', 'archived', 'public', 'copyrighted', 'deleted')
    search_fields = ('id', 'collection_name', 'owner__username')


@admin.register(Contents)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content_type', 'collection', 'published', 'views')
    list_filter = ('content_type', 'published', 'allow_definitions', 'allow_notes', 'allow_captions')
    search_fields = ('id', 'title', 'description', 'tags')


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'catalog_number', 'section_number', 'created', 'updated', 'deleted')
    list_filter = ('department', 'deleted')
    search_fields = ('id', 'department', 'catalog_number', 'section_number')


@admin.register(EmailLogs)
class EmailLogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'sender_email', 'subject', 'sent_date')
    list_filter = ('sent_date', 'deleted')
    search_fields = ('id', 'sender_email', 'subject', 'message')


@admin.register(FileKeys)
class FileKeysAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'user', 'created', 'updated', 'deleted')
    list_filter = ('deleted', 'created', 'updated')
    search_fields = ('id', 'file__filepath', 'user__username')


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'filepath', 'file_version', 'resource', 'aspect_ratio')
    list_filter = ('file_version', 'deleted')
    search_fields = ('id', 'filepath', 'metadata')


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'updated', 'deleted')
    list_filter = ('deleted',)
    search_fields = ('id',)


@admin.register(Migrations)
class MigrationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'applied', 'description')
    list_filter = ('applied',)
    search_fields = ('id', 'description')


@admin.register(ResourceAccess)
class ResourceAccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'resource', 'last_verified', 'created', 'updated', 'deleted')
    list_filter = ('last_verified', 'deleted')
    search_fields = ('id', 'username', 'resource__resource_name')


@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('id', 'resource_name', 'resource_type', 'requester_email', 'published', 'views')
    list_filter = ('resource_type', 'published', 'copyrighted', 'physical_copy_exists', 'full_video')
    search_fields = ('id', 'resource_name', 'requester_email')


@admin.register(Subtitles)
class SubtitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'content_0', 'created', 'updated', 'deleted')
    list_filter = ('language', 'deleted')
    search_fields = ('id', 'title', 'content')


@admin.register(UserCollectionsAssoc)
class UserCollectionsAssocAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'collection', 'account_role', 'created', 'updated', 'deleted')
    list_filter = ('account_role', 'deleted')
    search_fields = ('id', 'username', 'collection__collection_name')


@admin.register(UserCoursesAssoc)
class UserCoursesAssocAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'account_role', 'created', 'updated', 'deleted')
    list_filter = ('account_role', 'deleted')
    search_fields = ('id', 'user__username', 'course__department')


@admin.register(UserTypeExceptions)
class UserTypeExceptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'account_type', 'created', 'updated', 'deleted')
    list_filter = ('account_type', 'deleted')
    search_fields = ('id', 'username')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'account_name', 'account_type', 'last_login')
    list_filter = ('account_type', 'deleted', 'last_login')
    search_fields = ('id', 'username', 'email', 'account_name')


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'word', 'src_lang', 'dest_lang', 'created', 'updated', 'deleted')
    list_filter = ('src_lang', 'dest_lang', 'deleted')
    search_fields = ('id', 'word', 'user__username')
