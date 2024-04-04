import PyPDF2
import os

directory = input("directory: ")

merger = PyPDF2.PdfMerger()

for file in os.listdir(directory):
  if file.endswith(".pdf"):
    file_path = os.path.join(directory, file)
    merger.append(file_path)
  
output = os.path.join(directory, "combined.pdf")
merger.write(output)
merger.close()

for file in os.listdir(directory):
  if file.endswith(".pdf") and file != "combined.pdf":
    file_path = os.path.join(directory, file)
    os.remove(file_path)