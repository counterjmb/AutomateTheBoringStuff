#python -m pip install PyPDF2
import PyPDF2

pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfReader(pdfFile)
print(len(reader.pages))
#indexes for this module start at 0
page = reader.pages[0]
print(page.extract_text())

#combine meetinnotes1 and 2: 
pdf1File = pdfFile
pdf2File = open('meetingminutes2.pdf', 'rb')
reader2 = PyPDF2.PdfReader(pdf2File)
writer = PyPDF2.PdfWriter()
#add meeting 1
for pageNum in range(len(reader.pages)):
    page = reader.pages[pageNum]
    writer.add_page(page)

#add meeting 2
for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

outputFile = open('combined_minutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdfFile.close()
pdf1File.close()
pdf2File.close()