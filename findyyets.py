# -*- coding: utf-8 -*-

__author__ = 'Sagacity'

import urllib2
import xml.dom.minidom

theQuery = u"{query}"
# theQuery = u"all"
theQuery = theQuery.strip()
rssurl = 'http://www.yyets.com/rss/feed/'
urldoc = xml.dom.minidom.parse( urllib2.urlopen( rssurl ) )

print "<?xml version=\"1.0\"?>\n<items>"
for item in urldoc.getElementsByTagName('item'):
    title = item.getElementsByTagName('title')[0].firstChild.data.replace( "&", "#" )
    link = item.getElementsByTagName('link')[0].firstChild.data

    if title.__contains__(theQuery) or theQuery == "all":
        print "    <item uid=\"YYeTs\" arg=\""+ link +"\">"
        print "        <title>" + title.encode('utf-8') + "</title>"
        print "        <subtitle>" + title.encode('utf-8') + "</subtitle>"
        print '''        <icon type="fileicon">/Applications/QuickTime Player.app/</icon>
    </item>'''
print "</items>\n"