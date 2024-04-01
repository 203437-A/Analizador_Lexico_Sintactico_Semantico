from analizador_lexico import tokens
from analizador_sintactico import parser
import io
import sys

class TablaDeSimbolos:
    def __init__(self):
        self.simbolos = {}

    def agregar(self, nombre, tipo):
        self.simbolos[nombre] = tipo

    def obtener(self, nombre):
        return self.simbolos.get(nombre)

class IfStatement:
    def __init__(self, condicion, contenido):
        self.condicion = condicion
        self.contenido = contenido

class ForLoop:
    def __init__(self, variable, rango, contenido):
        self.variable = variable
        self.rango = rango
        self.contenido = contenido

class FunctionDefinition:
    def __init__(self, nombre, parametros, contenido):
        self.nombre = nombre
        self.parametros = parametros
        self.contenido = contenido

def analisis_semantico(arbol_sintactico, tabla_simbolos=None):
    if tabla_simbolos is None:
        tabla_simbolos = TablaDeSimbolos()

    if isinstance(arbol_sintactico, IfStatement):
        condicion = arbol_sintactico.condicion
        contenido = arbol_sintactico.contenido

    elif isinstance(arbol_sintactico, ForLoop):
        variable = arbol_sintactico.variable
        rango = arbol_sintactico.rango
        contenido = arbol_sintactico.contenido

    elif isinstance(arbol_sintactico, FunctionDefinition):
        nombre = arbol_sintactico.nombre
        parametros = arbol_sintactico.parametros
        contenido = arbol_sintactico.contenido

    return "Análisis semántico completado con éxito y el resultado es:\n"

def transformar_a_python(codigo):
    lineas = codigo.split(';') 
    lineas_transformadas = []

    for linea in lineas:
        linea = linea.strip()
        if not (linea.startswith("int ") or linea.startswith("string ") or linea.startswith("boolean ")):
            lineas_transformadas.append(linea)

    codigo_transformado = '\n'.join(lineas_transformadas)
    return codigo_transformado

def prueba_semantica(texto):
    try:
        arbol_sintactico = parser.parse(texto)
        resultado = analisis_semantico(arbol_sintactico)
        
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        codigo_python = transformar_a_python(texto)
        exec(codigo_python)

        sys.stdout = old_stdout
        output = new_stdout.getvalue()

        return resultado + '\n' + output
    except SyntaxError as e:
        sys.stdout = old_stdout
        return f"Error semántico: {e}"
    except Exception as e:
        sys.stdout = old_stdout
        return f"Error: {e}"



if __name__ == "__main__":
    codigo_prueba = "h();  def h(): print('a');print('ave');"
    prueba_semantica(codigo_prueba)
