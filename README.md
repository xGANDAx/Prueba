# Python test

[![Python](https://img.shields.io/badge/Python-3-5C4EE5.svg)](https://yaml.org)

El Objetivo del ejercicio es consumir una API de chistes y escribir la respuesta en archivo

## Criterios de acceptación

1. Ajustar (Tiene Errores de syntaxis) 

    ```
        python3 test-python.py 
    ```

2. Crear un segudo archivo llamado `joker.txt` y en el escribir la descripcion del chiste 

   - _Entradas:_  python3 test-python.py  
   - _Salida:_ joker.txt
     ```
        Chuck Norris single-handily won a game of football by completing a 97 yard touchdown pass to himself. It was the only offensive play of the game.
     ```

3. Adicionar como dependecia `colorama` y utilizarla para imprimir el json reotornado con el color  `azul`

   - _Entradas:_ python3 test-python.py  
   - _Salida:_ azul

     ```json
     {'categories': [], 'created_at': '2016-05-01 10:51:41.584544', 'icon_url': 'https://assets.chucknorris.host/img/avatar/chuck-norris.png', 'id': 'nzcohv1-QE2-FKcVw-1q0Q', 'updated_at': '2016-05-01 10:51:41.584544', 'url': 'https://api.chucknorris.io/jokes/nzcohv1-QE2-FKcVw-1q0Q', 'value': 'Chuck Norris single-handily won a game of football by completing a 97 yard touchdown pass to himself. It was the only offensive play of the game.'}

     ```
