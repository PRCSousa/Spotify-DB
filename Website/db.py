import logging
import pymysql
import re
import subprocess

# Change this if necessary
CONFIG = {
  'DB': 'guest',
  'USER': 'root',
  'PASSWORD': 'root',
  'HOST': '127.0.0.1',
  'PORT': 3306,
  'CHARSET': 'utf8'
}

global DB
DB = None

def connect():
  global DB
  c = pymysql.connect(db=CONFIG['DB'],
                       user=CONFIG['USER'], 
                       password=CONFIG['PASSWORD'],
                       host=CONFIG['HOST'], 
                       port=CONFIG['PORT'],
                       charset=CONFIG['CHARSET'],
                       cursorclass=pymysql.cursors.DictCursor)
  c._cursor_ = c.cursor()
  DB = c
  logging.info('Connected to database %s' % CONFIG['DB'])

def execute(sql,args=None):
  global DB
  sql = re.sub('\s+',' ', sql)
  print(sql)
  logging.info('SQL: {} Args: {}'.format(sql,args))
  DB._cursor_.execute(sql, args)
  return DB._cursor_

def commit():
  global DB
  DB.commit()

def rollback():
  global DB
  DB.rollback()

def close():
  global DB
  DB._cursor_.close()
  DB.close()

