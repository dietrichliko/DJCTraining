#! /usr/bin/env python

import os
import ROOT

from contextlib import contextmanager

ROOT.TH1.AddDirectory(False)

@contextmanager
def canvas(name="c1", stop=True, oname=None, xsize=580, ysize=760):
    canvas = ROOT.TCanvas(name, "canvas", xsize, ysize)
    yield canvas
    canvas.Update()
    if oname is not None:
        canvas.SaveAs(oname)
    if not stop or ROOT.gROOT.IsBatch():
        return
    canvas.Connect("Closed()", "TApplication",
                   ROOT.gApplication, "Terminate()")
    ROOT.gApplication.Run(True)

ROOT.gROOT.SetBatch(True)

INPUT_FILENAMES = '/local/dliko/working/DJCTraining/example_data/train_files.txt'
INPUT_DIR = os.path.dirname(INPUT_FILENAMES)

INPUT_FILES = (os.path.join(INPUT_DIR, name.strip()) for name in open(INPUT_FILENAMES, 'r').readlines())

df = ROOT.RDataFrame('tree', INPUT_FILES)

for name in df.GetColumnNames():
    print ( '{} : {}'.format(name,df.GetColumnType(name)) )           
print ('\nNumber of Entries = {}'.format(df.Count().GetValue()))

evt1 = df.Range(1).AsNumpy(columns=['image','xcoords','ycoords'])

image = evt1['image'][0]
xcoords = evt1['xcoords'][0]
ycoords = evt1['ycoords'][0]

hevt = ROOT.TH2F("hevt","Event 1",32,-0.5,31.5,32,-0.5,31.5)

for i in range(1024):
    hevt.Fill(xcoords[i],ycoords[i],image[i])

with canvas(oname='plot1_1.pdf') as fig:
    hevt.Draw('surf1')
