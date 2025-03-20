import asyncio
import websockets

async def server(websocket, path):
    await websocket.send("Hello, client!")

start_server = websockets.serve(server, "0.0.0.0", 5000)  # Ensure it binds to 5000

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
