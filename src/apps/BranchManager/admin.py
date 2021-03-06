#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+code@gmail.com"
#
# Copyright 2015-2016 liantian
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# Create your models here.

# Stdlib imports

# Core Django imports
from django.contrib import admin

# Third-party app imports


# Imports from your apps
from .models import *


# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class DepartmentTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["title", 'dot_code', 'for_short', 'area', 'type', 'for_short', 'db_active']
    list_filter = ['area', 'type', 'db_active']


class SubDepartmentAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', 'parent', 'for_short']
    list_filter = ['parent']


admin.site.register(Area, AreaAdmin)
admin.site.register(DepartmentType, DepartmentTypeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(SubDepartment, SubDepartmentAdmin)
