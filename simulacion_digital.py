'''
  * Descripción: funciones que simulan puertas logicas y sus implementaciones en circuitos usando pygame
  * documentos relacionados: logica_digital.py
  * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
  * fecha: 08 - 08 - 2024
  * --------------------------------- TODO -------------------------------------------------
  * Lista de feature por hacer:
  * - registros
  * - decodificador de 1 bit a 7 segmentos
  * - contador de 8 bits y un algoritmo para hacerlos porque ahora estan un poco mal implementados
  * - remplazar las imagenes feas por una construidas en el simulador web (en proceso)
  * - optimizar el codigo
  * - encontrar errores
  *
  * --------------------------------- ISSUES -----------------------------------------------
  * Lista de problemas conocidos:
  * - hacer contadores es una porqueria
  * - los contadores no funcionan correctamente
  *
  * ----------------------------------------------------------------------------------------
'''
# Importar librerias
from pygame import *
import sys
from logica_digital import *

funciones_logicas = {
    "and" : {
        "input": [(180, 240), (180, 325)],
        "output": [(580, 280)],
        "escala": [400, 200]
    },
    "or" : {
        "input": [(180, 240), (180, 325)],
        "output": [(580, 280)],
        "escala": [400, 200]
    },
    "not" : {
        "input": [(180, 280)],
        "output": [(580, 280)],
        "escala": [400, 200]
    },
    "xor" : {
        "input": [(180, 240), (180, 325)],
        "output": [(580, 280)],
        "escala": [400, 200]

    },
    "nand" : {
        "input": [(180, 240), (180, 325)],
        "output": [(580, 280)],
        "escala": [400, 200]
    },
    "nor" : {
        "input": [(180, 240), (180, 325)],
        "output": [(580, 280)],
        "escala": [400, 200]
    },
    "xnor" : {
        "input": [(180, 240), (180, 325)],
        "output": [(580, 280)],
        "escala": [400, 200]
    },
    "rs_flip_flop" : {
        "input": [(130, 420), (130, 160)],
        "output": [(630, 190), (630, 380)],
        "escala": [700, 400]
    },
    "sr_flip_flop" : {
        "input": [(80, 150), (80, 430)],
        "output": [(660, 170), (660, 390)],
        "clock": (80, 290),
        "escala": [700, 400]
    },
    "jk_flip_flop" : {
        "input": [(70, 170), (70, 390)],
        "output": [(680, 190), (680, 370)],
        "clock": (70, 280),
        "escala": [700, 400]
    },
    "d_flip_flop" : {
        "input": [(70, 150)],
        "output": [(660, 180), (660, 390)],
        "clock": (70, 285),
        "escala": [700, 400]
    },
    "t_flip_flop" : {
        "input": [(60, 175)],
        "output": [(680, 190), (680, 370)],
        "clock": (60, 285),
        "escala": [700, 400]
    },
    "semi_sumador" : {
        "input": [(135, 235), (135, 330)],
        "output": [(580, 220),(580, 345)],
        "escala": [600, 300]
    },
    "semi_substractor" : {
        "input": [(125, 200), (125, 370)],
        "output": [(590, 215),(590, 350)],
        "escala": [600, 300]
    },  
    "sumador_total" : {
        "input": [(60, 150), (60, 190), (60, 275)],
        "output": [(650, 190),(650, 335)],
        "escala": [700, 400]
    },
    "restador_total" : {
       "input": [(50, 150), (50, 190), (50, 230)],
        "output": [(670, 165),(670, 355)],
        "escala": [700, 400]
    },
    "multiplicador_4bits" : {
        "input": [(225, 90), (180, 90), (130, 90), (90, 90)],
        "output": [(680, 180), (680, 255), (680, 345),(680, 420)],
        "escala": [700,400]
    },
    "comparador_2_bits" : {
        "input": [(348, 150),  (275, 150), (160, 150), (80, 150)],
        "output": [(680, 200), (680, 345), (680, 420)],
        "escala": [800,400]
    },
    "contador_4_bits" : {
        "input" : [(120, 665)],
        "output": [(180, 340), (180, 280), (180, 225), (180, 165)],
        "clock": (120, 510),
        "escala": [700,400]
    }
}

