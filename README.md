rotate-bug-pics
===============

Requirements:
Install the pexif Python library (https://github.com/bennoleslie/pexif)

Usage:
./rotate_bug_pics.py <path_to_folder_containing_pics>

Notes:
The program will walk any subdirectories, looking at the exif data for file orientations!= 1.  If one if found, the exif value is changed to 1 and the file is saved. 


