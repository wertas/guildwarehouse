# -*- coding: utf-8 -*-
# Этот токен невалидный, можете даже не пробовать :)
import os
from boto.s3.connection import S3Connection
token = S3Connection(os.environ['CWGWbotAPIKEY'])
