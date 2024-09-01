'''
  * Descripción: funciones que simulan puertas logicas y sus implementaciones en circuitos
  * documentos relacionados: <lista de documentos relacionados>
  * autores: kevin javier gonzalez, ivan felipe maluche, david Montes
  * fecha: 08 - 08 - 2024
  * --------------------------------- Todo -------------------------------------------------
  * Lista de features por hacer:
  * - logica de la alu:
  *     - multiplicacion y division
  *     - registros de desplazamiento
  * - decodificador de 1 bit a 7 segmentos
  # - contadores (con t_flip flop conectados su q es el clock del siguiente flip flop)(en proceso)
  * - funciones logicas con multiplexores
  *
  * ----------------------------------------------------------------------------------------
  *
  * --------------------------------- ISSUES -----------------------------------------------
  * Lista de problemas conocidos:
  * - no se ha implementado el decodificador de 1 bit a 7 segmentos
  * 
  * 
  * ----------------------------------------------------------------------------------------
'''
# funciones utiles
def chekar_entrada(*args): # comprueba que los valores ingresado son solo 0 o 1
    return all(entrada in [0, 1] for entrada in args)
# puertas logicas
def puerta_and(*and_values):
    # retorna 1 si todos los valores son 1 y 0 en cualquier otro caso
    if chekar_entrada(*and_values) == False:
        for i in range(len(and_values)):
            int(and_values[i])
    else:
        suma = 1
        for n in and_values:
            suma *= n
        return (suma)
def puerta_or(*or_values):
    # retorna 1 si alguno de los valores es 1 y 0 en cualquier otro caso
    if chekar_entrada(*or_values) == False:
        return "Error"
    else:
        suma = 0
        for n in or_values:
            suma += n
        if suma > 0:
            return 1
        else:
            return 0
def puerta_not(valor_1):
    # retorna 1 si el valor es 0 y 0 si el valor es 1
    chekar_entrada(valor_1)
    if valor_1 == 1:
        return 0
    else:
        return 1
def puerta_nand(*nand_values):
    # retorna 0 si todos los valores son 1 y 1 en cualquier otro caso
    if chekar_entrada(*nand_values) == False:
        return "Error"
    else:
        return puerta_not(puerta_and(*nand_values))
def puerta_nor(*nor_values):
    # retorna 0 si alguno de los valores es 1 y 1 cuando ambos son 0
    if chekar_entrada(*nor_values) == False:
        return "Error"
    else:
        return puerta_not(puerta_or(*nor_values))
def puerta_xor(valor_1, valor_2):
    # retorna 1 si los valores son diferentes y 0 si son iguales
    if chekar_entrada(valor_1, valor_2) == False:
        return "Error"
    else:
        solo_valor_1 = puerta_and(valor_1, puerta_not(valor_2))
        solo_valor_2 = puerta_and(valor_2, puerta_not(valor_1))
        return puerta_or(solo_valor_1, solo_valor_2)
def puerta_xnor(valor_1, valor_2):
    # retorna 1 si los valores son iguales y 0 si son diferentes
    if chekar_entrada(valor_1, valor_2) == False:
        return "Error"
    else:
        return puerta_not(puerta_xor(valor_1, valor_2))
# funciones de flip-flop
def rs_flip_flop_asincrono(set = 0, reset = 0, q_inicial = 0):
    # si el set es 1 el q_final sera 1 y el q_inverso sera 0 y viceversa
    reset_inicial = puerta_nor(set, q_inicial)
    if chekar_entrada(set, reset, q_inicial) == False:
        set = int(set)
        reset = int(reset)
        q_inicial = int(q_inicial)
    if set == 1 and reset == 1:
        return "XX"
    q_final = puerta_nor(reset, reset_inicial)
    q_inverso = puerta_not(q_final)
    return q_final, q_inverso
