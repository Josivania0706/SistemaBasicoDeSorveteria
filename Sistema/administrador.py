
class Admin:
    def __init__(self, _login, _senha):
        self.login = _login
        self.senha = _senha
          
    def autenticar_Admin(self,_login, _Senha):
        if self.login == _login and self.senha == _Senha:
            return True
        else:
            return False


Administrador = Admin("admin", "admin")
