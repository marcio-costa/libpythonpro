class Enviador:

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise Emailinvalido(f'Email de remetente inválido: {remetente}')
        return remetente


class Emailinvalido(Exception):
    pass