
def return_list_of_lists(path):
    with open(path,"r") as log:
        return [list_of_data.strip().split(",") for list_of_data in log]
path = "C:\\Users\\bnf05\\PycharmProjects\\project\\ip project\\network_traffic.log"
x = return_list_of_lists(path)