# funcion que "importa" el funcionamiento del programa
def import_puertas(tipo_puerta, valor_clock,estado_anterior = [0, 0],*args_entrada):
    # puertas logicas
    if tipo_puerta == "and":
        return puerta_and(*args_entrada)
    elif tipo_puerta == "or":
        return puerta_or(*args_entrada)
    elif tipo_puerta == "not":
        return puerta_not(*args_entrada)
    elif tipo_puerta == "xor":
        return puerta_xor(*args_entrada)
    elif tipo_puerta == "nand":
        return puerta_nand(*args_entrada)
    elif tipo_puerta == "nor":
        return puerta_nor(*args_entrada)
    elif tipo_puerta == "xnor":
        return puerta_xnor(*args_entrada)
    # flip flops
    elif tipo_puerta == "rs_flip_flop":
        return rs_flip_flop_asincrono(*args_entrada)
    elif tipo_puerta == "sr_flip_flop":
        return rs_flip_flop_sincrono(*args_entrada, clock = valor_clock, estado_anterior = estado_anterior)
    elif tipo_puerta == "jk_flip_flop":
        return jk_flip_flop(*args_entrada, clock = valor_clock, estado_anterior = estado_anterior)
    elif tipo_puerta == "d_flip_flop":
        return d_flip_flop(*args_entrada, clock = valor_clock, estado_anterior = estado_anterior)
    elif tipo_puerta == "t_flip_flop":
        return t_flip_flop(*args_entrada, clock = valor_clock, estado_anterior = estado_anterior)
    # implementaciones
    elif tipo_puerta == "semi_sumador":
        return semi_sumador(*args_entrada)
    elif tipo_puerta == "semi_substractor":
        return semi_substractor(*args_entrada)
    elif tipo_puerta == "sumador_total":
        return sumador_total(*args_entrada)
    elif tipo_puerta == "restador_total":
        return restador_total(*args_entrada)
    elif tipo_puerta == "multiplicador_4bits":
        return multiplicador_4bits(*args_entrada)
    elif tipo_puerta == "comparador_2_bits":
        return comparador_2_bits(*args_entrada)
    elif tipo_puerta == "contador_4_bits":
        return contador_4_bits(*args_entrada, valor_clock, estado_anterior = estado_anterior)

# arma el rect de los botones de input, output y clock
def armador_boton_rect(funcion_logica , input_output_clock, cantidad_botones): 
    if input_output_clock == "input":
        input_rect = []
        for i in range(cantidad_botones):
            x = funciones_logicas[funcion_logica]["input"][i][0]
            y = funciones_logicas[funcion_logica]["input"][i][1]
            input_rect.append(Rect(x,y, 40, 40))
        return input_rect
    elif input_output_clock == "output":    
        output_rect = []
        for i in range(cantidad_botones):
            x = funciones_logicas[funcion_logica]["output"][i][0]
            y = funciones_logicas[funcion_logica]["output"][i][1]
            output_rect.append(Rect(x, y, 40, 40))
        return output_rect
    elif input_output_clock == "clock":
        clock_rect : Rect
        x = funciones_logicas[funcion_logica]["clock"][0]
        y = funciones_logicas[funcion_logica]["clock"][1]
        clock_rect = Rect(x, y, 40, 40)
        return clock_rect

# un funcion que actualiza el clock en el while loop
def actualizar_reloj(valor_clock = 0):
    valor_clock = puerta_not(valor_clock)
    return valor_clock

# dibuja el boton y su texto
def boton(ventana, boton_rect, valor_boton): # dibuja el boton y su texto
    draw.rect(ventana, BLANCO, boton_rect)
    texto = MAIN_FONT.render(str(valor_boton),True, NEGRO)
    ventana.blit(texto,(boton_rect.x+(boton_rect.width-texto.get_width())/2, boton_rect.y+(boton_rect.height-texto.get_height())/2))

# dibuja el boton de inicio y verifica si uno la da al boton inicio
def menu(ventana, ALTO, ANCHO):
    menu_rect = Rect(ALTO/2.3, ANCHO/2.3, 100, 60)
    boton(ventana, menu_rect, "Iniciar")
    for evento in event.get():
        if evento.type == QUIT:
            sys.exit()
        if evento.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
            if menu_rect.collidepoint(mouse.get_pos()):
                return True
            
# inicializacion pygame
init()

