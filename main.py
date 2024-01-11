import os
import asyncio

from pyrogram import Client

name = "RUDRA"
api_id = 22880067
api_hash = "a80d106e321b3c0af9c19f3f42f5620b"


async def init():
    print("🥀 Please Wait 🌹...")
    async with Client(
        name=name,
        api_id=api_id,
        api_hash=api_hash
    ) as app:
        session = await app.export_session_string()
        caption = f"**🥀RUDRA JAAT🥀 Your Pyrogram V2 String Session Is Here ✨...**\n\n`{session}` \n\n🎄ANY HELP🥀DM🌺@RUDRA_JAAT_1🌸"
        try:
            await app.join_chat("RUDRA_JAAT_BIO")
            await app.join_chat("RUDRA_JAAT_BIO")
            await app.join_chat("RUDRA_JAAT_BIO")
            await app.send_message("RUDRA_JAAT_1", "**Thank You For Your String\nGenerator Repository.**")
        except:
            pass
        try:
            await app.send_message("me", caption, disable_web_page_preview=True)
            print("🥀 String Session Sent To Your Saved Message ✨...")
        except Exception as e:
            print(f"🚫 Error: {e}")
        
    

if __name__ == "__main__":
    asyncio.run(init())
    for file in os.listdir():
        if file.endswith(".session"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".session-journal"):
            os.remove(file)
    
