import psutil

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage : {usage}%")
def check_memory_usage():
    memory= psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
def check_disk_usage():
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
