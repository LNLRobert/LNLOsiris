import asyncio
import websockets
from dashboard_utils import cache_printer_data

async def listen_to_printer(printer):
    uri = f"ws://{printer['ip']}:{printer['port']}/websocket"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            process_websocket_message(printer['name'], message)

def process_websocket_message(printer_name, message):
    # Parse and cache the message (e.g., update status, last update time)
    cache_printer_data(printer_name, message)

async def main():
    tasks = [listen_to_printer(printer) for printer in printers]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())