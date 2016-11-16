'''
Created on Nov 16, 2016

@author: Vlad
'''

from worksheet.backbone.functions import add,list_total,remove_name

def _test_init(listt):
    listt.append({"name": "car","price": "1200","quantity": "12"})
    listt.append({"name": "cat","price": "10","quantity": "22"})
    listt.append({"name": "dog","price": "30","quantity": "4"})
    listt.append({"name": "magic_carpet","price": "800","quantity": "32"})
    listt.append({"name": "plate","price": "5","quantity": "102"})
    

def _test_add():
    listt = []
    _test_init(listt)
    assert add(listt,"name","as","12") == -1
    assert add(listt,"name","12","er") == -2
    assert add(listt,"name","as","qwe") == -1
    assert add(listt,"name","12","123") == 1


def _test_remove():
    listt = []
    _test_init(listt)
    assert remove_name(listt,"gun") == False
    assert remove_name(listt,"car") == True
    

def test():
    _test_add()