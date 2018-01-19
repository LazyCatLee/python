#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = "@lee"

import pymongo
from pymongo import MongoClient
import random
import collections
import re



client=MongoClient('127.0.0.1',27017)
db_name='seedata_v8'
db=client[db_name]


make_date={}

def getData():

    ITEM_VALUE=[]
    finall_result=[]


    class_result=db.labdetail690012.distinct("ITEM_CLASS")
    class_result=class_result[0:9]
    # ITEM_CLASS =class_result
    for i in class_result:
        name_result=db.labdetail690012.find({"ITEM_CLASS":class_result[i]})
        name_result=list(set(name_result))
        # ITEM_NAME=name_result
        for j in name_result:
            value_result=db.labdetail690012.find({"ITEM_CLASS":class_result[i],"ITEM_NAME":name_result[j]})
            value_result=value_result.get("RESULT")
            value_result=list(set(value_result))
            if checkValue(value_result):
                value_result=changeNum(value_result)
                ITEM_VALUE=value_result.sort()
                finall_result.append(str(min(value_result)),str(max(value_result)))
            else:
                finall_result=value_result

            make_date={'ITEM_CLASS':class_result[i],'ITEM_CLASS':class_result[i],'RESULT':finall_result}
            simulation_test = {'ITEM_CLASS':class_result[i],'ITEM_CLASS':class_result[i],'RESULT':ITEM_VALUE}


    uploadDate(make_date,simulation_test),

            # make_date['ITEM_CLASS']=class_result[i]
            # make_date["ITEM_NAME"]=name_result[j]
            # make_date['RESULT']=finall_result


def uploadDate(make_date,simulation_test):
    db.made_datas_test.insert(make_date)
    db.made_normal_datas.insert(simulation_test)

def changeNum(str_list):
    for index, item in enumerate(str_list):
        str_list[index] = eval(item)
    return str_list


def checkValue(value):
    try:
        float(value[0])
        return True
    except:
        return False



if __name__ == '__main__':

    getData()