from PyPDF3 import PdfFileMerger
import os 

merger = PdfFileMerger()
for items in os.listdir():
  if items.endswith('.pdf'):
    merger.append(items)    
merger.write("Merged.pdf")
merger = PdfFileMerger()
merger.close()
