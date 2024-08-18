# proyecto_programacion_actualizado

<div align='center'>
<figure> <img src="https://res.cloudinary.com/dm0p2ljin/image/upload/v1714416338/error-418_dtb3ak.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

# proyecto_programacion

Este proyecto fue realizado para  

# diagramas y funcionamientos de las funciones

- funcionamiento de las puertas logicas en el proyecto

## puertas logicas

### puerta YES


<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
     <tr>
    <td> entrada </td> <td> salida </td> 
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> 
  </tr>
  <tr>
    <td> 1 </td> <td> 1 </td> 
  </table>
<br>

- Explicación: La puerta lógica YES considera una única entrada y una única salida, la salida tiene siempre el mismo valor que la entrada. Se puede recrear con un transistor.

Esta puerta lógica se puede programar de la siguiente manera:

```mermaid
flowchart TD
A(Puerta YES)-->B[Establecer valores lógicos, como 0=falso y 1=verdadero siendo inversos]
B-->F[Establecer una entrada y una salida]
F-->C{¿La entrada es verdadera?}
C-->|sí|D(salida=verdadero)
C-->|no|E(salida=falso)
```

</details>

### puerta NOT

<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
     <tr>
    <td> entrada </td> <td> salida </td> 
  </tr>
  <tr>
    <td> 0 </td> <td> 1 </td> 
  </tr>
  <tr>
    <td> 1 </td> <td> 0 </td> 
</table>
<br>
- Explicación: La puerta lógica NOT considera una única entrada y una única salida, la salida tiene siempre el valor inverso al de la entrada. Esta puerta se utiliza para crear puertas como la NAND o la NOR entre otras, al colocarse en la salida de la puerta que se desea invertir. Se puede recrear con un transistor cuya salida conecta a tierra y un nodo previo al colector por donde sale la información.

Esta puerta lógica se puede programar de la siguiente manera:

```mermaid
flowchart TD
A(Puerta NOT)-->B[Establecer valores lógicos, como 0=falso y 1=verdadero siendo inversos]
B-->F[Establecer una entrada y una salida]
F-->C{¿La entrada es verdadera?}
C-->|sí|D(salida=falso)
C-->|no|E(salida=verdadero)
```

</details>

### puerta AND
<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
     <tr>
    <td> a </td> <td> b </td> <td> salida </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td>
  </tr>
</table>
<br>
  - Explicacion: La puerta AND considera 2 entradas y una única salida en función de las entradas, encendiendose unicamente si ambas entradas están encendidas; en los otros casos la puerta se mantiene apagada. Se puede recrear con 2 transistores conectados en serie.

Esta puerta lógica se puede conectar de la siguiente forma:

```mermaid
flowchart TD
A(Puerta AND)-->B[Establecer valores lógicos, como 0=falso y 1=verdadero siendo inversos]
B-->F[Establecer un número n de entradas]
F-->C{¿Todas las entradas son verdaderas?}
C-->|sí|D(salida=verdadero)
C-->|no|E(salida=falso)
```

</details>

### puerta OR

<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
     <tr>
    <td> a </td> <td> b </td> <td> salida </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td>
  </tr>
</table>
<br>
- Explicación: La puerta OR considera 2 entradas y una única salida en función de las entradas, tal que si alguna de las dos entradas está encendida, la salida lógica también está encendida; el único caso en dónde la salida se encuentra apagada es si ambas entradas se encunetran apagadas. Se puede recrear con 2 transistores conectados en paralelo.

Esta puerta se puede programar de la siguiente forma:

```mermaid
flowchart TD
A(Puerta OR)-->B[Establecer valores lógicos, como 0=falso y 1=verdadero siendo inversos]
B-->F[Establecer un número n de entradas]
F-->C{¿Alguna de las entradas es verdadera?}
C-->|sí|D(salida=verdadero)
C-->|no|E(salida=falso)
```


</details>

### puerta XOR

<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
     <tr>
    <td> a </td> <td> b </td> <td> salida </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td>
  </tr>
</table>
<br>
- Explicación: La puerta XOR considera 2 entradas y una única salida en función de las entradas, tal que si alguna de las dos entradas está encendida, la salida lógica también está encendida; su comportamiento es muy parecido al de la puerta OR, solo que a diferencia de esta, se apaga si ambas entradas se encuentran encendidas. Se puede recrear haciendo un cirucito híbrido entre la puerta AND y la OR(conectando ambos transistores tanto en serie como en paralelo), el circuito OR mantiene sus salidas originales, mientras que el circuito AND tiene la salida conectada a tierra.

Esta puerta se puede programar de la siguiente forma:

```mermaid
flowchart TD
A(Puerta XOR)-->B[Establecer valores lógicos, como 0=falso y 1=verdadero siendo inversos]
B-->F[Establecer un número n de entradas]
F-->C{¿Alguna entrada es verdadera?}
C-->|sí|G{¿Todas las entradas son verdaderas?}
G-->|sí|E
G-->|no|D(salida=verdadero)
C-->|no|E(salida=falso)
```

</details>

## Flip flops

Los flip flops, biestables, o latch, son un circuito multivibrador(un tipo de circuito que puede generar una onda cuadrada), el cual pude almacenar 4 estados estables( estados en los cuales entrega información). Son las unidades básicas de memoria en lógica secuencial.

*pongamosle que sacado de wikipedia, de momento porque el profe no dijo que tocaba que utilizar fuentes*

### rs flip flop (asincrono)

<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
   <tr>
    <td> r </td> <td> s </td> <td> q </td> <td> q` </td>
  </tr>
  <tr>
  <td> 0 </td> <td> 0 </td> <td> sin cambios </td>
  </tr>
  <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td><td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td><td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td> estado invalido </td>
  </tr>
</table>
<br>
- Explicación: Los flip flops RS asíncronos (sin reloj), son aquellos que pueden tener 4 estados, 1¡uno de set(o ajuste), uno de memoria(correspondiente al antrior), uno de reset(reajuste o borrado), el cual invierte las salidas del estado de set, junto con su correspondiente estado de memoria. Y un estado indeterminado( en el cuál no se cumple la condición de inversión entre Q y Q', y puede variar según los componentes empleados para construir el flip flop).
</details>

### rs flip flop (sincrono)

<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
   <tr>
    <td> r </td> <td> s </td> <td> q </td> <td> q` </td>
  </tr>
  <tr>
  <td> 0 </td> <td> 0 </td> <td> sin cambios </td> 
  </tr>
  <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td><td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td><td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td> estado invalido </td>
  </tr>
</table>
<br>
- Explicación: 
</details>

### d flip flop 

<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
   <tr>
    <td> d </td> <td> q </td> <td> q` </td>
  </tr>
  <tr>
  <td> 0 </td> <td> 0 </td> <td> 1 </td> 
  </tr>
  <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td>
  </tr>
</table>
<br>
- Explicación: 
</details>

### jk flip flop

<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
   <tr>
    <td> j </td> <td> k </td>  <td> q </td> <td> q` </td>
  </tr>
  <tr>
  <td> 0 </td> <td> 0 </td> <td> sin cambios </td>
  </tr>
  <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td><td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td><td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td> toggle </td>
  </tr>
</table>
<br>
- Explicación: 
</details>

### t flip flop

<details><summary>explicacion</summary>
  - tabla de verdad:
  <table>
  <tr>
  <td> t </td> <td> q </td> <td> q` </td>
  </tr>
  <tr>
  <td> 0 </td>  <td> sin cambios </td>
  </tr>
  <tr>
  <td> 1 </td> <td> toggle  </td>
  <tr>
</table>
<br>
- Explicación: 
</details>