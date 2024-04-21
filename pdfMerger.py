import PyPDF2

pdfiles = ["Deepakshi's CV.pdf", "Deepakshi (SE) Resume.pdf"]
merger = PyPDF2.PdfMerger()

for fileName in pdfiles:
    pdfFile = open(fileName, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
    pdfFile.close()

merger.write("mergedResume.pdf")

