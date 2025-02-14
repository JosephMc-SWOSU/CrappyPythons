# Required installations:
# pip install psutil GPUtil setuptools

import psutil
import GPUtil
import platform
from datetime import datetime

def get_system_info():
    # Get CPU information
    cpu_load = psutil.cpu_percent(interval=1)
    cpu_clock_speed = psutil.cpu_freq().current

    # Get RAM information
    ram_info = psutil.virtual_memory()
    ram_usage = ram_info.percent
    total_ram = ram_info.total / (1024 ** 3)  # Convert bytes to GB

    # Get GPU information
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            'name': gpu.name,
            'load': gpu.load * 100,
            'memory_total': gpu.memoryTotal,
            'memory_used': gpu.memoryUsed,
            'memory_free': gpu.memoryFree
        })

    # Get other system information
    system_info = {
        'platform': platform.system(),
        'platform_version': platform.version(),
        'platform_release': platform.release(),
        'architecture': platform.machine(),
        'hostname': platform.node(),
        'processor': platform.processor()
    }

    return {
        'cpu_load': cpu_load,
        'cpu_clock_speed': cpu_clock_speed,
        'ram_usage': ram_usage,
        'total_ram': total_ram,
        'gpu_info': gpu_info,
        'system_info': system_info
    }

def print_system_info(info):
    print(f"CPU Load: {info['cpu_load']}%")
    print(f"CPU Clock Speed: {info['cpu_clock_speed']} MHz")
    print(f"RAM Usage: {info['ram_usage']}%")
    print(f"Total RAM: {info['total_ram']:.2f} GB")
    for gpu in info['gpu_info']:
        print(f"GPU Name: {gpu['name']}")
        print(f"GPU Load: {gpu['load']}%")
        print(f"GPU Memory Total: {gpu['memory_total']} MB")
        print(f"GPU Memory Used: {gpu['memory_used']} MB")
        print(f"GPU Memory Free: {gpu['memory_free']} MB")
    print(f"Platform: {info['system_info']['platform']}")
    print(f"Platform Version: {info['system_info']['platform_version']}")
    print(f"Platform Release: {info['system_info']['platform_release']}")
    print(f"Architecture: {info['system_info']['architecture']}")
    print(f"Hostname: {info['system_info']['hostname']}")
    print(f"Processor: {info['system_info']['processor']}")

def save_system_info(info, filename):
    if not filename.endswith('.txt'):
        filename += '.txt'
    with open(filename, 'w') as file:
        file.write(f"CPU Load: {info['cpu_load']}%\n")
        file.write(f"CPU Clock Speed: {info['cpu_clock_speed']} MHz\n")
        file.write(f"RAM Usage: {info['ram_usage']}%\n")
        file.write(f"Total RAM: {info['total_ram']:.2f} GB\n")
        for gpu in info['gpu_info']:
            file.write(f"GPU Name: {gpu['name']}\n")
            file.write(f"GPU Load: {gpu['load']}%\n")
            file.write(f"GPU Memory Total: {gpu['memory_total']} MB\n")
            file.write(f"GPU Memory Used: {gpu['memory_used']} MB\n")
            file.write(f"GPU Memory Free: {gpu['memory_free']} MB\n")
        file.write(f"Platform: {info['system_info']['platform']}\n")
        file.write(f"Platform Version: {info['system_info']['platform_version']}\n")
        file.write(f"Platform Release: {info['system_info']['platform_release']}\n")
        file.write(f"Architecture: {info['system_info']['architecture']}\n")
        file.write(f"Hostname: {info['system_info']['hostname']}\n")
        file.write(f"Processor: {info['system_info']['processor']}\n")

if __name__ == "__main__":
    info = get_system_info()
    print_system_info(info)

    save_option = input("Do you want to save the system info to a file? (y/n): ").strip().lower()
    if save_option == 'y':
        filename = input("Enter the filename to save the system info: ").strip()
        save_system_info(info, filename)
        print(f"System info saved to {filename}")