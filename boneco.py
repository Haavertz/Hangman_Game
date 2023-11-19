class Boneco():
    def __init__(self) -> None:
        pass    
    
    def exibir_forca(self, estado):
        parament = estado

        self.forca = [
            '''
            +---+
            |   |
                |
                |
                |
                |
            =========
            '''
            ,
            '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            '''
            ,
            '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            '''
            ,
            '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
            '''
            ,
            '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========
            '''
            ,
            '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========
            '''
        ]

        print(self.forca[parament])
