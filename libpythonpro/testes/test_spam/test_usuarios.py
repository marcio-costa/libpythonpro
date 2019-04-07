from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome = 'Marcio')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome = 'Marcio'), Usuario(nome = 'Renzo')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()



