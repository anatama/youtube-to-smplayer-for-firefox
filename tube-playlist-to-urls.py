#!/usr/bin/python
# coding: utf8
# Last change: 2012-06-23 17:20:44.
# Author: Kosuke Uchida.
# Description: Youtubeの再生リストに含まれる動画URLを全て返す

import sys
from urlparse import urlparse
from xml.etree import ElementTree
import urllib

MAXRESULTS = 25

def main():
    # 再生リストのフィードURLを取得
    feedurl = "http://gdata.youtube.com/feeds/api/playlists/%s" % \
            dict(map(lambda s:s.split("="),
                urlparse(sys.argv[1]).query.split("&")))["list"][2:]
    # 再生リストフィードに含まれる動画URLを全て取得し出力
    startindex = 1
    while 1:
        exist_file = False
        params = (("start-index", str(startindex)),
                ("max-results", str(MAXRESULTS)),)
        requrl = "?".join((feedurl,"&".join(
            map(lambda s:"=".join(s), params)),))
        root = ElementTree.fromstring(urllib.urlopen(requrl).read())
        for e in root.getiterator("{http://search.yahoo.com/mrss/}player"):
            print e.get("url")
            exist_file = True
        if not exist_file:break # 動画URLが見つからなければ全て出力した
        startindex += MAXRESULTS

if __name__ == '__main__':
    main()
