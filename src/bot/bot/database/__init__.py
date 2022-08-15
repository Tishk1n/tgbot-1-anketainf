from tortoise import Tortoise


async def init(db_url: str) -> None:
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ["bot.database.models.order",
                            "bot.database.models.worker",
                            ]})
    await Tortoise.generate_schemas()
