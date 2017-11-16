''' This script orders the stack from strongest M dwarf source to faintest '''

import numpy as np
import pyfits as pf
from stack.py import



radioSources = np.genfromtxt('/Users/Francis/gammaRayResearch/radioBased/radioSurvey_McLean_2012.txt',dtype=None, skip_header=71, skip_footer=2, delimiter=(8,9,15,13,5,4,5,6,6,2,6,4,6,33,10,10), autostrip=True)

xraySources = np.genfromtxt('/Users/Francis/gammaRayResearch/xrayBased/shkolnikMdwarfs.txt',dtype=None, skip_header=57, skip_footer=1, delimiter=(8,9,28,5,6,5,7,7,7,12,12), autostrip=True)

def recordList(Y):                  ## Same as star_list() in stack.py
    list = []
    removed = []
    with open("/Users/Francis/gammaRayResearch/mdwarfStack/"+Y+"/stackRecord.txt",'r') as f:
        f.readline()
        for line in f:
            if line.strip() != "" and line.find("Removed") == -1:                             ## Checks if "Removed" is not in the line and if line is not blank
                star = line.strip().split(" :: ")[0]
                list.append(star)
            elif line.find("Removed") != -1:
                rmstar = line.strip().split()[1]                            ## Makes list of stars that have been removed
                removed.append(rmstar)
        for rm in removed:
            list.remove(rm)
    return list

def rename(type):
    fileNameList = []
    for src in type:
        name = src[13]
        fileName = name.replace(" ","_")
        fileNameList.append(fileName)
    return fileNameList

def order(type):
    Sources = rename(type)
    if type == radioSources:
        for src in type:
        

def constructOrderedStk()
        
