import hashlib
import os

from libearth import crawler
from libearth.schema import write

feedlist = ['https://github.com/blog.atom',
            'http://feeds.feedburner.com/CodeMetaphor',
            'http://rss.egloos.com/blog/agile']

if not os.path.isdir('repo'):
    os.mkdir('repo')

generator = crawler.crawl(feedlist, 2)

for feed_url, (feed_data, crawler_hints) in generator:
    file_name = hashlib.sha1(feed_url).hexdigest()
    with open(os.path.join('repo', file_name + '.xml'), 'w') as f:
        for chunk in write(feed_data, indent='    ', canonical_order=True):
            f.write(chunk)