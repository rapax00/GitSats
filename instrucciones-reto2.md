# Bienvenido al reto 2 (ES)
Para el Reto 2 de gitSats, deberás utilizar git bisect para encontrar un bug que impide que la función special_sum funcione correctamente. Al corregir este bug, la función revelará dos palabras clave al ejecutarse. Sigue estos pasos:

## Instrucciones

- Inicio: Usa git bisect start para comenzar la búsqueda binaria entre los commits.
- Identificar Commits Bueno y Malo: Marca el commit actual como malo (git bisect bad) si la función no funciona correctamente, y luego marca un commit anterior donde la función funcionaba bien (git bisect good [commitID]).
- Testear y Marcar: En cada paso, ejecuta la función. Usa git bisect good o git bisect bad según el resultado, hasta encontrar el commit que introdujo el bug.
- Revelar Palabras: Una vez corregido el error y la función se ejecute correctamente, te revelará las palabras buscadas.
- Finalizar: Usa git bisect reset para terminar el bisect y volver al estado inicial del repositorio.

- Este reto te enseña a usar git bisect para depurar eficientemente, mientras avanzas en la búsqueda del Secreto Satoshi.


## Próximo paso:

Una vez completado este reto, dirígete a la rama feature/reto-3 para continuar tu búsqueda.
Recuerda, la paciencia y la observación son claves en este viaje. ¡Buena suerte!

# Welcome to Challenge 2 (EN)
For gitSats Challenge 2, you will use git bisect to find a bug that prevents the special_sum function from working properly. By fixing this bug, the function will reveal two keywords when executed. Follow these steps:

## Instructions

- Start: Use git bisect start to begin the binary search through the commits.
- Identify Good and Bad Commits: Mark the current commit as bad (git bisect bad) if the feature is not working properly, and then mark a previous commit where the feature worked fine (git bisect good [commitID]).
- Test and Mark: At each step, run the function. Use git bisect good or git bisect bad depending on the result, until you find the commit that introduced the bug.
- Reveal Words: Once the bug is fixed and the function runs correctly, it will reveal the searched words to you.
- Finish: Use git bisect reset to end the bisect and return to the initial state of the repository.

- This challenge teaches you how to use git bisect to debug efficiently, as you move forward in the search for the Satoshi Secret.


## Next step:

Once you have completed this challenge, head to the feature/reto-3 branch to continue your search.
Remember, patience and observation are key on this journey - good luck!