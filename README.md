# 📚 Sistema Editorial Técnico Modular - Colector Solar de Aire

Este repositorio alberga la estructura editorial modular profesional para el desarrollo colaborativo del libro técnico:

**"Diseño Termo-Fluidodinámico de Colectores Solares de Aire con Serpentín: Análisis Computacional CFD y Comparación CAD/CAE"**

---

## 🏗️ Filosofía de Arquitectura Modular

El proyecto está diseñado bajo estándares editoriales de ingeniería modernos:
1. **Un Archivo = Una Responsabilidad**: La configuración está separada de los contenidos. Cada capítulo tiene su propio orquestador (`main.tex`) y carpeta `sections/` donde cada tema es un archivo aislado.
2. **Regla "One Sentence per Line"**: Cada oración del texto está escrita en una línea independiente de LaTeX. Esto optimiza radicalmente el historial de Git, permitiendo ver aportaciones y corregir erratas exactas sin tocar el resto del párrafo y evitando conflictos de fusión al fusionar ramas de otros compañeros.
3. **Compilación Parcial**: Los scripts de Python permiten compilar únicamente un capítulo en el que estés trabajando para evitar demoras innecesarias al re-compilar un libro masivo.

---

## 👥 Guía de Colaboración para el Equipo de Trabajo

Esta sección detalla los pasos exactos para trabajar en conjunto con tus compañeros sin romper el proyecto.

### 1. Preparación del Entorno
Cada miembro del equipo debe instalar:
- **Distribución LaTeX**: [MiKTeX](https://miktex.org/) (Windows) o TeX Live (Mac/Linux).
- **Python 3.x** (para los scripts de automatización).
- **Git** (y opcionalmente [GitHub Desktop](https://desktop.github.com/) para gestión visual).
- **VS Code** con la extensión **LaTeX Workshop** instalada.

### 2. Clonación y Conexión al Repositorio
Para descargar el proyecto a tu ordenador local, abre una terminal (PowerShell o Git Bash) y ejecuta:
```bash
git clone <URL_DE_TU_REPOSITORIO_GITHUB>
cd libro-profesional
```

### 3. Crear una Rama de Trabajo (Feature Branch)
**NUNCA** trabajes directamente sobre la rama `main`. Cada miembro del equipo debe crear su propia rama de trabajo para sus capítulos o secciones asignadas:
```bash
# Asegurarse de tener los últimos cambios
git checkout main
git pull

# Crear una nueva rama para tu trabajo
git checkout -b capitulo-02-fundamentos
```

### 4. Compilar Aisladamente para Acelerar el Flujo
Si solo estás trabajando en el Capítulo 2, no necesitas compilar todo el libro. Puedes compilar únicamente tu capítulo con el script de automatización en Python:
```bash
python scripts/build.py --chapter 2
```
Esto modificará el orquestador principal temporalmente, compilará únicamente el Capítulo 2 y colocará el PDF resultante en `output/pdf/libro_capitulo_02.pdf`.

Si deseas compilar el **libro completo**:
```bash
python scripts/build.py
```
Y se generará el archivo final `output/pdf/libro_completo.pdf` con todos los capítulos e índices consolidados.

### 5. Sincronización e Integración Continua (GitHub Actions)
Cuando termines de redactar tus oraciones:
1. Haz commit de tus cambios locales:
   ```bash
   git add .
   git commit -m "Añade secciones 2.1 y 2.2 de fundamentos térmicos"
   ```
2. Sube la rama a GitHub:
   ```bash
   git push -u origin capitulo-02-fundamentos
   ```
3. Ve a GitHub y abre un **Pull Request (PR)** hacia la rama `main`.
4. El servidor de integración continua **GitHub Actions** compilará automáticamente el libro en la nube. Si no hay errores de sintaxis o referencias rotas, la compilación de la nube saldrá en verde y tus compañeros podrán revisar e integrar tu trabajo con seguridad.

### 6. Limpieza de Temporales
Para eliminar los molestos archivos intermedios de LaTeX que genera la compilación local, ejecuta en cualquier momento:
```bash
python scripts/clean.py
```
Esto dejará la raíz del proyecto limpia y libre de ruido.

---

## 🛠️ Estructura del Directorio
- `config/`: Archivos de configuración modular (`packages.tex`, `commands.tex`, `format.tex`, `metadata.tex`).
- `frontmatter/`: Páginas preliminares (portada, dedicatoria, agradecimientos, prefacio).
- `chapters/`: Contenidos técnicos separados por capítulos (Capítulo 1 al 10).
- `appendices/`: Anexos adicionales (Tablas, parámetros y planos).
- `bibliography/`: Base de datos de citas bibliográficas en formato BibTeX.
- `scripts/`: Scripts en Python para compilación y mantenimiento.
- `output/`: Directorio donde se exportan los PDFs construidos.
