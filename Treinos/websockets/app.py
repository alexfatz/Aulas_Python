from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from asyncio import Lock


class ConnectionsManager:
    def __init__(self):
        self.connections: set[WebSocket] = set()
        self.lock = Lock()


    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        async with self.lock:
            self.connections.add(websocket)


    async def disconnect(self, websocket: WebSocket):
        async with self.lock:
            if websocket in self.connections:
                self.connections.discard(websocket)


    async def broadcast(self, data: dict):
        async with self.lock:
            connections: list[WebSocket] = list(self.connections)

        connections_problematicas = []

        for connection in connections:
            try:
                await connection.send_json(data)
            except:
                connections_problematicas.append(connection)

        for connection in connections_problematicas:
            await app.state.connections_manager.disconnect(connection)


templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.state.connections_manager = ConnectionsManager()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await app.state.connections_manager.connect(websocket)
        while True:
            data = await websocket.receive_json()
            await app.state.connections_manager.broadcast(data)

    except WebSocketDisconnect:
        await app.state.connections_manager.disconnect(websocket)
    finally:
        await app.state.connections_manager.disconnect(websocket)
