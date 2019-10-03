from Taxas import Taxa

class TaxaContaCorrente(Taxa):

    def __init__(self, type_accout, taxa=0.03):
        super().__init__(type_accout, taxa)

    def get_taxa(self, valor):
        return valor * self.taxa + valor