#!/usr/bin/env python

###########################################################################

#String Ex2
#----------
### Work in your pynet_test repository ###

#a. Create a python script that prompts for an IP address.
#b. Use #! at top of file; make executable
#c. split on '.'     
#d. Print out four octets with column width of 12; left aligned.
#e. Check your code into github


###########################################################################

ip_addr = raw_input("Please provide an IP address: ")

ip_addr_list = ip_addr.split('.')

print '{:<12}{:<12}{:<12}{:<12}'.format(ip_addr_list[0],ip_addr_list[1],ip_addr_list[2],ip_addr_list[3])


