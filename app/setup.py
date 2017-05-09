#!/bin/python3
from os import environ
from subprocess import check_output
from passlib.hash import argon2

print('Starting app configuration')
password = input('Password: ')
pw_hash = argon2.hash(password)
environ['UM_PASSWORD'] = pw_hash

value = check_output('echo $UM_PASSWORD', shell=True)
assert pw_hash.encode() in value
