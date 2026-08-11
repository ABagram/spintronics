from markdown_pdf import MarkdownPdf, Section

# Initialize the PDF generator
pdf = MarkdownPdf(toc_level=2)

# Define your Markdown content and add it as a section
md_content = """
# My Document Title
This is a paragraph converted directly from **Markdown** to **PDF**.

## Features
* No external binaries required
* Built-in table of contents support
* Custom CSS styling support
"""

pdf.add_section(Section(md_content))

# Save the final PDF
pdf.save("output.pdf")
