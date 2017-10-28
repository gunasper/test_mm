from handlers.cpfs import CPFsHandler
from handlers.server_status import StatusHandler

ROUTES = [
    (r"/status", StatusHandler),
    (r"/cpfs", CPFsHandler),
    (r"/cpfs/([0-9.\-]*)", CPFsHandler)
]