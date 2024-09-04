# proyecto_programacion_actualizado

<div align='center'>
<figure> <img src="https://res.cloudinary.com/dm0p2ljin/image/upload/v1714416338/error-418_dtb3ak.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

# proyecto_programacion

Este proyecto fue realizado para algo, aún no defnimos que, pero para algo, suponemos que para disdfrutar de programar

## diagramas y funcionamientos de las funciones

funcionamiento de las puertas logicas en el proyecto

## puertas logicas

Las puertas lógicas son componentes fundamentales en la electrónica digital. Se utilizan para realizar operaciones lógicas básicas en circuitos digitales y están basadas en el álgebra booleana.

#### puerta YES


<details><summary>explicacion</summary>
  
  ##### tabla de verdad:
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

##### Explicación: 

La puerta lógica YES considera una única entrada y una única salida, la salida tiene siempre el mismo valor que la entrada. Se puede recrear con un transistor.

#### Esta puerta lógica se puede programar de la siguiente manera:

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

#### Explicación: 

La puerta lógica NOT considera una única entrada y una única salida, la salida tiene siempre el valor inverso al de la entrada. Esta puerta se utiliza para crear puertas como la NAND o la NOR entre otras, al colocarse en la salida de la puerta que se desea invertir. Se puede recrear con un transistor cuya salida conecta a tierra y un nodo previo al colector, donde se encuentra la salida lógica.

#### Esta puerta lógica se programo de la siguiente manera:

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
  
  #### tabla de verdad:
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

#### Explicacion:

La puerta AND considera 2 entradas y una única salida en función de las entradas, encendiendose unicamente si ambas entradas están encendidas; en los otros casos la puerta se mantiene apagada. Se puede recrear con 2 transistores conectados en serie.

#### Esta puerta lógica se programo de la siguiente forma:

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
  #### tabla de verdad:
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
  
#### Explicación:

La puerta OR considera 2 entradas y una única salida en función de las entradas, tal que si alguna de las dos entradas está encendida, la salida lógica también está encendida; el único caso en dónde la salida se encuentra apagada es si ambas entradas se encuentran apagadas. Se puede recrear con 2 transistores conectados en paralelo.

#### Esta puerta se programo de la siguiente forma:

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
  
  #### tabla de verdad:
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

#### Explicación: 

La puerta XOR considera 2 entradas y una única salida en función de las entradas, tal que si alguna de las dos entradas está encendida, la salida lógica también está encendida; su comportamiento es muy parecido al de la puerta OR, solo que a diferencia de esta, se apaga si ambas entradas se encuentran encendidas. Se puede recrear haciendo un cirucito híbrido entre la puerta AND y la OR(conectando ambos transistores tanto en serie como en paralelo), el circuito OR mantiene sus salidas originales, mientras que el circuito AND tiene la salida conectada a tierra.

#### Esta puerta se programo de la siguiente forma:

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

<<<<<<< Updated upstream
### puerta NAND

<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> a </td> <td> b </td> <td> salida </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td>
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

#### Explicacion:

La puerta NAND considera 2 entradas y una única salida en función de las entradas; siendo la versión negada de la puerta AND, esta enciende la salida mientras las dos entradas no se encuentren simúltaneamente encendidas. Se puede contruir con los componentes de una puerta AND y una puerta NOT en la salida de estos.

#### Esta puerta se programo de la siguiente forma:

```mermaid
flowchart TD
A(Puerta NAND)-->B[Establecer valores lógicos, como 0=falso y 1=verdadero siendo inversos]
B-->F[Establecer un número n de entradas]
F-->C{¿Todas las entradas son verdaderas?}
C-->|sí|D(salida=falso)
C-->|no|E(salida=verdadero)
```
</details>

### puerta NOR

<details><summary>explicacion</summary>

#### tabla de verdad:

  <table>
     <tr>
    <td> a </td> <td> b </td> <td> salida </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td>
  </tr>
</table>
<br>
  
#### Explicación:

La puerta NOR considera 2 entradas y una única salida en función de las entradas; al tratarse de la negación de la puerta OR, esta se enciende únicamente si ambas entradas están encendidas. Se puede construir como una puerta OR seguida de una puerta NOT.

#### Esta puerta se programo de la siguiente forma:

```mermaid
flowchart TD
A(Puerta NOR)-->B[Establecer valores lógicos, como 0=falso y 1=verdadero siendo inversos]
B-->F[Establecer un número n de entradas]
F-->C{¿Alguna de las entradas es verdadera?}
C-->|sí|D(salida=falso)
C-->|no|E(salida=verdadero)
```


