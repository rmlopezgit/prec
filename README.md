# Perfil de riesgo establecimientos de crédito

Repositorio git para el proyecto "Perfil de riesgo de los establecimientos de crédito" del grupo 2 despliegue de soluciones analiticas de la Maestría en inteligencia analítica de datos para la toma de decisiones MIAD Universidad de los Andes Colombia.

## Resumen: 

En estos tiempos de incertidumbre económica, y ante el cierre de entidades financieras de alto renombre mundial, se hace necesario, tanto para entidades públicas como para grandes inversionistas privados, encontrar metodologías de alta eficiencia y fácil ejecución en poco tiempo para  poder determinar el perfil de riesgo de las entidades bancarias de Colombia. En el siguiente proyecto, sugerimos un acercamiento mediante técnicas de aprendizaje no supervisado, específicamente de clustering, y de reducción de dimensionalidad, que permitan generar perfiles de riesgo con el fin de tomar las mejores decisiones de inversión y de salvamento según sea necesario, y que tengan la capacidad de adaptarse fácilmente al fluctuante escenario económico de nuestros tiempos.

## Introduccion: 

La supervisión bancaria, como señalan Hotori, et. al. (2022), corresponde a una necesidad del sistema financiero actual, como una respuesta al control que requieren las entidades públicas ante fenómenos como la información asimétrica que se posee sobre el mercado entre entidades financieras públicas y privadas, la constante fluctuación de externalidades y los riesgos de la economía moderna.  Incluso, entidades de alto reconocimiento a nivel mundial como Credit Suisse (Portafolio, 2022)  o Silicon Valley Bank (SVB) (Ferguson, 2023), que recientemente tuvieron que declararse en bancarrota debido a la falta de supervisión en tiempo real, hacen prioritario realizar la pregunta: ¿Cúal es una posible metodología que permita realizar una categorización y análisis del riesgo de las distintas entidades financieras de un país, en este caso particular de Colombia?

Este tipo de análisis resulta de interés para dos grupos:

- Entidades de supervisión bancaria en Colombia: Si bien, como señalan Estrada y Gutierrez (2009), la labor de supervisión bancaria en Colombia por parte del Banco de la República, así como de la Superintendencia Financiera de Colombia (SFC), ha resultado satisfactoria en el control de crisis y monitoreo periódico de las entidades bancarias, resulta necesario establecer criterios de medición que permitan tomar decisiones ante cambios súbitos y que sean de construcción e implementación más acelerada.

- Inversionistas extranjeros: Autores como Kandrac y Schlusche (2017) evidencian que, en escenarios donde la supervisión bancaria es mucho menor, era mayor la incidencia de pérdidas significativas en la inversión. Si bien la volatilidad del mercado extranjero y el score de riesgo de Colombia ha ido en aumento, un sistema eficaz de supervisión bancaria brinda confianza a los inversionistas.

Como es tradicional en los perfiles de riesgo, no se cuenta con categorías o definiciones fijas de los perfiles de riesgo, por lo que modelos de aprendizaje supervisado no se consideran como una respuesta al problema propuesto. Para este caso particular se considerará como un problema de clasificación no supervisada, por lo que se revisarán a detalle algoritmos de clustering. También, de ser necesario, se revisará la necesidad de reducción de dimensionalidad.

## Antecedentes bibliográficos

A nivel internacional, la revisión realizada por Guerra y Castelli (2021) brinda el mayor acercamiento al uso de machine learning para la supervisión bancaria. Llama la atención observar el volumen de trabajos que utilizan un enfoque supervisado para la predicción de los perfiles de riesgo (De una revisión de 41 papers publicados entre el 2000 y el 2021, únicamente 1 hace uso de técnicas de aprendizaje no supervisado)

