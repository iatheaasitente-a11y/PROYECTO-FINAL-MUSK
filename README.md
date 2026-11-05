# PROYECTO-FINAL-MUSK - Analisis avanzado de clientes y ventas

Script en Python que lee clientes (data/clients.json) y ventas (data/sales.csv), los cruza, calcula 10 metricas y genera un reporte final en final_report.json.

## Requisitos del ejercicio y donde se cumplen
| Requisito | Donde |
|---|---|
| Lectura de JSON y CSV | load_clients y load_sales (src/analyze.py) |
| Bucles | calc_client_stats, calc_top_client_by_country |
| Condicionales | promedio_ventas_client, calc_high_spending_clients |
| Programacion funcional | src/functional_utils.py (filter, map, lambda) y reduce en sum_amounts |
| Pandas | metricas 7 y 10 (groupby) y cruce ventas-clientes |
| POO | Client, Sale (con to_dict), ClientCollection, SalesCollection |
| JSON final | save_report genera final_report.json |
| Tests | carpeta tests/ con pytest |
| GitHub Actions | .github/workflows/ci.yml |

## Las 10 metricas
| # | Metrica | Tecnica |
|---|---|---|
| 1 | Total de clientes | len |
| 2 | Total de ventas | len |
| 3 | Total gastado por cliente | filter y reduce |
| 4 | Numero de ventas por cliente | SalesCollection (POO) |
| 5 | Promedio de gasto por cliente | condicional |
| 6 | Mejor cliente por pais | ClientCollection y bucle |
| 7 | Ventas por categoria | pandas groupby |
| 8 | Cliente con mas compras en Electronics | filter y max |
| 9 | Clientes de alto gasto (mas de 500) y su numero | bucle y condicional |
| 10 | Ventas por mes y acumuladas | pandas to_period y groupby |

## Estructura
- src/: codigo fuente
- data/: clients.json y sales.csv
- tests/: tests automaticos
- final_report.json: reporte generado

## Instalacion (Windows)
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt

## Uso
Desde la raiz del proyecto:

    python -m src.analyze

## Tests
    python -m pytest -q

## Validacion automatica
Cada push ejecuta GitHub Actions y lanza los tests.