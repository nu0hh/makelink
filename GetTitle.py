# coding: utf-8
from HTMLParser import HTMLParser
import urllib2

class GetTitle(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.title_flag = False

	def handle_starttag(self, tag, attrs):
		if tag == 'title':
			self.title_flag = True

	def handle_data(self, data):
		if self.title_flag:
			self.title = data
			self.title_flag = False
def main(url):
	resp = [] #take care reset position
	response = urllib2.urlopen(url)
	gt = GetTitle()
	gt.feed(response.read())
	gt.close()
	resp.append(url)
	resp.append(gt.title)
	return resp
if __name__ == '__main__':
	url = 'http://osksn2.hep.sci.osaka-u.ac.jp/~taku/osx/python/readfile.html'
	print (main(url))
#http://d.hatena.ne.jp/ichhi/20111015/1318699010
#http://osksn2.hep.sci.osaka-u.ac.jp/~taku/osx/python/readfile.html
