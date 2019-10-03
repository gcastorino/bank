import datetime
import uuid
from Contas import Proposta

class Cliente():
    __slots__ = ['_identifier','name','document', 'date_of_bird','city','date_create','date_update','accounts']

    def __init__(self, accounts=None, identifier= uuid.uuid1(), name='', document='', date_of_bird='', city='',
                 date_create=datetime.datetime.now(), date_update=datetime.datetime.now()):
        if accounts is None:
            accounts = {}
        self._identifier = identifier
        self.name = name
        self.document = document
        self.date_of_bird = date_of_bird
        self.city = city
        self.date_create = date_create
        self.date_update = date_update
        self.accounts = accounts

    def criar(self, name=None, type_account=None):
        """
        Criar nova conta
        """
        self.name = name
        if not name:
            self.name = input('Digite um nome: ')
        self.accounts = Proposta(type_account).criar_conta()

    def exibir_extrato(self):
        """
        Exibe o extrato da conta existente
        account: dict
        """
        print()
        print('=' * 50)
        print('*                    EXTRATO                     *')
        print(f' Cliente {self.name}')
        print('=' * 50)
        print()
        for number, account in self.accounts.items():
            print('*' * 50)
            print(f'** Conta: {account.type_account} {number} **')
            print('*' * 50)
            print()
            print('        Data       ', 'Descrição', 'Valor', sep='|')
            for line in account.extract:
                print(line['date_operation'].strftime("%Y/%m/%d %H:%M:%S"), line['desc'], line['value'], sep='|')
            print()
            print('*' * 50)
            print(f'Saldo : {account.balance}')
            print(f'Limit : {account.limit}')
            print('*' * 50)
            print()
        return True

if __name__ == '__main__':
    client = Cliente()
    client.criar()
    client.exibir_extrato()