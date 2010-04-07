#!/usr/bin/env python

"""
A quick hack to harvest all opds atom feeds starting with a given feed URL 
location:

  % harvest.py http://www.feedbooks.com/catalog.atom

This will save the feed in a file www.feedbooks.com/catalog.atom, and then 
look for opds or paging links in the feed, and grab them recursively.
"""

import os
import sys
import urllib
import logging
import urlparse

import feedparser

def get_feed(feed_url):
    """
    Fetches a feed, stashes it away on disk and returns a feedparser
    feed object for it.
    """
    # construct a filename based on the feed url
    uri = urlparse.urlparse(feed_url)
    file_parts = (uri.netloc + uri.path).split('/')
    if uri.query:
        file_parts[-1] = file_parts[-1] + '?' + uri.query
    feed_filename = os.path.join(*file_parts)
    feed_dir = os.path.dirname(feed_filename)
    if not os.path.isdir(feed_dir):
        os.makedirs(feed_dir)

    # get the feed, save it, and return a FeedParserDict for it
    logging.info("fetching feed: %s" % feed_url)
    feed_xml = urllib.urlopen(feed_url).read()
    open(feed_filename, 'w').write(feed_xml)
    return feedparser.parse(feed_xml)

def get_feeds(feed_url, seen):
    """
    Fetches a feed and all other opds atom feeds that are referenced.
    """
    # base case for recursive call
    if seen.has_key(feed_url):
        return 
    
    seen[feed_url] = True
    feed = get_feed(feed_url)
    for link in feed['feed']['links']:
        # follow opds rels and paging links
        rel = link.get('rel', None)
        if 'application/atom+xml' and ('opds-spec.org' in rel or rel == 'next'):
            url = link['href'] 
            if not url.startswith('http://'):
                # TODO: deal with relative hrefs
                continue
            # bit o' recursion
            get_feeds(url, seen)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "usage: harvest.py http://example.com/feed.xml"
        sys.exit(1)
    logging.basicConfig(level=logging.INFO)
    url = sys.argv[1]
    seen = {}
    get_feeds(url, seen)
    logging.info("retrieved %s feeds" % len(seen.keys()))

