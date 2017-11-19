# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Flows, WorkRequests, Roles, TaskTemplates, Tasks

# Register your models here.
admin.site.register(Flows)
admin.site.register(WorkRequests)
admin.site.register(Roles)
admin.site.register(TaskTemplates)
admin.site.register(Tasks)
