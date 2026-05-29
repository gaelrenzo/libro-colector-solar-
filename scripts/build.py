import os
import subprocess
import argparse
import shutil
import re

def parse_args():
    parser = argparse.ArgumentParser(description="Sistema de Compilación Editorial Inteligente")
    parser.add_argument("--chapter", type=int, help="Número del capítulo a compilar (1-10) de forma individual. Si se omite, se compila todo.")
    parser.add_argument("--engine", type=str, default="pdflatex", choices=["pdflatex", "xelatex", "lualatex"], help="Motor de compilación LaTeX.")
    parser.add_argument("--clean", action="store_true", help="Limpia temporales antes de compilar.")
    return parser.parse_args()

def clean_temp_files():
    temp_dir = "../output/temp"
    if os.path.exists(temp_dir):
        for f in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, f)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error al limpiar {file_path}: {e}")
    print("Directorio de trabajo temporal limpio.")

def compile_book(chapter=None, engine="pdflatex"):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_path)
    
    main_tex = "main.tex"
    temp_dir = "output/temp"
    pdf_out_dir = "output/pdf"
    
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(pdf_out_dir, exist_ok=True)
    
    # Manejar compilación parcial a través de includeonly
    with open(main_tex, "r", encoding="utf-8") as f:
        content = f.read()
        
    if chapter is not None:
        chap_path = f"chapters/cap{chapter:02d}/main"
        include_only_line = f"\\includeonly{{{chap_path}}}"
        # Activar el includeonly en el archivo main.tex
        new_content = re.sub(r"% \\includeonly\{.*\}", include_only_line.replace("\\", "\\\\"), content)
        new_content = re.sub(r"\\includeonly\{.*\}", include_only_line.replace("\\", "\\\\"), new_content)
        print(f"Configurando compilación selectiva para el Capítulo {chapter:02d}...")
    else:
        # Desactivar includeonly
        new_content = re.sub(r"\\includeonly\{.*\}", f"% \\\\includeonly{{chapters/cap01/main}}", content)
        print("Configurando compilación de libro completo...")
        
    with open(main_tex, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    # Comando de compilación
    cmd = [
        engine,
        "-interaction=nonstopmode",
        f"-output-directory={temp_dir}",
        main_tex
    ]
    
    print(f"Ejecutando: {' '.join(cmd)}")
    
    # Primera pasada
    res1 = subprocess.run(cmd, capture_output=True, text=True)
    if res1.returncode != 0:
        print("ERROR EN COMPILACIÓN LATEX (Pasada 1):")
        print(res1.stdout[-1000:])
        return False
        
    # Compilar bibliografía si es necesario
    bib_cmd = ["bibtex", os.path.join(temp_dir, "main")]
    print(f"Ejecutando: {' '.join(bib_cmd)}")
    subprocess.run(bib_cmd, capture_output=True)
    
    # Segunda y tercera pasada para consolidar índices y referencias cruzadas
    print("Consolidando referencias e índices (Pasada 2)...")
    subprocess.run(cmd, capture_output=True)
    print("Consolidando referencias e índices (Pasada 3)...")
    subprocess.run(cmd, capture_output=True)
    
    # Mover el PDF resultante
    src_pdf = os.path.join(temp_dir, "main.pdf")
    if os.path.exists(src_pdf):
        dest_filename = f"libro_completo.pdf" if chapter is None else f"libro_capitulo_{chapter:02d}.pdf"
        dest_pdf = os.path.join(pdf_out_dir, dest_filename)
        shutil.copy(src_pdf, dest_pdf)
        print(f"[OK] Compilacion terminada con exito! PDF exportado a: {dest_pdf}")
        return True
    else:
        print("Error: No se generó el PDF de salida en el directorio temporal.")
        return False

if __name__ == "__main__":
    args = parse_args()
    if args.clean:
        clean_temp_files()
    success = compile_book(chapter=args.chapter, engine=args.engine)
    sys.exit(0 if success else 1)
