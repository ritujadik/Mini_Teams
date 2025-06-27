from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import Dict, List

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

html = open("static/index.html").read()

@app.get("/")
async def get():
    return HTMLResponse(content=html)

# ✅ GLOBAL connection manager (shared for all connections)
class ConnectionManager:
    def __init__(self):
        self.teams: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, team: str):
        await websocket.accept()
        if team not in self.teams:
            self.teams[team] = []
        self.teams[team].append(websocket)
        print(f"🔗 New connection in team: {team}")

    def disconnect(self, websocket: WebSocket, team: str):
        if team in self.teams and websocket in self.teams[team]:
            self.teams[team].remove(websocket)
            print(f"❌ Disconnected from team: {team}")

    async def broadcast(self, message: str, team: str):
        print(f"📢 Broadcasting to team {team}: {message}")
        for connection in self.teams.get(team, []):
            await connection.send_text(message)

# ✅ Only one shared manager instance
manager = ConnectionManager()

@app.websocket("/ws/{team}")
async def websocket_endpoint(websocket: WebSocket, team: str):
    await manager.connect(websocket, team)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"💬 Received in team {team}: {data}")
            await manager.broadcast(data, team)
    except WebSocketDisconnect:
        manager.disconnect(websocket, team)
