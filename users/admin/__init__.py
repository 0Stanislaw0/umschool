from django.contrib import admin
from django.contrib.auth.models import Group

from users.admin.user import UserAdmin  # noqa

admin.site.unregister(Group)
