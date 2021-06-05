import sys
try:
   	f=open('xyz.txt')
	s=f.readline()
	i=int(s.strip())
except OSerror as err:
      print("OS error: {0}".format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

