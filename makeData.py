#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = "lee"

import pymongo
from pymongo import MongoClient
import random
import collections
import re



client=MongoClient('127.0.0.1',27017)
db_name='aimedical-admin'
db=client[db_name]
source_set = db.rule

info_date=collections.OrderedDict()

newdata=[]

def find_data(rule_id):
    temp_result=db.rule.find_one({"rule_id":rule_id})
    sex=temp_result.get("rule_sex")
    age=temp_result.get("rule_age")
    manifestations=temp_result.get("rule_manifestations")
    random_index = 0
    sex=getRandomSex(sex)
    age=getRandomAge(age)
    manifestations=getRandomM(manifestations)

    info_date['sex']=sex
    info_date['age']=age
    info_date['manifestations']=manifestations

    storageDate(info_date)

    print(sex)
    print(age)
    print(manifestations)

def storageDate(info_date,num):
    for i in num:
        db.data.insert(info_date)


def getRandomSex(parm):
    newdata =random.sample(parm,1)#随机获取一个list

    return newdata[0]


def getRandomAge(parm):
    newdata = random.sample(parm, 1)  # 随机获取一个list
    global random_index #记录一个与age位置相对应的
    random_index = parm.index(newdata[0])
    newdata = newdata[0].lstrip('[').rstrip(']').split(',')

    tmp_random = random.randint(int(newdata[0]), int(newdata[1]))  # 生成随机值
    newdata = []
    newdata.append(str(tmp_random))

    return newdata[0]

def getRandomM(parm):
    newdata=parm[random_index]  #与age级联获得数据
    for i in range(len(newdata)):#遍历
        random_data=newdata[i].get("value")
        random_data=random_data.lstrip('[').rstrip(']').split(',')
        random_data=random.uniform(0,float(random_data[1]))
        random_data=round(random_data,2)

        newdata[i]['value']=str(random_data)
    return newdata




if __name__ == '__main__':

    rule_id = "a723979f9c5f4039808b22d512e11111"
    find_data(rule_id)


