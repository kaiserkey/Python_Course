""" 
    El código ANSI es un estándar usado para controlar la forma en que se imprimen los caracteres 
    y la forma en que se realizan los cambios de color en la salida del terminal. Usando estos 
    códigos especiales, podemos cambiar los colores de la letra al imprimir en Python. Esto se 
    logra agregando un código especial al principio y al final de la cadena que se va a imprimir. 
    Por ejemplo, para imprimir una cadena en rojo, podemos usar el código ANSI \033[31m al principio 
    de la cadena y \033[0m al final, para restaurar el color a la configuración predeterminada. 
    Esto permite que los usuarios cambien el color de la salida de la terminal de forma fácil 
    y rápida para mejorar la legibilidad.
    
    Con python se pueden usar los caracteres especiales del codigo ANSI para dar el color a la letra, ejemplo:

    print('\033[31mEsta línea se imprime en rojo\033[0m') 
    print('\033[32mEsta línea se imprime en verde\033[0m') 
    print('\033[33mEsta línea se imprime en amarillo\033[0m') 

    EL formasto es el siguiente:
    
    \033[cod_formato;cod_color_texto;cod_color_fondom
    Codigo de formato:
    
    Sin efecto  =   '0'
    Negrita     =   '1'
    Débil       =   '2'
    Cursiva     =   '3'
    Subrayado   =   '4'
    Inverso     =   '5'
    Oculto      =   '6'
    Tachado     =   '7'
    RESET_ALL   = '\033[0m'
    
    Los códigos de color para el texto son los siguientes:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

""" 

print("\033[1;31mEsta línea se imprime en rojo y negrita\033[0m")
print("\033[1;32mEsta línea se imprime en verde y negrita\033[0m")
print("\033[1;33mEsta línea se imprime en amarillo y negrita\033[0m")
print("\033[1;34mEsta línea se imprime en azul y negrita\033[0m")
print("\033[1;35mEsta línea se imprime en magenta y negrita\033[0m")
print("\033[1;36mEsta línea se imprime en cyan y negrita\033[0m")
print("\033[1;37mEsta línea se imprime en blanco y negrita\033[0m")
print("\033[1;38mEsta línea se imprime en gris y negrita\033[0m")

""" 
    Los códigos de color para el fondo son los siguientes:
    
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'
""" 

print("\033[1;31;40mEsta línea se imprime en rojo y negrita con fondo negro\033[0m")
print("\033[1;32;41mEsta línea se imprime en verde y negrita con fondo rojo\033[0m")
print("\033[1;33;42mEsta línea se imprime en amarillo y negrita con fondo verde\033[0m")
print("\033[1;34;43mEsta línea se imprime en azul y negrita con fondo amarillo\033[0m")
print("\033[1;35;44mEsta línea se imprime en magenta y negrita con fondo azul\033[0m")
print("\033[1;36;45mEsta línea se imprime en cyan y negrita con fondo magenta\033[0m")
print("\033[1;37;46mEsta línea se imprime en blanco y negrita con fondo cyan\033[0m")
print("\033[1;38;47mEsta línea se imprime en gris y negrita con fondo blanco\033[0m")
print("\033[1;39;48mEsta línea se imprime en gris y negrita con fondo gris\033[0m")