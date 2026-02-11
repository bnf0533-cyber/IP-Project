from reader import *
def filter_by_sensitive_ports(data_rows):
    sensitive_ports = ["22", "23", "3389"]
    return [row for row in data_rows if row[3] in sensitive_ports]
# print(filter_by_sensitive_ports(x))

def get_external_ips(data_rows):
    return [external_ips[1] for external_ips in data_rows if not external_ips[1].startswith(("192.168","10"))]
# print(get_external_ips(x))

def checks_size(data_size):
    return [bigger for bigger in data_size if int(bigger[5]) > 5000]