# Configura el reloj
clock = time.Clock()

# Configura el temporizador
temporizador = USEREVENT + 1 # Evento personalizado que hace que funcione el reloj de los flip flops
time.set_timer(temporizador, 500)  # Cambia el estado del botón cada medio segundo
valor_clock = 0

# configuraciones generales y algunas constantes
ALTO = 600
ANCHO = 800
FPS = 30
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# configuracion pantalla
VENTANA = display.set_mode((ANCHO, ALTO))
display.set_caption('"simulacion digital"')
display.set_icon(image.load("imagenes\\error_418.png"))
MAIN_FONT = font.SysFont("cambria", 35)

# funcion que  crea las simulaciones
def simulacion(cantidad_botones_input, cantidad_botones_output, direccion_imagen , tipo_puerta, puerta_logica_flip_flop_implementacion,direccion_narracion,modo_abierto=False):
    estado_anterior = [0, 1]
    escala_grafico = funciones_logicas[tipo_puerta]["escala"]
    # menu
    boton_retroceder_menu=image.load("imagenes/simbolos/flechita_NOT.png")
    boton_retroceder_menu=transform.scale(boton_retroceder_menu,(203,77))
    boton_retroceder_rect_menu= boton_retroceder_menu.get_rect(center = (203/2, 77/2))
    boton_avanzar=image.load("imagenes/simbolos/flechita_YES.png") 
    boton_avanzar=transform.scale(boton_avanzar,(203,77))
    boton_avanzar_rect= boton_avanzar.get_rect(center = (ANCHO-203/2, 77/2))
    # grafico puerta
    puerta_grafico = image.load(direccion_imagen) 
    puerta_grafico = transform.scale(puerta_grafico, (escala_grafico))
    puerta_grafico_rect = puerta_grafico.get_rect(center = (ANCHO/2, ALTO/2)) # posicion de la imagen
    botones_input_rect = armador_boton_rect(tipo_puerta, "input", cantidad_botones_input) # botones de input
    botones_input_valor = [0]*cantidad_botones_input
    botones_output = armador_boton_rect(tipo_puerta, "output", cantidad_botones_output) # botones de output
    if puerta_logica_flip_flop_implementacion != "puerta_logica":
        if tipo_puerta != "rs_flip_flop":
            if puerta_logica_flip_flop_implementacion != "implementacion":
                global valor_clock
                clock_rect = armador_boton_rect(tipo_puerta, "clock", 1)
    resultado = [0]*cantidad_botones_output
    # sonido
    mixer.music.load(direccion_narracion)
    mixer.music.play(1)
    # banderas
    bandera_salida = True
    bandera = True
    # bucle principal
    while bandera:
        # Limita el bucle a 60 fotogramas por segundo
        clock.tick(FPS)
        # limpiar la pantalla
        VENTANA.fill(BLANCO)
        # dibujar la puerta logica
        VENTANA.blit(puerta_grafico, puerta_grafico_rect)
        # dibujar el texto de la imagen
        VENTANA.blit(MAIN_FONT.render(f"{tipo_puerta.replace('_',' ')}", True, "black"), (ALTO/2, 25)) # texto de la imagen
        #dibujar los botones de navegacion:
        VENTANA.blit(boton_retroceder_menu,boton_retroceder_rect_menu)
        if modo_abierto==False:
            VENTANA.blit(boton_avanzar,boton_avanzar_rect)       
        # dibujar los botones
        for i in range(cantidad_botones_input):
            boton(VENTANA, botones_input_rect[i], botones_input_valor[i])
        if puerta_logica_flip_flop_implementacion != "puerta_logica" and puerta_logica_flip_flop_implementacion != "implementacion":
            if tipo_puerta != "rs_flip_flop":    
                boton(VENTANA, clock_rect, valor_clock)
        # eventos
        pos_mouse = mouse.get_pos()
        for evento in event.get():
            if evento.type == QUIT:
                sys.exit() 
            if evento.type == MOUSEBUTTONDOWN:
                print(pos_mouse)
            if evento.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                for i in range(cantidad_botones_input):
                    if botones_input_rect[i].collidepoint(pos_mouse):
                        botones_input_valor[i] = puerta_not(botones_input_valor[i])
                if boton_avanzar_rect.collidepoint(pos_mouse):
                    bandera_salida = False
                    bandera = False
                if boton_retroceder_rect_menu.collidepoint(pos_mouse):
                    bandera_salida = True
                    bandera = False
            if evento.type == temporizador: # temporizador 
                valor_clock = actualizar_reloj(valor_clock) # actualziar el reloj por el valor 1 o 0
                if valor_clock == 1 or puerta_logica_flip_flop_implementacion != "flip_flop":
                    resultado = import_puertas(tipo_puerta, valor_clock , estado_anterior, *botones_input_valor)
                    estado_anterior = resultado
                else:
                    resultado = estado_anterior
        for i in range(cantidad_botones_output):
            if puerta_logica_flip_flop_implementacion == "puerta_logica":
                boton(VENTANA, botones_output[i], resultado)
            else:
                boton(VENTANA, botones_output[i], resultado[i])
        display.update()
    return bandera_salida

