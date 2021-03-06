# example: python duplicate.py document1.pdf 0 50 40

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys, os

mmFactor = 72 / 25.4 # approx 2.8346

infilename = sys.argv[1]    # relaive or absolute path to pdf file to process
inithshift = float(sys.argv[2]) * mmFactor  # leftmost image left margin
hshift = float(sys.argv[3]) * mmFactor  # horizontal offset added to each image
vshift = float(sys.argv[4]) * mmFactor  # vertical margin from bottom

print "infilename: %s, hshift: %f, vshift: %f" % (infilename, hshift, vshift)

output = PdfFileWriter()
input1 = PdfFileReader(open(infilename, "rb"))
input2 = PdfFileReader(open(infilename, "rb"))

destPage = input1.getPage(0)
srcPage = input2.getPage(0)
width = input1.getPage(0).mediaBox[2]
height = input1.getPage(0).mediaBox[3]
yShift = -height + vshift

destPage.addTransformation([1, 0, 0, 1, inithshift, yShift])
i = 1
while True:
    h = i * hshift + inithshift
    if h > width:
        break
    destPage.mergeTranslatedPage(srcPage,  h, yShift);
    i += 1

output.addPage(destPage)

outputStream = file(os.path.splitext(infilename)[0] + "-duplicated.pdf", "wb")
output.write(outputStream)
