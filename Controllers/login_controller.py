
class LoginController():

    def __init__(self, login_service):
        super().__init__()
        self.login_service = login_service
    
    def get_login(self): # copy login service
        pass