import fitz  # PyMuPDF
import os
import datetime

def print_file_modification_date(file_path):
    try:
        mod_time = os.path.getmtime(file_path)
        mod_datetime = datetime.datetime.fromtimestamp(mod_time)
        print(f"Last modified at {mod_datetime}: '{file_path}'")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

def combine_pdf_figures(pdf_paths, output_pdf, labels, cols_per_row, row_gap=2):
    for pdf_path in pdf_paths:
        print_file_modification_date(pdf_path)
    doc = fitz.open()  # Create a new PDF

    # Dictionaries to hold row-wise information
    row_pdfs = {}  # {row_index: [pdf_paths]}
    row_widths = {}  # {row_index: total_width}
    row_heights = {}  # {row_index: max_height}

    # Organize PDFs into rows and calculate dimensions for each row
    current_index = 0
    for row_index, num_cols in enumerate(cols_per_row):
        row_pdfs[row_index] = []
        row_widths[row_index] = 0
        row_heights[row_index] = 0

        for _ in range(num_cols):
            if current_index >= len(pdf_paths):
                break
            pdf_path = pdf_paths[current_index]
            row_pdfs[row_index].append(pdf_path)
            with fitz.open(pdf_path) as src_doc:
                src_page = src_doc[0]
                row_widths[row_index] += src_page.rect.width
                row_heights[row_index] = max(row_heights[row_index], src_page.rect.height) + row_gap
            current_index += 1

    # Calculate overall page dimensions
    page_width = max(row_widths.values())
    page_height = sum(row_heights.values())

    # Create a new page in the output document
    page = doc.new_page(width=page_width, height=page_height)

    # Place each PDF figure on the combined page
    current_y = 0
    label_idx = 0
    for row_index in row_pdfs:
        current_x = 0
        for pdf_index, pdf_path in enumerate(row_pdfs[row_index]):
            with fitz.open(pdf_path) as src_doc:
                src_page = src_doc[0]
                rect = fitz.Rect(current_x, current_y, current_x + src_page.rect.width, current_y + src_page.rect.height)
                page.show_pdf_page(rect, src_doc, 0)

                # Add label
                label_x, label_y = current_x + 5, current_y + 15  # Adjust label position
                page.insert_text((label_x, label_y), labels[label_idx], fontsize=10, fontname="Helvetica-Bold")

                # Update current_x for the next figure in the row
                current_x += src_page.rect.width
            label_idx += 1
        # Update current_y for the next row
        current_y += row_heights[row_index] + row_gap

    # Save the combined PDF
    doc.save(output_pdf)
    doc.close()
