perfil_admin = 'Admin'
perfil_admin_lower = 'admin'
perfil_user = 'User'
perfil_user_lower = 'user'

def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print("Bem Vindo, Administrador")
    else:
        print("Bem Vindo, Usuário")  

perfil_informado = input("Digite o seu perfil: ")

loginUsuario(perfil_informado)





loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('user')
loginUsuario('usuário')