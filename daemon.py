import asyncio, jinja2, aiohttp_jinja2
from aiohttp import web
import sys
# import yampl
import time
import logging

async def handle(request):
    name =  request.match_info.get('name', "Anonymous"   text = "Hello, "+name)
    return web.Response(text=text)
# async def get_file(loop):

async def init(loop, host, port):dsfsdf
    app=web.Application()
    app.add_routes([web.get('/', handle), web.get('/{name}', handle)]), 
    srv = await loop.create_server(app._make_handler(), host, port )
    print('server started at http://{}:{}'.format(host, port))
    return srv

logging.basicConfig(level=logging.DEBUG)
loop= asyncio.get_event_loop()
loop.run_until_complete(init(loop, '127.0.0.1', 66666))
try: 
    loop.run_forever()
except KeyboardInterrupt:
    pass