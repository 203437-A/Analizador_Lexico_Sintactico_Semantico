import ply.lex as lex
import re

tokens =  (
    'VARIABLE',
    'DECLARATIVO_INT',
    'DECLARATIVO_BOOLEAN',
    'DECLARATIVO_STRING',
    'CONDICIONAL_IF',
    'CICLO_FOR',
    'IN',
    'FUNCION_DEF',
    'PRINT',
    'RANGE',

    'PUNTO_Y_COMA',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MENOR_IGUAL',
    'MAYOR_IGUAL',
    'DOS_PUNTOS',
    'DIGITO',
    'PARENTESIS_INICIAL',
    'PARENTESIS_FINAL',
    'COMILLA',

)

t_PUNTO_Y_COMA = r';'
t_DOS_PUNTOS = r':'
t_MAYOR_QUE= r'>'
t_MENOR_QUE= r'<'
t_MAYOR_IGUAL= r'>='
t_MENOR_IGUAL = r'<='
t_DIGITO = r'\d+'
t_PARENTESIS_INICIAL = r'\('
t_PARENTESIS_FINAL = r'\)'
t_COMILLA = r'\''


lexema = []

def t_DECLARATIVO_INT(t):
    r'\bint\b'
    return t

def t_DECLARATIVO_BOOLEAN(t):
    r'\bboolean\b'
    return t

def t_DECLARATIVO_STRING(t):
    r'\bstring\b'
    return t

def t_PRINT(t):
    r'\bprint\b'
    return t

def t_RANGE(t):
    r'\brange\b'
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_VARIABLE(t):
    r'[a-z]*[a-z]'
    return t

def analisis(data):
    global lexema

    analizador = lex.lex()
    analizador.input(data)

    lexema.clear()
    has_invalid_token = False

    while True:
        token = analizador.token()
        if not token:
            break
        if token.type == 'TOKEN_INVALIDO':
            has_invalid_token = True
        estado = "{:16} {:16} {:4}".format(str(token.type), str(token.value), str(token.lexpos))
        lexema.append(estado)

    return not has_invalid_token, lexema

def t_error(t):
    global lexema
    estado = "TOKEN_INVALIDO {:16} {:4}".format(str(t.value[0]), str(t.lexpos))
    lexema.append(estado)
    t.lexer.skip(1)

analizador = lex.lex()