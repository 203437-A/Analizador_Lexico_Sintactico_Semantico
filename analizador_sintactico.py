from ply import  yacc
from analizador_lexico import tokens
# from analizador_lexico import analizador

def p_declaraciones(p):
    '''
    declaraciones : declaracion declaraciones
                  | declaracion
    '''
    if len(p) == 3:
        p[0] = p[1] + "\n" + p[2]
    else:
        p[0] = p[1]

def p_declaracion(p):
    '''
    declaracion : DECLARATIVO_INT VARIABLE PUNTO_Y_COMA
                | DECLARATIVO_STRING VARIABLE PUNTO_Y_COMA
                | DECLARATIVO_FLOAT VARIABLE PUNTO_Y_COMA
    '''
    p[0] = f'Declaracion: {p[1]} {p[2]} {p[3]}'

def p_expresion_condicional(p):
    '''
    declaracion : CONDICIONAL_IF VARIABLE MAYOR_QUE DIGITO DOS_PUNTOS CONTENIDO
                | CONDICIONAL_IF VARIABLE MENOR_QUE DIGITO DOS_PUNTOS CONTENIDO
                | CONDICIONAL_IF VARIABLE MENOR_IGUAL DIGITO DOS_PUNTOS CONTENIDO
                | CONDICIONAL_IF VARIABLE MAYOR_IGUAL DIGITO DOS_PUNTOS CONTENIDO
    '''
    p[0] = f'Expresion Condicional: {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]}'

def p_definicion_funcion(p):
    '''
    declaracion : FUNCION_DEF VARIABLE PARENTESIS_INICIAL PARENTESIS_FINAL DOS_PUNTOS CONTENIDO
    '''
    p[0] = f'Definicion de Funcion: {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]}'

def p_bucle(p):
    '''
    declaracion : CICLO_FOR VARIABLE IN VARIABLE DOS_PUNTOS CONTENIDO
    '''
    p[0] = f'Bucle For: {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]}'

def p_error(p):
    if p:
        print(f"Error de sintaxis en la entrada. Token inesperado: {p.value} en la línea {str(p.lineno)} en la posición {str(p.lexpos)}")
    else:
        print("Error de sintaxis en la entrada. Final inesperado o token no reconocido.")
        print(p)   

def prueba(data):
    parser = yacc.yacc(debug=True)
    try:
        result = parser.parse(data)
        if result:
            return result
        else:
            print("El análisis no tuvo éxito.")
            return None
    except Exception as e:
        print(f"Error durante el análisis sintáctico: {str(e)}")
        return None
