from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Money

admin.site.register(Money)
