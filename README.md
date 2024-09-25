# Trabajo de Fin de Grado

## Descripción 
En este trabajo se analizará la viabilidad de los LLM, desde varios puntos de vista, desarro-
llando para ello un prototipo capaz de generar código usando distintos LLM y modelos, y a su
vez, testear el código generado para así, intentar llegar a la conclusión de si estas tecnologías
son viables.
Para conseguirlo, se ha dividido en el trabajo en las siguientes tareas específicas:

  • Evaluar la calidad y eficiencia del código generado mediante tests y compararla según
  metodología y modelo utilizados.
  
  • Evaluar el tiempo empleado en generar el código y compararla según metodología y
  modelo utilizados.
  
  • Analizar el costo de la implementación de un LLM en un entorno grande para estudiar
  su viabilidad.

## Ejecución del Prototipo: 

EN PRIMER LUGAR ES NECESARIO CUBRIR LAS API KEYS EN LA CLASE CONFIG.PY.
 
  
  Usage: python main.py [ALGORITMO] [1|2] [3|4|5]

   ALGORITMO: bubble | merge | counting
    
   1: TEST GENERADOS POR LLM 
 
   2: TEST PRE-GENERADOS
	  
   3: GPT 3.5
    
   4: GPT 4 
    
   5: Mistral
