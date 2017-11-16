## This Script takes in an initial radius and a final radius and outputs the total counts within the annulus bounded by the two radii.
import numpy as np
import pyfits as pf


def annulusCounts(cmap,r,R):
    cmapData = pf.getdata(str(cmap))
#    cmapData = cmapData * 0 +1
    index = np.transpose(np.where(cmapData==cmapData))         ## coordinate [x,y] for each pixel
    center = [ len(cmapData)/2 , len(cmapData[0])/2 ]
    totalCounts = np.array([0])
    indices = np.array(['x','y'])
    for l in index:
        annulus = ((l[0] - center[0] )**2) + ((l[1] - center[1] )**2)      ## Equation of circle
        if annulus > r**2 and annulus <= R**2:
            totalCounts = np.append(totalCounts,cmapData[l[0],l[1]])       ## Appends count# from that index to totalCounts
            indices = np.vstack((indices,np.array([l[0],l[1]])))
    if r == 0:
        totalCounts = np.append(totalCounts,cmapData[center[0],center[1]])
        indices = np.vstack((indices,np.array([center[0],center[1]])))
#    print totalCounts
#    print(indices)
    print("Number of pixels: "+str(totalCounts.size-1))
    sum = np.sum(totalCounts) 
    print("Total counts in this annulus: "+ str(sum))
#    return indices
#    return totalCounts
    return sum

## We want counts within the same amount of Areas.
## For a circle of radius r and an annulus around that circle to have the same Area,
## the outer radius of the annulus has to be larger than the inner radius by a factor of sqrt(2). [R = r * sqrt(2)]
## For and additional annulii, the outer radius, R, is related to the radius of the initial circle, r, as:
## R_n = r * sqrt(n+1) , where n is the number of the annulus from the circle. 

def compareCounts(cmap):
    circCounts = annulusCounts(cmap,0,10)
    annCounts = annulusCounts(cmap,10,14.15) + cmap[42][31]                ## Note: Added a pixel to the annulus [point (32,43) on the ds9 map] to 
    ratio = circCount/annCounts                                            ## get same amount for circle and annulus
    return circCounts , annCounts , ratio
