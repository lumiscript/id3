import id3reader
import eyed3
from sys import argv

script, first, second, third = argv



choice = raw_input("1 to check id3 and 2 to reset id3: ")
filename = raw_input("Enter filename    ")
audiofile = eyed3.load(filename)

if choice == '1':
		print audiofile.tag.artist
		print audiofile.tag.title
		print audiofile.tag.album
		print audiofile.tag.artist
		print audiofile.tag.artist
		print audiofile.tag.artist


elif choice =='2':


	audiofile.tag.artist = u"Terry Baba"

	audiofile.tag.save()
	print audiofile.tag.artist


