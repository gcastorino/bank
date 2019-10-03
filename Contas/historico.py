import datetime
import uuid


class HistoricoMixIn:

    def __init__(self, extract):
        self.extract = extract

    def adicionar_historico(self, value, desc, identifier=uuid.uuid1(), date_operation=datetime.datetime.now()):
        return self.extract.append({
            'value': value,
            'desc': desc,
            'identifier': identifier,
            'date_operation': date_operation
        })
