from platform import system, version
import psutil
import cpuinfo
import os

ram_stats = psutil.virtual_memory()
cpu_stats = psutil.cpu_count
disk_stats = psutil.disk_usage('/')
cpu_info = cpuinfo.get_cpu_info()

print("   HARDWARE AND OPERATING SYSTEM INFO")
print()
print("   OS INFO")
print("   OS            :", system(), version())
print("   HOSTNAME      :", psutil.users()[0].name)
print()
print("   CPU INFO")
print("   CPU            :", cpu_info['brand'])
print("   ARCHITECHTURE  :", cpu_info['raw_arch_string'], "|", cpu_info['bits'], "bit")
print("   CPU CORES      :", (cpu_stats(logical=False)))
print("   CPU THREADS    :", cpu_info['count'])
print("   GHz per core   :", cpu_info['hz_actual'])
print()
print("   MEMORY INFO")
print("   USED RAM       :", (int(round(ram_stats[3] / 1024) / 1024)), "MB")
print("   AVAILABLE RAM  :", (int(round(ram_stats[1] / 1024) / 1024)), "MB")
print("   TOTAL RAM      :", (int(round(ram_stats[0] / 1024) / 1024)), "MB")
print()
print("   SYSTEM DISK INFO")
print("   OS USED SPACE  :", (int(round(disk_stats[1] / 1024 / 1024 / 1024))), "GB")
print("   OS FREE SPACE  :", (int(round(disk_stats[2] / 1024 / 1024 / 1024))), "GB")
print("   OS TOTAL SPACE :", (int(round(disk_stats[0] / 1024 / 1024 / 1024))), "GB")
print()
