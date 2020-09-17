# I Love China

__Author__ = 'Seenming'


import json
from apps import BaseHandler
from models.user_info import Account


class LoginHandler(BaseHandler):
    
    async def post(self, *args, **kwargs):
        try:
            data = json.loads(self.request.body)
            print(data)
        except json.decoder.JSONDecodeError:
            self.send_error(400, )
            return
        if "username" not in data:
            pass
        if "password" not in data:
            pass
        result = await Account.fetch_one(**data)
        if not result:
            self.send_error(400)
            return
        
        self.write(data)


class RegisterHandler(BaseHandler):
    
    def post(self, *args, **kwargs):
        pass
