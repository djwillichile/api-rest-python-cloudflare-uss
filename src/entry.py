from urllib.parse import urlparse

from workers import Response, WorkerEntrypoint


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        ruta = urlparse(request.url).path

        if request.method != "GET":
            return Response.json({"error": "Método no permitido"}, status=405,
                                 headers={"Allow": "GET"})
        if ruta == "/":
            return Response.json({"mensaje": "Hola, mundo", "estado": "online",
                                  "version": "1.0.0"})
        if ruta == "/estado":
            return Response.json({"estado": "online", "version": "1.0.0"})
        if ruta == "/productos":
            return Response.json({"productos": [
                {"id": 1, "nombre": "Cuaderno", "precio": 2500},
                {"id": 2, "nombre": "Lápiz", "precio": 500},
            ]})
        return Response.json({"error": "Ruta no encontrada"}, status=404)
