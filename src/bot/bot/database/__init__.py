from tortoise import Tortoise


async def init(db_url: str) -> None:
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ["bot.database.models.admins",
                            "bot.database.models.user",
                            "bot.database.models.deleted",
                            ]}
    )
    await Tortoise.generate_schemas()
