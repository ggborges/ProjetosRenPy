# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")


# The game starts here.

#label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    #return
label start:
    scene bg_cenario1

    "Bem-vindo a 'Cosmic Journey', uma história de exploração e descoberta espacial."
    "Você é um astronauta solitário, flutuando no espaço sideral."
    "A comunicação com a Terra é interrompida, e você está sozinho na vastidão do universo."

    menu:
        "Explorar o espaço":
            jump explorar_espaco
        "Refletir sobre a vida na Terra":
            jump refletir_vida_terra

label explorar_espaco:
    scene bg_cenario2

    "Você decide explorar o espaço e se aventurar além dos limites conhecidos."
    "Enquanto viaja pela galáxia, você encontra um planeta misterioso."

    menu:
        "Pousar no planeta":
            jump pousar_planeta
        "Continuar a jornada espacial":
            jump continuar_jornada

label refletir_vida_terra:
    scene bg_cenario3

    "Enquanto flutua no espaço, você reflete sobre a vida na Terra e as conexões que deixou para trás."
    "Memórias e emoções enchem sua mente."

    menu:
        "Lembrar dos entes queridos":
            jump lembrar_entes_queridos
        "Encontrar significado na solidão":
            jump encontrar_significado

label pousar_planeta:
    scene bg_cenario4

    "Você decide pousar no planeta desconhecido."
    "Ao explorar sua superfície, você descobre criaturas alienígenas amigáveis e paisagens deslumbrantes."

    menu:
        "Estabelecer contato com os alienígenas":
            jump contato_alienigenas
        "Prosseguir com a exploração":
            jump prosseguir_exploracao

label continuar_jornada:
    scene bg_cenario5

    "Você continua sua jornada espacial, explorando novos sistemas solares e maravilhas cósmicas."
    "Cada estrela e planeta revela segredos fascinantes."

    menu:
        "Descobrir um buraco negro":
            jump descobrir_buraco_negro
        "Navegar pelos anéis de Saturno":
            jump navegar_aneis_saturno

label lembrar_entes_queridos:
    scene bg_cenario6

    "Enquanto flutua no espaço, você se lembra dos entes queridos que deixou para trás na Terra."
    "Sentimentos de saudade e conexão preenchem seu coração."

    menu:
        "Retornar à Terra":
            jump retornar_terra
        "Continuar a explorar o espaço":
            jump continuar_explorar_espaco

label encontrar_significado:
    scene bg_cenario7

    "Na solidão do espaço, você encontra um novo sentido para a vida."
    "A vastidão cósmica o faz perceber sua pequenez e a grandiosidade do universo."

    menu:
        "Encontrar a paz interior":
            jump encontrar_paz_interior
        "Buscar respostas cósmicas":
            jump buscar_respostas_cosmicas

label contato_alienigenas:
    scene bg_cenario8

    "Você estabelece um contato amigável com os alienígenas do planeta."
    "Juntos, vocês compartilham conhecimento e experiências únicas."

    jump final_amizade

label prosseguir_exploracao:
    scene bg_cenario9

    "Você decide prosseguir com a exploração do planeta, descobrindo segredos antigos e tecnologias avançadas."

    jump final_exploracao

label descobrir_buraco_negro:
    scene bg_cenario10

    "Você descobre um buraco negro imenso, cuja força gravitacional desafia todas as leis conhecidas."
    "A imensidão e o perigo desse fenômeno cósmico o deixam perplexo."

    jump final_tragico

label navegar_aneis_saturno:
    scene bg_cenario11

    "Você navega com destreza pelos anéis de Saturno, apreciando sua beleza e singularidade."
    "É uma experiência transcendental que o conecta com a imensidão do universo."

    jump final_exploracao

label retornar_terra:
    scene bg_cenario12

    "Você toma a decisão de retornar à Terra, onde estão suas raízes e conexões mais profundas."
    "Ao retornar, você compartilha suas experiências cósmicas com o mundo."

    jump final_reencontro

label continuar_explorar_espaco:
    scene bg_cenario13

    "Você decide continuar explorando o espaço, fascinado pelo desconhecido e pela aventura."
    "Cada nova descoberta o leva a lugares além da imaginação."

    jump final_exploracao

label encontrar_paz_interior:
    scene bg_cenario14

    "Você encontra a paz interior, aceitando a solidão do espaço e encontrando significado em sua própria jornada."
    "O silêncio cósmico se torna uma sinfonia transcendental."

    jump final_paz_interior

label buscar_respostas_cosmicas:
    scene bg_cenario15

    "Você busca respostas cósmicas para as grandes questões da existência, mergulhando em estudos e pesquisas profundos."
    "A busca pelo conhecimento se torna sua missão na vastidão do universo."

    jump final_busca_conhecimento

label final_amizade:
    scene bg_cenario16

    "Uma amizade intergaláctica é formada, transcendo as barreiras do espaço e do tempo."
    "Juntos, vocês exploram o cosmos e compartilham aventuras incríveis."

    "Fim."

    return

label final_exploracao:
    scene bg_cenario17

    "Sua jornada de exploração espacial continua, revelando segredos e maravilhas inimagináveis."
    "Você se torna um guardião das estrelas, levando conhecimento e beleza a todos os cantos do universo."

    "Fim."

    return

label final_tragico:
    scene bg_cenario18

    "O poder avassalador do buraco negro o consome, levando-o a um destino desconhecido."
    "Sua coragem e curiosidade permanecerão como um legado duradouro."

    "Fim"

    return

