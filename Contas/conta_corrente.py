import random
from Contas import Conta

class ContaCorrente(Conta):
    def __init__(self, extract, type_account, number=None):
        super().__init__(extract, type_account, 1000.0, number)

    def criar_numero(self):
        return f'{random.randrange(1000, 10000)}-{random.randrange(0, 10)}'

