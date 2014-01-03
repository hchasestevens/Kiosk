#! /usr/bin/python
import os
failsafe = False
for drive in ['sda1','sdb1']:
	try:
		os.system('sudo mount /dev/' + drive + ' /mnt/flash_drive')
	except:
		pass
os.chdir('/mnt/flash_drive')
if len(os.listdir(os.getcwd())) == 0:
	failsafe = True
os.chdir('./tv_images')
images = [os.getcwd() + '/' + image for image in filter(lambda x:'.jpeg' in x or '.jpg' in x or '.png' in x or '.gif' in x,os.listdir(os.getcwd()))]
os.chdir('/home/pi/Desktop/web')
if not failsafe:
	try:
		f = open('~/Kiosk/index_part_1','r')
		prefix = f.read()
		f.close()
		f = open('~/Kiosk/index_part_2','r')
		suffix = f.read()
		f.close()
	except:
		failsafe = True
if not failsafe:
	try:
		f = open('index.html','w')
		f.write(prefix)
		for x in range(20):
			for image in images:
				f.write('<img src="' + image + '" style="width: 100%" />\n')
		f.write(suffix)
		f.close()
	except:
		pass
