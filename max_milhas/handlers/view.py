from .base import BaseHandler

class ViewHandler(BaseHandler):
    def get(self):
        self.render('../view/view.html')
