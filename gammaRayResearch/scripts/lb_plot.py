## This script is to plot the Galactical coordinates of the Mdwarfs on Shkolniks catalogue and to filter the data for Mdwarfs with Galactical latitudes away from the plane of the Milkyway (|Glat| < 25deg). The filtered soures are then saved to sourceList.txt file.
import numpy as np
from matplotlib import pyplot as plt


data = np.genfromtxt('/Users/Francis/gammaRayResearch/xrayBased/shkolnikMdwarfs.txt',dtype=None, skip_header=57, skip_footer=1, delimiter=(8,9,28,5,6,5,7,7,7,12,12), autostrip=True)
#print data , len(data)
XY = np.array([])
for a in range(len(data)):                ## Looping to add all the Glon & Glat values to the x & y-arrays.(Note: 'data' is an array containing lists; that's why data[i][j] is
   XY = np.append(XY,[data[a][0],data[a][1]],axis=None)                                                                                         ## used to indicate the values.
                                          ## np.append permanently adds an element to an array (Note: the elements to add must have the same number of dimensions.)
T = XY.reshape(155,2)
x,y = np.transpose(T)

XY_= np.array([])                     ## Since we want close stars we require that the Galactical Latitude of the Mdwarfs to be < -25deg & > 25deg.
for t in T:
   if np.absolute(t[1]) > 25:
       XY_= np.append(XY_,t,axis=None)
T_= XY_.reshape((len(XY_)/2),2)
x_,y_= np.transpose(T_)


plt.scatter(x,y,label="M-dwarfs from Shkolnik's servey")
plt.scatter(x_,y_,color='red',label='M-dwarfs 25deg away from the plane of the Milkyway')
plt.xlabel('Glon', fontsize='xx-large')
plt.ylabel('Glat', fontsize='xx-large')
plt.legend(loc='lower left', frameon=True)

## Now to filter the shkolnik .txt file to show the information for the close M-dwarfs and save/write it in a new file.
save = raw_input("Save sources to sourceList.txt (y,n)? ")
if save == 'y':
    with open('sourceList.txt','w') as srcfile:
        srcfile.write("# Glon (deg) | Glat(deg) | Name | Spt | Dist (pc) | e_Dist (pc) | Jmag (mag) | [Fx/Fj] ([-]) | W (Ha) (0.1nm) | RAJ2000 ('h:m:s') | DEJ2000 ('d:m:s') \n")
        for t in T_:
            for D in data:
                if t[0]==D[0] and t[1]==D[1]:
                    D_str = map(str,D)                     ## map(type,list) converts the elements of a list entered to the type(int, float, str). 
                    srcfile.write(" | ".join(D_str) + "\n")    ## We convert the elements into a list inorder to use the .join() command.
        print("Sent data to " + str(srcfile) + ".")
else:
## Put plt.show() at the end because the script pauses until you exit the plot.
    plt.show()
plt.show()      ## One plot() for the if statement, other to show plot anyway.
