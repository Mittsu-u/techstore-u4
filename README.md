\# TechStore U4 - Actividad 4 (CLN)



Proyecto desarrollado para la gestión de pedidos, aplicación de reglas de negocio mediante el Patrón Specification, máquina de estados y una API REST construida con FastAPI.



\## Estructura del Proyecto

\- `app/`: Contiene el núcleo del dominio (`domain.py`), las reglas de descuento (`specifications.py`) y la interfaz web (`api.py`).

\- `tests/`: Contiene las pruebas automatizadas utilizando `pytest`.

\- `datos/`: Almacena los archivos CSV iniciales (clientes, productos, pedidos, detalle de pedidos y escenarios).



\## Requisitos Previos

\- Python 3.11 o superior instalado en el equipo.



\## Pasos de Instalación y Ejecución



1\. \*\*Crear y activar el entorno virtual:\*\*



bash

python -m venv .venv

.venv\\Scripts\\actívate



2\. \*\*Instalar las dependencias necesarias:\*\*



bash

pip install fastapi uvicorn pytest httpx





3\. \*\*Cargar los datos iniciales:\*\*



bash

python cargar\_csv.py





4\. \*\*Ejecutar el servidor web:\*\*



bash

uvicorn app.api:app --reload





5\. \*\*Acceder a la documentación interactiva (Swagger UI):\*\*

Abre tu navegador y entra a: `http://127.0.0.1:8000/docs`



6\. \*\*Ejecutar las pruebas automatizadas (pytest):\*\*

Detén temporalmente el servidor con `Ctrl + C` y ejecuta:



bash

python -m pytest -q





\## Reglas de Negocio Implementadas

\- \*\*Moneda y Decimales:\*\* Uso estricto de la clase `Decimal` para evitar errores de precisión flotante. Se rechazan montos negativos en `Money`.

\- \*\*Límite de Unidades:\*\* Restricción estricta de un máximo de 20 unidades acumuladas por pedido.

\- \*\*Descuentos:\*\*

\- \*\*10% de descuento:\*\* Se aplica si el cliente es VIP, el total supera los 500 MXN, tiene 4 o más unidades y no cuenta con una promoción activa.

\- \*\*5% de descuento:\*\* Se aplica si el total supera los 5000 MXN y no tiene promoción activa (con prioridad del 10% si se cumplen ambas).

\- \*\*Máquina de Estados:\*\* Los pedidos inician obligatoriamente en estado `DRAFT` y transicionan mediante validaciones estrictas a `CONFIRMED`, `SHIPPED`, `DELIVERED`, `CANCELLED` o `RETURNED`, emitiendo sus respectivos eventos de dominio.



\## Endpoints Principales de la API

\- `GET /orders/{order\_id}`: Consulta los datos y el estado actual de un pedido.

\- `POST /orders/{order\_id}/confirm`: Confirma un pedido en estado DRAFT.

\- `POST /orders/{order\_id}/ship`: Envía un pedido confirmado requiriendo un número de guía.

\- `POST /orders/{order\_id}/cancel`: Cancela un pedido confirmado requiriendo un motivo.

