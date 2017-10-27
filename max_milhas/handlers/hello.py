from .base import BaseHandler

class HelloHandler(BaseHandler):
    """
    Handler implementing GET, POST, PUT and DELETE methods
    """

    async def get(self, cpf: str = ''):
        """
        GET
        """
        pass

    async def post(self, cpf: str = ''):
        """
        POST
        """
        pass

    async def put(self, cpf: str):
        """
        PUT
        """
        pass

    async def delete(self, cpf: str):
        """
        DELETE
        """
        pass
