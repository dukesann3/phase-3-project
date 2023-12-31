

def print_all_property_of_obj(obj):
    for property, value in vars(obj).items():
        print(property, ":", value)