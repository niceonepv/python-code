import asyncio
import telegram


async def main():
    bot = telegram.Bot("5438183271:AAGTl5o3J0AfdSZNh_O8ceAHRF3IZ1sff_c")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
