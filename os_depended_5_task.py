#!usr/bin/env python

import time
import commands
import webbrowser
option='''
select a number to perform an opration
press 1 : to check your os version
press 2 : to login your facebook account
press 3 : to check ram & cpu In your machine
press 4 : to search something In google search engine
press 5 : to listout All ip And mac address In your current network zone
'''
print option
def selection(z):
	if (z == "1"):
		print "your os version is:>>>>>>>>>>"
		My_Os_version=commands.getoutput('cat /etc/os-release | grep -i version | head -1')
		print " "
		print " "
		print "~~~~~~~~~~~~~~~~~~~~~~~~     "  +   My_Os_version      +"       ~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print " "
		print " "
	elif(z == "2"):
		print " just wait 4 few seconds i trying to login your facebook id..........................."
		time.sleep(1)
		print " "
		print "      Congratulation !! i got 2 options to login your facebook Account     "
		print " "
		print "          option    A:  To login with secan Qr-code.     "
		print "   "
		print "          option    B:  To login direct without any Authenticaton   "
		print " "
		print "    Note !   options are in Case-Sensitive formate "
		print " "
		login_option=raw_input("  please select any option from A to B :    ")
		if(login_option == "A" or login_option == "B"):
			if(login_option == "A"):
				Qr_code=commands.getoutput("qrencode -s 16*16 -o my_fb.png https://www.facebook.com/")
				print Qr_code
				display_Qr_code=commands.getoutput("eog my_fb.png")
			else:
				webbrowser.open_new_tab("https://www.facebook.com")
			
		else:
			print "     Please select a valid option !        "
	elif(z == "3"):
		print "your cpu model name is:>>>>>>>>>>>>"
		print " "
		print " "
		My_cpu=commands.getoutput("cat /proc/cpuinfo | grep -i model | tail -1")
		print "~~~~~~~~~~~~~~~       " + My_cpu + "        ~~~~~~~~~~~~~~~~~~~~~"
		print " "
		print " "
		ram=commands.getoutput("free -m")
		My_Machine_RAM=ram.split()[7]

		print " "
		print " "
		print "~~~~~~~~~~~~~~~~    RAM is:      "+My_Machine_RAM+"MB      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print " "
		print " "
	elif(z == "4"):
		data=raw_input("enter something to search on google:")
		print "we sending request to server to provide your result:"	
		time.sleep(1)
		print " "
		print " "
		webbrowser.open_new_tab("https://www.google.com/search?q="+data)
		print " "
		print " "
		time.sleep(2)


#........................... find out ip and mac address which connected to your internet...............................
	elif(z == "5"):
		x=False
		count=0
		index=0	
		Total_Host_Connected=0
		check_my_system_ip=''
		router=0

		router_mac=0	
	#        this is for getting ip...........................................
		try:
			getting_range_of_ip=commands.getoutput("ifconfig | grep inet")
			system_ip=getting_range_of_ip.split()[11]
	#   this is for gatting mac address...................
			s=commands.getoutput("ifconfig | grep ether")
			my_system_mac=s.split()
	#selecting range from 0 to 255..........................................................

			select_all_ip=getting_range_of_ip.split()[11][0: 11]
			getting_range_of_all_ip=select_all_ip + "0/24"
		except:
			print " "
			print " "
			print "you are not connected to internet please connect your system with any network"
			x=True
		if (x == False):
			print " "
			print " "
			print "just wait for few seconds i am going to search that how many systems are connected with your network "
			print " "
	
			getting_connected_ip_mac_address__device_name=commands.getoutput("nmap -sS -A"+" "+ getting_range_of_all_ip)
			searching_string_ip="Nmap scan rep"
			Searching_String_mac="MAC Address: "
		#    matching substring and find out index of string when it match with last char of substring..........................
			for i in range(len(searching_string_ip)):
				for j in range(len(getting_connected_ip_mac_address__device_name)):
					if(searching_string_ip[i]==getting_connected_ip_mac_address__device_name[j]):
						count +=1
						if(count ==13):#      length of "Nmap scan rep which is equal to "MAC Address: "   = 13"
							index=j
							count=0
							i=0
							Total_Host_Connected += 1
							router +=1
							print " "
		#............................................router ip ...............................................	
					
							if(router==1):
								getting_connected_ip=getting_connected_ip_mac_address__device_name[index+8: index+23]
								if(not getting_connected_ip[12].isdigit()):
									print "your router ip is: "+getting_connected_ip[0:12]
								elif(not getting_connected_ip[13].isdigit()):
									print "your router ip is: "+getting_connected_ip[0:13]
								elif(not getting_connected_ip[14].isdigit()):
									print "your router ip is: "+getting_connected_ip[0:14]
								else:
									print "your router ip is: "+getting_connected_ip[0:15]						
								print " "	
	#.............................................my System ip and other system connected ip................................................

		
							else:							
								getting_connected_ip=getting_connected_ip_mac_address__device_name[index+8: index+23]
								if(not getting_connected_ip[12].isdigit()):
									check_my_system_ip=getting_connected_ip[1:12]
							
									if(check_my_system_ip==system_ip):
										print "your System ip is : "+check_my_system_ip
										time.sleep(1)
				    #     .......            for my system mac address..................................................
										print "this is your ethernet mac :  "+ my_system_mac[1]
										print " "
										print "this is your wlsl mac :  "+ my_system_mac[6]
									
									else:
				
										print "Other connected System ip is: "+check_my_system_ip
										time.sleep(1)

