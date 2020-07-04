input('Pressione enter para continuar ')
print('Bem-Vindo(a) ao  Life is Hard Hack Trisse \nEsse jogo possui restrições de idade,portanto informe sua idade.')
idade = int(input('Qual a sua idade: '))

import os 

if idade < 15:
    print('Infelizmente você não pode jogar, volte em alguns anos') 
    os.system('pause')

elif idade >= 15:
    print('Ótimo, agora podemos continuar: \n')
    
    print('-' * 20)
    print('\nREGRAS DO JOGO: \n§ As respostas devem sempre ser apenas com o número da escolha, após a escolha apenas aperte ENTER. \n§ Alguns caminhos serão curtos e outros serão longos para saber todos eles, é só voltar a jogar. \n§ Se divirta!\n')
    print('-' * 20)

    personagem = input('Agora nos diga quem você quer ser?\n\nTrinity{1} ou Jesse{2}: ')
    
    if personagem == '1':
        print('\nSeu nome é Trinity, você tem 26 anos e entrou agora no curso de Sociologia na Universidade De Ética E Política em Atenas. Você chegou da sua cidade natal - Campina Grande - a pouco tempo e ainda não se acostumou com o clima Europeu. Seu dormitório é maravilhoso e tudo que você sempre sonhou.\nNo seu primeiro dia de aula você se arruma toda e corre para não se atrasar, mas há um problema, você não tem a menor ideia para que direção fica sua sala, você para em frente aos portões e não sabe aonde ir!!\n')
        esc = input('Voce tem que decidir pra onde ir, o que voce escolhe?\n1)Em frente\n2)Voltar\nResposta: ')

        if esc == '1':
            print('\nVocê segue em frente por uma estrada de tijolos brancos rodeada de enormes prédios de arquitetura clássica. Durante seu passeio você encontra um grupo de jovens.')
            esc1 = input('O que você faz?\n1)Vai lá e conversa com eles\n2)Segue reto pois não gosta de falar com estranhos\nResposta: ')
            
            if esc1 == '1':
                print('\nVocê se aproxima desse grupo e descobre que eles também fazem Sociologia, e um dos rapazes em especial te chama a atenção.')
                esc2 = input('\nO que você faz em seguida? \n1)Você se apresenta e procura saber o nome de todos\n2)Você conta uma piada e tenta descontrair antes de falar alguma coisa\nResposta: ')

                if esc2 == '1': 
                    print('\nVocê percebe que todos os olhares se voltam para você, e aquele rapaz em especial te esquadrinha por completo.\nApós 10 minutos de fala, você já sabe o nome das três pessoas que estavam lá:\nDimietri,Alieknovina e Eros.\nDimietri não era nada especial:tinha olhos castanhos, de pele caucasiana e era menor do que Trinity.\nAlieknovina tinha um ar ameaçador: aparentava ser ucraniana, com uma pele branca e fina e longos cabelos cor de palha.\nEros era o mais belo: possuia um porte atlético,era maior que todos os presentes e se parecia com o Tom Cruise.')
                    esc3 = input('Eros então te olha de cima a baixo e se oferece a te ajudar a encontrar a sua sala.\nVocê aceita?\n1)Sim\n2)Não\nResposta: ')
                    
                    if esc3 == '1':
                        print('\nVocê e Eros então se despedem dos seus mais novos amigos e partem em direção na busca de sua sala\n')
                        esc4 = input('Voces caminham por mais 5 minutos e então chegam em frente a uma porta onde está escrito: Etica e Moral Socratica 101. Voce se volta para Eros com a intenção de agradecê-lo e então sente seu corpo sendo puxado para frente e então a boca dele encontra a sua.O que voce faz?\n1)Se entrega ao beijo.\n2)O afasta e entra correndo pra dentro sala.\nResposta: ')
                        
                        if esc4 == '1':
                            print('\nAo sentir o toque daqueles ternos labios voce se não consegue se controlar e se entrega totalmente a Eros. Sua língua se enrola com a dele num vai e vem intenso, voce perde a noção de espaço, seu corpo é empurrado para trás...\nA porta estava entreaberta e voce e seu companheiro caem espantados no chão frio da sua sala, um momento de silencio... e então a sala se preenche com os risos, ao olhar para cima voce percebe seu professor lhe olhando friamente.\n')
                            esc5 = input("O que voce faz?\n1)Empurra Eros para longe de si e corre para se sentar no fundo da classe olhando para baixo.\n2)Se levanta rapidamente enquanto ajuda Eros a se levantar e pede desculpas a turma e ao professor.\nResposta: ")

                            if esc5 == '1':
                                print("\nVoce passa o resto da aula de cabeça baixa querendo morrer e não consegue prestar atenção em nada, até que as duas eternas horas passam e voce se levanta após todos os seus colegas sairem da sala. Decidida a não passar mais vergonha, voce caminha para suas próximas aulas do dia.\nO dia passa e voce volta para o dormitorio totalmente derrotada, no meio do caminho voce ve de longe aquelas pessoas que voce conheceu mais cedo.\n")
                                esc6 = input('O que voce faz?\n1)Vai falar com eles.\n2)Finge que não os viu e vai direto para o quarto.\nResposta: ')
                                if esc6 == '1':
                                    print('\nMesmo tomada de vergonha voce vai falar com Dimietri, Alieknovina e Eros. Ao chegar mais perto percebe que eles estão rindo de algo e voce escuta seu nome.\n')
                                    esc7 = input('O que voce faz? \n1)Dá meia volta e desiste de falar.\n2)Se aproxima e pergunta do que eles estão falando.\nResposta: ')
                                    
                                    if esc7 == '1':
                                        print('\nAo ouvir seu nome voce pressupõe que eles estão falando do seu vergonhoso ato que cometeu com Eros, e com toda razão voce pensou pois era ele que estava falando enquanto todos os outros apenas riam da situação. Voce dá meia volta e corre para seu dormitório, mas não rápido o suficiente para que o grupo risonho não percebesse sua presença. Eles gritam seu nome, mas voce continua correndo.\n\nAo chegar no seu dormitorio voce joga seu material em uma escrivaninha e deita com a cabeça encerrada nos travesseiros, voce tem vontade de ficar ali e nunca mais sair. Entretanto voce sente um odor de podridão e então se dá conta que o seu suvaco.\n')
                                        esc8 = input('O que voce vai fazer?\n1)Tomar um banho.\n2)Permanecer como está e ir dormir.\nResposta: ')
                                        if esc8 == '1':
                                            print('\nVoce percebe que sua mente esá agitada demais e pensa em como Simone de Beauvoir resolveria aquela situação. Bem, talvez ela simplesmente não tivesse deixado que Eros a beijasse e rompesse com o pensamento patriarcalistica de que um homem pode beijá-la quando bem entender... Voce divaga sobre isso enquanto se dirige ao banheiro.\n\nApós limpar a mente com uma boa cucha, voce escuta seu celular apitar diversas vezes... É sua mãe perguntando se está tudo bem, dezenas da mesma mensagem.\n')
                                            esc9 = input('O que voce faz?\n1)Conta a verdade, afinal, voce confia em sua mãe.\n2)Fala que está tudo bem, já que voe não tem intimidade com ela, mesmo ela sendo sua mãe.\nResposta: ')

                                            if esc9 == '1':
                                                print("\nVoce decide ligar para sua mãe para contar o que aconteceu e antes que ela pudesse ao menos dizer 'Alo?', voce despejou tudo aquilo que estava entalado na sua garganta em meio a lagrimas e soluços.\n Mas após todo o seu desabafo, a sua mãe disse:'Mas filha, eu estou preocupada por causa das bombas que estão lançando por todo o mundo. Por enquanto aqui no Brasil não fomos atingidos, mas ficamos sabendo que a Itália, Grécia e Turquia seriam bombardeadas e por isso queria saber como voce está e para dizer que eu quero que voce pegue o primeiro v--...\n\n E antes que mais uma palavra sequer fosse dita, todo o prédio do dormitório explodiu. Seu quarto ficava no quarto e ultimo andar e por isso foi o primeiro a ser atingido mas voce não foi ferida... Poeira, destroços, tudo era um grande borrão em sua mente.\n ")
                                                esc10 = input('O que voce faz?\n1)Grita por socorro\n2)Tenta sair sozinha dos destroços.\nResposta: ')
                                                
                                                if esc10 == '1':
                                                    print('\nVocê grita por socorro com todas as suas forças, clama por ajuda desesperadamente até que ouve alguém dizer seu nome ao longe \n..(trinity)..\n..(trinity)..\n..(trinity)..\nVocê chama a atenção daquela voz para si, e em alguns instantes você vê Eros sobre si, com uma cara de desesperado ele começa a retirar os destroços de cima de você enquanto pergunta se você está bem e enquanto fala que estava preocupadissimo. \nAo retirar tudo que lhe impedia de se mexer, ele te abraçou e te pegou no colo dum jeito incrivelmente heroico enquanto te consolava dizendo que tudo ficaria bem. Vocês saem do prédio destruído, diversas vozes pediam por ajuda, cheiro de queimado e de poeira molhada enchiam todos os sentidos. \nApós alguns metros de caminhada, Eros te coloca no chão e diz que tem que ir ajudar as outras pessoas.\n ')
                                                    esc11 = input('O que voce faz?\n1)Pede para ir com ele, mesmo estando machucada\n2)Diz que tudo bem e que vai esperá-lo onde está \nResposta: ')

                                                    if esc11 == '1':
                                                        print('\nVocê diz que prefere não ficar sozinha e que prefere ir com ele. Eros reluta em te deixar ir, pois seu corpo está com diversos ferimentos, mas nada muito sério, então ele aceitou embora não concordasse. \nVocê ficou se perguntando se realmente era uma boa ideia ir e se você não atrapalharia mais ele.\n')
                                                        esc12 = input('Você tem certeza de que quer ir?\n1)Sim\n2)Não\nResposta: ')
                                                        
                                                        if esc12 == '1':
                                                            print('\nVocê está decidida, Eros vai ter que aceitar que você, embora machucada, também quer ajudar as outras pessoas.\nEle lhe leva de volta para o seu prédio, que está completamente destruído, era um pŕedio simples com quatro andares, uma escada se localizava dividindo ao meio a construção enquanto que haviam seis comodos de cada lado do prédio. Tudo o que sobrou foi uma parte da escada que tinha apenas alguns lances de degrau, já os quartos estavam todos soterrados, via-se braços balançando por todos os lados entre os escombros.\nVocê corre para socorrer uma menina caída embaixo da escada, a perna dela estava totalmente quebrada em ângulos sobrenaturais e ela chorava dor. Ao se apressar para tirar a menina dali não percebe que a escada já não mais se sustenta em pé e está prestes a cair.\n')
                                                            esc13 = input('Você sabe que não conseguirá tirar a menina antes que a escada desabe. O que voce faz?\n1)Pega a menina nos braços e tenta correr\n2)Corre para longe\nResposta: ')

                                                            if esc13 == '1':
                                                                print('\nVocê não vai abandoná-la, como você viveria sabendo que abandonou um ser humano para a morte? Você junta todas as suas forças e pega aquela menina, ela grita com a dor, você não era nenhuma médica, mas achava que ela tinha quebrado algumas costelas. Ao colocá-la nos braços, seus pés já estão em movimento, você corre...\ntenta sair dalí...\n...e por pouco você consegue com a escada desabando no exato momento em que você sai debaixo dela.\nVocê respira aliviada...\n\n\nUM CLARÃO SEGUIDO DE UM SOM ESTRONDOSO...\n\n\n\nVocê consegue se mexer e ao olhar para baixo percebe que suas pernas não estão mais lá, a menina que estava em seus braços está destroçada em seu peito...\nSua respiração começa a ficar mais lenta...\nSeus olhos ficam pesados...\nVocê tem um último pensamento enquanto sua mente fica nublada:"Por que?"')

                                                            elif esc13 == '2':
                                                               print('Mesmo toda a sua alma dizendo que aquilo é errado, no fundo seu único desejo é sobreviver. Você pede desculpas para aquela pobre garota que te olha suplicante para que não a deixe, mas você apenas se vira e começa a correr para longe dali.\nSeus olhos se enchem de lágrimas, você não consegue entender porque tomou uma atitude tão absurda. Ao olhar para trás, a escada imediatamente cai, devorando a pobre garota num turbilhão de poeira, você não aguenta ficar ali, corre desesperada em busca de Eros gritando que quer sair dali, mas antes que qualquer pensamento seu se completasse...\nUM CLARÃO SEGUIDO DE UM SOM ESTRONDOSO...\nSua cabeça começa a girar e subitamente, antes que qualquer coisa passasse pela sua cabeça, tudo escureceu.')
                                                        
                                                        elif esc12 == '2':
                                                            print('Você volta atrás na sua decisão e pensa mais calmamente, se você for, talvez você não seja forte o suficiente e acabe atrapalhando Eros. Ao olhar em volta percebe que ele te levou pra uma praça bastante iluminada e que também possuia diversas pessoas feridas por lá e que havia gente vestida de branco correndo para elas, demorou mas você entendeu que eram médicos socorrendo quem precisasse. De repente uma dessas pessoas chega próximo a você e pergunta se você quer ajuda e para de repente meio espantada, você demora um pouco para perceber mas quem está a sua frente é Dimietri te olhando com um olhar preocupado.\n')
                                                            esc13_1 = input('O que você faz?\n1)Pergunta o que ele está fazendo ali.\n2)Diz que está bem e que ele não precisa se preocupar.\nResposta: ')

                                                            if esc13_1 == '1':
                                                                print('Você fica confusa com o fato de Dimietri estar naquele meio de gente e então você pergunta o que danado ele estava fazendo ali. Ele dá uma risadinha e diz que havia feito enfermagem antes de ir para Sociologia, ele começa a analisar seus ferimentos e declara que não há sinais de fraturas e nem de hemorragia interna. Após essa rápida checagem ele pergunta se você quer ir ao shopping perto dali que estava recebendo os atingidos pelas bombas.\n ')
                                                                esc14 = input('O que você faz?\n1)Prefere ir ao shopping.\n2)Decide ficar e esperar por Eros.\nResposta: ')
                                                                if esc14 == '1':
                                                                    print('Ao olhar para ambos os lados e ver pessoas sangrando por todos os lados com visceras espalhados pelo chão você decide que aquele não seria um bom local para permanecer e pergunta em que direção fica o shopping. Dimietri então pareceu um pouco irritado e perguntou se você não gostaria que ele te levasse até lá para a proteger, você ficou imaginando como um nanico como ele a protegeria, mas você guardou esse comentário para si. Você o perguntou de que ele te protegeria, e ele então já com a cara bem vermelha de raiva disse que muita gente podia se aproveitar de uma situação difícil como aquela para fazer maldades.\n ')
                                                                    esc15 = input('O que você decide?\n1)Permite que ele te acompanhe.\n2)Agradece a intenção mas diz que pode se cuidar sozinha.\nResposta: ')

                                                                    if esc15 == '1':
                                                                        print('Você pensa com cuidado e acaba permitindo que ele te acompanhe, embora alguma coisa pareça muito errada...\nVocê e Dimietri então começam a caminhar para longe daquela praça, mas aquele caminho era muito estranho, os postes estavam todos quebrados e não há ninguém por lá, você então pergunta a Dimietri se aquele caminho era seguro e ele apenas deu um sorriso sinistro dizendo que estava tudo bem já que ele estava lá.\nApós percorrer mais dez minutos, você percebe que o caminho começa a ficar de terra e mal-iluminado e então Dimietri para diante de você - por todo o caminho ele andou em sua frente - e começou a rir, então com uma voz sinistra ele falou "Voces meninas que nunca saíram do colinho do papai não sabem mesmo que não se deve confiar em pessoas que acabaram de conhecer não é" e voltou a rir. Dimietri então começou a se aproximar de você enquanto sacava algo de seu bolso .. uma enorme faca de caça brilhava em sua mão .. \n')
                                                                        esc16 = input('O que você faz?\n1)Fica parada pois não consegue se mexer.\n2)Se vira e corre para longe.\nResposta: ')
                                                                        if esc16 == '1':
                                                                            print('\nVocê não consegue se mover, sua mente simplesmente não consegue entender como alguém que parecia tão bondoso como Dimietri fosse andar com uma faca e ainda mais falar aquele tipo de coisa. Ele se aproxima mais e pergunta se você não vai fugir, você não responde por medo e a cara dele começa a ficar vermelha de raiva e então ele começa a te insultar em russo, você podia não entender, mas sabia que com aquele tom ele só poderia estar lhe chamando de puta e mandando você se foder. Por um longo momento você fica observando assustada ele vociferar aquelas palavras, até que ele começa a se acalmar, ele guarda a faca e então fala que não tem graça brincar com quem não foge dele e vai embora desaparecendo na escuridão a frente de você.\n')
                                                                            esc17 = input('O que você faz?\n1)Senta e começa a chorar.\n2)Volta correndo para a praça.\nResposta: ')
                                                                            if esc17 == '1':
                                                                                print('Tudo aquilo foi demais para você. Você desaba no chão e começa a chorar, sem ligar para mais nada. Na sua mente uma única pergunta passava na sua cabeça era por que tudo aquilo estava acontecendo na sua vida, você tinha uma vaga numa das melhores universidades de toda Grécia, tinha finalmente sua independencia, tinha um lugar só seu e tinha sonhos a serem conquistados. Você abaixou sua cabeça e começou a choramingar baixinho repetindo "por que?" diversas vezes...\n\ne esse foi seu último pensamento antes que você sentisse algo frio entrando atrás do seu pescoço e então escuridão.\n')

                                                                            elif esc17 == '2':
                                                                                print('\nTudo aquilo foi demais para você, mas esperar que ele voltasse isso você não faria. Você então voltou correndo para a praça onde Eros havia te deixado, aquela corrida pareceu que demorou um século, mas enfim você chegou na praça e correu os olhos buscando seu salvador, e lá estava ele, com seu belo corpo totalmente coberto de poeira, você correu chorando para ele mas ele não pareceu te notar, até que você chegou mais perto e entendeu tudo.\nOs olhos de Eros estavam aberto mas não se moviam, seus ouvidos estavam cheios de sangue e ele não respondia a nenhum estímulo... Eros tinha ficado cego e surdo... você se vira para uma enfermeira e pergunta o que aconteceu, ela então explica que um novo bombardeio atingiu o local em que ele estava ajudando, mas que pelo fato de ele estar mais afastado levando mais alguém a bomba não o matou, mas lhe tirou os sentidos da visão e da audição.\n\nOito anos se passaram desde aquele dia horrível, você voltou ao Brasil e trouxe consigo Eros que agora não conseguia mais ser independente. Sua vida não era bem o que você queria, mas ao menos você sobreviveu e por isso agradece aos céus pela oportunidade de estar viva.\n')
                                                                        
                                                                        elif esc16 == '2':
                                                                            print('\nAo ver a faca na mão daquele louco sua reação não é outra que não se virar e começar a correr em direção a praça. Você se virar e começa a correr até que escuta uma gargalhada estrondosa vinda de Dimietri logo atrás de você, ele repetia consigo mesmo enquanto parecia estar extremamente excitado "isso mesmo, assim que eu gosto "suka"" e então ele disparou atrás de você, embora pequeno, ele conseguia bastante rápido e alcançou em instantes. Ele então pula em suas costas tal qual um gato atrás de um pequeno pardal e dá a primeira apunhalada, você cai com a dor e começa a gritar enquanto ele apenas ri da situação, ele se aproxima mais e então te dá outra facada, só que agora no seu peito. Seu sangue quente escorre pelo seu peito e ele ao perceber que você está prestes a perder a consciência começa a te furar cada vez mais, você o olha nos olhos e tudo o que vê é um animal... e essa foi a última coisa que seus olhos puderam ver.\n')
                                                                    
                                                                    elif esc15 == '2':
                                                                        print('\nVocê agradece a intenção de Dimietri mas fala que pode muito bem se cuidar sozinha e que não imagina quem poderia se aproveitar de uma situação de crise como aquela, mas ele apenas só sorri maliciosamente para você e sai de perto. Aquilo foi bem estranho, mas isso não te abalou e você foi perguntar a outra pessoa onde ficava o shopping que estava recebendo os desabrigados. Você avistou uma mulher e foi questioná-la sobre o local, e ela apenas lhe olhou surpresa e perguntou quem havia te dito uma mentira tão descarada como essa, a mulher explicou então que toda a cidade estava destruída, apenas alguns locais abertos como aquela praça ainda estavam intactos.\nVocê espera então por um momento junto daquela mulher que tratava os feridos, mesmo estando totalmente enojada com a situação. Um zumbido então toma o ar e você algo indo direto para onde Eros se encontrava.\n ')
                                                                        esc16_1 = input('O que você faz?\n1)Corre para avisar Eros\n2)Espera com aquela mulher.\nResposta: ')

                                                                        if esc16_1 == '1': 
                                                                            print('\nVocê não pensa duas vezes e começa a correr para onde Eros te resgatou gritando seu nome desesperadamente.\n Você corre por meio de imensas arvores que não lembra de ter passado ali, até que vê ele, heroicamente carregando alguém em seus braços, você apressa seus passos, mas o destino é cruel... Uma das bombas atinge a praça perto de onde vocês estão e então... CLARÃO...SOM DE ARVORE CAINDO... e de repente... uma escuridão total.\n')
                                                                        
                                                                        elif esc16_1 == '2':
                                                                            print('\nVocê continua a olhar apreensivamente para os céus e então pergunta a mulher ao seu lado o que você deveria fazer, "fique AQUI" disse ela num tom sério também olhando para os céus e de repente um clarão não tão longe quase as cegou. Um bombardeio atingiu justamente o local em que Eros estava, você se levanta para correr em busca dele, mas a mulher ao seu lado te puxa e aponta para o céu, diversos aviões estão lançando mísseis justamente nos aviões que bombardearam seu pobre e lindo Eros, destroços começam a cair do céu, e caem justamente em um monte de arvores, derrubando-as. Seu coração não tem mais esperança...\n\nOito anos depois você está de volta ao Brasil, conseguiu terminar seus estudos e publicou um livro de muito sucesso sobre a guerra em que sobreviveu, sua vida foi pacata e feliz desde então...\n')
                                                    
                                                    elif esc_11 == '2':
                                                        print('\nVocê começa a chorar e diz que tudo bem, que ficaria esperando por ele e pede que ele volte o quanto antes. Após a saída de Eros, ainda atônita devido a explosão, você levanta a cabeça e tenta identificar o lugar onde ele te deixou. Era um lugar amplo e bem iluminado, uma praça onde diversas pessoas continuavam chegando e outras corriam para elas com maletas e luvas nas mãos.\nEnquanto tentava esquadrinhar o local, um rapaz ruivo se aproximou de você com a mesma aparência daqueles que ajudavam quem ali chegava e perguntou se ele poderia te examinar, já tirando da maleta um estetoscópio.\n')
                                                        esc_12 = input("O que você faz?\n1)Permite que ele te examine\n2)Diz que não precisa e que você está se sentindo bem\nResposta: ")

                                                        if esc_12 == '1':
                                                            print('Você diz que pode sim, e ele começa a te examinar')

                                                        
                                                        elif esc_12 =='2':
                elif esc2 == '2':
                    print('')

            elif esc1 == '2':
                print('')

        elif esc == '2':
            print('Voce PERDEU seu primeiro dia de aula, e morre quando uma bomba atinge inesperadamente o dormitório onde voce foi procurar refúgio após ter se acorvadado.\n')
						
    elif personagem == '2':
        print('\n--- ESTE PERSONAGEM SÓ ESTARÁ DISPONÍVEL A PARTIR DE 10/06/2020, POR FAVOR AGUARDE ATÉ O LANÇAMENTO --- \n')
			
print('\nObrigado por jogar !\n')
print('-' * 20)
print('CRÉDITOS FINAIS \nDiretor Geral - Álef Ádonis\nProgramador - Álef Ádonis\nRoteirista - Álef Ádonis\nEditor Chefe - Álef Ádonis\n\nUM PEQUENO GESTO PARA DEMOSTRAR MEU AMOR')
print('-' *20)
