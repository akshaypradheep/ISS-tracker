import urllib2
import json
import sys
sys.tracebacklimit=0
while(True):
	req = urllib2.Request("http://api.open-notify.org/astros.json")
	response = urllib2.urlopen(req)
	loc = urllib2.Request("http://api.open-notify.org/iss-now.json")
	location = urllib2.urlopen(loc)
	locdata = json.loads(location.read())

	
	obj = json.loads(response.read())
	print "********************************************************"
	print "location of International Space Staion"
	print "latitude:" ,locdata['iss_position']['latitude']
	print "longitude:",locdata['iss_position']['longitude']
	print "\n"
	print "number of astros in International Space Staion is  ",obj['number']
	num=obj['number']
	na=obj['people']
	for x in range(0,num):
		a = na[x]
		print a['name']
	print "********************************************************"
	print ("\n\n")