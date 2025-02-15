# import streamlit as st
# import os
# from pathlib import Path

# def get_pdf_files():
#     """Get list of PDF files from the allpdfs directory."""
#     pdf_dir = Path("allpdfs")
#     if not pdf_dir.exists():
#         st.error("The 'allpdfs' directory doesn't exist. Please create it and add your PDF files.")
#         return []
    
#     pdf_files = list(pdf_dir.glob("*.pdf"))
#     return [pdf.name for pdf in pdf_files]

# def display_pdf(pdf_file):
#     """Display the selected PDF file using Streamlit's native PDF display."""
#     try:
#         with open(os.path.join("allpdfs", pdf_file), "rb") as f:
#             pdf_bytes = f.read()
#         st.download_button(
#             label="Download PDF",
#             data=pdf_bytes,
#             file_name=pdf_file,
#             mime="application/pdf"
#         )
#         st.write("PDF Preview:")
#         st.pdf(pdf_bytes)
#     except Exception as e:
#         st.error(f"Error displaying PDF: {str(e)}")

# def main():
#     st.title("PDF Viewer App")
    
#     # Add some basic styling
#     st.markdown("""
#         <style>
#         .stApp {
#             max-width: 1200px;
#             margin: 0 auto;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     # Get list of PDF files
#     pdf_files = get_pdf_files()
    
#     if not pdf_files:
#         st.warning("No PDF files found in the 'allpdfs' directory.")
#         st.info("Please add your PDF files to the 'allpdfs' directory.")
#         return
    
#     # Create a dropdown to select PDF file
#     selected_pdf = st.selectbox(
#         "Select a PDF to view",
#         pdf_files,
#         index=0 if pdf_files else None
#     )
    
#     if selected_pdf:
#         st.write(f"Displaying: {selected_pdf}")
#         display_pdf(selected_pdf)

# if __name__ == "__main__":
#     main()


import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer

# Set the directory containing PDFs
PDF_FOLDER = "allpdfs"

# Get the list of PDF files
pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]

st.title("PDF Viewer App")

if not pdf_files:
    st.warning("No PDF files found in the 'allpdfs' folder.")
else:
    # Dropdown to select a PDF file
    selected_pdf = st.selectbox("Select a PDF", pdf_files)

    # Full path to the selected PDF
    pdf_path = os.path.join(PDF_FOLDER, selected_pdf)

    # Display the PDF
    pdf_viewer(pdf_path)
