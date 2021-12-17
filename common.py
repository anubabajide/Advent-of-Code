def get_input(file_name):
    with open(file_name, "r") as handler:     
        vals = handler.read().split('\n')
    return vals

def get_numeric_input(file_name):
    with open(file_name, "r") as handler:     
        nums = [int(x) for x in handler.read().split('\n')]
    return nums