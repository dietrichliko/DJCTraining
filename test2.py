#! /usr/bin/env python

import os
import ROOT

INPUT_FILENAMES = '/local/dliko/working/DJCTraining/example_data/train_files.txt'
INPUT_DIR = os.path.dirname(INPUT_FILENAMES)

INPUT_FILES = (os.path.join(INPUT_DIR, name.strip()) for name in open(INPUT_FILENAMES, 'r').readlines())

df = ROOT.RDataFrame('tree', INPUT_FILES)

df1 = df.Define("x", "gRandom->Uniform(-1.0, 1.0)")\
        .Define("x2","Dot(image,xcoords)/Sum(xcoords)")

#for name in df1.GetColumnNames():
#    print ( '{} : {}'.format(name,df.GetColumnType(name)) )
print ('\nNumber of Entries = {}'.format(df1.Count().GetValue()))

print ( df.Mean('x2').GetValue() )
