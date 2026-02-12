from sys import path_importer_cache

from reader import *
def count_requests_by_ip(data):
    all_ip = [row[1] for row in data]
    return {ip: all_ip.count(ip) for ip in set(all_ip)}
all_ips = count_requests_by_ip(x)

def map_port_to_protocol(data):
    return {int(row[3]): row[4] for row in data}
print(map_port_to_protocol(x))