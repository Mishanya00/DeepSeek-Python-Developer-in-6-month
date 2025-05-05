import time
import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse


app = FastAPI()


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            const clientId = Date.now();
            document.querySelector("#ws-id").textContent = clientId;
            const ws = new WebSocket(`ws://localhost:8000/ws/${clientId}`);

            ws.onopen = function(event) {
                console.log("WebSocket connection established");
                addMessage("System: Connected to chat.");
            };

            ws.onmessage = function(event) {
                // Check for ping message
                if (event.data === "__ping__") {
                    // Send pong back immediately
                    ws.send("__pong__");
                    console.log("Received ping, sent pong."); // Optional logging
                    return; // Don't display ping as a message
                }
                // Otherwise, display the message
                addMessage(event.data);
            };

            ws.onclose = function(event) {
                console.log("WebSocket connection closed:", event);
                addMessage(`System: Connection closed. Code=${event.code}, Reason=${event.reason || 'N/A'}`);
            };

            ws.onerror = function(event) {
                console.error("WebSocket error:", event);
                addMessage("System: WebSocket error occurred.");
            };

            function sendMessage(event) {
                event.preventDefault();
                const input = document.getElementById("messageText");
                const message = input.value;
                if (message.trim()) { // Only send non-empty messages
                    ws.send(message);
                    input.value = '';
                }
            }

            function addMessage(messageText) {
                const messages = document.getElementById('messages');
                const message = document.createElement('li');
                const content = document.createTextNode(messageText);
                message.appendChild(content);
                messages.appendChild(message);
                // Optional: Scroll to the bottom
                messages.scrollTop = messages.scrollHeight;
            }
        </script>
    </body>
</html>
"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


PING_INTERVAL = 20
PONG_TIMEOUT = 45


async def ping_sender(websocket: WebSocket):
    while True:
        try:
            await asyncio.sleep(PING_INTERVAL)
            await websocket.send_text("__ping__")
            print(f"Sent ping to {websocket.client}") # Optional debug logging
        except (WebSocketDisconnect):
            print(f"Ping sender: Connection closed for {websocket.client}. Stopping.")
            break
        except asyncio.CancelledError:
            print(f"Ping sender: Task cancelled for {websocket.client}. Stopping.")
            break
        except Exception as e:
            print(f"Error sending ping to {websocket.client}: {e}")
            break


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)

    ping_task = asyncio.create_task(ping_sender(websocket))

    try:
        while True:
            try:
                # Wait for a message from the client with a timeout
                # This timeout ensures we detect unresponsive clients
                data = await asyncio.wait_for(
                    websocket.receive_text(),
                    timeout=PONG_TIMEOUT
                )

                if data == "__pong__":
                    print(f'received pong from {websocket.client}')

                await manager.send_personal_message(f"You wrote: {data}", websocket)
                await manager.broadcast(f"Client #{client_id} says: {data}")
            
            except asyncio.TimeoutError:
                manager.disconnect(websocket)
                await manager.broadcast(f"Client #{client_id} left the chat")
    
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
    finally:
        ping_task.cancel()
        try:
            await asyncio.wait_for(ping_task, timeout=1)
        except asyncio.TimeoutError:
             print(f"Ping task for {client_id} did not cancel cleanly.")
        except asyncio.CancelledError:
             pass # good
        