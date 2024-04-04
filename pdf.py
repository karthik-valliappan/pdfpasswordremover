import os
import tkinter as tk
from tkinter import filedialog
import PyPDF2

def remove_password_from_pdf(filename, password=None):
    pdf = PyPDF2.PdfFileReader(filename)
    if pdf.isEncrypted:
        pdf.decrypt(password)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(pdf.getNumPages()):
            pdf_writer.addPage(pdf.getPage(page_num))
        output_filename = "pdf_file_with_no_password.pdf"
        with open(output_filename, "wb") as output_file:
            pdf_writer.write(output_file)
        return output_filename
    else:
        print("The PDF is not password-protected.")
        return None

def handle_upload():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        password_label.config(state="normal")
        password_entry.config(state="normal")
        convert_button.config(state="normal")
        global input_pdf
        input_pdf = file_path

def handle_convert():
    password = password_entry.get()
    output_pdf = remove_password_from_pdf(input_pdf, password)
    if output_pdf:
        status_label.config(text=f"Password removed. Modified PDF saved as {output_pdf}")

# Create the main window
root = tk.Tk()
root.title("PDF Password Remover")

# Create widgets
upload_button = tk.Button(root, text="Upload Password-Protected PDF", command=handle_upload)
password_label = tk.Label(root, text="Enter PDF password:", state="disabled")
password_entry = tk.Entry(root, show="*", state="disabled")
convert_button = tk.Button(root, text="Convert PDF", command=handle_convert, state="disabled")
status_label = tk.Label(root, text="")

# Arrange widgets using grid layout
upload_button.grid(row=0, column=0, padx=10, pady=10)
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry.grid(row=1, column=1, padx=10, pady=5)
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
