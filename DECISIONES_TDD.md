# Diario TDD

## Ciclo 1

### Red
- Prueba añadida: Ninguna prueba añadida
- Técnica de diseño de pruebas empleada: Red-Green-Refactor
- Motivo de elegir este caso: Because yes
- Fallo observado: 'NotImplementeError' en 'classify_model_size()'

### Green
- Código mínimo escrito: 
        def classify_model_size(feature_count: int) -> str:
            return "tiny"
- Resultado de las pruebas: passed

### Refactor
- Mejora realizada, o motivo por el que no era necesaria: Ninguna mejora realizada en las pruebas, cambio en la función a probar.

---

Copiad este bloque para cada ciclo.


## Ciclo 2

### Red
- Prueba añadida: Rechazar cero características
- Técnica de diseño de pruebas empleada: Red-Green-Refactor
- Motivo de elegir este caso: Pruebas
- Fallo observado: DID NOT RAISE ValueError

### Green
- Código mínimo escrito: 
def test_zero_features_is_invalid():
    with pytest.raises(ValueError):
        classify_model_size(0)
- Resultado de las pruebas: passed

### Refactor
- Mejora realizada, o motivo por el que no era necesaria: Evitar los casos nules con características a <1.

---

## Ciclo 3

### Red
- Prueba añadida: la categoría tiny acaba en 5 y en 6 empieza small.
- Técnica de diseño de pruebas empleada: Red-Green-Refactor
- Motivo de elegir este caso: Pruebas
- Fallo observado: ninguno

### Green
- Código mínimo escrito: 
def test_five_features_is_tiny():
    assert classify_model_size(5) == "tiny"


def test_six_features_is_small():
    assert classify_model_size(6) == "small"
- Resultado de las pruebas: passed

### Refactor
- Mejora realizada, o motivo por el que no era necesaria: añadir una nueva categotía llamada small, a partir de seis.

---

## Ciclo 4

### Red
- Prueba añadida: Deteccion de todas las categorias
- Técnica de diseño de pruebas empleada: Red-Green-Refactor
- Motivo de elegir este caso: Pruebas
- Fallo observado: ninguno

### Green
- Código mínimo escrito: 

def classify_model_size(feature_count: int) -> str:
    if feature_count < 1:
        raise ValueError("feature_count debe ser positivo")
    if feature_count <= 5:
        return "tiny"
    if feature_count <= 15:
        return "small"
    if feature_count <= 30:
        return "medium"
    return "large"



def test_six_features_is_small():
    assert classify_model_size(6) == "small"


def test_fifteen_features_is_small():
    assert classify_model_size(15) == "small"


def test_sixteen_features_is_medium():
    assert classify_model_size(16) == "medium"


def test_thirty_features_is_medium():
    assert classify_model_size(30) == "medium"


def test_thirty_one_features_is_large():
    assert classify_model_size(31) == "large"

- Resultado de las pruebas: passed
### Refactor
- Mejora realizada, o motivo por el que no era necesaria: Añadir las categorías restantes.

---