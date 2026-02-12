from sys import path_importer_cache
from checks import *
from reader import *
def count_requests_by_ip(data):
    all_ip = [row[1] for row in data]
    return {ip: all_ip.count(ip) for ip in set(all_ip)}
all_ips = count_requests_by_ip(x)

def map_port_to_protocol(data):
    return {int(row[3]): row[4] for row in data}
# print(map_port_to_protocol(x))

def check_night_activity(night_data):
    return [line for line in night_data if line[0].split()[1].startswith(("00", "01", "02", "03", "04", "05"))]
# print(check_night_activity(x))

def identify_suspicions_per_ip(data):
    ext_ips = set(get_external_ips(data))
    sens_ips = {row[1] for row in filter_by_sensitive_ports(data)}
    large_ips = {row[1] for row in checks_size(data)}
    night_ips = {row[1] for row in check_night_activity(data)}
    unique_ips = {row[1] for row in data}
    return {
        ip: [
            tag for condition, tag in [
                (ip in ext_ips, "EXTERNAL_IP"),
                (ip in sens_ips, "SENSITIVE_PORT"),
                (ip in large_ips, "LARGE_PACKET"),
                (ip in night_ips, "NIGHT_ACTIVITY")
            ] if condition
        ]
        for ip in unique_ips
    }
# print(identify_suspicions_per_ip(x))

def filter_high_risk_ips(suspicions_dict):
    return {ip: tags for ip, tags in suspicions_dict.items()if len(tags) >= 2}
all_data = identify_suspicions_per_ip(x)
final_filtered_data = {ip: tags for ip, tags in all_data.items() if len(tags) >= 2}
print(final_filtered_data)