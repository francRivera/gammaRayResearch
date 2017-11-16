## This script is simply for building the stacked maps of the M-Dwarfs

import pyfits as pf
import numpy as np
import os
from datetime import datetime as dt


srcname = os.environ['srcname']
type = os.environ['type']


def stack(x,star,resid,stkType):
    currentStack = pf.getdata('/Users/Francis/gammaRayResearch/mdwarfStack/'+stkType+'/stackedMaps.fits')
    resData = pf.getdata(resid)
    if x == "add":        
        record("add",star,stkType)
        starList = star_list(stkType)                                                              
        stackdata = currentStack + resData                                                   ## New algorthim to add residual map or remove existing 
#        stackdata = currentStack + ((resData - currentStack)/(len(starList)))               ## residual map to/from the current average (currentStack).
    elif x == "rm":                                                                          ## NOTE: one code for avg counts, another for sum of counts.
        record("rm",star,stkType)
        starList = star_list(stkType)
        stackdata = currentStack - resData
#        stackdata = currentStack + ((currentStack - resData)/(len(starList)))
    pf.writeto('/Users/Francis/gammaRayResearch/mdwarfStack/'+stkType+'/stackedMaps.fits', stackdata, clobber=True)	## Updates the new stack
    return stackdata


def star_list(Y):
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

def record(x,rmStar,type):
    if x == "add":
        with open("/Users/Francis/gammaRayResearch/mdwarfStack/"+type+"/stackRecord.txt",'a') as f:
            f.write(rmStar+" :: "+str(dt.now())+"\n")
    elif x == "rm":
        with open("/Users/Francis/gammaRayResearch/mdwarfStack/"+type+"/stackRecord.txt",'a') as f:
            f.write("Removed "+rmStar+" :: "+str(dt.now())+"\n")

def add():
    starList = star_list(type)
    if srcname not in starList:
        resMap = srcname+"_residualMap.fits"	        ## Stores the working directory's residual map as resMap
        stackData = stack('add',srcname,resMap,type)			## Adds resMap to the stack
        starList = star_list(type)
        print ("\n Stack Updated: Added "+srcname+" \n")
        print (" Number of Residual Maps in Stack :"+str(len(starList))+" \n")
    else:
        print ("\n Error: "+srcname+" is already in stack \n")

def remove():
    stackType = raw_input("Which stack do you want to remove from? [xray or radio] >> ")
    rmStar = raw_input("Which source do you want to remove? [include any underscores] >> ")
    starList = star_list(stackType)
    if rmStar in starList:
        resMap = "/Users/Francis/gammaRayResearch/"+stackType+"Based/"+rmStar+"/"+rmStar+"_residualMap.fits"
        stackData = stack('rm',rmStar,resMap,stackType)
        starList = star_list(stackType)
        print ("\n Stack Updated: Removed " +rmStar+" \n")
        print ("\n Residual Maps in Stack :"+str(len(starList))+" \n")
    else: 
        print("\n Error: "+rmStar+" is not in stack \n")
        
## A record of the stack is made with bash command in /Users/Francis/gammaRayResearch/mdwarfStack/stackRecord.txt
    
