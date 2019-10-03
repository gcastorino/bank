import random
import datetime
from abc import ABC, abstractmethod
from Contas.historico import HistoricoMixIn
from errors import SaldoInsulficienteError


class Conta(ABC, HistoricoMixIn):
    def __init__(self, extract, type_account, limit, number=None, balance=0,
                 date_create=datetime.datetime.now(), date_update=datetime.datetime.now()):
        if not number:
            number = self.criar_numero()
        self.number = number
        self.type_account = type_account
        self._balance = balance
        self.limit = limit
        self.date_create = date_create
        self.date_update = date_update
        super().__init__(extract)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if (self.limit + self._balance + value) < 0:
            raise SaldoInsulficienteError
        self._balance = value

    @abstractmethod
    def criar_numero(self):
        pass

