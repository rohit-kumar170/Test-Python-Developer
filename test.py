import subprocess
import speedtest
import tkinter as tk
import platform
import os
import multiprocessing
import GPUtil
import psutil
import requests
import ctypes
import netifaces

def  get_software_list():
    softwares=subprocess.check_output(['wmic','product','get','name'])
    softwares=str(softwares)
    try:
        for i in range(len(softwares)):
            print(softwares.split("\\r\\r\\n")[6:][i]) 

    except IndexError as e:
        print("All done!")
            
            
            
def internet_speed():
    s = speedtest.Speedtest()
    print("Download speed:",s.download()/1024/1024)
    print("Upload speed:",s.upload()/1024/1024)
        
            
def get_screen_resolution():
    root = tk.Tk()
    root.withdraw()  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(f"Screen Resolution:{screen_width}x{screen_height}")
         
        
def get_cpu_model():
    try:
        st= platform.uname()
        cpu_model=st.processor
        print(f"CPU Model: {cpu_model}")
    except:
        print("Not available")


        
        
def get_cpu_info():
     cpu_cores = os.cpu_count()
     cpu_threads = multiprocessing.cpu_count()
     print(f"Number of CPU Cores: {cpu_cores}")
     print(f"Number of CPU Threads: {cpu_threads}")
        
        
def get_gpu_model():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            print("No GPU found")
            gpu_model = gpus[0].name
            print(f"GPU Model: {gpu_model}")
    except Exception as e:
        print(f"Error retrieving GPU information: {e}")
        
def get_ram_size():
    try:
        memory_info = psutil.virtual_memory()
        ram_size_gb = memory_info.total / (1024 ** 3)  
        print(f"RAM Size: {ram_size_gb:.2f} GB")
    except Exception as e:
        print(f"Error retrieving RAM information: {e}")
    
def get_mac_addresses():
    try:
        interfaces = netifaces.interfaces()
        mac_addresses = {}
        for interface in interfaces:
            try:
                mac_address = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
                mac_addresses[interface] = mac_address
            except (ValueError, KeyError):
                pass
        return mac_addresses
    except Exception as e:
        return f"Error retrieving MAC addresses: {e}"
        
def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        data = response.json()
        public_ip = data['ip']
        return public_ip
    except Exception as e:
        return f"Error retrieving public IP address: {e}"
        
def get_windows_version():
    try:
        windows_version = platform.system() + " " + platform.version()
        return windows_version
    except Exception as e:
        return f"Error retrieving Windows version information: {e}"
        
def get_screen_size():
    try:
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(0)  
        height = user32.GetSystemMetrics(1)  
        dpi = 96  # Convert screen size to inches (assuming standard DPI of 96)
        screen_size_inches = (width / dpi, height / dpi)
        return screen_size_inches
    except Exception as e:
        return f"Error retrieving screen size information: {e}"


    

    
        
        
     
            
     
        
        