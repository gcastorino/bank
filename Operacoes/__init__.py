from Taxas import Taxa
from Taxas.taxa_conta_corrente import TaxaContaCorrente
from Taxas.taxa_conta_poupanca import TaxaContaPoupanca
from errors import SaldoInsulficienteError


class Operacao:

    def __init__(self, account):
        self.account = account
        if self.account.type_account == 'P':
            self.taxa = TaxaContaPoupanca(self.account.type_account)
        elif self.account.type_account == 'C':
            self.taxa = TaxaContaCorrente(self.account.type_account)
        else:
            self.taxa = Taxa(self.account.type_account)

    def sacar(self, value, desc=None):
        if value < 0:
            raise ValueError('Valor deve ser positivo')
        try:
            tax = self.taxa.get_taxa(value)
            self.account.balance -= value + tax
            self.account.adicionar_historico(- value, desc)
            self.account.adicionar_historico(- tax, 'Taxa de retirada')
            return True
        except SaldoInsulficienteError:
            return False

    def depositar(self, value, desc=None):
        if value < 0:
            raise ValueError('Valor deve ser positivo')
        self.account.balance += value
        self.account.adicionar_historico(value, desc)

    def transfer(self, operation_to,name, value):
        if self.sacar(value, f'transferencia para {name}'):
            operation_to.depositar(value, f'transferencia da conta {self.account.number}')
