# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.test import TestCase

for i in range(22):
    data = {'name': 'name' + str(i), 'age': i + 5}
    requests.post(url='http://127.0.0.1:8000/users/', json=data)
    print i