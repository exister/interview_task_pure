import asyncio
import logging
from motor import motor_asyncio

from io import BytesIO
from PIL import Image
from aiohttp import ClientSession


logger = logging.getLogger()


mongo = motor_asyncio.AsyncIOMotorClient('mongodb://mongo/db').get_database()


async def load_url(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            await store_url(url, data)


async def store_url(url, data):
    image = BytesIO(data)

    try:
        pil_image = Image.open(image)
    except OSError as e:
        logger.error('Unable to open image for url %s (%s)', self.url, e)
        return

    image_info = {
        'url': url,
        'width': pil_image.width,
        'height': pil_image.height,
        'format': pil_image.format.lower()
    }

    await mongo.images.find_one_and_update(
        {'url': url},
        {'$set': image_info},
        upsert=True
    )


async def load_urls(urls):
    if not urls:
        return

    await asyncio.gather(*[load_url(url) for url in urls])


loop = asyncio.get_event_loop()
loop.run_until_complete(load_urls(['https://medialeaks.ru/wp-content/uploads/2017/10/catbread-03-600x400.jpg']))
