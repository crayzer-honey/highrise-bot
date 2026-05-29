from highrise import BaseBot, Position
import asyncio

class Bot(BaseBot):

    async def on_start(self, session_metadata):
        print("Bot connecté")
        asyncio.create_task(self.gold_loop())

    async def on_user_join(self, user, position):
        await self.highrise.chat(f"Bienvenue {user.username} 👋")

    async def on_chat(self, user, message):
        msg = message.lower()

        if msg == "come":
            self.follow = user.id

        elif msg == "stop":
            self.follow = None

        elif msg == "walk_to":
            pos = await self.highrise.get_user_position(user.id)
            await self.highrise.walk_to(pos)

        elif msg == "turn":
            await self.highrise.walk_to(Position(5, 0, 5))

    async def on_user_move(self, user, position):
        if hasattr(self, "follow") and self.follow == user.id:
            await self.highrise.walk_to(position)

    async def gold_loop(self):
        while True:
            users = (await self.highrise.get_room_users()).content
            for user, _ in users:
                try:
                    await self.highrise.tip_user(user.id, 1)
                except:
                    pass

            await asyncio.sleep(1200)
