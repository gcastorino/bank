from Contas.conta import Conta
from Contas.conta_corrente import ContaCorrente
from Contas.conta_poupanca import ContaPoupanca
from Contas.conta_investimento import ContaInvestimento


class Proposta:
    def __init__(self, type_account = None,extract=[]):
        self.type_account = type_account
        self.extract = extract

    def criar_conta(self, account=None):
        """
        Criar nova conta
        """
        if account is None:
            account = {}
        if not self.type_account:
            self.type_account = input('Digite o tipo da conta: ')

        if self.type_account == 'P':
            new_accountCP = ContaPoupanca(self.extract.copy(), self.type_account)
            account[new_accountCP.number] = new_accountCP
        elif self.type_account == 'C':
            new_accountCC = ContaCorrente(self.extract.copy(), self.type_account)
            account[new_accountCC.number] = new_accountCC
            new_accountCP = ContaPoupanca(self.extract.copy(), 'P', f'100{new_accountCC.number}')
            account[new_accountCP.number] = new_accountCP
        elif self.type_account == 'I':
            new_accountCI = ContaInvestimento(self.extract.copy(), self.type_account)
            account[new_accountCI.number] = new_accountCI
        return account
