from PyPDF2 import PdfFileMerger, PdfFileReader
 
# Call the PdfFileMerger
mergedObject = PdfFileMerger()
 
#Name all files that to be marged as 1.pdf, 2.pdf and so on
for fileNumber in range(1,9):#The upper range will be (the number of pdf + 1)
    mergedObject.append(PdfFileReader(str(fileNumber)+ '.pdf', 'rb'))
 
# Write all the files into a file which is named as shown below
mergedObject.write("Marged_PDF.pdf")
