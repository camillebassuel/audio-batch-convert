import os 
import importlib as imp
import numpy as np
import matplotlib.pyplot as plt
import batchmp3
import random, string
from os import listdir
from genericpath import isdir
from os.path import isfile, join
imp.reload(batchmp3)

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def getAllFolders(pathin):
        return [f for f in listdir(pathin) if isdir(join(pathin, f))]

def getAllFiles(pathin):
        return [f for f in listdir(pathin) if isfile(join(pathin, f))]

def getPathFilesAndFolders(path):
    return (path, getAllFolders(path))



def getAllNestedFolders(path, ret):
    tup = getPathFilesAndFolders(path)
    if len(tup)>0:
        ret.append(tup)
    for folder in tup[1] :
        fpath = path + '/'+ folder
        getAllNestedFolders(fpath,ret)

pathin =  'the folder it will read files from'
pathout =  'the folder it will write the files to'

pathdatas = []
getAllNestedFolders(pathin,pathdatas)

for datas in pathdatas :
    dirin = datas[0]
    dirout = pathout
    if not os.path.isdir(dirout):
        os.mkdir(dirout)
    batchmp3.convert(dirin,dirout)
