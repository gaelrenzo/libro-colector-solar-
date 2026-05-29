import os
import shutil
from datetime import datetime

def export():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_path)
    
    pdf_dir = "output/pdf"
    book_pdf = os.path.join(pdf_dir, "libro_completo.pdf")
    
    if not os.path.exists(book_pdf):
        print("Error: No existe el archivo 'output/pdf/libro_completo.pdf'. Por favor compila el libro completo primero.")
        return
        
    # Crear nombre con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_name = f"libro_colector_solar_v1.0_{timestamp}.pdf"
    export_path = os.path.join(pdf_dir, export_name)
    
    shutil.copy(book_pdf, export_path)
    print(f"✅ Versión exportada con éxito como: {export_path}")

if __name__ == "__main__":
    export()
