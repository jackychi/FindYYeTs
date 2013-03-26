# -*- coding: utf-8 -*-

__author__ = 'Sagacity'

import urllib2
import json

theQuery = "{query}"

theQuery = theQuery.strip()
apiurl = 'http://www.yyets.com/php/search/api?keyword='
urldoc = json.loads( urllib2.urlopen( apiurl + theQuery ).read())

results = urldoc["data"]

if not results:
    exit()

print "<?xml version=\"1.0\"?>\n<items>"
for res in results:
    link = "http://www.yyets.com/" + res["type"] + "/" + res["itemid"]
    title = res["title"].replace( "&", "#" )
    print "    <item uid=\"YYeTs\" arg=\""+ link +"\">"
    print "        <title>" + title.encode('utf-8') + "</title>"
    print "        <subtitle>" + (res["prefix"] + title).encode('utf-8') + "</subtitle>"
    print '''        <icon type="fileicon">/Applications/QuickTime Player.app/</icon>
    </item>'''

print "</items>\n"
