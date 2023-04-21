# Regresión

Es una relación entre variables dependientes e independientes

Este tiene 2 varibales:

- Variables dependientes (Respuesta)
- Varaiables independites (Predictivas)

Tipos de variable:

- Lineal
- Polinomia (Esto realmente es un caso especial): Esto hace refencia a un polinomio sobre las indepentientes, pero es lineal respecto a los parametros del modelo $\theta_1 x_1 + \theta_2 x_2²$
- Logistica: Es una represión en el rango entre 0 y 1

---

# Lineal

Una función generica sería:

$$
y = f(x_1, x_2, ... x_n) + \epsilon
$$

Donde:

- $y$ es la variables dependiente
- $x_1, x_2, ... x_n$ la variables independientes
- $epsilon$ el error
- $f()$ es la función de hipotesis

Esta función de hipotesis es esa función que se considera que mejor predice el valor de $y$; veamos esta función de hipotesis:

$$
h_{\theta}(\bar{x}) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + ... \theta_n x_n = \sum_{i=0}^{n}{\theta_i X_i} = \bar{\theta} \bar{X}
$$

$\theta$ son los parametros de mi modelo

> El objetivo fundamental en Machine Learning es buscar los mejores parametros que me permitan minimizar mi función de perdida; es decir, el error entre el modelo y los datos de mi experimento (Data set)

## Función de consto o de perdida

Estas son utiles para determinar que tanto falla un modelo; si mejorando entre este tipo de funciones podemos llegar a una bastante útil

### Diferencia entre los puntos

$\sum{\hat{y}-y} = -2$

## MAE

$\frac{1}{N} \sum{|\hat{y}-y|} = \frac{4}{3}$

Este es MAE (Min Absolute Error); MAE NO es diferenciable, en pocos contextos es util, realmente es diferenciación es util, sobre todo como metrica para analizar los modelos en si mismos

MAE tambien se puede expresar como:

$$
\frac{1}{N} \sum_{i}^{N}{|\hat{y}_i - y_i|} = \frac{1}{N} \sum_{i}^{N}{|f(x_i) - y_i|}
$$

Donde el dataset vendría dado por: $X_i Y_i$

### MSE (Mean Square Error)

> Esta función no me permite tener la misma unidad dimensional; para eso se puede usar el RMSE (Root Mean Square Error); esta función si me permite tener la misma unidad dimensional

MSE se expresa con la siguiente función

$$
T(\theta) = \frac{1}{2N} \sum^{N}_{i=1}{(h_{\theta}(x_i) - y_i)^{2}}
$$

$H_{\theta}(x) = X\theta$

Supongamos que:

$(a - b)^2 = (a - b)^{T} (a - b)$

Podemos replantear $J(\theta)$ como:

$$
J(\theta) = \frac{1}{2N} (X\theta - y)^{T} (X\theta - y)
$$

Donde:

- $(X\theta - y)^{T}$ es $1*N$

- $(X\theta - y)$ es $N*1$

$\nabla J(\theta) = \frac{\partial J(\theta)}{\partial \theta} = 0$

$$
J(\theta) = \frac{1}{2N} (X\theta - y)^{T} (X\theta - y)
$$

Por leyes de los vectores $(A*B)^T = B^T*A^T$

$$
J(\theta) = \frac{1}{2N} (\theta^TX^T - y^T) (X\theta - y)
$$

Podemos hacer distribución

$$
J(\theta) = \frac{1}{2N} (\theta^TX^TX\theta - \theta^TX^Ty - y^TX\theta + y^Ty) (X\theta - y)
$$

Donde, $\theta^TX^Ty = (\theta^TX^Ty)^T = y^TX\theta$ por lo que ahora 2 terminos son iguales

> Recordar que $a_{1x1} = a^T_{1x1} = a$ 

$$
J(\theta) = \frac{1}{2N} (\theta^TX^TX\theta - 2y^TX\theta + y^Ty) (X\theta - y)
$$
