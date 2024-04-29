# TC3002B.201_IA

##Data Set

El siguiente data set fue obtenido de Kaggle y contiene imagenes de tomates comprados en un mercado de egipto. Dichos tomates despues fueron clasificados en tomates maduros, no mamduros y tomates rechazados. Esto basandose en los estanderes impuestos por el Departamento de Agricultura de los Estados Unidos (USDA).

Cada clase contiene alrededor de 800 fotos y se eliminaron algunas fotos que estaban mal clasificadas. Las imagenes fueron separadas en carpetas distintas segun sus clases y tambien separadas en carpetas para realizar el entrenamiento de la IA, hacer el validation y para hacer el testing dividiendo las imagenes en 70%, 10%, y 20% respectivamente.

[Link al dataset en Kaggle](https://www.kaggle.com/datasets/nexuswho/tomatofruits)

[Link al dataset en drive](https://drive.google.com/drive/folders/12cqsCAiacAMyk3WtWODylPf7yVJtRhJg?usp=drive_link)

##Preprosesamiento

Para el preprosesamiento de imagenes se normalizaron los datos para que todas tuvieran 224 x 224 pixeles y se hizo un zoom para que la el tomate ocupara la mayor parte la imagen. No se le aplico ningun filtro a la imagen ya que se observo que el modelo aprendia mejor dejando los colores del tomate.

##Modelo

El modelo que utilice fue un CNN comunmente utilizado para problemas de image classification y para mi problema a resolver tuvo un accuracy de 83 por ciento. Viendo los resultados la mayoria de los errores ocurren en la clase "ripe" donde confunde 47 entradas por tomates de la clase reject.

El modelo tiene 3 capas convolutivas que se encargan de extraer las caracterisitcas de las imagenes, maxpooling para que calcule el maximo de sus elementos y pueda extraer la caracteristica mas relevante, capas densas para la clasificación y tambien utilizo dropouts para evitar que solo una neurona del modelo sea la encargada de activarse ante cierto patron y forzar al modelo que aprenda mejor.

[Link al archivo del modelo](https://drive.google.com/file/d/1sAPm0lo1A1zdsf6YKw4vCTa-BFluABLH/view?usp=sharing)

[Link al paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8756165)

##Cambios al modelo original

Originalmente se tenia un modelo que tenia menos capas densas y no hacia el dropout. Dicho modelo tenia