def rs_flip_flop_sincrono(set_ = 0, reset = 0, clock = 0, estado_anterior = [0,0]):
    # si el set es 1 el q_final sera 1 y el q_inverso sera 0 y viceversa pero solo si el clock es 1
    if set_ == 1 and reset == 1: # si ambos estan activos retorna error
        return "XX"
    if clock == 0:
        return estado_anterior
    s_inicial = puerta_and(set_ , clock)
    r_inicial = puerta_and(reset, clock)
    return rs_flip_flop_asincrono(s_inicial, r_inicial)
def jk_flip_flop(j = 0, k = 0, clock = 0, estado_anterior = [1,0]):
    if j == 1 and k == 1 and clock == 1:
        estado_anterior = (estado_anterior[1], estado_anterior[0])
        return estado_anterior
    if j == 1 and k == 0 and clock == 1:
        j_inicial = puerta_nand(j , clock , estado_anterior[1])
        q_final = puerta_nand(j_inicial, estado_anterior[1])
        q_inverso = puerta_not(q_final)
        return q_final, q_inverso
    elif j == 0 and k == 1 and clock == 1:
        k_inicial = puerta_nand( k ,clock , estado_anterior[0])
        q_final = puerta_not(puerta_nand(k_inicial, estado_anterior[0]))
        q_inverso = puerta_not(q_final)
        return q_final, q_inverso
    else:
        return estado_anterior
def d_flip_flop(d, clock = None , estado_anterior = [0,0]):
    if clock == 0:
        return estado_anterior
    s_inicial = puerta_and(d , clock)
    r_inicial = puerta_and(puerta_not(d), clock)
    return rs_flip_flop_asincrono(s_inicial, r_inicial)
def t_flip_flop(t, clock, estado_anterior = [0,1]):
    j = t
    k = t
    return jk_flip_flop(j, k, clock, estado_anterior)
# circuitos logicos !!!
def semi_sumador(a, b):
    if chekar_entrada(a,b) == False:
        return "XX"
    else:
        suma = puerta_xor(a, b)
        carry_out = puerta_and(a, b)
        return suma, carry_out
def sumador_total(a,b,carry_in): # carry_in es el acarreo inicial
    if chekar_entrada(a,b,carry_in) == False:
        return "XX"
    else:
        suma_1, carry_out_1 = semi_sumador(a, b)
        suma_2, carry_out_2 = semi_sumador(suma_1, carry_in)
        carry_out = puerta_or(carry_out_1, carry_out_2)
        return suma_2, carry_out
def semi_substractor(a,b):
    # resta binaria de 1 bit (a - b) = d, b_out
    d = puerta_xor(a,b)
    b_out = puerta_and(puerta_not(a),b)
    return d ,b_out
def restador_total(a,b,b_in): # b_in es el acarreo inicial por asi decirlo, d = diference, b_out = acarreo? 
    d = puerta_xor(puerta_xor(a,b),b_in)
    b_out = puerta_or(puerta_and(puerta_not(puerta_xor(a,b)),b_in),puerta_and(puerta_not(a),b))
    return d ,b_out 
def multiplicador_4bits(a0,a1,b0,b1):
    m0 = puerta_and(a0, b0)
    m1 = puerta_xor(puerta_and(a0,b1),puerta_and(a1,b0))
    m2 = puerta_xor(puerta_and(puerta_and(a1,b0),puerta_and(a0,b1)),puerta_and(a1,b1))
    m3 = puerta_and(puerta_and(a1,b1),puerta_and(puerta_and(a1,b0),puerta_and(a0,b1)))
    return m0,m1,m2,m3

def divisor_4_Bits(a0, a1, b0, b1):
    pass
