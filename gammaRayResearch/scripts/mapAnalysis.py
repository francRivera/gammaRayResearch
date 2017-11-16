## This script creates a residual map .fits file by subtracting each pixel value of the counts map from the model map.
## Also, this script calculates the significance map each pixel value of the residual map divided by the sqrt(model map pixel values)]
import pyfits as pf
import numpy as np
import os 

srcname = os.environ['srcname']


def calcResidMap(cMap,mMap):
    cdata , cheader = pf.getdata(str(cMap) ,header=True)
    mdata , mheader = pf.getdata(str(mMap) ,header=True)
    residMap = cdata - mdata
    return residMap , cheader

def calcSigMap(cMap,mMap):
    cdata , cheader = pf.getdata(str(cMap) ,header=True)
    mdata , mheader = pf.getdata(str(mMap) ,header=True)
    sigMap = (cdata - mdata) / (np.sqrt(mdata))
    return sigMap , cheader


# def main():
#     cMap = raw_input("Counts Map: ")
#     mMap = raw_input("Model Map: ")
#     Residual_fileDir = raw_input("Residual file Destination: ")
#     Significance_fileDir = raw_input("Significance file Destination: ")
#     rdata , rheader = calcResidMap(cMap,mMap)
#     pf.writeto(Residual_fileDir, rdata, rheader, clobber=True)
#     sdata , sheader = calcSigMap(cMap,mMap)
#     pf.writeto(Significance_fileDir, sdata, sheader , clobber=True)

## MODIFIED TO RUN AUTONOMOUSLY:
def main(srcname,cMap,mMap):
     rdata , rheader = calcResidMap(cMap,mMap)
     pf.writeto(str(srcname)+'_residualMap.fits', rdata, rheader, clobber=True)
     sdata , sheader = calcSigMap(cMap,mMap)
     pf.writeto(str(srcname)+'_significanceMap.fits', sdata, sheader , clobber=True)
     statResCount = str(np.mean(rdata))+" +/- "+ str(np.std(rdata, ddof=1))
     print ("RESIDUAL MAP STATISTICS:\n"+ statResCount)


# if __name__=="__main__":
#     main()
# else:
#     print ("Name not equal to main:", __name__ )
