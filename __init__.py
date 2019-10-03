from Clientes import Cliente
from Operacoes import Operacao
from errors import SaldoInsulficienteError


class Banco:
    def criar_cliente_conta(self,name, type_account):
        client = Cliente()
        client.criar(name,type_account)
        return client

if __name__ == '__main__':
    try:
        cliente1 = Banco().criar_cliente_conta('Gabriel','P')
        cliente2 = Banco().criar_cliente_conta('Maria', 'C')

        operation = []
        i= 0
        accounts = []
        for number, account in cliente1.accounts.items():
            accounts.append(account)
        for number, account in cliente2.accounts.items():
            accounts.append(account)
        operation1 = Operacao(accounts[0])
        operation1.sacar(50, 'supermercado')
        operation1.depositar(100, 'cache')
        operation1.sacar(50, 'supermercado')
        cliente1.exibir_extrato()
        print('#' * 50)

        operation2 = Operacao(accounts[1])
        operation2.sacar(150, 'alura')
        operation2.depositar(200, 'salario')
        operation2.sacar(50, 'alura')
        cliente2.exibir_extrato()
        print('#' * 50)

        operation2.transfer(operation1,cliente1.name, 250)
        cliente1.exibir_extrato()
        cliente2.exibir_extrato()
    except ValueError:
        print('Valor deve ser positivo')
    except SaldoInsulficienteError:
        print('Saldo insulficiente')


