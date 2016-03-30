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

# Stdlib imports

# Core Django imports

# Third-party app imports


# Imports from your apps
from .views import BaseView
from apps.SupportTicketSystem.models import SupportTicketSystemUser


class Index(BaseView):
    def get(self, request):
        if request.user.is_authenticated():
            try:
                if request.user.support_ticket_system_user.is_admin:
                    return self.go(viewname="SupportTicketSystem:admin")
                elif request.user.support_ticket_system_user.is_watcher:
                    return self.go(viewname="SupportTicketSystem:create_ticket")
                elif request.user.support_ticket_system_user.is_worker:
                    return self.go(viewname="SupportTicketSystem:me")
            except SupportTicketSystemUser.DoesNotExist:
                pass
        return self.go(viewname="BusinessSystem:bs_view")