</details>

### puerta XNOR

<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> a </td> <td> b </td> <td> salida </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td>
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

#### Explicación: 

La puerta XNOR considera 2 entradas y una única salida en función de las entradas; al tratarse de la negación de la puerta XOR, esta unicamente enciende la salida si ambas entradas están apagadas, o si ambas entradas se encuentran encendidas. El circuito para construirla se basa en contruir una puerta XOR y colocarle una puerta NOT en la salida

#### Esta puerta se programo de la siguiente forma:

```mermaid
flowchart TD
A(Puerta XNOR)-->B[Establecer valores lógicos, como 0=falso y 1=verdadero siendo inversos]
B-->F[Establecer un número n de entradas]
F-->C{¿Alguna entrada es verdadera?}
C-->|sí|G{¿Todas las entradas son verdaderas?}
G-->|sí|E
G-->|no|D(salida=falso)
C-->|no|E(salida=verdadero)
```

</details>

# implementaciones de las puertas lógicas 
### Comparador de 2 bits
<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> a1 </td> <td> a0 </td> <td> b1 </td> <td> b0 </td> <td> A">"B </td> <td> A"<"B </td> <td> A"="B </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
</table>
<br>
      
#### Explicación:

El comparador de 2 bits es un cirucito digital el cual tiene como fin comparar 2 bits, dando un resultado de 1 en la salida que represente el resultado de esta comparacion (igual, mayor o menor).

#### Esta puerta se programo de la siguiente forma:

```mermaid
flowchart TD
A(comparador de 2 bits)-->B[Establecer los valores logicos, teniendo a 0 como falso y 1 como verdadero]
B-->F[Se plantea la cantidad de 4 entradas, una para uno de los 2 bits de los bits a y b que se compararan]
F-->C{¿que resultado dio la comparacion de los valores de los bits a y b?}
C-->|A es mayor que B|D(la primera salida se volvera 1 y todas las demas se mantendran como 0)
C-->|A es menor que B|E(la segunda salida se volvera 1 y todas las demas se mantendran como 0)
C-->|A es igual que B|G(la tercera salida se volvera 1 y todas las demas se mantendran como 0)
```


</details>

### Multiplicador 4 bits
<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> A1 </td> <td> A0 </td> <td> B1 </td> <td> B0 </td> <td> M3 </td> <td> M2 </td> <td> M1 </td> <td> M0 </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
</table>
<br>
      
#### Explicación:

Un multiplicador de 4 bits es un circuito digital que nos entrega el producto de la multiplicacion de 2 pares de bits (a y b), este producto estar acompuesto por 4 bits

#### Esta puerta se programo de la siguiente forma:

```mermaid
flowchart TD
A(Multiplicador de 4 bits)-->B[Establecer los valores logicos, teniendo a 0 como falso y 1 como verdadero]
B-->F[Se plantea la cantidad de 4 entradas, una para uno de los 2 pares de bits]
F-->P[Se realizar una puerta and en ciertos valores A0 y B0=K1, A1 y B1=K2, A1 y B0=k3]
P-->C{¿que resultado nos dara k1, k2 y k3?}
C-->|k1=1|D(M0 sera 1)
C-->G[Se realizara una puerta XOR=l1 y una puerta AND=l2 ENTRE K1 Y K2 como entrada de ambas]
G-->|l1=1|E(M1=1)
G-->Z[Se realiza ahora otra puerta XOR=z1 y And=z2 entre l2 y k2]
Z-->|Z1=1|M(M2=1)
Z-->|Z2=1|N(M3=1)
```


</details>

### Restador total
<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> A </td> <td> B </td> <td> C </td> <td> Difference </td> <td> Borrow 
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> 
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> 
  </tr>
     <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> 
  </tr>
     <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> 
  </tr>
</table>
<br>
      
#### Explicación:

El restador total es un circuito ditigal que tomando 3 entradas (A: Minuendo, B: Sustraendo, C: Prestamo de entrada) para regresar 2 salidas (Diferencia y prestamo de salida).

#### Este circuito se programo de la siguiente forma:

