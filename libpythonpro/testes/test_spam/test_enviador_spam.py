import pytest

from libpythonpro.spam.enviador_de_email import Enviador, Emailinvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['renzo@python.com.br', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'luciano@python.com.br',
        'Curso Python Pro',
        'Primeira turma'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['renzo', '']
)
def test_remetente_invalidos(destinatario):
    enviador = Enviador()
    with pytest.raises(Emailinvalido):
        enviador.enviar(
            destinatario,
            'luciano@python.com.br',
            'Curso Python Pro',
            'Primeira turma'
        )