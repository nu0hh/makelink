# coding: utf-8
import clipboard
import CreateLink
import codecs
import console

def main():
	text = ''
	with codecs.open('LinkStack.txt', 'r', 'utf-8') as f:
		for line in f:
			text += CreateLink.main(line[:-1]) + '\n'
	clipboard.set(text)
	console.alert('Link Created!', '', 'OK', hide_cancel_button=True)
	with codecs.open('LinkStack.txt', 'w', 'utf-8') as f:
		f.write('')
	
if __name__ == '__main__':
	main()