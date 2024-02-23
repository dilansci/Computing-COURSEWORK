
class LoginController():

    def __init__(self, login_service):
        super().__init__()
        self.login_service = login_service
    
    def get_login(self, pin, access_level):
        return self.login_service.get_login(pin, access_level)