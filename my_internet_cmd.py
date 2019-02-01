#!/usr/bin/python
import commands
import sys
import os
import time
import pyspeedtest
print "################################################################################################################################"
print "?????????????                      Do you want to check your internet status ? type y/n              ???????????????"
print " "
print " "
my_choice=raw_input()
if 'y' in my_choice:
	print "^^--^^--@@  please wait 4 few seconds..  __^^__^^__@@"
	print " "
	print " "	
	time.sleep(1)
	web_response=commands.getoutput('ping -c 1 google.com')
	if '0' in web_response:
		print " "
		print " "
		print "                              &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
		print "                              &&&&   Congratulation! your are connected to internet      &&&&&"
		print "                              &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
		time.sleep(1)
		print " "
		print " "
		print"################################################################################################################################"
		print "?????????????                Do you want to check your internet Speed ? type y/n              ???????????????"
		print " "
		print " "
		my_speed=raw_input()
		if 'y' in my_speed:
			print "__--__--__--__--your network speed calculating now just wait.......... __--__--__--__--"
			print " "
			print " " 
			os.system('curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -')

							
		else:
			print " "
			print " "		
			print "@@@@@@@@@@@  Thanks for use this command.....   @@@@@@@@@@@@@@"
			print " "
			print " " 
		time.sleep(1)
		print " "
		print " "
		print "###############################################################################################################################"
		print "?????????????                      Do you want to check your internet service provider ? type y/n              ???????????????"
		print " "
		print " "
		my_operator=raw_input()
		if 'y' in my_operator:
			print " "
			print " "
			print "  -------------------------------          your isp is...------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>"
			print " "
			print " "
			os.system('curl ipinfo.io/org')
			print " "
			print " "
		else:
			print " "
			print " "		
			print "@@@@@@@@@@@  Thanks for use this command.....   @@@@@@@@@@@@@@"
			print " "
			print " "



	else:
		print " "
		print " "
		
		print "!!!!    sorry! your are not connected to internet  !!!!"
		print " "
		print " "
	
elif 'n' in my_choice:
	print " "
	print " "		
	print "@@@@@@@@@@@  Thanks for use this command.....   @@@@@@@@@@@@@@"
	print " "
	print " "
	sys.exit()

















