import random


def gera_palavra(dificuldade):

    faceis = ["Amarelo", "Amiga", "Amor", "Ave", "Avião", "Avó",
              "Balão", "Bebê", "Bolo", "Branco", "Cama", "Caneca",
              "Celular", "Clube", "Copo", "Doce", "Elefante", "Escola",
              "Estojo", "Faca", "Foto", "Garfo", "Geleia", "Girafa", "Janela",
              "Limonada", "Mãe", "Meia", "Noite", "Óculos", "ônibus", "Ovo", "Pai",
              "Pão", "Parque", "Passarinho", "Peixe", "Pijama", "Rato", "Umbigo"]

    dificeis = ["Acender", "Afilhado", "Ardiloso", "Áspero", "Assombração", "Asterisco",
                "Basquete", "Caminho", "Champanhe", "Chiclete", "Chuveiro", "Coelho", "Contexto",
                "Convivência", "Coração", "Desalmado", "Eloquente", "Esfirra", "Esquerdo", "Exceção",
                "Fugaz", "Gororoba", "Heterossexual", "Horrorizado", "Impacto", "Independência",
                "Modernidade", "Oftalmologista", "Otorrinolaringologista", "Paralelepípedo", "Pororoca",
                "Prognóstico", "Quarentena", "Quimera", "Refeição", "Reportagem", "Sino", "Taciturno",
                "Tênue", "Visceral"]

    aleatorio = ["Afobado", "Amendoim", "Banheiro", "Caatinga", "Cachorro", "Campeonato", "Capricórnio",
                 "Catapora", "Corrupção", "Crepúsculo", "Empenhado", "Esparadrapo", "Forca", "Galáxia",
                 "História", "Magenta", "Manjericão", "Menta", "Moeda", "Oração", "Paçoca", "Palavra",
                 "Pedreiro", "Pneumonia", "Pulmão", "Rotatória", "Serenata", "Transeunte", "Trilogia", "Xícara"]

    if dificuldade == '1':
        return faceis[random.randint(0, len(faceis) - 1)].upper()
    elif dificuldade == '2':
        return dificeis[random.randint(0, len(dificeis) - 1)].upper()
    elif dificuldade == '3':
        return aleatorio[random.randint(0, len(aleatorio) - 1)].upper()

