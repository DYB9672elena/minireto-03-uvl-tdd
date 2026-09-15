# Minirreto 3: pruebas de software con TDD y pair programming

Trabajaréis en parejas para implementar `classify_model_size()` mediante ciclos pequeños **Red-Green-Refactor**.

## Preparación rápida

```bash
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
# .venv\Scripts\activate      # Windows PowerShell
python -m pip install -r requirements-dev.txt
python -m pytest
```

Al comenzar debe fallar alguna prueba porque la función está deliberadamente sin implementar.

## Reglas que hay que descubrir e implementar

- de 1 a 5 características: `tiny`
- de 6 a 15: `small`
- de 16 a 30: `medium`
- 31 o más: `large`
- un número menor que 1 es inválido

No implementéis todas las reglas de una vez. Añadid una prueba pequeña, comprobad que falla, escribid el código mínimo, comprobad que pasa y revisad el diseño. Alternad quién escribe el código en cada ciclo.

Documentad cada ciclo en `DECISIONES_TDD.md`.
