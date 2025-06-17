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

    def __str__(self):
        return f"AuthTokensAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(CollectionCoursesAssoc)
class CollectionCoursesAssocAdmin(admin.ModelAdmin):
    list_display = ('id', 'collection', 'course', 'created', 'updated', 'deleted')
    list_filter = ('deleted', 'created', 'updated')
    search_fields = ('id', 'collection__collection_name', 'course__department')

    def __str__(self):
        return f"CollectionCoursesAssocAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(Collections)
class CollectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'collection_name', 'owner', 'published', 'archived', 'public', 'copyrighted')
    list_filter = ('published', 'archived', 'public', 'copyrighted', 'deleted')
    search_fields = ('id', 'collection_name', 'owner__username')

    def __str__(self):
        return f"CollectionsAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(Contents)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content_type', 'collection', 'published', 'views')
    list_filter = ('content_type', 'published', 'allow_definitions', 'allow_notes', 'allow_captions')
    search_fields = ('id', 'title', 'description', 'tags')

    def __str__(self):
        return f"ContentsAdmin({self._abbreviate_id(self.list_display[0])}, {self.list_display[1]})"


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'catalog_number', 'section_number', 'created', 'updated', 'deleted')
    list_filter = ('department', 'deleted')
    search_fields = ('id', 'department', 'catalog_number', 'section_number')

    def __str__(self):
        return f"CoursesAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(EmailLogs)
class EmailLogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'sender_email', 'subject', 'sent_date')
    list_filter = ('sent_date', 'deleted')
    search_fields = ('id', 'sender_email', 'subject', 'message')

    def __str__(self):
        return f"EmailLogsAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(FileKeys)
class FileKeysAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'user', 'created', 'updated', 'deleted')
    list_filter = ('deleted', 'created', 'updated')
    search_fields = ('id', 'file__filepath', 'user__username')

    def __str__(self):
        return f"FileKeysAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'filepath', 'file_version', 'resource', 'aspect_ratio')
    list_filter = ('file_version', 'deleted')
    search_fields = ('id', 'filepath', 'metadata')

    def __str__(self):
        return f"FilesAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'updated', 'deleted')
    list_filter = ('deleted',)
    search_fields = ('id',)

    def __str__(self):
        return f"LanguagesAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(Migrations)
class MigrationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'applied', 'description')
    list_filter = ('applied',)
    search_fields = ('id', 'description')

    def __str__(self):
        return f"MigrationsAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(ResourceAccess)
class ResourceAccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'resource', 'last_verified', 'created', 'updated', 'deleted')
    list_filter = ('last_verified', 'deleted')
    search_fields = ('id', 'username', 'resource__resource_name')

    def __str__(self):
        return f"ResourceAccessAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('id', 'resource_name', 'resource_type', 'requester_email', 'published', 'views')
    list_filter = ('resource_type', 'published', 'copyrighted', 'physical_copy_exists', 'full_video')
    search_fields = ('id', 'resource_name', 'requester_email')

    def __str__(self):
        return f"ResourcesAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(Subtitles)
class SubtitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'content_0', 'created', 'updated', 'deleted')
    list_filter = ('language', 'deleted')
    search_fields = ('id', 'title', 'content')

    def __str__(self):
        return f"SubtitlesAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(UserCollectionsAssoc)
class UserCollectionsAssocAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'collection', 'account_role', 'created', 'updated', 'deleted')
    list_filter = ('account_role', 'deleted')
    search_fields = ('id', 'username', 'collection__collection_name')

    def __str__(self):
        return f"UserCollectionsAssocAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(UserCoursesAssoc)
class UserCoursesAssocAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'account_role', 'created', 'updated', 'deleted')
    list_filter = ('account_role', 'deleted')
    search_fields = ('id', 'user__username', 'course__department')

    def __str__(self):
        return f"UserCoursesAssocAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(UserTypeExceptions)
class UserTypeExceptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'account_type', 'created', 'updated', 'deleted')
    list_filter = ('account_type', 'deleted')
    search_fields = ('id', 'username')

    def __str__(self):
        return f"UserTypeExceptionsAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'account_name', 'account_type', 'last_login')
    list_filter = ('account_type', 'deleted', 'last_login')
    search_fields = ('id', 'username', 'email', 'account_name')

    def __str__(self):
        return f"UsersAdmin({self._abbreviate_id(self.list_display[0])})"


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'word', 'src_lang', 'dest_lang', 'created', 'updated', 'deleted')
    list_filter = ('src_lang', 'dest_lang', 'deleted')
    search_fields = ('id', 'word', 'user__username')

    def __str__(self):
        return f"WordsAdmin({self._abbreviate_id(self.list_display[0])})"

# Utility function to abbreviate IDs
def _abbreviate_id(id_field):
    if len(id_field) > 6:
        return f"{id_field[:3]}...{id_field[-3:]}"
    return id_field
