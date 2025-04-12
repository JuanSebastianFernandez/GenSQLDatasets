# SQLDataGen

SQLDataGen es un generador de datos aleatorios en Python 3.13 diseñado para crear datasets para ejercicios SQL utilizando la instrucción `INSERT ALL`. El proyecto genera datos realistas para dos escenarios distintos:

1. **Manager de Cursos**: Incluye datos sobre cursos, profesores y estudiantes.
2. **Manager de Cruceros**: Incluye datos sobre cruceros, compañías, países, categorías, puertos de salida, destinos, usuarios y estados.

Los datos generados se exportan como scripts SQL en archivos `.txt` listos para ser utilizados en bases de datos SQL.

---
# Estructura del Proyecto

El repositorio está organizado en las siguientes carpetas y archivos:
```bash
📦 SQLDataGen/
├── 📂 Data/
│     ├── 📜 courses_data.py       # Listas de datos para cursos, profesores y estudiantes
│     └── 📜 cruceros_data.py      # Listas de datos para cruceros, compañías, países, categorías, puertos, destinos, usuarios y estados
├── 📂 data_generated/
│     └── 📜 *.txt                 # Archivos generados con sentencias INSERT ALL para SQL
├── 📜 courses.py                # Script para generar datos SQL para el manager de cursos
├── 📜 cruceros.py               # Script para generar datos SQL para el manager de cruceros
├── 📜 functions.py              # Funciones compartidas para la generación de datos SQL
└── README.md                 # Documentación del proyecto
```

- **Data/**: Contiene los archivos con las listas de datos base.
  - `courses_data.py`: Datos estáticos para cursos, profesores y estudiantes.
  - `cruceros_data.py`: Datos estáticos para cruceros, compañías, países, categorías, puertos de salida, destinos, usuarios y estados.
- **data_generated/**: Almacena los archivos `.txt` con las sentencias `INSERT ALL` generadas.
- **Raíz**:
  - `functions.py`: Módulo con las funciones principales para generar datos aleatorios y formatear las sentencias SQL.
  - `courses.py`: Script que utiliza `functions.py` y `courses_data.py` para generar datos SQL para el escenario de cursos.
  - `cruceros.py`: Script que utiliza `functions.py` y `cruceros_data.py` para generar datos SQL para el escenario de cruceros.
 
---

# Requisitos

- Python 3.13 o superior.
- No se requieren dependencias externas.
---

# Instalación

1. Clona el repositorio:
   ```bash
   git clone git@github.com:tu_usuario/SQLDataGen.git
   cd SQLDataGen
   ```
2. Asegúrate de tener Python 3.13 instalado:
```bash
python --version
```
---

# Uso
## 1. Generar datos para el Manager de Cursos:
Ejecuta el script courses.py:
```bash
python courses.py
```
Esto generará un archivo .txt con sentencias INSERT ALL en la carpeta data_generated/, listo para usar en tu base de datos SQL.

## 2. Generar datos para el Manager de Cruceros:
Ejecuta el script cruceros.py:
```bash
python cruceros.py
```
Esto generará un archivo .txt con sentencias INSERT ALL en la carpeta data_generated/.

## 3. Uso de los archivos generados:
* Los archivos .txt en data_generated/ contienen sentencias SQL compatibles con la instrucción INSERT ALL. Puedes copiar y pegar estas sentencias en tu motor de base de datos SQL (por ejemplo, Oracle, que soporta INSERT ALL) o importarlas directamente.
---
# Ejemplo de Salida
Un archivo generado en data_generated/ podría verse así:
```sql
INSERT ALL
    INTO CRUCEROS (NOMBRE, COMPANIA, PAIS_REGISTRO, CAPACIDAD, ANO_CONSTRUCCION, CATEGORIA) VALUES ('Atlantic Star', 'Titanium Oceanic', 'Qatar', 2350, 2007, 'Lujo')
    INTO CRUCEROS (NOMBRE, COMPANIA, PAIS_REGISTRO, CAPACIDAD, ANO_CONSTRUCCION, CATEGORIA) VALUES ('Aurora Seas', 'Emerald Ocean Tours', 'República Dominicana', 2650, 2021, 'Económico')
    INTO CRUCEROS (NOMBRE, COMPANIA, PAIS_REGISTRO, CAPACIDAD, ANO_CONSTRUCCION, CATEGORIA) VALUES ('Blue Horizon', 'Caribbean Cruise', 'Dinamarca', 2100, 2007, 'Económico')
    INTO CRUCEROS (NOMBRE, COMPANIA, PAIS_REGISTRO, CAPACIDAD, ANO_CONSTRUCCION, CATEGORIA) VALUES ('Blue Lagoon', 'Galactic Oceanic', 'Alemania', 1950, 2011, 'Premium')
SELECT * FROM DUAL;
```
---
# Personalización

**Modificar datos base:** Edita los archivos en la carpeta Data/ (courses_data.py o cruceros_data.py) para ajustar las listas de nombres, categorías u otros valores según tus necesidades.
**Ajustar la lógica de generación:** Modifica functions.py para cambiar el formato de las sentencias SQL o la cantidad de datos generados.
**Ampliar escenarios:** Crea nuevos scripts en la raíz siguiendo la estructura de courses.py o cruceros.py para generar datos para otros casos.

---
# Contribuciones
¡Las contribuciones son bienvenidas! Si quieres mejorar el generador, añadir nuevos escenarios o corregir errores:

1. Haz un fork del repositorio.
2. Crea una rama para tus cambios (git checkout -b feature/nueva-funcionalidad).
3. Commitea tus cambios (git commit -m "Descripción de los cambios").
4. Haz push a tu rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request en GitHub.
---

# Licencia
Este proyecto no está bajo ninguna licencia . Siéntete libre de usarlo y modificarlo según tus necesidades.

---
# Contacto
Si tienes preguntas o sugerencias, abre un issue en el repositorio o contactame en GitHub.
   
