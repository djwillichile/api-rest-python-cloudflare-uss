# API REST con Python y Cloudflare Workers

Ejemplo educativo para Taller de Programación II, Universidad San Sebastián. Expone datos ficticios en formato JSON sin base de datos ni frameworks web.

## Objetivos

Practicar solicitudes GET, respuestas HTTP y JSON; ejecutar un Worker localmente y publicarlo en Cloudflare.

## Tecnologías y arquitectura

Python, Cloudflare Workers, Pywrangler, uv, Node.js y Git. El navegador envía una solicitud HTTPS a Cloudflare; el Worker ejecuta Python y devuelve una respuesta JSON. GitHub almacena el código, pero no ejecuta esta API.

## Archivos

- `src/entry.py`: clase que recibe y responde solicitudes.
- `wrangler.toml`: nombre, archivo principal y compatibilidad del Worker.
- `pyproject.toml`: requisitos Python y herramientas de desarrollo.
- `uv.lock`: versiones resueltas, cuando se genera durante la instalación.
- `.gitignore`: excluye entornos, cachés y archivos que pueden contener secretos.

## Requisitos y ejecución local

Instalar Python 3.13 o posterior, Node.js, uv y Git. En la terminal de la carpeta del proyecto:

```powershell
uv --version
node --version
uv sync
uv run pywrangler dev
```

Abrir la dirección local indicada por la terminal, normalmente `http://localhost:8787/`. Detener con Ctrl+C.

## Despliegue

Iniciar sesión en una cuenta Cloudflare y habilitar Workers Free y un subdominio workers.dev. A continuación ejecutar:

```powershell
uv run pywrangler login
uv run pywrangler deploy
```

Seguir las indicaciones de autenticación y abrir la dirección HTTPS que muestra el despliegue. URL pública comprobada: https://api-rest-python-estudiantes.djwillichile.workers.dev/

## Rutas

| Método | Ruta | Respuesta |
| --- | --- | --- |
| GET | `/` | Bienvenida, estado y versión |
| GET | `/estado` | Estado y versión |
| GET | `/productos` | Productos ficticios |
| GET | Otra ruta | Error 404 |

Ejemplo de `GET /`:

```json
{"mensaje":"Hola, mundo","estado":"online","version":"1.0.0"}
```

Los métodos distintos de GET reciben 405. Los precios son valores ficticios.

## Autoría

Material docente para la asignatura Taller de Programación II. Docente: Guillermo Fuentes Jaque.
