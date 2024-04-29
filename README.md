

# TC3002B.201_IA

## Data Set

El siguiente data set fue obtenido de Kaggle y contiene imagenes de tomates comprados en un mercado de egipto. Dichos tomates despues fueron clasificados en tomates maduros, no mamduros y tomates rechazados. Esto basandose en los estanderes impuestos por el Departamento de Agricultura de los Estados Unidos (USDA).

Cada clase contiene alrededor de 800 fotos y se eliminaron algunas fotos que estaban mal clasificadas. Las imagenes fueron separadas en carpetas distintas segun sus clases y tambien separadas en carpetas para realizar el entrenamiento de la IA, hacer el validation y para hacer el testing dividiendo las imagenes en 70%, 10%, y 20% respectivamente.

[Link al dataset en Kaggle](https://www.kaggle.com/datasets/nexuswho/tomatofruits)

[Link al dataset en drive](https://drive.google.com/drive/folders/12cqsCAiacAMyk3WtWODylPf7yVJtRhJg?usp=drive_link)

## Preprosesamiento

Para el preprosesamiento de imagenes se normalizaron los datos para que todas tuvieran 224 x 224 pixeles y se hizo un zoom para que la el tomate ocupara la mayor parte la imagen. No se le aplico ningun filtro a la imagen ya que se observo que el modelo aprendia mejor dejando los colores del tomate.

## Modelo

El modelo que utilice fue un CNN comunmente utilizado para problemas de image classification y para mi problema a resolver tuvo un accuracy de 83 por ciento. Viendo los resultados la mayoria de los errores ocurren en la clase "ripe" donde confunde 47 entradas por tomates de la clase reject.

El modelo tiene 3 capas convolutivas que se encargan de extraer las caracterisitcas de las imagenes, maxpooling para que calcule el maximo de sus elementos y pueda extraer la caracteristica mas relevante, capas densas para la clasificación y tambien utilizo dropouts para evitar que solo una neurona del modelo sea la encargada de activarse ante cierto patron y forzar al modelo que aprenda mejor.

[Link al archivo del modelo](https://drive.google.com/file/d/1sAPm0lo1A1zdsf6YKw4vCTa-BFluABLH/view?usp=sharing)

[Link al paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8756165)

## Cambios al modelo original

Originalmente se tenia un modelo que tenia menos capas densas y no hacia el dropout.

<img width="631" alt="Screen Shot 2024-04-28 at 11 38 46 p m" src="https://github.com/Andres7702/TC3002B.201_IA/assets/74391630/e8d763a1-a154-464e-a26a-8d62cc8a6c13">

Este tenia un accuracy de casi 83 por ciento en el entrenamiento y mantenia dicho rendimiento en los casos de prueba

<img width="847" alt="Screen Shot 2024-04-28 at 11 35 42 p m" src="https://github.com/Andres7702/TC3002B.201_IA/assets/74391630/ca425fa4-3d45-4820-bb9d-ec9f06e83a41">

<img width="178" alt="Screen Shot 2024-04-28 at 11 35 51 p m" src="https://github.com/Andres7702/TC3002B.201_IA/assets/74391630/3c8e58b0-66a1-44de-8851-2419956bab36">

Sin embargo se notaba que habia un comportamiento raro en los resultados ya que, aunque podia clasificar a la perfeccion los tomates que no estan maduros, tenia un poco de problemas clasificando los tomates defectuosos y los maduros. 

<img width="207" alt="Screen Shot 2024-04-28 at 11 34 56 p m" src="https://github.com/Andres7702/TC3002B.201_IA/assets/74391630/34c01183-a0f7-4cc2-aede-795d1a34b985">

Segun mi observación esto se debia a que habia fotos de tomates defectuosos que parecian tomates maduros. Esto es porque las fotos eran de tomates vistos de diferentes angulos y aunque de un alguno el tomate claramente estaba defectuoso de otro angulo no y esto confundia mucho al modelo.

Lo que se hizo para mejorar este modelo fue eliminar las fotos de esos tomates que confundian al modelo, hacer data augmentation triplicando los datos con los que entrenaria la IA y agregar mas capas al modelo para hacerlo un poco mas complejo.

## Resultados

Este nuevo modelo tuvo un accuracy del 87 por ciento durante el entrenamiento y casi 85 por ciento en las pruebas. Junto con la grafica del validation podemos ver que el modelo no esta teniendo overfit.

<img width="858" alt="Screen Shot 2024-04-29 at 12 11 06 a m" src="https://github.com/Andres7702/TC3002B.201_IA/assets/74391630/21155aff-c5bc-4c77-bd63-205c7d715eab">


<img width="188" alt="Screen Shot 2024-04-29 at 12 12 36 a m" src="https://github.com/Andres7702/TC3002B.201_IA/assets/74391630/e90fba06-dd8a-4d6a-bc2f-7a3d40a16a3e">

En las pruebas podemos ver que el modelo aun tiene un poco de problema identificando entre los tomates maduros y defectuosos, pero el error es un poco menor.

<img width="177" alt="Screen Shot 2024-04-29 at 12 15 13 a m" src="https://github.com/Andres7702/TC3002B.201_IA/assets/74391630/485621d5-7482-402e-bd9d-86b0bcace0d7">

<img width="1141" alt="Screen Shot 2024-04-29 at 12 15 46 a m" src="https://github.com/Andres7702/TC3002B.201_IA/assets/74391630/6016949a-1e39-4b8a-884e-4b7a645fc557">

Al pasarle una foto mia de un tomate que yo compre podemos ver que lo clasifico de manera correcta.

<img width="459" alt="Screen Shot 2024-04-29 at 12 16 32 a m" src="https://github.com/Andres7702/TC3002B.201_IA/assets/74391630/8daa6212-e594-4a56-bf7d-88b54424fe54">
