## Explicación consignas SQL

1) PRIMERA CONSIGNA: Obtener los números de tarjeta que no tengan consumos en el último mes pero que pertenecen a personas que hayan comprado al menos un total de $5000 en el último mes en los rubros (FARMACIA y SUPERMERCADOS) en conjunto. (Si es posible, tener en cuenta el punto EXTRA mencionado previamente).

**La sentencia de creación de tablas e ingesta de datos se encuentra en dbchallenge.db**

**Explicación consigna 1**
Para optimizar el rendimiento de la consulta, se agregó los siguientes indices, pensados para acelerar las operaciones de búsqueda:
- CREATE INDEX idx_compra_nro_fecha ON Compra(nro_tarjeta, fecha_compra);
Este indice es útil para la primera parte de la consulta, donde se utiliza NOT EXIST para verificar si una tarjeta tiene compras recientes. Al estar ordenado por nro_tarjeta y fecha_compra, permite una búsqueda eficiente por este rango de fechas, filtrando únicamente las compras correspondientes a la tarjeta evaluada.

- CREATE INDEX idx_tarjeta_id_titular ON Tarjeta(id_titular);
Este índice permite al motor de base de datos, localizar de manera rápida, todas las tarjetas asociadas a un titular. Esto es fundamental para la segunda parte de la consulta, donde se evaluan los consumos de un mismo titular independientemente de la tarjeta que haya utilizado.

- CREATE INDEX idx_compra_fecha_rubro_monto_nro ON Compra(fecha_compra, rubro, monto, nro_tarjeta);
Este índice está diseñado para optimizar la parte de la consulta que filtra por fecha_compra y rubro y luego realiza una función de agregación por monto. Al priorizar las columnas fecha_compra y rubro, mejora la eficiencia en la selección de registros relevantes para la suma total de consumos.

Al comparar los tiempos de ejecución de la consulta con y sin índices, se observó una mejora significativa en el rendimiento.
Con los índices aplicados, el tiempo de respuesta disminuyó aproximadamente un 50%, lo que demuestra que la estrategia de indexación seleccionada permite optimizar eficazmente el acceso a los datos, reducir la carga de procesamiento y acelerar las operaciones de filtrado y agregación.

La sentencia de consulta es:

```sql
SELECT DISTINCT t.nro_tarjeta 
-- Consulta general que selecciona numeros de tarjeta de la Tabla Tarjeta
FROM Tarjeta t 
WHERE NOT EXISTS( 
    -- Primer subconsulta que verifica la existencia de tarjetas que no tengan consumos en el último mes. Se utiliza NOT EXISTS para filtrar las tarjetas que no tengan consumos en el último mes.
    SELECT 1 -- Select 1 porque solo se verifica la existencia o no de registros.
    FROM Compra c 
    WHERE c.nro_tarjeta = t.nro_tarjeta 
    AND c.fecha_compra >=  '2025-04-01') 
AND EXISTS (
    -- Segunda subconsulta que verifica la existencia de tarjetas que pertenezcan al mismo titular que la primera subconsulta y que tengan consumo en el ultimo mes en farmacia y supermercado sumando un monto mayor o igual a 5000.
    SELECT 1 FROM Compra c2 
    INNER JOIN Tarjeta t2 ON c2.nro_tarjeta= t2.nro_tarjeta 
    WHERE t2.id_titular = t.id_titular -- Condición 1
    AND c2.fecha_compra >= '2025-04-01' -- Condición 2
    AND c2.rubro IN ('Farmacia', 'Supermercado') -- Condición 3
    GROUP BY t2.id_titular -- Condición 4
    HAVING SUM(c2.monto)>=5000 -- Condición 5
    );
```

Para los datos presentes en esta base de datos la salida es: 

nro_tarjeta
1003
1006
1013

El id titular 3 tiene dos tarjetas: 1003 (nro_tarjeta obtenida -->no realizó compra en el último mes) y 1004 (Si realizó compras en el último mes para Farmacia y Supermercado sumando un monto mayor o igual a 5000).

El id titular 4 tiene dos tarjetas: 1006(nro_tarjeta obtenida -->no realizó compra en el último mes) y 1005(Si realizó compras en el último mes para Farmacia y Supermercado sumando un monto mayor o igual a 5000).

El id titular 6 tiene dos tarjetas: 1013(nro_tarjeta obtenida -->no realizó compra en el último mes) y 1008(Si realizó compras en el último mes para Farmacia y Supermercado sumando un monto mayor o igual a 5000).



2) SEGUNDA CONSIGNA:
**Explicación consigna 2**

```sql
    SELECT P1.dni, COUNT(DISTINCT( P2.id ))
    FROM Persona P1 
    JOIN Persona P2 on P1.id_padre = P2.id 
    JOIN Persona P3 on P2.id_padre = P3.id 
    WHERE P3.sexo = 'MASCULINO' 
    GROUP BY P1.dni 
```

- 2.1 Pregunta: ¿Qué se obtiene como resultado? 
Respuesta: Se obtiene como resultado, todos los dni de las personas registradas como P1 y la cantidad de personas registradas como P2 que son padre de P1 y a su vez, las personas registradas como P2 tienen como padre a personas registradas como P3 con sexo MASCULINO.
En este caso, se obtiene el dni de la persona P1 (12345678), el cual tiene 1 (un) padre con con DNI 23456789 registrado como P2, el cual tiene como padre a la persona con DNI 34567890 registrada como P3, con sexo MASCULINO.

salida

```sql
dni	COUNT(DISTINCT( P2.id ))
12345678	1
```


- 2.2 Pregunta: ¿Quienes son P1, P2 y P3? 
Respuesta: P1, P2 y P3 son personas registradas en la base de datos en la tabla Persona, cada una con un id único y se relacionan entre sí mediante el id_padre. Por ejemplo en este caso, P2 es padre de P1 y P3 es padre de P2.

- 2.3 Pregunta: --(EXTRA) Si supiera que la tabla Persona se carga completa todos los días del año, cada día teniendo una foto guardada con un valor distinto dentro de una variable llamada partition_date. Por ej: uno puede consultar todos los ids de la fecha 2021-05-27 o de la fecha que quiera. ¿Cambiaría algo la siguiente query si quisiera obtener el mismo resultado para la última fecha disponible?

Suponiendo que se agrega una columna llamada partition_date, se incorporó a la sentencia de búsqueda una condición adicional para obtener la última fecha registrada en dicha columna dentro de la tabla Persona. Para ello, se utilizó la función MAX(partition_date) para obtener la última fecha disponible, en una subconsulta, cuyo resultado se asigna como valor a la variable partition_date.

```sql
SELECT P1.dni, COUNT(DISTINCT( P2.id ))
FROM Persona P1 
JOIN Persona P2 on P1.id_padre = P2.id 
JOIN Persona P3 on P2.id_padre = P3.id 
WHERE P3.sexo = 'MASCULINO' AND P1.partition_date = (SELECT MAX(partition_date) FROM Persona)
GROUP BY P1.dni 
```