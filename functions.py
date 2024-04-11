from psutil import disk_partitions, disk_usage
from shutil import copy
from os.path import join as os_join, exists as os_exists, getsize as os_getsize
from time import sleep, time
from win32api import GetVolumeInformation
from os import getcwd

# Find the camera using the volume name, and look for files
def find_camera():
    for partition in disk_partitions(all=True):
        try:
            volume_name = GetVolumeInformation(partition.device)[0]
        except Exception:
            volume_name = None
        if volume_name == "CAMPSNAP":
            camera_drive = partition.mountpoint
            necessary_files = ["ISP.BIN", "DRAMPARA.txt", "1628.bin"]
            if not all(os_exists(os_join(camera_drive, f)) for f in necessary_files):
                return camera_drive
            return False
    return None

# Import new filter files
def new_filter(filter_name):
    camera_drive = find_camera()
    if camera_drive is None:
        print("Camera not found")
        return None
    if camera_drive is False:
        print("Files already exist, restart camera")
        return False

    filter_dir = os_join(getcwd(), "filters", filter_name)
    print(filter_dir)
    for filename in ("ISP.BIN", "DRAMPARA.txt", "1628.bin"):
        source_file = os_join(filter_dir, filename)
        target_file = os_join(camera_drive, filename)
        if os_exists(source_file):
            copy(source_file, target_file)
            print(f"{filename} transferred.")
            start_time = time()
            while os_getsize(source_file) != os_getsize(target_file):
                elapsed_time = time() - start_time
                if elapsed_time >= 10:
                    print(f"Timed out waiting for {filename} transfer.")
                    return
                sleep(1)
            print(f"Size of transferred {filename} matches the original.")
        else:
            print(f"{filename} not found.")
            return
    return True

'''
# Debug
def main(filter_name):
    new_filter(filter_name)

main("vintage-filter")
'''