# funcion que simula los contadores
def simulacion_contadores(cantidad_botones_input, cantidad_botones_output, direccion_imagen , tipo_puerta, puerta_logica_flip_flop_implementacion = "puerta_logica"):
    estado_anterior = [0,0,0,0]
    # estado_anterior_1 = 0 # estado anterior de los flip flops
    # estado_anterior_2 = 0 # estado anterior de los flip flops
    # estado_anterior_3 = 0 # estado anterior de los flip flops
    # estado_anterior_4 = 0 # estado anterior de los flip flops
    puerta_grafico = image.load(direccion_imagen)
    puerta_grafico = transform.scale(puerta_grafico, (800, 600))
    puerta_grafico_rect = puerta_grafico.get_rect(center=(800,600))
    botones_input_rect = armador_boton_rect(tipo_puerta, "input", cantidad_botones_input) # botones de input
    botones_input_valor = [0]*cantidad_botones_input
    botones_output = armador_boton_rect(tipo_puerta, "output", cantidad_botones_output) # botones de output
    global valor_clock
    clock_rect = armador_boton_rect(tipo_puerta, "clock", 1)
    bandera = True
    while bandera:
        # Limita el bucle a 60 fotogramas por segundo
        clock.tick(FPS)
        # limpiar la pantalla
        VENTANA.fill(BLANCO)
        # dibujar la puerta logica
        VENTANA.blit(puerta_grafico, puerta_grafico_rect)
        # dibujar el texto de la imagen
        VENTANA.blit(MAIN_FONT.render(f"{tipo_puerta.replace("_"," ")}", True, "black"), (ALTO/2.3, 100)) # texto de la imagen
        # dibujar los botones
        for i in range(cantidad_botones_input):
            boton(VENTANA, botones_input_rect[i], botones_input_valor[i])
        boton(VENTANA, clock_rect, valor_clock)
        # eventos 
        pos_mouse = mouse.get_pos()
        for evento in event.get():
            if evento.type == QUIT:
                quit()
                sys.exit() 
            if evento.type == MOUSEBUTTONDOWN:
                for i in range(cantidad_botones_input):
                    if botones_input_rect[i].collidepoint(pos_mouse):
                        botones_input_valor[i] = puerta_not(botones_input_valor[i])
            if evento.type == temporizador: # temporizador 
                valor_clock = actualizar_reloj() # actualziar el reloj por el valor 1 o 0
                if valor_clock == 1: 
                        estado_anterior[0] = import_puertas(tipo_puerta, valor_clock, estado_anterior[0], *botones_input_valor)
                        for i in range(3):
                            estado_anterior[i + 1] = import_puertas(tipo_puerta, estado_anterior[i], estado_anterior[i + 1], *botones_input_valor)
            for i in range(cantidad_botones_output):
                boton(VENTANA, botones_output[0], estado_anterior[0])
        display.update()

