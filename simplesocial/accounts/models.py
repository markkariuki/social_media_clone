# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conotrib import auth

# Create your models here.
class User(auth.models.user,auth.models.PermissionsMixin):

    def_str_(self):
        return "@{}".format(self.username)
