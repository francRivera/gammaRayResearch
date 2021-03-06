## This script takes in the binned1_output.xml file and sets the free parameters of all sources (except the source being studied) to zero.
## Then it'll save the new xml file as "<source>_binned1_output2.xml".
from lxml import etree

def addSource(srcname, infile, RA, DEC):
    source_library = etree.parse(infile)
    root = source_library.getroot()
    addedSrc = etree.fromstring('''<source name="'''+srcname+'''" type="PointSource">
    <spectrum type="PowerLaw2">
      <parameter error="0.0004651207134" free="1" max="1000" min="1e-08" name="Integral" scale="1e-08" value="7.009504005e-08" />
      <parameter error="1802.205645" free="1" max="-1" min="-5" name="Index" scale="1" value="-2.336895014" />
      <parameter free="0" max="100000" min="100" name="LowerLimit" scale="1" value="100" />
      <parameter free="0" max="100000" min="100" name="UpperLimit" scale="1" value="100000" />
    </spectrum>
    <spatialModel type="SkyDirFunction">
      <parameter free="0" max="360" min="-360" name="RA" scale="1" value="'''+RA+'''" />
      <parameter free="0" max="90" min="-90" name="DEC" scale="1" value="'''+DEC+'''" />
    </spatialModel>
  </source>
''')
    root.append(addedSrc)
    return root

def modify(srcname, RA, DEC, infile):
    modSrc = addSource(srcname, infile, RA, DEC)
    modFile = open(srcname+'_binned1_output_modified.xml','w')
    modFile.write(etree.tostring(modSrc,pretty_print=True))
    modFile.close()
    for source in modSrc:
        parameters = source.findall('spectrum/parameter')+source.findall('spatialModel/parameter')
        if source.attrib.get('name') != srcname:
            for p in parameters:
                p.set('free','0')
    saveFile = open(srcname+'_binned1_output2.xml','w')
    saveFile.write(etree.tostring(modSrc,pretty_print=True))
    saveFile.close()
    
    
# if __name__=="__main__":
#     from lxml import etree
# else:
#     print ("Name not equal to main:", __name__ )


# modify('TESTING_SOURCE','-999','-999','/Users/Francis/fermiTools/practiceFermiTools/3C279_binned_output_noplot.xml')
