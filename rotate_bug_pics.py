#!/usr/bin/env python

# Look for improperly rotated pictures and fix them

# Thanks to pexif and http://stackoverflow.com/questions/22045882/modify-or-delete-exif-tag-orientation-in-python  


from pexif import JpegFile
import sys
import os

# usage = """Usage: dump_exif.py <root_directory>"""


def main():

	# If no argument is passed, exit
	if len(sys.argv) != 2:
		print >> sys.stderr, usage
		sys.exit(1)

	# Set the directory you want to start from
	rootDir = sys.argv[1]

	# Walk the tree and process all of the files
	for dirpath, subdirList, fileList in os.walk(rootDir):
		print('Found directory: %s' % dirpath)
		for fname in fileList:
			check_and_rotate(os.path.join(dirpath, fname))



def check_and_rotate(filepath):

	print "Now checking file: %s" % filepath

	try:
		img = JpegFile.fromFile(filepath)
		orientation = img.exif.primary.Orientation[0]
		if orientation != 1:
			print "Orientation value is: %d, switching to 1" % orientation
			img.exif.primary.Orientation = [1]
			img.writeFile(filepath)
			print "Saved new orientation"
	except IOError:
		type, value, traceback = sys.exc_info()
		print >> sys.stderr, "Error opening file:", value
	except JpegFile.InvalidFile:
		type, value, traceback = sys.exc_info()
		print >> sys.stderr, "Error opening file:", value
	except AttributeError:
		type, value, traceback = sys.exc_info()
		print >> sys.stderr, "Could not get orientation attribute:", value



if __name__ == '__main__':
    main()
