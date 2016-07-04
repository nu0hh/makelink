# coding: utf-8
import GetTitle
def main(url):
	mylink = GetTitle.main(url)
	mytext = '<a href="' + mylink[0] + '" target="_blank">' + mylink[1] + '</a>'
	return mytext
if __name__ == '__main__':
	url = 'http://google.com'
	print (main(url))
