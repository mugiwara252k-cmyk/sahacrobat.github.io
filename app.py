from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from PyPDF2 import PdfMerger
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def create_pdf(title, content, filename=None):
    if not filename:
        filename = f"{title.replace(' ', '_')}.pdf"
    
    p = canvas.Canvas(filename, pagesize=letter)
    
    # Green theme colors
    dark_green = Color(0.1, 0.4, 0.1)
    light_green = Color(0.9, 0.95, 0.9)
    
    # Background
    p.setFillColor(light_green)
    p.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
    
    # Add title
    p.setFillColor(dark_green)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, title)
    
    # Add content
    p.setFillColor(Color(0.2, 0.5, 0.2))
    p.setFont("Helvetica", 12)
    y = 700
    for line in content.split('\n'):
        p.drawString(100, y, line)
        y -= 20
        if y < 50:  # Start new page if needed
            p.showPage()
            p.setFillColor(light_green)
            p.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
            p.setFillColor(Color(0.2, 0.5, 0.2))
            p.setFont("Helvetica", 12)
            y = 750
    
    p.save()
    print(f"PDF created: {filename}")
    return filename

def merge_pdfs_gui():
    root = tk.Tk()
    root.title("SAH ACROBAT - PDF Merger")
    root.geometry("600x500")
    
    pdf_list = []
    
    def add_pdfs():
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        for file in files:
            if file not in pdf_list:
                pdf_list.append(file)
        update_listbox()
    
    def remove_selected():
        selected = listbox.curselection()
        for i in reversed(selected):
            del pdf_list[i]
        update_listbox()
    
    def clear_all():
        pdf_list.clear()
        update_listbox()
    
    def move_up():
        selected = listbox.curselection()
        if selected and selected[0] > 0:
            i = selected[0]
            pdf_list[i], pdf_list[i-1] = pdf_list[i-1], pdf_list[i]
            update_listbox()
            listbox.selection_set(i-1)
    
    def move_down():
        selected = listbox.curselection()
        if selected and selected[0] < len(pdf_list) - 1:
            i = selected[0]
            pdf_list[i], pdf_list[i+1] = pdf_list[i+1], pdf_list[i]
            update_listbox()
            listbox.selection_set(i+1)
    
    def update_listbox():
        listbox.delete(0, tk.END)
        for pdf in pdf_list:
            listbox.insert(tk.END, os.path.basename(pdf))
    
    def merge_pdfs():
        if len(pdf_list) < 2:
            messagebox.showwarning("Warning", "Select at least 2 PDFs to merge")
            return
        
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_file:
            merger = PdfMerger()
            for pdf in pdf_list:
                merger.append(pdf)
            merger.write(output_file)
            merger.close()
            messagebox.showinfo("Success", f"PDFs merged to {os.path.basename(output_file)}")
    
    # GUI Layout
    tk.Label(root, text="SAH ACROBAT - PDF Merger", font=("Arial", 16)).pack(pady=10)
    
    frame1 = tk.Frame(root)
    frame1.pack(pady=10)
    
    tk.Button(frame1, text="Add PDFs", command=add_pdfs).pack(side=tk.LEFT, padx=5)
    tk.Button(frame1, text="Remove Selected", command=remove_selected).pack(side=tk.LEFT, padx=5)
    tk.Button(frame1, text="Clear All", command=clear_all).pack(side=tk.LEFT, padx=5)
    
    listbox = tk.Listbox(root, height=15, width=70)
    listbox.pack(pady=10)
    
    frame2 = tk.Frame(root)
    frame2.pack(pady=10)
    
    tk.Button(frame2, text="Move Up", command=move_up).pack(side=tk.LEFT, padx=5)
    tk.Button(frame2, text="Move Down", command=move_down).pack(side=tk.LEFT, padx=5)
    tk.Button(frame2, text="Merge PDFs", command=merge_pdfs, bg="green", fg="white").pack(side=tk.LEFT, padx=10)
    
    root.mainloop()

if __name__ == '__main__':
    while True:
        print("\nSAH ACROBAT")
        print("-" * 20)
        print("1. Create PDF")
        print("2. Merge PDFs")
        print("3. Clear all PDFs")
        print("4. Exit")
        
        choice = input("Choose option (1-4): ")
        
        if choice == '1':
            title = input("Enter title: ")
            print("Enter content (press Enter twice to finish):")
            
            content_lines = []
            while True:
                line = input()
                if line == "" and content_lines and content_lines[-1] == "":
                    break
                content_lines.append(line)
            
            content = '\n'.join(content_lines[:-1])
            filename = create_pdf(title, content)
            
            if os.name == 'nt':
                os.startfile(filename)
            else:
                os.system(f'open "{filename}"')
                
        elif choice == '2':
            merge_pdfs_gui()
            
        elif choice == '3':
            pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
            if pdf_files:
                for pdf in pdf_files:
                    os.remove(pdf)
                print(f"Cleared {len(pdf_files)} PDF files")
            else:
                print("No PDF files to clear")
                
        elif choice == '4':
            break
        else:
            print("Invalid option")