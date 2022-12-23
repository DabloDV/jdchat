class Usuario():

    def __init__(self, id, pais=None) -> None:
        self.id = id
        self.pais = pais

    def to_JSON(self):
        return {
            'id': self.id, 
            'pais': self.pais
            }