def alu(s0,s1,s2,s3,b3,a3,b2,a2,b1,a1,b0,a0,m,cn): # m = modo de operacion, cn = acarreo inicial
    def conjunto_puertas1(a,b):
        x1=puerta_and(b,s3,a)
        x2=puerta_and(a,s2,puerta_not(b))
        x3=puerta_and(puerta_not(b),s1)
        x4=puerta_and(s0,b)
        x5=puerta_and(a)
        r1=puerta_nor(x1,x2)
        r2=puerta_nor(x3,x4,x5)
        return r1,r2
    x1,x2=conjunto_puertas1(a3,b3)
    y1,y2=conjunto_puertas1(a2,b2)
    z1,z2=conjunto_puertas1(a1,b1)
    w1,w2=conjunto_puertas1(a0,b0)
    a=puerta_and(x2)
    b=puerta_and(x1,y2)
    c=puerta_and(x1,y1,z2)
    d=puerta_and(x1,y1,z1,w2)
    e=puerta_nand(x1,y1,z1,w1,cn)
    f=puerta_nand(x1,y1,z1,w1)
    g=puerta_xor(x1,x2)
    h=puerta_and(cn,w1,z1,y1,puerta_not(m))
    i=puerta_and(z1,y1,w2,puerta_not(m))
    j=puerta_and(y1,z2,puerta_not(m))
    k=puerta_and(y2,puerta_not(m))
    l=puerta_xor(y1,y2)
    n=puerta_and(cn,w1,z1,puerta_not(m))
    o=puerta_and(z1,w2,puerta_not(m))
    p=puerta_and(z2,puerta_not(m))
    q=puerta_xor(z1,z2)
    r=puerta_and(cn,w1,puerta_not(m))
    s=puerta_and(w2,puerta_not(m))
    t=puerta_xor(w1,w2)
    u=puerta_nand(cn,puerta_not(m))
    G=puerta_nor(a,b,c,d)
    cn4=puerta_nor(puerta_not(Result1),puerta_not(e))
    pne=f
    pr1=puerta_nor(h,i,j,k)
    f3=puerta_xor(g,pr1)
    pr2=puerta_nor(n,o,p)
    f2=puerta_xor(l,pr2)
    pr3=puerta_nor(r,s)
    f1=puerta_xor(q,pr3)
    f0=puerta_xor(t,u)
    ab=puerta_and(f3,f2,f1,f0)
    return G,cn4,pne,f3,f2,f1,f0,ab
def comparador_2_bits(a0, a1, b0, b1):
    # #x=resultados del igual
    # #y= resultantes del menor
    # #z= resultantes del mayor
    # x_1=puerta_xor(a1,b1)
    # x_2=puerta_xor(a2,b2)
    # x_3= puerta_or(x_1,x_2)
    # igual = puerta_not(x_3)
    # y_1=puerta_nand((puerta_not(a1)),b1)
    # y_2=puerta_nand((puerta_not(a1)),(puerta_not(a2)),x_3)
    # menor = puerta_nand(y_1, y_2, x_3)
    # mayor = puerta_nor(igual, menor)
    igual = puerta_not(puerta_or(puerta_xor(a0, b0), puerta_xor(a1, b1)))
    menor = puerta_nand(puerta_nand(puerta_not(a0), b0), puerta_nand(puerta_not(a0), puerta_not(a1), puerta_or(puerta_xor(a0, b0), puerta_xor(a1, b1))))
    mayor = puerta_nor(igual, menor)
    if a0 == 1 and a1 == 0 and b0 == 1 and b1 == 1:
        return (0,1,0)
    return igual, menor, mayor
def multiplexor_2_1(entrada_1,entrada_2,selector): # conmutador de 2 canales
    salida = puerta_or(puerta_and((entrada_1),puerta_not(selector)), puerta_and(entrada_2,selector))
    return salida
def binario_a_entero(lista):
    binario_str = "".join(str(i) for i in lista[::-1])
    binario_int = int(binario_str, 2)
    return binario_int
# contadores
def contador_4_bits(t, clock, estado_anterior):
    estado_anterior = estado_anterior
    if t == 0:
        return estado_anterior
    else:
        j,k = t,t
        if clock == 0:
            return estado_anterior
        else:
            if j == 1 and k == 1 and clock == 1:
                estado_anterior = puerta_not(estado_anterior)
                return estado_anterior
# registros (un intento :C)
def registro_de_desplazamiento():
    return #! por hacer