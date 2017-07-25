import sys

# sys.argv
# want to get help with -help or -help


def get_optional_arg(position):
    try:
        return sys.argv[position]
    except IndexError:
        pass

def get_required_arg(position):
    try:
        return sys.argv[position]
    except IndexError:
        raise IndexError("Required param was not passed!")

def parse_sysargv_to_list_of_dicts():
    parsed_list = {}
    flag = False
    for index, item in enumerate(sys.argv):
        if flag is True:
            parsed_list.update({list(parsed_list.items())[-1][0]: item})
            pass

        if item == "-help":
            print("some help here...")
            break
        elif  item.startswith("-"):
            print("it's probably an option - hext param is a value")
            parsed_list.update({item:None})
            flag=True
        print(str(index) + " " + str(item))
        print(parsed_list)

parse_sysargv_to_list_of_dicts()



# try:

# except? e:
#     raise e