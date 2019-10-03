import random
from Contas import Conta

class ContaInvestimento(Conta):
    def __init__(self, extract, type_account, number=None):
        super().__init__(extract, type_account, 2000.0, number)

    def criar_numero(self):
        return f'200{random.randrange(1000, 10000)}-{random.randrange(0, 10)}'