# funcion que recopila las simulaciones
def recopilatorio_simulaciones(puerta_logica_flip_flop_implementacion):
    if puerta_logica_flip_flop_implementacion == "and":
        valor = simulacion(2, 1, "imagenes\\puertas_logicas\\puerta_and.png", "and","puerta_logica","narraciones/AND.mp3")
    elif puerta_logica_flip_flop_implementacion == "or":
        valor = simulacion(2, 1, "imagenes\\puertas_logicas\\puerta_or.png", "or", "puerta_logica","narraciones/OR.mp3")
    elif puerta_logica_flip_flop_implementacion == "not":
        valor = simulacion(1, 1, "imagenes\\puertas_logicas\\puerta_not.png", "not", "puerta_logica","narraciones/NOT.mp3") #cambiar en todas menos esta
    elif puerta_logica_flip_flop_implementacion == "xor":
        valor = simulacion(2, 1, "imagenes\\puertas_logicas\\puerta_xor.png", "xor", "puerta_logica","narraciones/XOR.mp3")
    elif puerta_logica_flip_flop_implementacion == "nand":
        valor = simulacion(2, 1, "imagenes\\puertas_logicas\\puerta_nand.png", "nand", "puerta_logica","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "nor":
        valor = simulacion(2, 1, "imagenes\\puertas_logicas\\puerta_nor.png", "nor", "puerta_logica","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "xnor":
        valor = simulacion(2, 1, "imagenes\\puertas_logicas\\puerta_xnor.png", "xnor", "puerta_logica","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "rs_flip_flop":
        valor = simulacion(2, 2, "imagenes\\flip_flops\\rs_flip_flop.png", "rs_flip_flop", "flip_flop","narraciones/RS_flip_flop.mp3")
    elif puerta_logica_flip_flop_implementacion == "sr_flip_flop":
        valor = simulacion(2, 2, "imagenes\\flip_flops\\sr_flip_flop.png", "sr_flip_flop", "flip_flop","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "jk_flip_flop":
        valor = simulacion(2, 2, "imagenes\\flip_flops\\jk_flip_flop.png", "jk_flip_flop", "flip_flop","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "d_flip_flop":
        valor = simulacion(1, 2, "imagenes\\flip_flops\\d_flip_flop.png", "d_flip_flop", "flip_flop","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "t_flip_flop":
        valor = simulacion(1, 2, "imagenes\\flip_flops\\t_flip_flop.png", "t_flip_flop", "flip_flop","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "semi_sumador":
        valor = simulacion(2, 2, "imagenes\\implementaciones\\semi_sumador.png", "semi_sumador", "implementacion","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "semi_substractor":
        valor = simulacion(2, 2, "imagenes\\implementaciones\\semi_substractor.png", "semi_substractor", "implementacion","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "sumador_total":
        valor = simulacion(3, 2, "imagenes\\implementaciones\\sumador_total.png", "sumador_total", "implementacion","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "restador_total":
        valor = simulacion(3, 2, "imagenes\\implementaciones\\restador_total.png", "restador_total", "implementacion","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "multiplicador_4bits":
        valor = simulacion(4, 4, "imagenes\\implementaciones\\multiplicador_4bits.png", "multiplicador_4bits", "implementacion","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "comparador_2_bits":
        valor = simulacion(4, 3, "imagenes\\implementaciones\\comparador_2_bits.png", "comparador_2_bits", "implementacion","narraciones/NOT.mp3")
    elif puerta_logica_flip_flop_implementacion == "contador_4_bits":
        valor = simulacion_contadores(1, 4, "imagenes\\implementaciones\\contador_4_bits.png", "contador_4_bits", "implementacion","narraciones/NOT.mp3")
    return valor

def menu_simulacion(VENTANA, ALTO, ANCHO):
    inicio = True
    bandera_1 = True
    bandera_2 = True
    bandera_3 = True
    bandera_4 = True
    bandera_5 = True
    bandera_6 = True
    bandera_7 = True
    bandera_8 = True
    bandera_9 = True
    bandera_10 = True
    bandera_11 = True
    bandera_12 = True
    bandera_13 = True
    bandera_14 = True
    bandera_15 = True
    bandera_16 = True
    bandera_17 = True
    bandera_18 = True
    bandera_19 = True
    
    while True:
        while inicio:
            VENTANA.fill(BLANCO)
            iniciar = menu(VENTANA, ANCHO, ALTO)
            if iniciar:
                inicio = False
                bandera_1 = False
            display.update()
        if not bandera_1:
            inicio = False
            bandera_2 = recopilatorio_simulaciones("and")
            if bandera_2:
                inicio = True
        if not bandera_2:
            bandera_1 = True
            bandera_3 = recopilatorio_simulaciones("or")
            if bandera_3:
                bandera_1 = False
        if not bandera_3:
            bandera_2 = True
            bandera_4 = recopilatorio_simulaciones("not")
            if bandera_4:
                bandera_2 = False
        if not bandera_4:
            bandera_3 = True
            bandera_5 = recopilatorio_simulaciones("xor")
            if bandera_5:
                bandera_3 = False
        if not bandera_5:
            bandera_4 = True
            bandera_6 = recopilatorio_simulaciones("nand")
            if bandera_6:
                bandera_4 = False
        if not bandera_6:
            bandera_5 = True
            bandera_7 = recopilatorio_simulaciones("nor")
            if bandera_7:
                bandera_5 = False
        if bandera_7 == False:
            bandera_6 = True
            bandera_8 = recopilatorio_simulaciones("xnor")
            if bandera_8 == True:
                bandera_6 = False
        if not bandera_8:
            bandera_7 = True
            bandera_9 = recopilatorio_simulaciones("rs_flip_flop")
            if bandera_9:
                bandera_7 = False
        if not bandera_9:   
            bandera_8 = True
            bandera_10 = recopilatorio_simulaciones("sr_flip_flop")
            if bandera_10:
                bandera_8 = False
        if not bandera_10:
            bandera_9 = True
            bandera_11 = recopilatorio_simulaciones("jk_flip_flop")
            if bandera_11:
                bandera_9 = False
        if not bandera_11:
            bandera_10 = True
            bandera_12 = recopilatorio_simulaciones("d_flip_flop")
            if bandera_12:
                bandera_10 = False
        if not bandera_12:
            bandera_11 = True
            bandera_13 = recopilatorio_simulaciones("t_flip_flop")
            if bandera_13:
                bandera_11 = False
        if not bandera_13:
            bandera_12 = True
            bandera_14 = recopilatorio_simulaciones("semi_sumador")
            if bandera_14:
                bandera_12 = False
        if not bandera_14:
            bandera_13 = True
            bandera_15 = recopilatorio_simulaciones("semi_substractor")
            if bandera_15:
                bandera_13 = False
        if not bandera_15:
            bandera_14 = True
            bandera_16 = recopilatorio_simulaciones("sumador_total")
            if bandera_16:
                bandera_14 = False
        if not bandera_16:
            bandera_15 = True
            bandera_17 = recopilatorio_simulaciones("restador_total")
            if bandera_17:
                bandera_15 = False
        if not bandera_17:
            bandera_16 = True
            bandera_18 = recopilatorio_simulaciones("multiplicador_4bits")
            if bandera_18:
                bandera_16 = False
        if not bandera_18:
            bandera_17 = True
            bandera_19 = recopilatorio_simulaciones("comparador_2_bits")
            if bandera_19:
                bandera_17 = False
        # if not bandera_19:
        #     bandera_18 = True
        #     bandera_20 = recopilatorio_simulaciones("contador_4_bits")
        #     if bandera_20:
        #         bandera_18 = False
        if not bandera_19:
            bandera_19 = True
            inicio = True


if __name__ == "__main__":
#* descomenten para simular alguna puerta logica, flip flop o implementacion
    print("hola")
    #recopilatorio_simulaciones("and")
    #recopilatorio_simulaciones("or")
    #recopilatorio_simulaciones("not") 
    #recopilatorio_simulaciones("xor")
    #recopilatorio_simulaciones("nand")
    #recopilatorio_simulaciones("nor")
    #recopilatorio_simulaciones("xnor")
    #recopilatorio_simulaciones("rs_flip_flop") 
    #recopilatorio_simulaciones("sr_flip_flop") 
    #recopilatorio_simulaciones("jk_flip_flop")
    #recopilatorio_simulaciones("d_flip_flop") 
    #recopilatorio_simulaciones("t_flip_flop")
    #recopilatorio_simulaciones("semi_sumador")
    #recopilatorio_simulaciones("semi_substractor")
    #recopilatorio_simulaciones("sumador_total")
    #recopilatorio_simulaciones("restador_total")
    #recopilatorio_simulaciones("multiplicador_4bits") # falta actualizar pos botones
    recopilatorio_simulaciones("comparador_2_bits") # falta actualizar pos botones
    #recopilatorio_simulaciones("contador_4_bits") # marca nonetypes buscar que lo causa
    # menu_simulacion(VENTANA, ALTO, ANCHO)
# fin