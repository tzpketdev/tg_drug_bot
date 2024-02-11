import link
import metrics
from aiogram import Bot, Dispatcher
import asyncio
import model_metrics
import drop_dist
import start
from config_reader import config
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


async def main() -> object:
    dp.include_routers(
        model_metrics.router,
        drop_dist.image_rout,
        metrics.metrics_router,
        start.start_router,
        link.link_router
    )
    await dp.start_polling(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
