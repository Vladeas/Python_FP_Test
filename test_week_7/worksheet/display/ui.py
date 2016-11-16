'''
Created on Nov 16, 2016

@author: Vlad
'''

from worksheet.backbone.functions import add,list_total,remove_name,initialize
from _ast import arguments





def _add_ui(warehouse_list, *arguments):
    '''
    List error message if incorrect
    input : list , arguments
    output : -
    '''
    code = add(warehouse_list, *arguments)
    if code == -1:
        print(">>>Incorrect price")
    elif code == -2:
        print(">>>Incorrect quantity")
    elif code == -3:
        print(">>>Incorrect number of arguments")
    pass


def _list(ware_house):
    '''
    List all the items in the list
    input : list of items
    output : -
    '''
    for item in ware_house:
        print(">>>Name : %s, Price : %s, Quantity %s" %(item["name"],item["price"],item["quantity"]))


def _list_ui(warehouse_list,*arguments):
    '''
    Decide Which list option was given
    '''
    if arguments[0] == "all":
        _list(warehouse_list)
    elif arguments[0] == "total":
        print(list_total(warehouse_list))
    else : print(">>>Incorrect command")
    

def _remove_ui(warehouse_list, name):
    '''
    Call the remove function & display message if name was nor found
    input : list, name
    output : -
    '''
    if remove_name(warehouse_list,name) == False:
        print(">>>Name not found")
    pass
    

def _read_command():
    '''
    Read the commands
    output : main command and arguments
    '''
    user_input = input("<<<")
    x = user_input.find(" ")
    if x == -1:
        return user_input,""
    first_c = user_input[:x]
    arguments = user_input[x:]
    return first_c,arguments.split()


def project_start():
    '''
    Call each function accordingly
    '''
    warehouse_list = []
    initialize(warehouse_list)
    commands = {"add": _add_ui, "list": _list_ui, "remove": _remove_ui}
    go = True
    while go:
        try:
            cmd, arguments = _read_command()
            if cmd == "exit":
                go = False
            
            commands[cmd](warehouse_list, *arguments)
        except KeyError:
            print("Incorrect command")
        except ValueError:
            print("Incorrect command")
        except IndexError:
            print("Incorrect command")
            
