from aiohttp import ClientSession


async def get_bytes_document(url_doc: str):
    async with ClientSession() as session:
        async with session.get(url_doc) as response:
            return await response.read()
