#!/usr/bin/python2
from django.core.management import execute_from_command_line
from sys import argv
from os import environ

environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
execute_from_command_line(argv)
