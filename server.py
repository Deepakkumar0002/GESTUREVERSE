import asyncio
import websockets

# Store connected players
connected_players = set()

async def handler(websocket, path):
    # Add new player to the connected set
    connected_players.add(websocket)
    try:
        async for message in websocket:
            # Broadcast received message to all players
            for player in connected_players:
                if player != websocket:
                    await player.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Remove disconnected player
        connected_players.remove(websocket)

# Start WebSocket server
start_server = websockets.serve(handler, "localhost", 8765)

print("WebSocket server started on ws://localhost:8765")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
