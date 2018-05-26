# -*- coding: utf-8 -*-
# Этот токен невалидный, можете даже не пробовать :)
import os
from boto.s3.connection import S3Connection
token = S3Connection(os.environ['API_ID'], os.environ['API_KEY'])
print('lalala=',token)
print(os.environ['API_KEY'])
print(os.environ['API_ID'])
