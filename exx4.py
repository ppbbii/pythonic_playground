import sys

# sys.argv
# want to get help with -help or -help
import logging


logging.basicConfig(level=logging.INFO)

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
    flag_dict = {
        'f1': 1,
        'f2': 2,
        'f3': 3,
    }

    known_option_dict = {
        '-h': 0,
        '-help': 0
    }

    next_item_is_value = False
    option_name = ''

    for index, item in enumerate(sys.argv):

        # if flag is True:
        #     parsed_list.update({list(parsed_list.items())[-1][0]: item})
        #     pass
        #
        if item == "-help":
            print("some help here...")
            break
        elif item.startswith("-"):
            logging.info("it's probably an option - next param is a value {0}".format(item))
            # parsed_list.update({item:None})
            next_item_is_value=True
            option_name = item
        elif next_item_is_value is True:
            next_item_is_value = False
            logging.info("This {0} is value for option {1}".format(item, option_name))
        # print(str(index) + " " + str(item))
        # print(parsed_list)
        elif item in flag_dict.keys():
            logging.info("This is probably a flag: {}".format(item))

parse_sysargv_to_list_of_dicts()



# try:

# except? e:
#     raise e