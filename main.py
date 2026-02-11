
def return_list_of_lists(path):
    list_of_data = []
    with open(path,"r") as log:
        for line in log:
            list_of_data.append(list(line.split()))
        return list_of_data
data = return_list_of_lists("C:\\Users\\bnf05\\PycharmProjects\\project\\ip project\\network_traffic.log")