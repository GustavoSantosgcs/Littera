def sugestao_genero(genero_favorito):
    """
    Recebe o gênero informado pelo usuário e devolve:
        1. um comentário breve sobre o gênero
        2. uma sugestão de leitura
    Retorna (comentario, dica).
    """
    genero = genero_favorito.strip().lower()

    match genero:

        case "comédia" | "comedia" | "humor":
            comentario = "Rir é mesmo um ótimo remédio — histórias divertidas aliviam qualquer dia pesado."
            dica = ("😂 *Comédia*: **'Três Homens em um Barco'** (Jerome K. Jerome) ou\n"
                    "**'O Guia do Mochileiro das Galáxias'** (Douglas Adams).")
            return comentario, dica        
        
        case "religião" | "religiao":
            comentario = "Mergulhar em temas espirituais ajuda a ampliar a visão de mundo."
            dica = ("🙏 *Religião*: **'Confissões'** (Santo Agostinho) ou\n"
                    "**'Uma História de Deus'** (Karen Armstrong).")
            return comentario, dica

        case "futebol":
            comentario = "Futebol vai muito além do gramado – é cultura e identidade."
            dica = ("⚽ *Futebol*: **'Futebol ao Sol e à Sombra'** (Eduardo Galeano) ou\n"
                    "**'Futebol: The Brazilian Way of Life'** (Alex Bellos).")
            return comentario, dica

        case "cultura" | "cultural":
            comentario = "Livros sobre cultura mostram como ideias e hábitos se propagam."
            dica = ("🎭 *Cultura*: **'A Cultura da Convergência'** (Henry Jenkins) ou\n"
                    "**'Outliers'** (Malcolm Gladwell).")
            return comentario, dica

        case "ação" | "acao" | "action":
            comentario = "Histórias de ação entregam ritmo acelerado e pura adrenalina."
            dica = ("💥 *Ação*: **'O Código Da Vinci'** (Dan Brown) ou\n"
                    "**'O Ultimato Bourne'** (Robert Ludlum).")
            return comentario, dica

        case "fantasia" | "fantasy":
            comentario = "Fantasia abre portais para mundos completamente novos."
            dica = ("🔮 *Fantasia*: experimente **'O Nome do Vento'** (Patrick Rothfuss) ou\n"
                    "**'A Guerra da Rainha Vermelha'** (Mark Lawrence).")
            return comentario, dica

        case ("ficção científica" | "ficcao cientifica" |
              "sci-fi" | "tecnologia"):
            comentario = "Sci-fi mistura ciência, futuro e um bom tanto de imaginação."
            dica = ("🚀 *Sci-Fi*: **'Duna'** (Frank Herbert) ou\n"
                    "**'Neuromancer'** (William Gibson).")
            return comentario, dica

        case "romance":
            comentario = "Romances exploram emoções, relações e, claro, corações partidos."
            dica = ("💕 *Romance*: **'Orgulho e Preconceito'** (Jane Austen) ou\n"
                    "**'A Culpa é das Estrelas'** (John Green).")
            return comentario, dica

        case "terror" | "horror":
            comentario = "Gênero perfeito para quem curte aquele friozinho na espinha."
            dica = ("👻 *Terror*: **'It – A Coisa'** ou\n"
                    "**'O Iluminado'** (Stephen King).")
            return comentario, dica

        case "suspense" | "thriller":
            comentario = "Suspense mantém a mente ligada, tentando prever cada virada."
            dica = ("😱 *Suspense/Thriller*: **'Garota Exemplar'** (Gillian Flynn) ou\n"
                    "**'O Silêncio dos Inocentes'** (Thomas Harris).")
            return comentario, dica

        case "policial" | "mistério" | "misterio":
            comentario = "Nada como seguir pistas e desvendar crimes junto com o detetive."
            dica = ("🕵️ *Policial/Mistério*: **'Assassinato no Expresso do Oriente'** "
                    "(Agatha Christie) ou\n"
                    "**'O Colecionador de Ossos'** (Jeffery Deaver).")
            return comentario, dica

        case "autoajuda" | "desenvolvimento pessoal":
            comentario = "Livros de autoajuda trazem ferramentas práticas para crescer."
            dica = ("🌱 *Autoajuda*: **'O Poder do Hábito'** (Charles Duhigg) ou\n"
                    "**'Mindset'** (Carol Dweck).")
            return comentario, dica

        case "não ficção" | "nao ficcao" | "biografia":
            comentario = "Não ficção entrega conhecimento real com histórias fascinantes."
            dica = ("📚 *Não ficção*: **'Sapiens'** (Yuval Noah Harari) ou\n"
                    "**'Fatos e Ficção'** (Jill Lepore).")
            return comentario, dica

        case "aventura":
            comentario = "Aventura é um dos gêneros mais escolhidos para quem adora explorar."
            dica = ("🏔️ *Aventura*: **'As Aventuras de Huckleberry Finn'** (Mark Twain) ou\n"
                    "**'A Ilha do Tesouro'** (R. L. Stevenson).")
            return comentario, dica

        case "poesia":
            comentario = "Poesia condensa emoções em poucas linhas poderosas."
            dica = ("📝 *Poesia*: **'Folhas de Relva'** (Walt Whitman) ou\n"
                    "**'Alguma Poesia'** (Carlos Drummond de Andrade).")
            return comentario, dica

        case "quadrinhos" | "gibi" | "hq":
            comentario = "Quadrinhos unem arte visual e narrativa dinâmica."
            dica = ("🦸 *HQs*: **'Watchmen'** (Alan Moore & Dave Gibbons) ou\n"
                    "**'Sandman'** (Neil Gaiman).")
            return comentario, dica

        case "mangá" | "manga":
            comentario = "Mangás oferecem universos vastos em preto-e-branco cheios de emoção."
            dica = ("🎌 *Mangá*: **'Fullmetal Alchemist'** (Hiromu Arakawa) ou\n"
                    "**'Monster'** (Naoki Urasawa).")
            return comentario, dica

        case "drama":
            comentario = "Drama mergulha em conflitos humanos profundos e verossímeis."
            dica = ("🎭 *Drama*: **'A Menina que Roubava Livros'** (Markus Zusak) ou\n"
                    "**'Pequenas Grandes Mentiras'** (Liane Moriarty).")
            return comentario, dica

        case "história" | "historia":
            comentario = "Obras históricas reconstroem épocas e explicam o presente."
            dica = ("🏰 *História*: **'Os Pilares da Terra'** (Ken Follett) ou\n"
                    "**'Guns, Germs and Steel'** (Jared Diamond).")
            return comentario, dica

        case "erótico" | "erotico":
            comentario = "Literatura erótica explora desejo, sensualidade e tabus."
            dica = ("💋 *Erótico*: **'Delta de Vênus'** (Anaïs Nin) ou\n"
                    "**'Cinquenta Tons de Cinza'** (E. L. James).")
            return comentario, dica

        case _:
            comentario = "Gênero pouco conhecido por aqui, mas vamos arriscar!"
            dica = ("🤔 Experimente **'O Curioso Incidente do Cão na Noite'** "
                    "(Mark Haddon – mistério) ou\n"
                    "**'A Menina que Roubava Livros'** (Markus Zusak – drama).")
            return comentario, dica
