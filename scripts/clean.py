import os
import shutil

def clean():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_path)
    
    # Directorios a limpiar
    temp_dir = "output/temp"
    
    # Archivos basura en las carpetas de capítulos y raíz
    extensions = [".aux", ".log", ".toc", ".out", ".lof", ".lot", ".bbl", ".blg", ".synctex.gz", ".fdb_latexmk", ".fls"]
    
    # Limpiar temp
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)
        print(f"Limpiado el directorio: {temp_dir}")
        
    # Limpiar recursivamente archivos sueltos
    count = 0
    for root, dirs, files in os.walk(base_path):
        # Evitar limpiar carpetas del sistema
        if ".git" in root or ".github" in root:
            continue
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    path = os.path.join(root, file)
                    os.remove(path)
                    count += 1
                    
    print(f"Limpieza profunda completada. Se eliminaron {count} archivos temporales auxiliares.")

if __name__ == "__main__":
    clean()
