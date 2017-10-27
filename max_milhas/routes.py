from handlers.cpfs import CPFsHandler
from handlers.hello import HelloHandler
from handlers.server_status import StatusHandler

ROUTES = [
    (r"/", HelloHandler),
    (r"/status", StatusHandler),
    (r"/cpfs", CPFsHandler),
    (r"/cpfs/([0-9.\-]*)", CPFsHandler)
]