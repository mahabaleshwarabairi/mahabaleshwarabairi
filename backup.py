#!/usr/bin/python
import os
import time
import datetime
import pipes
##import pdb; pdb.set_trace()
DB_HOST='localhost'
DB_USER='root'
DB_USER_PASSWORD='maha'
DB_NAME='test_data'
BACKUP_PATH='/root'
DATETIME=time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH=BACKUP_PATH+'/'+DATETIME
try:
   os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)

if os.path.exists(DB_NAME) :
   file1 = open(DB_NAME)
   multi=1
   print ("Databases file found...")
   print ("Starting backup of all dbs listed in file " + DB_NAME)
else:
   print ("Databases file not found...")
   print ("Starting backup of database " + DB_NAME)
   multi = 0

   dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + "DB_NAME " > " + pipes.quote(TODAYBACKUPPATH) + "/"+ DB_NAME +  ".sql"
   os.system(dumpcmd)
   gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + DB_NAME + ".sql"
   os.system(gzipcmd)
 
print ("")
print ("Backup script completed")
print ("Your backups have been created in '" + TODAYBACKUPPATH + "' directory")


