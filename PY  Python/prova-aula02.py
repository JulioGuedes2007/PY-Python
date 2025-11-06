usuarios= {
    'Joao': 'joao123',
    'Maria': 'maria456',
    'Pedro': 'pedro789',
    'marcos': 'marcos000',
    'julia': 'julia111'
}

usuario= input('Digite seu nome de usuário: ')
senha= input('Digite sua senha: ')

for i in usuarios.keys():
    if i == usuario:
        if usuarios[i] == senha:
            print('Login realizado com sucesso!')
            break
        else:
            print('senha incorreta.')
            break 
else:
    print('Usuário não encontrado.')
