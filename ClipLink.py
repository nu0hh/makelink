# coding: utf-8
import appex
import os
import console
import codecs

def main():
	if appex.is_running_extension():
		text = appex.get_url()
		with codecs.open('LinkStack.txt', 'a', 'utf-8') as f:
			f.write('%s\n' % (text))
		count=0
		with codecs.open('LinkStack.txt', 'r', 'utf-8') as f:
			for line in f:
				count = count + 1
		console.alert('ClippedLink : %i' % count, '', 'OK', hide_cancel_button=True)
if __name__ == '__main__':
	main()