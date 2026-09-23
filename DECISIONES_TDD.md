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