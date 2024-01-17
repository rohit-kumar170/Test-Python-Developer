from test import *


print('############### All Installed software’s list ###############################')
get_software_list()
print('##############################################################')
print('\n')

print('############### Internet Speed ###############################')
internet_speed()
print('##############################################################')
print('\n')

print('############### Screen resolvution ###############################')
get_screen_resolution()
print('##############################################################')
print('\n')

print('############### CPU model ###############################')
get_cpu_model()
print('##############################################################')
print('\n')

print('############### No of core and threads of CPU ###############################')
get_cpu_info()
print('##############################################################')
print('\n')
print('############### GPU model ( If exist ) ###############################')
get_gpu_model()
print('##############################################################')
print('\n')
print('############### RAM Size ( In GB ) ###############################')
get_ram_size()
print('##############################################################')
print('\n')

print('############ Screen size ( like, 15 inch, 21 inch) ########################')
print(get_screen_size())
print('##############################################################')
print('\n')

print('############ Wifi/Ethernet mac address ########################')
mac_addresses=get_mac_addresses()
if mac_addresses:
        print("MAC Addresses:")
        for interface, mac_address in mac_addresses.items():
            print(f"{interface}: {mac_address}")
else:
        print("No MAC addresses found.")
print('##############################################################')
print('\n')

print('############ Public IP address ########################')
print(get_public_ip())
print('##############################################################')
print('\n')

print('############ Windows version ########################')
print(get_windows_version())
print('##############################################################')
print('\n')


    
