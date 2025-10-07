# SAH ACROBAT

A Python-based PDF creation and merging tool with a green theme and intuitive interface.

## Features

- **Create PDFs**: Generate PDFs with custom titles and content
- **Merge PDFs**: Combine multiple PDFs with drag-and-drop ordering
- **Green Theme**: Professional green color scheme for all PDFs
- **Clear All**: Remove all PDF files from directory
- **Auto-open**: Generated PDFs open automatically

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

## Usage

### Main Menu Options:
1. **Create PDF** - Generate new PDF with title and content
2. **Merge PDFs** - Open GUI to combine multiple PDFs
3. **Clear all PDFs** - Delete all PDF files in current directory
4. **Exit** - Close application

### PDF Merger Features:
- **Add PDFs** - Select multiple PDF files
- **Remove Selected** - Remove PDFs from merge list
- **Clear All** - Clear entire merge list
- **Move Up/Down** - Reorder PDFs before merging
- **Merge PDFs** - Combine all PDFs in specified order

## Requirements

- Python 3.6+
- reportlab==4.0.4
- PyPDF2==3.0.1
- tkinter (included with Python)

## File Structure

```
ggs/
├── app.py              # Main application
├── requirements.txt    # Dependencies
└── README.md          # This file
```