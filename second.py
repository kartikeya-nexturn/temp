import streamlit as st
import os
from pathlib import Path
import base64

def get_pdf_files():
    """Get list of PDF files from the allpdfs directory."""
    pdf_dir = Path("allpdfs")
    if not pdf_dir.exists():
        st.error("The 'allpdfs' directory doesn't exist. Please create it and add your PDF files.")
        return []
    
    pdf_files = list(pdf_dir.glob("*.pdf"))
    return [pdf.name for pdf in pdf_files]

def display_pdf(pdf_file):
    """Display the selected PDF file."""
    try:
        with open(os.path.join("allpdfs", pdf_file), "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        
        # Embed PDF viewer
        pdf_display = f"""
            <iframe
                src="data:application/pdf;base64,{base64_pdf}"
                width="100%"
                height="800"
                type="application/pdf">
            </iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error displaying PDF: {str(e)}")

def main():
    st.title("PDF Viewer App")
    
    # Add some basic styling
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Get list of PDF files
    pdf_files = get_pdf_files()
    
    if not pdf_files:
        st.warning("No PDF files found in the 'allpdfs' directory.")
        st.info("Please add your PDF files to the 'allpdfs' directory.")
        return
    
    # Create a dropdown to select PDF file
    selected_pdf = st.selectbox(
        "Select a PDF to view",
        pdf_files,
        index=0 if pdf_files else None
    )
    
    if selected_pdf:
        st.write(f"Displaying: {selected_pdf}")
        display_pdf(selected_pdf)

if __name__ == "__main__":
    main()