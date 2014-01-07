#! /usr/bin/python
import os
failsafe = False
HOME_FOLDER = '/home/pi/'
GIT_REPO = HOME_FOLDER + 'Kiosk/'
IMAGE_EXTENSIONS = "jpeg jpg png gif".split()
DEBUG = True
DEBUG_FILENAME = HOME_FOLDER + 'debug_out.txt'
if DEBUG:
    DEBUG_FILE = open(DEBUG_FILENAME, 'a'); DEBUG_FILE.write('\n==SESSION==\n')

# Mount flashdrive:
for drive in ['sda1','sdb1']:
	try:
		os.system('sudo mount /dev/' + drive + ' /mnt/flash_drive')
	except:
		pass
os.chdir('/mnt/flash_drive')
if len(os.listdir(os.getcwd())) == 0:
	failsafe = True
	if DEBUG: DEBUG_FILE.write('Failsafe: no files in flashdrive mount.\n')
os.chdir('./tv_images')
images = [os.getcwd() + '/' + filename 
          for filename in 
          os.listdir(os.getcwd()) 
          if any(filename.endswith(extension) for extension in IMAGE_EXTENSIONS)]
os.chdir(HOME_FOLDER + 'Desktop/web')

if not failsafe:
	try:
		with open(GIT_REPO + 'index_part_1', 'r') as f:
		    prefix = f.read()
		with open(GIT_REPO + 'index_part_2', 'r') as f:
		    suffix = f.read()
	except:
		failsafe = True
		if DEBUG: DEBUG_FILE.write('Failsafe: unable to read prefix or suffix.')

if not failsafe:
	try:
		with open('index.html', 'w') as f:
		    f.write(prefix)
		    for __ in range(20):
		        for image in images:
		            f.write('<img src="' + image + '" style="width: 100%" />\n')
		    f.write(suffix)
	except:
		pass

#testing out:
with open('index.html', 'w') as f:
	f.write("<h1>Hello world.</h1>")

if DEBUG: DEBUG_FILE.close()
