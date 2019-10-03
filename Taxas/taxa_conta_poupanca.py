from Taxas import Taxa


class TaxaContaPoupanca(Taxa):

    def __init__(self, type_accout):
        super().__init__(type_accout)

    def get_taxa(self, valor):
        return valor * self.taxa