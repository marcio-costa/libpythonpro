from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renzo', email='renzo@pythonpro.com'),
            Usuario(nome='Luciano', email='renzo@pythonpro.com')
        ],
        [
            Usuario(nome='Renzo', email='renzo@pythonpro.com')
        ]
    ]
)


def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@pythonpro.com.br',
        'Curso Python Pro',
        'confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@pythonpro.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@pythonpro.com',
        'Curso Python Pro',
        'confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with == (
        'luciano@pythonpro.com',
        'renzo@pythonpro.com',
        'Curso Python Pro',
        'confira os módulos fantásticos'
    )