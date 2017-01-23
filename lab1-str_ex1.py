
###########################################################################

#String Ex1
#----------
### Work in your pynet_test repository ###

#a. Create a python script with three strings representing three names
#b. Print these three names out in a column 30 wide, right aligned
#c. Execute the script verify the output
#d. Add a prompt for a fourth name, print this out as well
#e. check your code into GitHub

###########################################################################


apple = "apple1"
banana = "banana1"
orange = "orange1"

fruit = raw_input("Please provide a fruit name: ")

print '{:>30}{:>30}{:>30}{:>30}'.format(apple,banana,orange,fruit)


