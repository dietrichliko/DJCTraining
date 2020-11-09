#! /usr/bin/env python

import os
import ROOT

INPUT_FILENAMES = '/local/dliko/working/DJCTraining/example_data/train_files.txt'
INPUT_DIR = os.path.dirname(INPUT_FILENAMES)

INPUT_FILES = (os.path.join(INPUT_DIR, name.strip()) for name in open(INPUT_FILENAMES, 'r').readlines())

df = ROOT.RDataFrame('tree', INPUT_FILES)

df = df.Define('xcen','Dot(xcoords,image)/Sum(image)')\
       .Define('ycen','Dot(ycoords,image)/Sum(image)')

for name in df.GetColumnNames():
    print ( '{} : {}'.format(name,df.GetColumnType(name)) )           
print ('\nNumber of Entries = {}'.format(df.Count().GetValue()))

print ( df.Mean('xcen').GetValue() )
