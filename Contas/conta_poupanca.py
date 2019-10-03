import random
from Contas import Conta

class ContaPoupanca(Conta):
    def __init__(self, extract, type_account, number=None):
        super().__init__(extract, type_account, 0, number)

    def criar_numero(self):
        return f'100{random.randrange(1000, 10000)}-{random.randrange(0, 10)}'
