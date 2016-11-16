'''
Created on Nov 16, 2016

@author: Vlad
'''

def initialize(warehouse_list):
    '''
    Initialize the list with given items
    '''
    warehouse_list.append({"name": "car","price": "1200","quantity": "12"})
    warehouse_list.append({"name": "cat","price": "10","quantity": "22"})
    warehouse_list.append({"name": "dog","price": "30","quantity": "4"})
    warehouse_list.append({"name": "magic_carpet","price": "800","quantity": "32"})
    warehouse_list.append({"name": "plate","price": "5","quantity": "102"})
    warehouse_list.append({"name": "boot","price": "13","quantity": "56"})
    warehouse_list.append({"name": "apple","price": "4","quantity": "1000"})
    warehouse_list.append({"name": "house","price": "10200","quantity": "2"})
    warehouse_list.append({"name": "helicopter","price": "1000","quantity": "1"})
    warehouse_list.append({"name": "plane","price": "450","quantity": "17"})


def check_integer(number):
    '''
    Check if a string is a positive integer
    '''
    try:
        x = int(number)
        if x < 0:
            return False
        return True
    except ValueError:
        return False


def add(warehouse_list, *arguments):
    '''
    Add a new item to the ware_house list
    input : List of items & Name, price & quantity
    output : a numerical value
    '''
    if len(arguments) != 3:
        return -3
    elif check_integer(arguments[1]) == False:
        return -1
    elif check_integer(arguments[2]) == False:
        return -2
    warehouse_list.append({"name": arguments[0],"price": arguments[1],"quantity": arguments[2]})
    return 1


def list_total(warehouse_list):
    '''
    Calculate the total value of the products
    input : item list
    output : total value
    '''
    total = 0
    for item in warehouse_list:
        total += int(item["price"])*int(item["quantity"])
    return total


def _remove(warehouse_list, name):
    '''
    Remove an element
    '''
    warehouse_list[:] = [item for item in warehouse_list if item["name"] != name]


def remove_name(warehouse_list, name):
    '''
    check if the the item was found and call the remove function
    input : item list
    output : True or False
    '''
    x = len(warehouse_list)
    _remove(warehouse_list, name)
    if x != len(warehouse_list):
        return True
    return False
    pass