import PyPDF2
import sys

pdfObj=open("./Documents/management-center-admin-72.pdf","rb")
newFile = open("./Documents/management-center-admin-72-marked.pdf", 'wb')

pdfReader = PyPDF2.PdfFileReader(pdfObj)
pdfWriter = PyPDF2.PdfFileWriter()



print(pdfReader.numPages)

for page in range(pdfReader.numPages):
  
        # creating rotated page object
        pageObj = pdfReader.getPage(page)
        # adding rotated page object to pdf writer
        pdfWriter.addPage(pageObj)

newFile = open("./Documents/management-center-admin-72-marked.pdf", 'wb')
    
# writing rotated pages to new file
pdfWriter.write(newFile)


pdfObj.close()
newFile.close()