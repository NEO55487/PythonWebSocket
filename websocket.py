import asyncio
import websockets
from datetime import datetime



async def handler(websocket):
   oldmessage = ""
   async for message in websocket:
        if message != oldmessage:
            filepath = str("files/"+str(datetime.now().hour)+" "+str(datetime.now().minute)+" "+str(datetime.now().second)+"."+str(datetime.now().microsecond)+"sec.txt")
            f = open(filepath, "x")
            f.write(message)
            f.close()
            oldmessage = message
        else:
            oldmessage = message
        print(str(datetime.now().hour)+" "+str(datetime.now().minute)+" "+str(datetime.now().second)+"."+str(datetime.now().microsecond)+" > "+str(message))
        await websocket.send(message)
        


async def main():
    async with websockets.serve(handler, "", 8080):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())