import pyttsx3
import pdfplumber
import PyPDF2
from tkinter import *
from tkinter import filedialog


def read_pdf():
    selected_pdf = filedialog.askopenfilename()  # Click to upload
    pdf_obj = open(selected_pdf, 'rb')  # Create PDF file object
    pdf_reader = PyPDF2.PdfFileReader(pdf_obj)  # Create a PDF File reader object
    pages = pdf_reader.numPages  # Get the number of pages
    print(pages)
    with pdfplumber.open(selected_pdf) as pdf:
        # Loop through pages
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            print(text)
            speaker = pyttsx3.init()
            speaker.say(text)
            speaker.runAndWait()


window = Tk()
btn = Button(window, text="Select pdf", command=read_pdf)
btn.pack(side="bottom", fill="both", expand="yes", padx="50", pady="50")
window.mainloop()