Entre las técnicas más utilizadas se encuentra el uso de bagging y boosting, así como redes neuronales, para la determinación de perfiles de riesgo. El estudio más referenciado por bibliografía académica (y también el único que emplea técnicas de aprendizaje no supervisadio), dentro de los revisados por Guerra y Castelli (2021), es el realizado por Boyacioglu et. al (2009), en el cual revisa diferentes metodologías de machine learning que permitieran identificar bancos que estuvieran en riesgo de una posible bancarrota. Dentro de las metodologías analizadas se utilizó el algoritmo de k-medias, sin embargo no obtuvo un desempeño superior frente a metodologías más robustas. En este caso, los métodos propuestos no permiten solucionar el problema ya que no se ha llegado a la bancarrota (A diferencia de estos estudios que tomaron información de bancos que ya habían quebrado anteriormente), y no se tiene una única variable de respuesta, por lo que el aprendizaje no supervisado sigue siendo la metodología recomendada.

Dentro de los estudios realizados con aprendizaje no supervisado más relevantes para resolver la pregunta de interés, se encuentra el estudio de Lee, Booth y Alam (2005), en el cual compara redes neuronales artificiales tanto supervisadas como no supervisadas (denominadas redes Kohonen) para la predicción de bancarrota de entidades financieras en Corea. De dicho estudio es posible concluir que, si bien las redes no supervisadas no poseen el mismo poder predictivo que aquellas que utilizan aprendizaje supervisado, permiten realizar predicciones en un tiempo más cercano, además que permite evaluar casi en tiempo real tanto la evolución de la entidad como de sus alrededores para tomar decisiones.

Finalmente, la revisión de literatura colombiana sobre el tema suele estar centrada en perfiles de riesgo para los clientes del banco (Como el realizado por Giraldo y Marín (2021) acerca de machine learning para riesgo de crédito), pero no para clasificar los bancos en niveles de riesgo, por lo que esta investigación supone un pivote académico para incentivar la profundización en el uso de machine learning para perfilar el riesgo de bancos colombianos.

## Propuesta metodológica

En Colombia existe la Red de Seguridad del Sistema Financiero, conformada por entidades como la Superintendencia Financiera, el Banco de la República, Ministerio de Hacienda y Fogafín, la cual se encarga de monitorear al sistema financiero, dentro de éste a los bancos, con el fin de identificar posibles riesgos y vulnerabilidades que podrían tener algún efecto sobre la estabilidad financiera de la economía colombiana. Sobre todo, en una coyuntura económica como la actual, de desaceleración económica, condiciones financieras más restrictivas y una inflación elevada, el monitoreo de indicadores financieros de las entidades por parte de la Red cobra mayor relevancia. Así mismo después de la crisis financiera del 2008, los agentes reguladores a nivel global se han interesado en desarrollar herramientas que les permitan monitorear los riesgos financieros. En este documento proponemos calcular una medida de riesgo para los bancos colombianos que recoja el comportamiento de los indicadores mencionados en la sección anterior y que contribuya a la labor de supervisión que realiza la Red. Para ello se utilizará la metodología de componentes principales que permite la reducción de la dimensionalidad de los datos y el indicador sería el primer componente principal el cual explica la mayor varianza de los datos. Así mismo, esta metodología permite conocer el peso que tiene cada variable sobre el componente principal a partir de los loadings.
 
Por otro lado, se realizará un análisis de clústeres para identificar aquellos bancos que tienen perfiles de riesgo similares para que la Red supervise en mayor medida aquellos clústeres con mayor riesgo evitando posibles futuras quiebras de bancos o contagio sobre el resto del sistema financiero. Existen distintos métodos de clustering como k-medias, k-medoides o clustering jerárquico. Una de las ventajas de este último frente a los primeros es que no se necesita definir a priori el número de clústeres a calcular y es la metodología que se usa en la literatura revisada. Sin embargo, en este documento se probarán distintos métodos y a partir de los resultados se seleccionará el que genere los mejores resultados.

## Solución planteada

Se creará una herramienta de visualización de tendencias históricas para dichos indicadores de riesgo, con la posibilidad de que el usuario final pueda revisar por entidad la evolución de dicho indicador. También en dicha herramienta se podrá observar las distintas agrupaciones de entidades financieras por perfil de riesgo.

## Integrantes: 
- Laura Becerra
- Cesar Porras
- Diego Monroy
- Robert Lopez

Octubre 2023.
