
import abc
class Taxa(abc.ABC):
    def __init__(self, type_accout, taxa=0.01):
        self.taxa = taxa
        self.type_accout = type_accout

    def taxa_sobra_saque(self, valor):
        valor += valor * self.taxa
        return valor

    @abc.abstractmethod
    def get_taxa(self, valor):
        pass