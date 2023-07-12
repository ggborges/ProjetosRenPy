label start:
    scene bg_cenario1

    "Bem-vindo ao 'Cosmic Festival', um evento mágico que transcende as fronteiras da realidade."
    "Você é um jovem aventureiro, ansioso para explorar esse festival cósmico único."

    menu:
        "Explorar as barracas e as artes":
            jump explorar_barracas_artes
        "Encontrar uma conexão especial":
            jump encontrar_conexao

label explorar_barracas_artes:
    scene bg_cenario2

    "Você se aventura pelas barracas repletas de cores e símbolos místicos."
    "Artes, músicas e danças enchem o ar enquanto pessoas de todo o universo se reúnem."

    menu:
        "Participar de uma oficina de arte":
            jump oficina_arte
        "Assistir a uma performance musical":
            jump performance_musical

label encontrar_conexao:
    scene bg_cenario3

    "Enquanto caminha pelo festival, você sente uma energia especial no ar."
    "Seus olhos encontram os de uma pessoa misteriosa, e você sente uma conexão instantânea."

    menu:
        "Seguir a pessoa misteriosa":
            jump seguir_pessoa_misteriosa
        "Esperar por um sinal":
            jump esperar_sinal

label oficina_arte:
    scene bg_cenario4

    "Você participa de uma oficina de arte, mergulhando nas cores e nas formas abstratas."
    "Cada pincelada é uma expressão de liberdade e criatividade."

    "Você se junta a outros artistas cósmicos e criam uma obra de arte coletiva."
    "A energia criativa e a colaboração preenchem o ambiente, proporcionando uma experiência única."

    jump transicao_espaco

label performance_musical:
    scene bg_cenario5

    "Você se encanta com uma performance musical hipnotizante, enquanto melodias cósmicas preenchem seus ouvidos."
    "Cada nota toca sua alma e desperta um senso de aventura."

    "Inspirado pela música, você se junta a um grupo de dançarinos e dança sob as estrelas."
    "Seus movimentos fluidos e ritmados se mesclam com a música, criando uma harmonia perfeita."

    jump transicao_espaco

label seguir_pessoa_misteriosa:
    scene bg_cenario6

    "Você decide seguir a pessoa misteriosa através de um portal dimensional."
    "Uma jornada inesperada pelo cosmos começa, revelando segredos cósmicos e maravilhas além da imaginação."

    "A pessoa misteriosa revela-se como um guia cósmico, levando você a diferentes planetas e dimensões."
    "Juntos, vocês exploram civilizações alienígenas, desvendam mistérios antigos e vivem aventuras emocionantes."

    jump transicao_espaco

label esperar_sinal:
    scene bg_cenario7

    "Você decide esperar por um sinal da pessoa misteriosa, confiando no destino e nas forças cósmicas."
    "O universo conspira a seu favor, e um portal dimensional se abre diante de você."

    "O portal leva você a uma jornada pelo espaço sideral, onde encontra seres intergalácticos e testemunha fenômenos cósmicos."
    "Você descobre conhecimentos ancestrais e segredos ocultos, ampliando sua compreensão do universo."

    jump transicao_espaco

label transicao_espaco:
    scene bg_cenario8

    "Através do portal dimensional, você é transportado para uma realidade além do tempo e do espaço."
    "A música e as cores se fundem, criando um espetáculo cósmico deslumbrante."

    menu:
        "Explorar o desconhecido":
            jump explorar_desconhecido
        "Encontrar o caminho de volta":
            jump encontrar_caminho_volta

label explorar_desconhecido:
    scene bg_cenario9

    "Você se aventura nas vastas paisagens cósmicas, encontrando seres alienígenas e maravilhas celestiais."
    "Cada encontro revela um segredo e amplia sua compreensão do universo."

    "Ao explorar um planeta desconhecido, você se depara com uma civilização avançada."
    "Através do diálogo e da troca de conhecimentos, vocês aprendem uns com os outros e deixam um legado duradouro."

    jump transicao_space_oddity

label encontrar_caminho_volta:
    scene bg_cenario10

    "Guiado por sua intuição, você busca o caminho de volta para casa."
    "No entanto, desafios e obstáculos cósmicos testam sua coragem e determinação."

    "Você encontra um sábio cósmico que oferece orientação e sabedoria para superar os desafios."
    "Com determinação renovada, você continua sua jornada em busca do caminho de volta."

    jump transicao_space_oddity

label transicao_space_oddity:
    scene bg_cenario11

    "Após uma jornada emocionante pelo desconhecido, você se encontra diante de uma espaçonave."
    "A melodia de 'Space Oddity' ecoa no ar, chamando-o de volta para casa."

    menu:
        "Embarcar na espaçonave":
            jump embarcar_espaconave
        "Escolher continuar a aventura":
            jump continuar_aventura

label embarcar_espaconave:
    scene bg_cenario12

    "Você embarca na espaçonave e se prepara para retornar ao seu planeta natal."
    "Enquanto se afasta do Cosmic Festival, sentimentos de gratidão e maravilha enchem seu coração."

    jump final_retorno

label continuar_aventura:
    scene bg_cenario13

    "Você decide continuar sua aventura, explorando o cosmos e descobrindo novos horizontes."
    "A melodia de 'Space Oddity' o acompanha enquanto você parte para novas fronteiras."

    jump final_continuar

label final_retorno:
    scene bg_cenario14

    "De volta ao seu planeta natal, você compartilha histórias e memórias do Cosmic Festival com aqueles que ficaram."
    "As experiências vividas no festival se tornam lendas e inspiram futuras gerações."

    "Fim."

label final_continuar:
    scene bg_cenario15

    "Sua jornada cósmica continua, guiada pela música e pela curiosidade infinita."
    "O universo é seu lar, e cada estrela é uma nova oportunidade de descoberta."

    "Fim."
