# 📚 Diseño Termo-Fluidodinámico de Colectores Solares de Aire con Serpentín
### *Sistema Editorial Técnico, Modular y Automatizado en LaTeX*

[![Build LaTeX Document](https://github.com/gaelrenzo/libro-colector-solar/actions/workflows/build.yml/badge.svg)](https://github.com/gaelrenzo/libro-colector-solar/actions/workflows/build.yml)
[![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=flat&logo=latex&logoColor=white)](http://www.latex-project.org/)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este repositorio contiene el sistema editorial técnico y modular profesional para el desarrollo colaborativo, control de versiones e integración continua de la obra de investigación:

> **"Diseño Termo-Fluidodinámico de Colectores Solares de Aire con Serpentín: Análisis Computacional CFD y Comparación CAD/CAE"**

---

## 🏗️ Filosofía de la Arquitectura Editorial

A diferencia de los proyectos de LaTeX tradicionales que acumulan miles de líneas en un único archivo inmanejable, este libro implementa una **arquitectura modular de grado editorial**:

1. **Responsabilidad Única por Módulo**: Las configuraciones de diseño (`config/`), las páginas preliminares (`frontmatter/`), los anexos (`appendices/`) y cada uno de los 10 capítulos están aislados físicamente.
2. **Regla de Oro: "One Sentence per Line"**: Cada oración del texto está escrita en una línea independiente de LaTeX. Esto optimiza radicalmente el historial de Git, permitiendo ver aportaciones y corregir erratas exactas sin tocar el resto del párrafo y evitando conflictos de fusión al fusionar ramas de otros compañeros.
3. **Compilación Selectiva e Inteligente**: A través de scripts de Python, los miembros del equipo pueden compilar un único capítulo en el que estén trabajando de manera instantánea, sin tener que esperar la renderización de todo el libro de cientos de páginas.

---

## 📂 Mapa de la Estructura de Directorios

```text
libro-profesional/
├── main.tex                            # Orquestador del libro completo
├── config/                             # Núcleo de diseño y estilos LaTeX
│   ├── packages.tex                    # Paquetes estructurados por categorías
│   ├── commands.tex                    # Macros termodinámicas (Nu, Re, Cp) y cajas tcolorbox
│   ├── format.tex                      # Paleta de colores HSL, cabeceras fancyhdr y geometría
│   └── metadata.tex                    # Título, autor y fecha global
├── frontmatter/                        # Páginas preliminares estilizadas (portada minimalista, dedicatoria)
├── chapters/                           # Capítulos del libro (10 módulos individuales)
│   ├── cap01/ (Introducción)
│   ├── cap02/ (Fundamentos)
│   ├── cap03/ (Estado del Arte)
│   ├── cap04/ (Metodología General)
│   ├── cap05/ (Diseño Geométrico)
│   ├── cap06/ (Modelado Térmico)
│   ├── cap07/ (Simulación CFD)
│   ├── cap08/ (Comparación de Software CAD/CAE - CATIA, SOLIDWORKS, Inventor, Solid Edge)
│   ├── cap09/ (Resultados y Discusión)
│   └── cap10/ (Conclusiones y Recomendaciones)
├── appendices/                         # Anexos técnicos (A a F)
├── bibliography/                       # Referencias globales en formato BibTeX
├── scripts/                            # Herramientas de automatización en Python (build, clean, export)
├── output/                             # PDFs finales exportados y registros de compilación
└── .github/workflows/                  # CI/CD: Compilación en la nube ante cada push
```

---

## 👥 Guía Técnica de Colaboración (Para el Equipo)

Para mantener la integridad del repositorio y trabajar de manera coordinada con tus compañeros, se establece el siguiente flujo de trabajo:

### 1. Requisitos Previos
Cada miembro del equipo debe contar con:
- **LaTeX**: [MiKTeX](https://miktex.org/) (Windows) o TeX Live (Mac/Linux).
- **Python 3.x** (para los scripts de automatización).
- **Git** (y opcionalmente [GitHub Desktop](https://desktop.github.com/) para una gestión visual cómoda).
- **Editor**: VS Code con la extensión **LaTeX Workshop**.

### 2. Primeros Pasos: Descarga y Preparación
Clona el repositorio en tu computadora local:
```bash
git clone https://github.com/gaelrenzo/libro-colector-solar.git
cd libro-colector-solar
```

### 3. Flujo de Trabajo Seguro (Control de Versiones)
**NUNCA** realices commits directos sobre la rama `main`. Sigue siempre este flujo:
```bash
# 1. Asegúrate de tener la última versión estable
git checkout main
git pull

# 2. Crea una rama de trabajo para tu sección o capítulo asignado
git checkout -b capitulo-05-absorbedor

# 3. Trabaja en tus archivos .tex locales (escribe una frase por línea)
# ... realiza tus ediciones ...

# 4. Verifica tus aportes compilando tu capítulo de forma local
python scripts/build.py --chapter 5

# 5. Guarda tus avances en tu rama local
git add .
git commit -m "Añade modelo matemático del absorbedor y dimensiones base"

# 6. Sube tus cambios a GitHub
git push -u origin capitulo-05-absorbedor
```
Una vez subida la rama, abre un **Pull Request (PR)** en GitHub para que el equipo pueda ver tus cambios y fusionarlos a `main` tras la aprobación de la integración continua.

---

## 💻 Panel de Comandos de Automatización

En la raíz del proyecto, puedes ejecutar estos comandos en consola para simplificar el flujo editorial:

| Comando | Acción | Descripción |
| :--- | :--- | :--- |
| `python scripts/build.py` | **Compilar el libro completo** | Compila todo el documento, consolida el índice analítico, lista de figuras, de tablas y bibliografía global. Genera `output/pdf/libro_completo.pdf`. |
| `python scripts/build.py --chapter X` | **Compilación parcial selectiva** | Compila en segundos **únicamente el Capítulo X** (ej. `--chapter 5`). Mantiene la numeración real y genera `output/pdf/libro_capitulo_05.pdf`. |
| `python scripts/clean.py` | **Limpieza profunda** | Elimina recursivamente todas las extensiones auxiliares y molestas de LaTeX (`.aux`, `.log`, `.toc`, etc.) para dejar tu carpeta limpia. |
| `python scripts/export.py` | **Exportación histórica** | Copia el PDF completo y lo renombra con la fecha y hora exacta en `output/pdf/` para guardar un control de versiones de entregas. |

---

## 🚀 Integración Continua (DevOps)

El proyecto cuenta con **GitHub Actions** preconfigurado:
* **Compilación en la Nube (`build.yml`)**: Cada vez que se crea un Pull Request o se hace un push a la rama `main`, un contenedor Linux con LaTeX compila el documento completo para confirmar que compila al 100% y sin errores de sintaxis o referencias rotas.
* **Publicación de Versiones (`release.yml`)**: Al etiquetar un commit estable (ej. `v1.0`), GitHub generará de forma automática una entrega (Release) adjuntando el PDF final del libro listo para su descarga y distribución.