```mermaid
flowchart TD
A(Restador total)-->B[Establecer los valores logicos, teniendo a 0 como falso y 1 como verdadero]
B-->F[Se plantea la cantidad de 3 entradas para los valores a restar y un valor de prestamo]
F-->P[Se realiza una puerta XOR entre b y c=K1]
F-->C[Se realiza una puerta AND entre el negado de b y c=K2]
P-->D
C-->D[Se realizan 2 puertas logicas, un XOR entre a y k1=x1, un AND entre a y el negado de K1=x2]
D-->|x1=1|G(La salida diferencia sera igual a 1)
D-->Z[Se realiza una puerta or entre x2 y k2=x3]
Z-->|x3=1|M(El prestamo de salida sera igual a 1)
```


</details>

### Semi substractor
<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> A </td> <td> B </td> <td> Diferencia </td> <td> Borrow </td> 
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> 
  </tr>
  <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> 
  </tr>
     <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> 
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> 
  </tr>
</table>
<br>
      
#### Explicación:

El semisubstractor es un circuito digitial que resta 2 entradas (a y b) y nos entrega el resultado de la resta y su prestamo .

#### Este circuito se programo de la siguiente forma:

```mermaid
flowchart TD
A(semi substractor)-->B[Establecer los valores logicos, teniendo a 0 como falso y 1 como verdadero]
B-->F[Se plantea la cantidad de 2 entradas para los valores a restar]
F-->P[Se realiza una puerta XOR entre a y b=K1 y una puerta AND entre el negado de a y b=k2]
P-->|k1=1|C(La diferencia sera igual a 1)
P-->|k2=1|D(El prestamo sera igual a 1)
```


</details>

### semi sumador
<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> a </td> <td> b </td> <td> acarreo </td> <td> salida </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td>
  </tr>

</table>
<br>
      
#### Explicación:

El semisumador es un circuito digital que permite ingresar 2 bits a modo de entrada (a y b) y entrega una salida y un posible acarreo.

#### Esta circuito digital se programo de la siguiente forma:

```mermaid
flowchart TD
A(semi sumador)-->B[Establecer los valores logicos, teniendo a 0 como falso y 1 como verdadero]
B-->F[Se plantea la cantidad de 2 entradas para los valores a sumar]
F-->P[Se realiza una puerta XOR entre a y b=K1 y una puerta AND entre el a y b=k2]
P-->|k1=1|C(La salida sera igual a 1)
P-->|k2=1|D(El acarreo sera igual a 1)
```


</details>

### Sumador total
<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> A </td> <td> B </td> <td> C </td> <td> Acarreo </td> <td> Salida </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> 
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> 
  </tr>
     <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> 
  </tr>
     <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> 
  </tr>
</table>
<br>
      
#### Explicación:

El sumador total es un circuito digital el cual al recibir 3 entradas (a,b y el acarreo) nos devuelve 2 salidas, la suma y su acarreo.

#### Este circuito digital se programo de la siguiente forma:

```mermaid
flowchart TD
A(Sumador total)-->B[Establecer los valores logicos, teniendo a 0 como falso y 1 como verdadero]
B-->F[Se plantea la cantidad de 3 entradas para los valores a sumar y un valor de prestamo]
F-->P[Se realiza una puerta XOR entre a y b=K1]
P-->C[Se realiza una puerta XOR entre k1 y c=l1, una puerta And entre c y k1=l2 y una puerta and entre a y b=l3]
C-->|l1=1|D(la salida es igual a 1)
C-->E[Se aplica una puerta or entre l2 y l3=x1]
E-->|x1=1|Z(el acarreo es igual a 1)
```


</details>

### Contador 4 bits
<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> Q0 </td> <td> Q1 </td> <td> Q2 </td> <td> Q3 </td> <td> Count </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> 
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> 
  </tr>
     <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 2 </td> 
  </tr>
     <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 3 </td> 
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 4 </td> 
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 5 </td> 
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 6 </td> 
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 7 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 8 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 9 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 10 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 11 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 12 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 13 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 14 </td> 
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 15 </td> 
  </tr>
</table>
<br>
      
#### Explicación:

El contador de 4 bits es un circuito digital que nos permite a partir de 4 flip flops hacer una cuenta hasta cierto numero, siendo en este caso 15.

#### Este circuito se programo de la siguiente forma:

```mermaid
flowchart TD
A(Scontador de 4 bits)-->B[Establecer los valores logicos, teniendo a 0 como falso y 1 como verdadero]
B-->F[Se plantea la cantidad de 4 entradas para los valores a resultantes de los flip flops, estos seran valores binarios]
F-->P[Se evalua el resultado binario y se transforma a centesimal,entregando este valor como salida]
P-->|Q3=1|E[Se suma 1 al resultado centesimal]
P-->|Q2=1|G[Se suma 2 al resultado centesimal]
P-->|Q1=1|C[Se suma 4 al resultado centesimal]
P-->|Q0=1|D[Se suma 8 al resultado centesimal]
```


