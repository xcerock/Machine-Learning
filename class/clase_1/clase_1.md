## Aprendizaje supervizado

Es cuando tenemos un "algo" en donde tengo una entrada y una salida

| in (X)  | out / label (Y) |
| ------- | --------------- |
| dataset | muestra         |


¿Cuales son los mejores parametros tal que se minimese el error?

En un regresión lineal, se llega al minimo global del forma global

En Aprendizaje supervizado tenemos 2 grandes areas:

- Regresión

- clasificación

En regresión las etiquetas son valores continuos

Mientras en clasificación son valores discretos

## Aprendizaje no supervizado

No se tienen etiquetas, solo entradas X. Si solo tengo entradas puedo analizar que tan parecidas son y determinar como hacer set (Clustering)

Un uso de eso es LLM (Como ChatGPT), en donde la entrada son millones de documentos

- Para entrenar algo así, se usan un biding; se oculta una palabra y se intenta que el modelo determine que palabra es esa que se le está ocultando, de esta manera se puede tener una metrica de perdida, con una entropia cruzada

- Otra forma de entrenar un LLM es hacer predicción de cual será la siguiente palabra de una frase

En este método tambien es donde se trabaja reducción de dimesionalidad:

- PCA
- t-SNE
