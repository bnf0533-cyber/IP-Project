
def return_list_of_lists(path):
    with open(path,"r") as log:
        return [list_of_data.strip().split(",") for list_of_data in log]
path = "C:\\Users\\bnf05\\PycharmProjects\\project\\ip project\\network_traffic.log"
x = return_list_of_lists(path)

def get_external_ips(data_rows):
    return [external_ips[1] for external_ips in data_rows if not external_ips[1].startswith(("192.168","10"))]
print(get_external_ips(x))