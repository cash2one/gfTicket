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
import os

from redis import Redis
from rq import Queue

# Core Django imports


from django.core.management.base import BaseCommand
# Third-party app imports

# Imports from your apps

from ...models import Subnet
from ...controller import ping_subnet

redis_conn = Redis()


class Command(BaseCommand):
    help = 'ping host in subnet'

    def add_arguments(self, parser):
        parser.add_argument('--count', '-c', default=100, type=int, dest='count')

    def handle(self, *args, **options):
        q = Queue('ping_subnet', connection=redis_conn)
        q.empty()
        count = options['count']
        all_subnet = Subnet.objects.order_by("ping_latest_time").all()[:count]
        for subnet in all_subnet:
            q.enqueue(ping_subnet, subnet)