</details>

### Contador 8 bits
<details><summary>explicacion</summary>
  
  #### tabla de verdad:
  <table>
     <tr>
    <td> a1 </td> <td> a0 </td> <td> b1 </td> <td> b0 </td> <td> A">"B </td> <td> A"<"B </td> <td> A"="B </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td>
  </tr>
       <tr>
    <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 1 </td> <td> 0 </td> <td> 0 </td> <td> 1 </td>
  </tr>
</table>
<br>
      
#### Explicación:

La puerta NOR considera 2 entradas y una única salida en función de las entradas; al tratarse de la negación de la puerta OR, esta se enciende únicamente si ambas entradas están encendidas. Se puede construir como una puerta OR seguida de una puerta NOT.

#### Esta puerta se programo de la siguiente forma:

```mermaid
flowchart TD
A(Puerta NOR)-->B[Establecer valores lógicos, como 0=falso y 1=verdadero siendo inversos]
B-->F[Establecer un número n de entradas]
F-->C{¿Alguna de las entradas es verdadera?}
C-->|sí|D(salida=falso)
C-->|no|E(salida=verdadero)
```


</details>

## Flip flops

Los flip flops, biestables, o latch, son un circuito multivibrador(un tipo de circuito que puede generar una onda cuadrada), el cual pude almacenar 4 estados estables( estados en los cuales entrega información). Son las unidades básicas de memoria en lógica secuencial.

**pongamosle que sacado de wikipedia, de momento porque el profe no dijo que tocaba que utilizar fuentes**

<details><summary>RS flip flop (asincrono)</summary>
  
  #### tabla de verdad:
  <table>
   <tr>
    <td> r </td> <td> s </td> <td> q </td> <td> q` </td>
  </tr>
  <tr>
  <td> 0 </td> <td> 0 </td> <td colspan ="2"> sin cambios </td>
  </tr>
  <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td><td> 0 </td>
  </tr>
     <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td><td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td colspan ="2"> estado invalido </td>
  </tr>
</table>
<br>

<<<<<<< Updated upstream
#### Explicación: 
Los flip flops RS asíncronos (sin reloj), son aquellos que pueden tener 4 estados, uno de set(o ajuste), uno de memoria(correspondiente al anterior), uno de reset(reajuste o borrado), el cual invierte las salidas del estado de set, junto con su correspondiente estado de memoria. Y un estado indeterminado( en el cuál no se cumple la condición de inversión entre Q y Q', y puede variar según los componentes empleados para construir el flip flop).

#### Esta puerta se programo de la siguiente forma:

```mermaid
flowchart TD
    A(rs flip flop asincrono) --> B --> b
    B{entrada de datos set / reset}
    b{si entradas = 1 o 0}--> |no se cumple|c[se convierten en enteros las entradas] --> C
    b --> |se cumple|C{se verifica si ambas entradas son 1} --> |se cumple|D[ return XX]
    C --> E[se calcula q y q_inverso]
    E --> F[return q y q_inverso]
```
=======
- Explicación: Los flip flops RS asíncronos (sin reloj), son aquellos que pueden tener 4 estados, uno de set(o ajuste), uno de memoria(correspondiente al anterior), uno de reset(reajuste o borrado), el cual invierte las salidas del estado de set, junto con su correspondiente estado de memoria. Y un estado indeterminado( en el cuál no se cumple la condición de inversión entre Q y Q', y puede variar según los componentes empleados para construir el flip flop).

>>>>>>> Stashed changes
</details>


<details><summary>RS flip flop (sincrono)</summary>
  
  ####  tabla de verdad:
  <table>
   <tr>
    <td> r </td> <td> s </td> <td> q </td> <td> q` </td>
  </tr>
  <tr>
  <td> 0 </td> <td> 0 </td> <td colspan ="2"> sin cambios </td> 
  </tr>
  <tr>
    <td> 0 </td> <td> 1 </td> <td> 1 </td><td> 0 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 0 </td> <td> 0 </td><td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td colspan ="2"> estado invalido </td>
  </tr>
</table>
<br>
  
#### Explicación: 