#.....................................if ip length is 13....................................................

								elif(not getting_connected_ip[13].isdigit()):
									check_my_system_ip=getting_connected_ip[1:13]
									if(check_my_system_ip==system_ip):
										print "your System ip is : "+check_my_system_ip
										time.sleep(1)
				    #     .......            for my system mac address..................................................
										print "this is your ethernet mac :  "+ my_system_mac[1]
										print " "
										print "this is your wlsl mac :  "+ my_system_mac[6]
								
									else:
										print "Other connected System ip is: "+check_my_system_ip
										time.sleep(1)
						



# ......................................if ip length is 14..............................................

								elif(not getting_connected_ip[14].isdigit()):
									check_my_system_ip=getting_connected_ip[1:14]				
									if(check_my_system_ip==system_ip):	
										print "your System ip is : "+check_my_system_ip
										time.sleep(1)
				    #     .......            for my system mac address..................................................
										print "this is your ethernet mac :  "+ my_system_mac[1]
										print " "
										print "this is your wlsl mac :  "+ my_system_mac[6]
									else:
										print "Other connected System ip is: "+check_my_system_ip
										time.sleep(1)

#.............ip length >15...................................................................
								else:				
									check_my_system_ip=getting_connected_ip[1:15]			
									if(check_my_system_ip==system_ip):
										print "your System ip is : "+check_my_system_ip
										time.sleep(1)
                                           #     .......            for my system mac address..................................................
										print "this is your ethernet mac :  "+ my_system_mac[1]
										print " "
										print "this is your wlsl mac :  "+ my_system_mac[6]
								
									else:
										print "Other connected System ip is: "+check_my_system_ip
										time.sleep(1)
						
						
											
						else:
							i +=1
					elif(Searching_String_mac[i]==getting_connected_ip_mac_address__device_name[j]):
						count +=1
						if(count ==13):#      length of "Nmap scan rep which is equal to "MAC Address: "   = 13"
							index=j
							count=0
							i=0
							router_mac+=1			
							if(router_mac==1):
								getting_connected_system_mac_address=getting_connected_ip_mac_address__device_name[index+0: index+18]
								time.sleep(1)	
								print "your router mac Address is: "+getting_connected_system_mac_address[0:]
												
								print " "
							else:
								time.sleep(1)
								getting_connected_system_mac_address=getting_connected_ip_mac_address__device_name[index+0: index+18]
								print "Other System Mac Address :   "+getting_connected_system_mac_address[0:]

						else:
							i +=1

					else:
						i=0
						count=0
				print "Online host are:   " +  str(Total_Host_Connected)
				break

z=raw_input("enter your choice :  ")
if(z == "1" or z == "2" or z == "3" or z =="4" or z == "5"):
	selection(z)
else:
	print "enter valid number from 1 to 5"
while True:
	x=raw_input("  Do you want to search more ? type 'y' or 'n'  ")
	if(x == "y"):
		z = raw_input("  enter your choice:  ")
		if(z == "1" or z == "2" or z == "3" or z =="4" or z == "5"):
			selection(z)
		
		else:
			print "please enter a valid number from 1 to 5"	
	elif(x == "n"):
		break
									
		
	else:
		print "only use 'y' or 'n' "
		
