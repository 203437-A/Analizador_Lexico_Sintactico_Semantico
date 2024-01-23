import ply.lex as lex
import re

reservada = (
    'INT',
    'FLOAT',
    'STRING',
    'IF',
    'FOR',
    'DEF',
)
tokens = reservada + (
    'VARIABLE',
    'DECLARATIVO_INT',
    'DECLARATIVO_FLOAT',
    'DECLARATIVO_STRING',
    'CONDICIONAL_IF',
    'CICLO_FOR',
    'IN',
    'FUNCION_DEF',

    'PUNTO_Y_COMA',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MENOR_IGUAL',
    'MAYOR_IGUAL',
    'DOS_PUNTOS',
    'DIGITO',
    'CONTENIDO',
    'PARENTESIS_INICIAL',
    'PARENTESIS_FINAL',
)

t_PUNTO_Y_COMA = ';'
t_DOS_PUNTOS = r':'
t_MAYOR_QUE= r'>'
t_MENOR_QUE= r'<'
t_MAYOR_IGUAL= r'>='
t_MENOR_IGUAL = r'<='
t_DIGITO = r'[0-9]*[0-9]'
t_CONTENIDO = r'C'
t_PARENTESIS_INICIAL = r'\('
t_PARENTESIS_FINAL = r'\)'

lexema = []

def t_DECLARATIVO_INT(t):
    r'\bint\b'
    return t

def t_DECLARATIVO_FLOAT(t):
    r'\bfloat\b'
    return t

def t_DECLARATIVO_STRING(t):
    r'\bstring\b'
    return t

def t_CONDICIONAL_IF(t):
    r'\bif\b'
    return t

def t_CICLO_FOR(t):
    r'\bfor\b'
    return t

def t_FUNCION_DEF(t):
    r'\bdef\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_espacios(t):
    r'\s+'
    pass

def t_VARIABLE(t):
    r'[a-z]*[a-z]'
    return t

def analisis(data):
    global lexema

    analizador = lex.lex()
    analizador.input(data)

    lexema.clear()
    while True:
        token = analizador.token()
        if not token:
            break
        estado = "{:16} {:16} {:4}".format(str(token.type), str(token.value), str(token.lexpos))
        lexema.append(estado)
    return lexema

def t_error( t):
    global lexema
    estado = "TOKEN_INVALIDO {:16} {:4}".format(str(t.value[0]), str(t.lexpos))
    lexema.append(estado)
    t.lexer.skip(1)

