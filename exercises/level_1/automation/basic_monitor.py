# TODO: make it work
from threaders import threaders
import psutil
import datetime
import time


def system_stats_raw():
    boot_time = psutil.boot_time()
    return {
        "memory": psutil.virtual_memory(),
        "cpu": psutil.cpu_percent(),
        "disk": psutil.disk_usage("/"),
        "pids": len(psutil.pids()),
        "boot_time": datetime.datetime.fromtimestamp(boot_time),
        "uptime": time.time() - boot_time,
    }


def bytes_to_GB(bytes):
    return round(bytes/1000000000, 3)


def monitor_machine():
    def get_stats():
        """:rtype: threaders.Thread"""
        stats = system_stats_raw()
        print(f"CPU {stats['cpu']}%  MEMORY {stats['memory'].percent}%  DISK {stats['disk'].percent}%  Running Processes {stats['pids']}")

    @threaders.threader()
    def quit():
        """:rtype: threaders.Thread"""
        input('\n         Press Enter to stop monitoring\n\n')


    print("======================== Monitor ========================")
    stats = system_stats_raw()
    print(f"Last Boot: {stats['boot_time']}")
    print(f"System Uptime: {datetime.timedelta(seconds=stats['uptime'])}\n")

    print(
        f"MEMORY"
        f" total {bytes_to_GB(stats['memory'].total)}GB "
        f"| used {bytes_to_GB(stats['memory'].used)}GB "
        f"| free {bytes_to_GB(stats['memory'].free)}GB "
    )
    print(
        f"DISK"
        f" total {bytes_to_GB(stats['disk'].total)}GB "
        f"| used {bytes_to_GB(stats['disk'].used)}GB "
        f"| free {bytes_to_GB(stats['disk'].free)}GB "
    )

    stop_thread = quit()
    time.sleep(2)
    while stop_thread.is_alive():
        get_stats()
        time.sleep(2)

    stop_thread.join()


monitor_machine()