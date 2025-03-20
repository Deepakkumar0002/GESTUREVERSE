import asyncio
import websockets

# Define your WebSocket handler
async def handler(websocket, path):
    async for message in websocket:
        await websocket.send(f"Received: {message}")

# Main function to start the WebSocket server
async def main():
    async with websockets.serve(handler, "0.0.0.0", 10000):  # Change port if needed
        await asyncio.Future()  # Keeps the server running

# Run the server
if __name__ == "__main__":
    asyncio.run(main())