Los flip flops RS síncronos, a diferencia del asincrono espera a que la entrada del reloj (clock) sea 1 para "activar" las entradas; en el caso de que el clock sea 0 simplemente no pasa nada. Estos flip flops tienen los mismos 4 estado que su version asincrona.

#### Este circuito se programo de la siguiente forma:

  ```mermaid
flowchart TD
    A(sr flip flop sincrono) --> B --> b
    B{entrada de datos set / reset}
    b{si entradas = 1 o 0}--> |no se cumple|c[se convierten en enteros las entradas] --> g
    g{si clock = 1} --> |no se cumple|H[return estado anterior]
    b -->|se cumple|g -->|se cumple| C{se verifica si ambas entradas son 1 y clock es 1} --> |se cumple|D[ return XX]
    C --> E[se calcula q y q_inverso con el clock y las entradas del circuito]
    E --> F[return q y q_inverso]
```
</details>


<details><summary> D flip flop </summary>
  
  #### tabla de verdad:

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

  
#### Explicación:

Simplemente es un RS flip flop con una sola entrada (d), en este flip flop la entrada d va directo al set y para el reset se niega la entrada haciendo que este flip flop solo tenga dos estados, si d = 1, set = 1 y reset = 0, sino d = 0, set = 0 y reset = 1.

#### Este circuito se programo de la siguiente forma:

```mermaid
flowchart TD
    A(d flip flop) --> B[entrada d] --> C[set = d, reset = not d]
    --> D[ se pasan los datos a la funcion rs flip flop sincrono]
```
</details>


<details><summary>JK flip flop</summary>
  
  #### tabla de verdad:

  <table>
   <tr>
    <td> j </td> <td> k </td>  <td> q </td> <td> q` </td>
  </tr>
  <tr>
  <td> 0 </td> <td> 0 </td> <td colspan ="2"> sin cambios </td>
  </tr>
  <tr>
    <td> 0 </td> <td> 1 </td> <td> 0 </td><td> 1 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 0 </td> <td> 1 </td><td> 0 </td>
  </tr>
     <tr>
    <td> 1 </td> <td> 1 </td> <td colspan ="2"> toggle </td>
  </tr>
</table>
<br>

#### Explicación: 

El circuito logico jk flip-flop es una versión modificada de un flip-flop R-S sin estado de salida “inválido”, en el que las antiguas entradas R y S han sido renombradas como J y K. Ahora, las puertas AND de 2 entradas se han reemplazado por puertas AND de 3 entradas que reciben retroalimentación de las salidas Q y no-Q. Esto asegura que las entradas J y K no se activen simultáneamente: J solo tiene efecto cuando el circuito está "reset", y K solo cuando está "set". Si ambas entradas son 1, el flip-flop alternará entre los estados "set" y "reset" con cada pulso de reloj.

#### Este circutio se programo de la siguiente forma:

```mermaid
flowchart TD
    A(jk flip flop) --> B --> b
    B{entrada de datos J / K, estado anterior,clock}
    b{si entradas = 1 o 0}--> |no se cumple|c[se convierten en enteros las entradas] --> g
    g{si clock = 1} --> |no se cumple|H[return estado anterior]
    b -->|se cumple|g -->|se cumple| C{se verifica si ambas entradas son 1 y clock es 1} --> |se cumple|D[return estado anterior ::-1 ]
    C --> E[se calcula q y q_inverso con el clock ylas entradas del circuito y el estado anterior en el circuito]
    E --> F[return q y q_inverso]
```
</details>


<details><summary>T flip flop</summary>
  
  #### tabla de verdad:
<table>
   <tr>
    <td> t </td>   <td> q </td> <td> q` </td>
  </tr>
  <tr>
  <td> 0 </td>  <td colspan ="2"> sin cambios </td>
  </tr>
     <tr>
    <td> 1 </td>  <td colspan ="2"> toggle </td>
  </tr>
</table>
<br>

#### Explicación: 

El comportamiento de un flip-flop tipo T es equivalente al de un flip-flop tipo J-K con sus entradas J y K unidas. De este Modo, si la entrada T presenta un nivel bajo ‘0’ el dispositivo está en su modo de memoria, y si a la entrada T se encuentra a nivel alto ‘1’ el dispositivo cambia de estado(toggle).

#### Este circuito se programo de la siguiente forma:

```mermaid
flowchart TD
    A(t flip flop) --> B --> b
    B[entrada de datos J / K, estado anterior,clock]
    b[J = t,K = t ]--> c[se pasan J,K como entradas a la funcion jk flip flop]
```
</details>
