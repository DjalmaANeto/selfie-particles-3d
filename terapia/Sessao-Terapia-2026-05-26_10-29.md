# Sessão de Terapia - 26/05/2026

## 🎧 Áudio da Sessão
![[Voz_260526_102949.mp3]]

## Metadados
- **Data Original:** 26/05/2026
- **Horário:** 10:29:49
- **Duração:** 108.5 minutos
- **Arquivo Original:** `Voz 260526_102949.m4a`

---

Abaixo está a organização e transcrição integral do áudio fornecido.

---

### 1. Resumo Geral da Reunião

O áudio registra uma reunião técnica e de alinhamento de processos entre a equipe de desenvolvimento/suporte de sistemas (representada principalmente por Vinícius e Djalma) e a equipe operacional da Secretaria de Educação/Central de Vagas (representada principalmente por Paulinho e colegas). 

O objetivo central do encontro foi mapear e redesenhar o fluxo do sistema da **Central de Vagas** para creches/educação infantil, simplificando o excesso de *status* que vinha gerando divergências em relatórios mensais e chamados de suporte. Durante a conversa, detalhou-se todo o ciclo de vida do aluno no sistema: desde a inscrição inicial realizada pela família no Portal da Comunidade, passando pela etapa de validação/deferimento de documentos (pré-inscrição), inserção na lista de espera/candidatos, convocação/aprovação mediante vagas disponíveis informadas pelas escolas, até a efetivação da matrícula na plataforma SED (Secretaria Escolar Digital). 

Ficou acordada a simplificação dos status, o tratamento de recusas/desistências como desistência formal sem reabertura de ficha, a automatização da baixa de vagas a partir do espelhamento de matrículas da SED (via rotina noturna/*crawler*), além de uma solução emergencial para emissão do relatório consolidado de aprovados do mês de abril utilizando os registros (*logs*) de aprovação do Paulinho.

---

### 2. Principais Tópicos e Temas Abordados

1. **Problemas Atuais e Excesso de Status:**
   - Dificuldade de acompanhamento e divergência de números entre a lista de espera, convocações e relatórios mensais de fechamento.
   - Existência de múltiplos status redundantes em diferentes submódulos que causavam inconsistência quando diretores escolares ou operadores alteravam registros manualmente.

2. **Fluxo do Aluno na Central de Vagas:**
   - **Inscrição/Pré-inscrição:** Pais inscrevem a criança pelo Portal da Comunidade, anexando comprovantes de endereço e certidão de nascimento. O sistema direciona para a turma conforme a idade (Berçário, Maternal) e proximidade (regra geral de 1,5 km, transporte para Bolsa Família).
   - **Deferimento documental:** A equipe da Central de Vagas (Paulinho, Paula, Gabriela) analisa os documentos. Se estiver incorreto/ilegível ou fora do município, a ficha é indeferida e a família deve refazer o processo do zero (garantindo transparência e rastreabilidade na fila).
   - **Lista de Candidatos (Aguardando vaga):** Fichas deferidas ficam ordenadas aguardando a oferta de vagas.
   - **Aprovação / Convocação:** Havendo vaga informada pela creche, o operador (Paulinho) aprova o candidato, movendo-o para a lista de aprovados/contemplados.
   - **Desistência vs. Recusa:** Definição de que a recusa da vaga pela família ou não comparecimento deve ser tratada como desistência, mantendo o registro de que a vaga foi ofertada para prestação de contas com o Ministério Público/publicação oficial.
   - **Matrícula e Integração com a SED:** A escola efetiva a matrícula na SED. Propôs-se a eliminação da necessidade de o diretor alterar o status no sistema da Central de Vagas, integrando a verificação automática via rotina periódica (*crawler*) na SED.

3. **Resolução Imediata para o Relatório de Abril:**
   - Para atender o fechamento pendente de abril (onde o relatório oficial constava 305 aprovações, mas a tela puxava números inflados como 390 por alterações posteriores dos diretores), a equipe técnica puxará o relatório filtrando estritamente os *logs* de ação realizados pelo próprio Paulinho.

---

### 3. Transcrição Completa Organizada por Interlocutor

**Interlocutor 1 (Técnico / Vinícius):** Vamos... os status da Central. Deixar sem nenhum status. Cada status para um submódulo.

*(Ruídos na sala e conversas paralelas ao fundo)*

**Interlocutora 1 (Equipe):** Tá. E...

**Interlocutor 2 (Djalma / Di):** Oi?

**Interlocutor 1:** Ô, eu vou comer aqui... se não conseguir tirar um pedaço... Eu tô morrendo de fome, cara.

**Interlocutora 2:** É que ele tá nervoso, senão teria comprado tudo.

**Interlocutor 1:** Ia ser melhor ainda se você fizesse um de japa.

**Interlocutora 2:** Eu preferia... Às vezes, se viesse um de cada um já tava ótimo.

**Interlocutor 1:** Vocês achavam que era tipo uma simulação, tá ligado? Achavam que era tipo um aplicativo, vocês ligavam lá no Meet e aparecia eu lá com a IA.

**Interlocutora 2:** Mas acredito que vai ter sim uma coisinha ou outra.

**Interlocutor 1:** É, eu vou passar para conversar... Talvez eu tenha que falar com o de cima também. Mas essa... Vamos desenrolar essa Central. Porque a Central...

**Interlocutor 2:** Vou pegar uma água no corredor.

**Interlocutor 1:** Quer pegar uma água? Pega um copo para mim também? Obrigado. A Central é, teoricamente, para ser algo simples que fica muito complicado, tá ligado? Você vê, ó, que eu acho que... Desde que entrou, todo fechamento de mês não deu um problema? Cara, vai continuar sendo assim. Por questão daqueles status, por questão da... da Central não estar resolvendo o fluxo da galera. E qual que é o fluxo? A gente vai descobrir agora, trocando uma ideia junto, melhor.

**Interlocutora 2:** Mas aí o fluxo que vocês querem é: a criança chega, a criança cadastrada, vocês abrem a inscrição, aí vocês aprovam...

**Interlocutor 1:** Tudo. Do zero. Até o que o diretor faz, o caminho feliz, o caminho triste... Pra gente identificar o que que tá tendo de margem.

**Interlocutor 2:** É, vamos... vamos debater esse rolê da história do cara, tá ligado? Tipo assim: como começa a história? Começa com a criança criando uma inscrição, validando... Vamos saber assim: o que que acontece aqui no início, tá ligado? Basicamente, o que a gente anda conversando é que a gente não tem sentido para cada submódulo ter 'N' status.

**Interlocutora 2:** Não, mas tá puxando...

**Interlocutor 2:** Do jeito que tá, não tá atendendo. Sacou?

**Interlocutor 1:** Deu um salve no Paulinho?

**Interlocutor 2:** Não. Acho que...

**Interlocutora 2:** Achei que vocês tinham passado lá.

**Interlocutor 1:** Eu acho válido se vier ele também.

**Interlocutora 2:** Ah, mas você que chegou, você que tem que falar que tá aqui.

**Interlocutor 1:** Ah, não, mas é você que recebe a casa. Geralmente é assim que funciona. Tipo assim, você é a dona da casa, você recebe a gente.

**Interlocutora 2:** Ah, entendi.

**Interlocutor 1:** Obrigado pelo suco, Di. Eu tô muito feliz com esse pãozinho, na moral. Pra mim já é...

**Interlocutora 2:** É muito gostoso.

*(Ruídos de mastigação e movimentação na sala)*

**Interlocutor 1:** Opa, o que que foi isso? Ele tá tentando abrir isso na Matrix? É aqueles buraco maldito? É...

**Interlocutor 2:** Não, vim só no sentido pra cá.

*(Conversa paralela inaudível de fundo entre outras pessoas na sala)*

**Interlocutor 1:** Rua Ernest... O que que tá acontecendo, na verdade?

**Interlocutor 2:** É...

**Interlocutora 2:** O módulo de atribuição tá apresentando coisas... algumas dificuldades. Por exemplo, acabei de falar... Que tem alguns status de servidores que não faz sentido aparecer no módulo de atribuição. Por exemplo, exonerado, se foi remanejado, se é readaptado, enfim... Eles estão aparecendo. Isso de alguma forma acaba impactando a gente no procedimento de atribuição. E quando rolar o processo de remoção, que já é agora em agosto, você tá sabendo agora?

**Interlocutor 1:** É, remoção começa no final do ano.

**Interlocutora 2:** É. Em agosto a gente já começa a movimentação.

**Interlocutor 2:** Sim, muito justo.

**Interlocutora 2:** E aí o sistema precisa estar funcionando para os secretários, para que a gente faça um processo liso, igual a gente fez no setor de compras, por exemplo.

**Interlocutor 1:** Sim. Eu acho válido, acho válido a gente dar uma atenção para atribuição também. É que a atribuição a gente precisa saber o que que tá dando problema. Tipo a Central de Vagas... Aí é mais fácil da gente fechar.

**Interlocutora 2:** Atribuição é isso, por enquanto. São status que não deveriam estar constando na atribuição.

**Interlocutor 1:** Ué, então isso é fácil.

**Interlocutora 2:** Mas é fácil de resolver? Imagina, deve ser muito fácil. E ela me mandou uma questão ontem... Sabe aquele módulo que a gente mexeu de atribuir escolas? Que não tava aparecendo a listazinha da pessoa para poder escolher e você habilitou? Agora o problema parece que tá em AEE. Os AEEs que estão atribuídos nas escolas também não estão aparecendo para escolher.

**Interlocutor 1:** Ah, isso aí é atribuição de escola...

**Interlocutora 2:** A gente mexeu em módulo, agora vai precisar olhar AEE também.

**Interlocutor 1:** O AEE não é atribuído na turma, né? É só na escola. São coisas de boa, aparentemente.

**Interlocutor 2:** É, mas tá bom.

**Interlocutor 1:** Porque a atribuição, cara, é muito difícil ter uma mudança de regra brusca, tipo para mudar o processo.

**Interlocutora 2:** Não, eu acredito que seja mais coisas que estavam funcionando e que estavam caminhando e por algum momento desalinharam.

**Interlocutor 1:** É.

**Interlocutor 2:** Sim. Pô, Di, esse... pelo menos esse negócio de AEE cabe um chamado, tá ligado? Pra gente ter... dar um...

**Interlocutora 2:** Eu ia abrir um chamado, você falou que ia até me ouvir...

**Interlocutor 1:** Não, é... Esse do AEE me parece um chamado.

**Interlocutora 2:** Tá.

**Interlocutor 1:** De qualquer forma, com o chamado aí, se for desenvolvimento também, a gente consegue tipo parar assim, porque ele vai ganhar prioridade.

**Interlocutor 2:** Não, status desenvolvimento. O que tipo assim, funcionava e não tá funcionando, vamos botar como chamado. Sabe por quê? Porque com o chamado a gente para...

**Interlocutora 2:** Mas status também é uma questão assim. A minha cabeça funciona assim, você que me falou: não estava funcionando e está, é chamado. Então o status...

**Interlocutor 1:** Então é chamado! Não, então é chamado, sem dúvida. É chamado.

*(Pausa com passos e movimentação de pessoas)*

**Interlocutora 2:** Você já avisou o Paulinho?

**Interlocutor 1:** Quer que precisa? Eu ajudo lá.

*(Porta abre, passos e conversas de entrada)*

**Interlocutora 3:** Sabem que vocês só vão sair daqui hoje à noite, né?

**Interlocutor 1:** Essa é a intenção, pessoal! Essa é a intenção, ué.

*(Risos)*

**Interlocutora 2:** Eu quero só limpar o lugar que você tá comendo.

**Interlocutor 1:** Beleza, obrigado.

**Interlocutora 2:** É estranho ver o Djalma pessoalmente, não é?

**Interlocutora 3:** Então, eu achei que ele fosse IA!

*(Risos)*

**Interlocutor 1:** É para dar uma melhor qualidade, né?

**Interlocutora 2:** Qual que é? É o Gabriel?

**Interlocutor 1:** Não, esse é o Djalma.

**Interlocutora 3:** Eu achava que ele era uma IA. Eu também não sabia que ele vinha.

**Interlocutor 2:** Grande surpresa! Mas eu vim para escutar vocês mesmo.

**Interlocutora 3:** Ah, então continua a IA! Só para escutar?

**Interlocutor 2:** Tô obrigado a isso.

**Interlocutora 3:** Você tá para escutar e resolver nossos problemas, todos!

**Interlocutora 2:** Na agilidade de uma IA.

**Interlocutor 1:** Essa é a intenção!

**Interlocutor 2:** A intenção é resolver melhor, né? Que a IA geralmente resolve meio estranho.

**Interlocutora 3:** É. Hoje não era para ser a Central de Vagas?

**Interlocutora 2:** É, mas aí a gente já quer aproveitar que estão os dois e já...

**Interlocutor 1:** A Central a gente vai estender um pouquinho. Talvez se vocês quiserem... A gente vai dar um sinal para vocês, porque a Central a gente vai passar passo a passo. Porque ela tá dando um pouquinho de dor de cabeça.

**Interlocutora 3:** Então, quando vocês terminarem, vocês me chamam?

**Interlocutor 1:** Chamo a Ju.

**Interlocutora 3:** Me chamem, que eu fico ali na minha sala.

**Interlocutor 2:** Não, mas é bom acompanhar os dois...

**Interlocutora 3:** É só para não ficar muita gente.

*(Conversa paralela de saída da sala)*

**Interlocutor 2:** O pessoal tudo animadão.

**Interlocutor 1:** Pessoal tá animado, você viu?

*(Barulho de passos, portas fechando e preparativos de tela)*

**Interlocutor 1:** Ô, Paulinho?

**Paulinho:** Beleza? Tudo certo?

**Interlocutor 1:** Beleza, tudo bem?

**Interlocutora 2:** As meninas vêm?

**Paulinho:** A Josi tá vindo. Só passar aqui no banheiro.

**Interlocutora 2:** Tá bom. E daí...

**Interlocutor 1:** Não, a gente pode ir no outro dia para... porque sobrou planejamento...

*(Conversas paralelas e ruídos de cadeiras se acomodando)*

**Interlocutor 1:** Bom, o intuito da reunião de hoje é a gente falar um pouquinho sobre a Central de Vagas. A gente vê que a Central de Vagas ela tá... tá enfrentando bastante dificuldade, a gente tá tendo bastante chamado sobre ela. Chega final do mês, abre chamado; final do mês vocês tão precisando de um número ali e a gente não tá conseguindo acompanhar. E a construção da Central de Vagas foi há 5 anos atrás e a gente não sabia muito bem, a gente não concebia muito bem o que era uma Central de Vagas no momento. Hoje a gente é muito mais experiente com o trabalho junto, né, com o conjunto de vocês, do que que é a Central de Vagas, como que funciona, como que tem que ser. Mas ainda assim, o que que a gente tá propondo? Dar uma refatorada na Central de Vagas, ajustar ela para que não tenha esse tipo de problema. E para isso eu queria ouvir um pouco de vocês o passo a passo mesmo, do zero, do que que é feito, o processo da Central de Vagas. Porque daí eu vou fazendo algumas perguntas e aí a gente vai encaixando no que que a gente tá errando, para parar de dar esse tipo de chamado. Porque assim: vem sendo cansativo para vocês, a gente sabe; vem sendo cansativo pra gente, que a gente também mexe ali e às vezes não resolve. Então falei: vamos fazer uma reunião, vamos enfrentar o problema lá na raiz lá, pra gente parar de ter esses erros, pra não ter mais essa recorrência de chamado. Então a proposta de trazer o Djalma... porque o Djalma é o responsável pela Central de Vagas e também pelo Recursos Humanos. Então a maioria dos chamados é o Djalma que atende, a maioria dos desenvolvimentos é o Djalma que atende. Então falei: "Djalma, vamos lá comigo pra gente conversar com eles pra gente conseguir conceber uma ideia". Então assim, começar de verdade do zero na Central de Vagas. Com o máximo de detalhes que vocês conseguirem passar pra gente: como que é feito, em que momento que vai pro diretor, se quando chega no diretor pode devolver... Mas vamos começando devagarzinho. Pode começar do... bem do princípio mesmo. A gente sabe como que funciona, mas eu falei: vamos escutar deles lá também, pra gente parar de tirar deduções, né? Vamos ouvir do Paulinho lá.

**Paulinho:** Tá certo. Então a gente pode começar desde quando a mãe faz a inscrição?

**Interlocutor 1:** Pode, por favor.

**Paulinho:** Bom, então... quando a mãe faz a inscrição, ela vai escolher a escola e a turma, né? Na verdade, a própria idade já... já direciona pra qual é a turma, se é Berçário ou se é Maternal, né? Porque o sistema já tá fazendo isso, né? Ela coloca a data de nascimento e o sistema já fala: é Berçário, é Maternal. Então ele já filtra ali e já é pra escolher uma escola. Aí a mãe vai e escolhe a escola: Berçário, por exemplo; aí escolhe a escola EMEB Zilda, por exemplo, né? Maravilha. E aí ela coloca todos os dados, coloca os documentos e vem pra... e vem pra gente aqui deferir.

**Interlocutor 1:** Tá. Eu posso ir fazendo algumas perguntas? Aqui vocês têm limitação pra quilometragem, né?

**Paulinho:** Temos.

**Interlocutor 1:** Tá. Dependendo do CEP, ele é limitado pra escola. E quantas escolas que aparecem de opção, você lembra? Eu não lembro da regra daqui.

**Paulinho:** Então, a regra daqui é 1,5 km, mas é mais pros ensinos fundamental e infantil.

**Interlocutor 1:** Aham.

**Paulinho:** A gente também tá tendo alguma coisa na creche, na questão dos... dos alunos que participam do Bolsa Família. Então a criança que participa do Bolsa Família e está acima de 1,5 km, elas vão ter o benefício de ter um transporte.

**Interlocutor 1:** Entendi.

**Paulinho:** Então essa é a... é a regra em questão da creche.

**Interlocutora 2:** E o benefício ali é o transporte que a própria rede disponibiliza ou é aquele passe livre da mãe?

**Paulinho:** É o... no caso, a... a criança vai... a família vai comprovar que está a 1,5 km e eles vão receber o passe.

**Interlocutor 1:** Maravilha. Aí, da inscrição, ele já cai pra vocês...

**Paulinho:** A mãe finalizou a inscrição, foi no botãozinho lá, colocou lá que fez a inscrição, já aparece aquele papel lá de que... de que foi... é... deu tudo certo, né? Ela imprime o comprovante, aí aparece pra gente... o... pra... pra nós, né? Eu, a Paula e a Gabriela, pra fazer o deferimento.

**Interlocutor 1:** Tá.

**Interlocutora 2:** Paulinho, isso em pré-inscrição, né? No submódulo de pré-inscrição.

**Paulinho:** Exato. No submódulo de pré-inscrição.

**Interlocutor 1:** Na hora que faz a inscrição, ela já aparece lá na pré-inscrição. Nesse momento, você confere a documentação?

**Paulinho:** Isso.

**Interlocutor 1:** Você faz toda a conferência da documentação? Você pega ali uma inscrição e vê se o documento de comprovante de endereço condiz com o que ela tá pedindo?

**Paulinho:** Exato. É isso. O nome, a data de nascimento... Porque a mãe às vezes digita lá a data de nascimento do irmãozinho.

**Interlocutor 1:** Uhum.

**Paulinho:** Sem querer, às vezes, né? E aí a gente olha lá: "Opa, a certidão de nascimento tá marcando que é uma... que é a data tal". Então a gente vai no que tá na certidão de nascimento.

**Interlocutor 2:** Sim.

**Paulinho:** Por isso que a gente precisa deferir.

**Interlocutor 1:** Entendi.

**Paulinho:** E às vezes não tem... ou às vezes não colocam o comprovante de endereço da casa...

**Interlocutor 1:** Sim. E quando você indefere isso aí? Quando você fala: "Putz, peguei um comprovante de endereço e tá um outro endereço"? Qual que é a sua ação?

**Paulinho:** Aí a gente entra em contato com a família e fala: "Ó, o endereço daqui tá... é... tá de Morato, Francisco Morato. Então a gente vai indeferir pra vocês, porque é só de Franco da Rocha". Ou, por exemplo, a mãe coloca a certidão de nascimento ilegível, ou qualquer outro documento ilegível. Aí a gente também pede pra... a gente indefere. Ou a mãe coloca um outro documento que não tem nada a ver.

**Interlocutor 1:** Só anexa qualquer coisa.

**Paulinho:** Só anexa qualquer coisa. Aí às vezes não consegue, não sabe...

**Interlocutor 1:** Entendi. Aí vocês indeferem, vocês mudam o status pra 'Indeferido'? O que que vocês fazem de ação ali naquele momento?

**Paulinho:** É, tem o botãozinho do lado. A gente indefere, entra em contato com ela, ela entra pelo Portal da Comunidade e ela faz a atualização dessa ficha...

**Interlocutor 1:** Não...

**Paulinho:** Aí o que que a gente faz? A gente fala assim: "Olha..." A gente pede pra elas mandar por e-mail pra gente, a gente tem o nosso e-mail institucional, os documentos corretos, e nós mesmos fazemos a... a substituição.

**Interlocutor 1:** Aí você usa a mesma ficha que tava indeferida e você muda o status dela? Pra deferida?

**Paulinho:** Exato. Uhum. Ou quando tá indeferido, a gente pede pra fazer uma nova inscrição e dá certo também. A mãe vai lá e faz uma nova inscrição e coloca os documentos.

**Interlocutor 2:** Essas indeferidas, vocês têm um tratamento pra elas assim? Elas são consideradas indeferidas e daí elas ficam no cantinho lá, na tela das indeferidas? Existe a... igual você falou, quando chega por e-mail a documentação correta, existe o cenário então onde essa inscrição ali é editada e ela passa pra outra listagem? Ela pode ser que não acabe ali?

**Paulinho:** É, pode ser que ela não acabe ali, pode ser uma segunda chance. Exato.

**Interlocutor 1:** Tá, então só pra eu recapitular: pode chegar uma ficha pra você que você pega ali e ela não tá com a documentação correta, você indefere ela. Aí você tem dois caminhos dentro da plataforma: um que você entra em contato com ela e usa a mesma ficha que você já indeferiu, que você muda o status lá pra deferida, ou você pede pra ela fazer outra. Em qual cenário que se encaixa um e outro assim? Ou é meio que tipo... Como que você toma essa decisão de indeferir de vez uma ficha ou falar: "Não, faz de novo"?

**Paulinho:** Então, o indeferimento a gente já indefere na hora que a gente vê que tem algum problema.

**Interlocutor 1:** Sim.

**Paulinho:** Aí vai depender do que a gente vai conversar com a mãe. Se a mãe falar assim: "Ah, olha, eu não tô aqui... eu não consigo mandar por e-mail agora, não dá... mas eu vou entrar mais tarde e fazer a inscrição novamente". Ou a mãe fala: "Não, eu já tenho aqui, eu vou mandar pra vocês".

**Interlocutor 1:** Tá. Porque eu não acho muito viável a gente ter esses dois caminhos dentro da plataforma. Porque pode ser que em algum momento isso aí pode perder alguma rastreabilidade. O ideal seria a gente definir agora um ponto do que que vai ser feito com essas indeferidas. Vai ser sempre uma ficha nova que ela vai ter que fazer? Vai ser sempre uma... a edição que vocês vão fazer? Eu acho que a gente fecharia mais a possibilidade de começar a dar problema, que é o intuito que a gente tá fazendo nessas reuniões. Que assim: se a gente vai deixando mais abas abertas, mais problemas podem acontecer de status, de mudança de... Aí a gente poderia definir um caminho fixo, assim: "Ah, não, indeferiu, a gente vai usar a mesma ficha? Não, indeferiu, vamos orientar ela a fazer uma nova".

**Paulinho:** É, a gente orienta a fazer uma nova. Pode ser essa... esse caminho.

**Interlocutor 1:** Então... Porque aí a gente usa a indeferida como realmente indeferida. Acabou. Acabou a jornada ali, não tem mais como avançar a partir da indeferida.

**Paulinho:** Porque aí, no caso, são dois trabalhos nossos, pra gente, se a gente fizer isso que tá fazendo já de substituir.

**Interlocutor 1:** Mas aí eu tenho uma pergunta: se ela faz a solicitação, a primeira solicitação é por conta de questão de prioridade. Então se ela faz às 10h da manhã e vocês indeferem, quando ela faz uma outra, ela vai perder a prioridade, correto?

**Paulinho:** Correto. Ela só vai valer a quando ela fizer que tá correta.

**Interlocutora 2:** A primeira, né?

**Interlocutor 1:** Então, porque daí a gente cai na regra da primeira ficha...

**Interlocutora 3:** Espera aí, ô Paulinho, eu não acompanhei. A pessoa fez a inscrição a primeira às 10 horas da manhã. Às 14h ela faz outra. Valida a primeira ou a segunda?

**Paulinho:** Ah, tá. No caso, a gente... valida a segunda, porque é a que tá correta.

**Interlocutora 3:** Ah, tá, quando ela retifica.

**Paulinho:** É. Porque a gente tá falando no caso de quando a gente indefere. Porque se a gente fizer a de 10 horas, vai tá errada.

**Interlocutor 1:** Isso. É responsabilidade do responsável também fazer a documentação correta, né? Então não dá pra lesar outros por conta disso. Maravilha. Então a gente vai seguir o caminho aqui de o indeferimento ser indeferido, a gente não vai alterar mais essa ficha.

**Paulinho:** Sim. Aí a mãe faz novamente. A gente liga pra mãe: "Ó, precisa fazer novamente, porque você entregou..." Que a gente tá fazendo assim: a gente tá pegando e liga pra mãe e fala assim: "Ó, mãe, tá faltando a certidão de nascimento legível. Você poderia mandar uma foto pra gente no nosso e-mail que a gente faz a substituição aqui?" A gente tá fazendo isso. Mas aí agora a gente tá decidindo que, ao invés de fazer isso, a gente já pede pra mãe fazer um novo registro com a certidão legível.

**Interlocutor 1:** Tem sentido?

**Interlocutor 2:** Eu posso só trazer uma questão? Assim, a gente pode definir sem problema a gente optar pela inscrição assim... ter uma nova toda vez, mas essas novas inscrições, elas não vão afetar em alguma contabilidade de vocês? Em algum relatório mensal, algo assim? Porque pensa: se a gente olhar agora para as indeferidas, vai ter o mesmo nome de aluno de uma inscrição aprovada ou então de uma pré-inscrição aguardando deferimento. Se esse cenário não tiver problema algum, não tem problema mesmo. Mas se começar a aparecer assim: "Poxa, mas tipo assim, vamos supor, deu 50 inscrições, metade disso foi indeferida, outra metade tá aguardando deferimento, só que tem o mesmo aluno nas duas, então devia considerar 49..." Se isso acontecer...

**Interlocutora 3:** Mas a gente não consegue invalidar a primeira e ela sair do sistema?

**Interlocutor 1:** É bom a gente ter esse registro, na verdade. Eu acredito que seja bom assim... para registro. Para vocês terem ali: "Putz, cara, ó, a gente tá ofertando a vaga cinco vezes para essa mãe, as cinco vezes ela tá anexando o documento errado na ficha do estudante". Eu acho que isso não interfere no cálculo deles. Porque assim, a gente vai considerar que o indeferido é uma ficha que não avançou. Foi indeferida a documentação.

**Interlocutora 3:** Ah, tá, daí ela fica num banco ali...

**Interlocutor 1:** Isso, a gente deixa ela só indeferido, paradinho.

**Interlocutor 2:** No indeferimento já tem uma observação, inclusive. A gente pode seguir essa linha onde pode colocar uma observação no indeferimento ou deferimento, para ter essa justificativa. Assim: "Ah, a mesma inscrição que parece indeferida, ela aparece como deferida. Isso tem alguma justificativa?" A gente pode ir atrás, a gente conseguiria ir atrás disso.

**Paulinho:** E quando vai para o botão pré-inscrição, é... se a gente... enquanto a gente não defere, ele vai ficar lá como 'Aguardando Deferimento'.

**Interlocutor 2:** Isso. Eu acho que seria manter essa dinâmica. O indeferimento acontece essa ação de vocês, sabe? Vocês fazem essa ação com a análise de vocês e daí a inscrição segue.

**Paulinho:** Lembrando que o que vai para a lista de espera é só os deferidos.

**Interlocutor 1:** Isso, exatamente! Não contabiliza. É só no conceito de informação. Se a gente for consultar: "Pô, o Paulinho, cinco vezes aqui, eu lembro dele, mas por que que não tava avançando?" Aí vocês colocam o comentário: "Ó, comprovante errado, comprovante de endereço errado". E aí vocês conseguem rastrear e talvez até orientar a mãe, falar: "Mãe, ó, teve cinco inscrições suas aqui que a gente não passou. O que que tá acontecendo isso, né? O que que tá errado aqui?" Só uma dúvida: ela já chega na pré-inscrição com o status de 'Aguardando Deferimento'?

**Paulinho:** Aguardando deferimento, exatamente. Quando chega pra gente lá que a Paula e a Gabriela fazem, tá lá: 'Aguardando Deferimento'.

**Interlocutor 1:** Caiu pra vocês, é esse status.

**Paulinho:** Deferido. Ainda não faz parte da lista de espera.

**Interlocutor 1:** Sim. Quando cai na pré-inscrição, você altera o status? Você entra na ficha do estudante lá e faz a alteração de status?

**Paulinho:** Não, só quando... Depois de conferir, tem o botãozinho lá embaixo de 'Deferir' ou 'Indeferir'. Aí você coloca deferir, aí já vai pra lista. Não entro naquela partezinha lá de cima lá que... daquele status lá no começo da tela. A gente só faz naquela lá de baixo.

**Interlocutor 2:** Lida somente com aquela ação. O status mesmo...

**Interlocutor 1:** Legal. Porque a gente já pode matar inscrição por status. Ter um status só, que é o 'Aguardando Deferimento' da inscrição, não ter mais nenhum outro status. Pra gente não abrir margem pra ter erro de status. Então a gente vai até sumir com aquele botão de status... Não precisa sumir não, mas a gente deixa só ele de opção ali.

**Interlocutor 2:** É, a gente pode ir simplificando, na verdade, essas etapas. Porque igual: na pré-inscrição, se a gente abrir ela agora ali, uma inscrição que tá na pré-inscrição, você pode mudar ela direto pra 'Matriculado'.

**Interlocutor 1:** É, e isso acaba ocasionando pra erros.

**Interlocutor 2:** Isso pode... não ser tão legal.

**Paulinho:** Porque se colocar direto pra matriculado lá no status, ele nem entra...

**Interlocutor 1:** Ah, não, pra matriculado não. A gente pode definir o quê: que a inscrição caiu na pré-inscrição, igual é hoje em dia, 'Aguardando Deferimento', e deixar só o 'Aguardando Deferimento'. O que que vocês acham? A não ser que vocês aprovam, aí avança; ou indefere.

**Interlocutor 2:** Isso, que é uma lista que não contabiliza, só no conceito de informação.

**Interlocutor 1:** Maravilha. Então só recalculando: inscrição cai, faz o processo de conferência; o indeferimento a gente vai refazer a ficha, vai orientar a refazer uma ficha pra gente ter essa informação; e quando defere? Quando você fala assim: "Putz, tá certinha a documentação, 100%, tá mil feliz"?

**Paulinho:** É isso. Aí a gente vai e defere. Aperta no botãozinho lá de deferir e já cai exatamente na lista da creche que a pessoa escolheu.

**Interlocutor 1:** 'Solicitação Aprovada'?

**Paulinho:** Não, isso ainda não. Isso ainda não é a solicitação aprovada ainda.

**Interlocutor 1:** Maravilha. Então deferiu, ele cai na lista de...

**Paulinho:** Lista de espera da creche. Ó, aí vai cair... Vamos supor: a gente acabou de fazer uma inscrição e cai aqui, ó, na 'Lista de Candidatos'. 'Lista de Candidatos', tá? Pode abrir. Deixa eu ver...

*(Navegando no sistema)*

**Paulinho:** Ó, por exemplo, aqui vamos supor que a gente acabou de deferir a Laura.

**Interlocutor 1:** Maravilha. Então a Laura veio pra cá.

**Paulinho:** Sim. E ele fica no 'Aguardando Vaga Disponível'.

**Interlocutor 1:** O status 'Aguardando Vaga Disponível', o que que ele significa pra você? É que deu certa a documentação, você viu que a ficha tá pronta e só tá aguardando uma vaga da creche? É só nesse cenário que se enquadra?

**Paulinho:** Exato. Porque aí ela compõe a lista de candidatos.

**Interlocutor 1:** Tá. Em algum momento você altera esse status aí quando ele tá na lista de candidatos?

**Paulinho:** Por exemplo, hoje, um exemplo: vou fazer uma chamada de duas crianças no Cecília Meireles, por exemplo. Aí eu vou olhar lá: "Opa, tem duas crianças". Então eu vou chamar a Yonara e a Laura. Eu vou clicar aqui no verdinho, no 'tiquezinho' aqui, ó.

**Interlocutora 2:** 'Aprovar Inscrição'.

**Paulinho:** Isso. É isso aí que aprova, que aparece lá nas ações da escola. E a escola consulta e verifica que a gente chamou a Yonara e a Laura.

**Interlocutor 1:** Tá. Então aqui o 'Aguardando Vaga Disponível' é na lista de candidatos. Então em algum momento você consegue declinar isso aí? Cancelar com aquela ficha e falar: "Putz, cara, surgiu uma vaga da Laura, mas ela não quer"? O que que você faz nesse momento?

**Paulinho:** Ah, tá. Então, isso tem um detalhe.

**Interlocutor 1:** Ou se ela não quer, ou se tem uma outra negativa que pode acontecer nesse meio-tempo. Porque você aprovou a ficha, você viu que a documentação tá legal. Então ela tá agora esperando uma vaga. O que que pode acontecer de ruim nisso aí, tipo assim, de dar errado a jornada?

**Paulinho:** É, por exemplo: se não surgir nenhuma vaga na escola Cecília Meireles, até o final do ano ficar zerado de vagas lá, essa criança vai ficar o ano inteiro na fila de espera. Na lista de candidatos.

**Interlocutor 1:** Com o 'Aguardando Vaga Disponível'.

**Paulinho:** Exato.

**Interlocutor 1:** Tá. Então essa mudança de status aqui só vai acontecer quando a escola Cecília Meireles apontar que tem uma vaga? Positivamente, é o caminho feliz.

**Paulinho:** Isso, isso.

**Interlocutor 1:** Tá. E se ela desiste?

**Paulinho:** Se a criança desiste... Se a criança desiste, a mãe liga aqui: "Olha, mudei para Morato". A mãe da Laura liga aqui e fala assim... da Yonara. A mãe da Yonara liga aqui e fala assim: "Olha, eu não quero mais a vaga. Você pode tirar. Ela não é mais a primeira da lista, não quero". Aí a Laura vai virar a segunda... virar a primeira. Aí o que que a gente faz? A gente copia o nome da Yonara e vai lá no outro botão lá... Porque por aqui, ó, não dá pra gente fazer o que eu tô dizendo, o que eu tô querendo mostrar. Porque quando a gente olha no olhinho nessa parte aqui, a gente só consegue ver a situação dos dados do cadastro. Então o que que a gente faz? A gente copia, vem aqui, ó, em 'Inscrições'...

**Interlocutora 3:** Gente, eu vou deixar vocês aí, depois eu volto. Porque eu acho que esse problema não vai resolver agora, então eu vou almoçar. Depois eu volto.

**Interlocutor 1:** É o que eu falei: vai ser bem passo a passo mesmo.

**Interlocutora 3:** É. Depois eu volto.

*(Interlocutora 3 sai da sala)*

**Paulinho:** Vem em 'Inscrições'... Aí nessa parte aqui que a gente vai ter o acesso às demais funções. Vem aqui nas ações...

**Interlocutor 1:** Tá. Lembrando que a inscrição, ela cai no... 'Lista de Candidatos' e 'Inscrições' é a mesma coisa?

**Paulinho:** É a mesma coisa.

**Interlocutor 1:** Beleza, é só visualizações diferentes. Então aqui é o 'Aguardando Vaga Disponível'.

**Paulinho:** Não, as 'Inscrições' é que assim: na lista de candidatos tá dividido em creche e por turma. As inscrições é geral, o total de todas as crianças. Inclusive as que já foram realizadas no ano passado, aparecem todas.

**Interlocutor 1:** Maravilha.

**Paulinho:** Então aqui tem essas opções, né? Aí a gente desce... Aqui tem os telefones, a escola pega o telefone, liga, ou então pega o e-mail e manda um e-mail. Aí vem... e aqui a gente não mexe em nada. Só sobe lá...

**Interlocutor 1:** Tem que editar.

**Paulinho:** Desceu. Isso, ó. Aqui tem esses status aqui: 'Pré-matrícula', 'Rematrícula', 'Transferência'... Mudou, né?

**Interlocutora 2:** É aqui embaixo, não é, ó?

**Paulinho:** Ah, é aqui. 'Aguardando Resposta do Responsável', 'Aguardando Matrícula', 'Matriculado', 'Aguardando Conferência', 'Indeferido'. Por exemplo, o menino vai e leva a documentação, eles fazem a matrícula e cadastram na SED. Esse é a matrícula mesmo. Então o ideal é que a escola venha aqui e coloque pra 'Matriculado'. Se por acaso a mãe não quer a vaga, aí ela vem aqui nesse... 'Indeferida'.

**Interlocutor 1:** Que é esse caminho que a gente tá fazendo agora.

**Paulinho:** É. Então, aí esse 'Indeferida' aqui, pra gente não confundir com aquele... Porque aquele 'Indeferida' é o nosso, aquele primeiro da primeira parte é o nosso. Essa daqui, se vocês quiserem mudar esse botãozinho aqui pra não confundir com o outro, eu acho interessante: 'Mãe não aceitou', alguma coisa... algum termo nesse sentido.

**Interlocutor 1:** É, na verdade essa jornada já tá um pouquinho errada, acredito eu. Porque o ideal seria o quê? Na lista de candidatos você já conseguir fazer o indeferimento ali por motivos que a mãe recusou. Nessa jornada, nessa etapa, o único motivo do caminho não ser feliz é porque a mãe não quer. Porque a parte da documentação já deu certo. A gente já poderia condicionar naquele status de lista de candidato essa ação do indeferimento da mãe. Aí a gente pode mudar para uma nomenclatura que seja de acordo: 'Mãe desistiu', alguma coisa assim. Porque a gente sabe que da escola, ela vai ficar naquele mesmo status, ela não vai avançar para um outro status. Não vai ter uma negativa da escola.

**Interlocutor 2:** Mas na lista de candidatos tem ação de indeferimento. Essa ação de indeferimento então ela não atende à ação feita na escola, na secretaria?

**Paulinho:** Essa lista de candidatos só eu tenho acesso. Porque só eu que faço a aprovação. Eu que faço a aprovação dos alunos que conseguem a vaga. Nesse caso aqui a gente tá falando de uma mãe que quer desistir.

**Interlocutor 1:** Sim. Pode ser uma desistência.

**Paulinho:** É, desistência da família. Trocar esse termo 'Indeferido', senão vai confundir com aquele outro.

**Interlocutor 1:** É, na verdade a gente vai ter um lugar para o indeferimento de inscrição e uma desistência da mãe. Vão ser coisas diferentes. Tem sentido?

**Interlocutor 2:** Sim. No caso a mãe desistiu porque...

**Interlocutor 1:** Desistiu. A gente tira esse 'Indeferido' daí e coloca um 'Desistiu'. Porque daí, pelo que eu vejo, quando ele chega no status de 'Aguardando Vaga Disponível', só tem um caminho pra seguir, que é o caminho feliz: a escola disponibilizar uma vaga, que é o único status, 'Aguardando Vaga Disponível'. E o desistente, que é a mãe, que é o caminho triste. É só essas duas condicionantes que tem. Não tem mais para onde avançar, não tem um status que mude mais. Correto?

**Paulinho:** Uhum.

**Interlocutor 1:** Então 'Indeferir se a mãe recusa', que vai ser o desistir.

**Paulinho:** Aí, por exemplo, se a gente continuar nessa tela, a gente pede para que o coordenador da secretaria justifique. Por exemplo: "A mãe ligou tal dia e falou que não quer porque mudou para Morato", ou "A mãe não compareceu na data que a gente marcou a vinda aqui na escola". Então a gente usa muito isso aqui, as observações.

**Interlocutor 1:** Beleza. Se a mãe não desistiu, é porque eles só mudam o status de 'Aguardando Vaga Disponível' caso tenha uma vaga disponível na escola.

**Paulinho:** É, porque aí no caso, quando fez a matrícula de fato, que a mãe foi lá e cadastrou na SED, aí é o que a gente considera como matriculado.

**Interlocutor 1:** Fechou. Quando a mãe desiste, a gente vai ter o status para desistência da mãe. Essa ficha pode voltar algum momento? Pode ter tipo a mãe: "Nossa, cara, deu ruim a minha viagem aqui e eu preciso voltar pra fila"? Você orienta ela a fazer uma nova inscrição ou vai ser condicionada a fazer uma nova?

**Paulinho:** É, faz uma nova inscrição. Aí a gente precisa... fazer uma nova inscrição no sentido assim, de quando a mãe volta... Isso já é feito: quando coloca o CPF da criança que a criança já tem inscrição, a mãe não consegue fazer uma nova inscrição sendo que já tem uma outra inscrição. Por exemplo, tá na creche Cecília Meireles e quer fazer uma... "Ah, tá mais pertinho, quero deixar na lista de espera do Guido", por exemplo. Isso já acontece, já tem essa trava. Então a única forma da mãe não conseguir fazer a inscrição é o que já acontece, que é quando já tem...

**Interlocutora 2:** Quando já tá matriculado.

**Paulinho:** Aí o que que acontece também: a mãe da Yonara não quer mais na lista de espera do Cecília, quer ficar na lista de espera da EMEB Guido. Aí nós cancelamos pra ela.

**Interlocutora 2:** Cancela a inscrição.

**Paulinho:** Nós cancelamos a inscrição. Ela liga aqui e fala assim: "Olha, não quero mais. Eu quero mudar de creche, mas eu não tô conseguindo porque já tem uma inscrição". Então a gente cancela. Nós aqui cancelamos.

**Interlocutor 2:** Ah, isso é interessante também. Como vocês tratam as edições dessa ficha, né? As edições dela é importante.

**Paulinho:** É, digamos só quem tem o poder de cancelar é a gente. Porque senão... se a gente deixar pra que a mãe cancele, qualquer pessoa vai cancelar: "Opa, tem três crianças na minha frente aqui, vou cancelar a primeira, segunda e a terceira".

*(Risos)*

**Paulinho:** Tem que ser só nós mesmos.

**Interlocutor 1:** Beleza.

**Interlocutor 2:** Então a gente avançou até a lista de candidatos, né? Da pré-inscrição até a lista de candidatos. Depois disso, tem essa daqui, ó, que tem dado problema, que é a lista de aprovados.

**Interlocutora 2:** Mas você vê que agora, passando passo a passo, vocês já entendem mais os status que a gente tá filtrando ali, né? Tá bem mais claro.

**Interlocutor 1:** Ó, mas deixa eu só recapitular aqui, Di, só um minutinho. Caiu na lista de candidatos, a gente tem uma tomada de decisão de a mãe poder desistir. E aí se ela desistir, ela pode fazer uma nova inscrição caso ela se arrependa, ou ela só desiste ali. E quando ele avança? Quando tem uma vaga disponível? Quando deu o caminho certo ali?

**Paulinho:** Quando deu o caminho certo, aí a escola sinaliza que tem a vaga. Eu vou lá na lista de candidatos e na lista de candidatos eu vou no negocinho verdinho de aprovar. Aí eu vou nesse de aprovar. Aí eu aprovo, só eu aprovo.

**Interlocutor 1:** Beleza, só você tem esse controle. Esse 'Aprovar', ele vai pra onde?

**Interlocutora 2:** Deveria ir para 'Solicitações Aprovadas', né?

**Paulinho:** É, isso.

**Interlocutor 2:** É, aquelas solicitações aprovadas têm esse defeito atualmente. Tem muitos status que consideram nela lá, sabe? E alguns deles não seguem esse caminho. Por isso que...

**Interlocutor 1:** É, vamos remover eles.

**Paulinho:** Essa daqui acho que é a mais importante, por quê? Depois que a gente aprova, a gente no final do mês precisa publicizar. Na publicização a gente coloca todas as crianças que foram aprovadas durante o mês. Então, por exemplo, esse mês foram... mês de abril foram 305.

**Interlocutor 1:** Mas aprovadas que conseguiram vaga, então?

**Paulinho:** Conseguiram vaga.

**Interlocutor 2:** Esses aprovados, eles todos têm matrícula? Têm garantia de matrícula?

**Paulinho:** Todos eles têm garantia de matrícula. Se por acaso a Yonara não fez a matrícula, de qualquer forma fica registrado que a vaga foi disponibilizada. Se ela não fez, é problema dela.

**Interlocutor 1:** Tá. Deixa eu pensar um cenário aqui em que deu certo, conseguiu a vaga, só que a mãe desistiu. Ele contabiliza ainda? Porque o status desistência a gente tem que pensar se ele vai contabilizar na solicitação aprovada ou não. Porque o status desistência é: passou por você, você aprovou, você conseguiu uma vaga pra ela e a mãe desistiu por qualquer motivo. Ela tem que contabilizar na solicitação aprovada? Porque você conseguiu essa vaga, a vaga foi disponibilizada.

**Paulinho:** Não... Ela tem que... Mesmo que ela tenha desistido depois, ou não tenha conseguido contato com a mãe, o nome dela tem que estar registrado lá nessas... nesses aprovados.

**Interlocutor 1:** Beleza. Então o status 'Desistiu' vai ter que aparecer no aprovado também. Correto?

**Paulinho:** É, na verdade não digo o status, mas o nome da lista...

**Interlocutor 1:** Ah, não. É porque assim: a gente tá limitando e tá condicionando os status. Então nesse momento a gente vai ter o quê? Vai ter o status de desistiu da mãe e o status que você muda ali, que é o 'Aprovar Inscrição'. Vai ter esses dois caminhos. Pra esses dois caminhos, eles vão ter que exibir na solicitação aprovada, mesmo que a mãe desistiu. Pegou?

**Interlocutor 2:** Sim, sim.

**Interlocutor 1:** Aí eu acho então que o status desistir vai ter que compor a lista de solicitação aprovada.

**Paulinho:** Assim, mas pensando na publicidade, isso não precisa aparecer.

**Interlocutor 1:** Não vai aparecer 'Desistiu', vai aparecer o nome dela.

**Paulinho:** Vai aparecer, por exemplo, o nome da Yonara vai aparecer lá que a gente chamou.

**Interlocutor 1:** Exatamente. O 'Desistiu' não aparece os status, vai aparecer só que a Yonara desistiu da vaga e ela vai aparecer que você ofertou.

**Paulinho:** E aí o que a gente precisa só...

**Interlocutor 1:** Mas aí eu tenho uma outra dúvida que me surgiu aqui: a gente tá pensando num caminho em que você ofertou a vaga pra mãe da Yonara e ela desistiu. Você conseguiu essa vaga pra ela e ela desistiu. E agora uma outra coisa que eu vou levantar aqui: e se ela desiste antes de você conseguir uma vaga?

**Paulinho:** Então, é aquela outra parte que a gente tava falando de quando a gente cancela porque mudou pra outro município ou foi pra outra creche.

**Interlocutor 2:** Deveria ser tratada como indeferida nesse caso, né?

**Interlocutor 1:** Então a gente permanece o status de indeferida quando tiver na lista de aprovados? É isso que eu tô tentando fechar mais.

**Interlocutora 2:** Porque ela nem foi contemplada ainda pra lista de aprovados.

**Interlocutor 1:** Não, ele já aprovou... Ele já aprovou a documentação, deu tudo certo. Ela tá aguardando vaga disponível agora.

**Interlocutor 2:** Uma ação que é importante é esse clique aqui, ó: 'Aprovar Inscrição'.

**Interlocutor 1:** Não, sim. Entendi, ó. Mas pensa comigo: ele viu a documentação, deu tudo certo. 'Aguardando Vaga Disponível', tá nesse status. A gente tem o cenário em que você consegue essa vaga e a mãe desiste, que daí você vai pôr o status 'Desistir'. E a gente tem o cenário em que você não conseguiu a vaga ainda e a mãe desistiu antes disso. O que que a gente faz com essa ficha? Pra qual status que ela vai? Ela tem que compor na lista de solicitação aprovada? Ela não tem que compor?

**Interlocutora 2:** Ela não vai pra aprovada, né?

**Paulinho:** É, não. Porque neste caso a criança ainda tá na lista de candidatos.

**Interlocutor 1:** 'Aguardando Vaga Disponível'.

**Paulinho:** Isso.

**Interlocutor 1:** Tá, maravilha. Então maravilha.

**Paulinho:** Agora aqui seria a... a elaboração da lista de aprovados, né? Depois que a criança conseguiu a vaga, que a creche falou: "Opa, tem uma vaga aqui", a gente vai e aprova a Yonara. Aí ela vai pra uma outra lista, que é a lista dos contemplados, que a gente diz como contemplados.

**Interlocutor 2:** Essa lista de contemplados, ela entra na de inscrições aprovadas, né? São elas lá. Então ainda tem o meio-termo da inscrição aprovada com a matriculada, né?

**Paulinho:** Tem. Ainda tem isso.

**Interlocutor 2:** Eu queria saber o que que acontece entre essa inscrição aprovada e a matrícula. Quais são os status possíveis?

**Interlocutor 1:** Não vamos lidar mais com status, senão a gente viu que isso daí já dá confusão. Vamos pensar assim: no processo mesmo, sabe? O processo entre a lista de candidatos aprovada e a matrícula efetuada. A matrícula do cara lá, já aluno ingressado.

**Interlocutor 2:** Eu tenho que levantar só mais uma coisa aqui: solicitação aprovada, beleza, a gente tem que... o desistir vai contemplar a solicitação aprovada, porque antes disso ele ainda não... Só pra bater o martelo nessa regra aqui: se a mãe desiste antes de você conseguir uma vaga, você vai tratar ela como uma indeferida? Como que você vai tratar ela? Preciso determinar isso por quê? A gente tem que saber o que que a gente vai fazer nessa situação. Onde que ela tem que exibir? Porque a gente sabe que se ela desiste depois que você conseguiu uma vaga, ela vai pra solicitação aprovada. Beleza. E se é antes de você conseguir uma vaga? Nesse status aqui, 'Aguardando Vaga Disponível', nesse exato momento se a mãe desiste... Quando você entra aqui e a mãe ligou pra você e desistiu, não conseguiu vaga, não conseguiu nada...

**Paulinho:** A Yonara... Ela tava no Cecília.

*(Pausa enquanto buscam a tela no sistema)*

**Interlocutor 1:** Maravilha. Nesse exato momento a mãe te ligou: "Ô Paulinho, cara, não quero mais a vaga".

**Paulinho:** Aí a gente vai lá...

**Interlocutora 2:** Copia o nome da criança, igual a gente fez.

**Paulinho:** Isso, copia o nome da criança, por favor.

**Interlocutor 1:** Então a gente vai ter que ter o...

**Interlocutor 2:** Aí vai ter uma operação... Essa é a sua operação de aprovação...

**Interlocutora 2:** Então, porque aqui não tem, ó. Porque dá pra invalidar a inscrição e reativar a inscrição.

**Interlocutor 2:** Nos status da inscrição, clica neles aí, por favor.

**Interlocutor 1:** De novo acho que a gente vai cair numa outra regra. Eu tô levantando um monte de possibilidade, tá? Você invalidar a inscrição nessa etapa tem o mesmo peso de você invalidar uma inscrição quando você pega a documentação dela e tá errada? É a mesma coisa pra você? Você considera a mesma coisa?

**Interlocutor 2:** Após a pré-inscrição?

**Interlocutor 1:** É. Após ele... Eu quero entender por quê: se a gente considerar que isso aí vai ser uma invalidação de inscrição, ela vai cair na mesma regra de você pegar uma ficha que caiu na pré-inscrição e falar: "Documento errado, invalidei". Vai ser a mesma... o mesmo peso. É o mesmo peso pra você? Ela não tem que considerar em lugar nenhum, ela é só um conceito de informação?

**Paulinho:** É, acho que é diferente. Porque quando a gente indefere porque tá errada, a gente dá uma... No caso, a gente fala pra mãe que tá errado e pede pra ela fazer uma nova inscrição. Então até aí a criança ainda não fez parte ainda da lista dos candidatos e aguardando vaga. Agora, nesse cenário aqui, já houve uma inscrição que ela fez, que deu certo, e aí ela não quer e vai pra outra... ou pra outra creche... Aí aqui, eu acredito que a gente podia fazer uma... para uma outra lista...

**Interlocutor 1:** É, o que a gente não vai fazer é mais status. Status a gente vai fechar mais. A gente pode pensar no quê: nesse cenário, quando acontece isso, ele ser diferente da invalidar, então invalidar a gente já não vai usar. Invalidar sempre vai ser pra quando você pega uma ficha e tá com a documentação errada.

**Interlocutor 2:** Uma coisa que eu percebi: o que muda dos indeferimentos da ficha após a pré-inscrição é a comunicação que vocês têm com os pais, com os responsáveis, né? Então eles não entram numa listagem diferente de indeferimento, né? É sempre uma inscrição considerada indeferida, ela não vai prosseguir mais.

**Interlocutor 1:** É exatamente esse ponto que eu tava querendo chegar mesmo.

**Interlocutor 2:** Não cabe uma observação? Um esquema que a gente possa trazer assim essa transparência dentro da ficha, uma observação de indeferimento legal assim, que vocês consigam ter o controle? Por exemplo, um caso onde a inscrição foi indeferida por não ter contato com o pai, daí o pai faz contato com vocês, o trabalho vai ser abrir a ficha. Vocês abrem a ficha e vai ter a razão do indeferimento lá.

**Interlocutor 1:** Mas aí você tá trocando status por razão do indeferimento.

**Interlocutor 2:** Não, mas a observação sempre vai ter que ter. O campo de observação, sabe? Ela vai ser a razão do indeferimento e daí mata ali com essa observação, entende?

**Interlocutor 1:** Tá. Então você tá propondo eles darem um select com algumas opções de indeferimentos que podem acontecer?

**Interlocutor 2:** Isso. Porque igual aqui, ó: já tem a ação de vocês pegarem uma ficha de inscrição na lista de candidatos e buscar por ela na lista de inscrições, que é uma ação que vocês querem fazer com a Yonara. Na lista de inscrições tem todas as inscrições, desde o passado, todas ali. A mesma coisa pode ter com indeferimento, mas fazendo o controle, por exemplo, por ano, por nome, por CPF, sabe? Ali dentro do indeferimento. Razão com indeferimento fica de um lado mesmo. Se fizer sentido pra vocês, claro.

**Interlocutor 1:** Quando você indefere as inscrições aqui, você tira algum relatório disso de quantas foram? Não?

**Interlocutora 2:** Não tem a listagem. Podia.

**Interlocutor 2:** É, mas tem que entender o peso dela. Eu entendi agora o peso dela.

**Interlocutor 1:** A gente pode seguir por essa linha. Porque, ó: ele não tira nenhuma listagem. A gente entende que tem peso diferente um deferimento da documentação com o indeferimento que a mãe recusou quando tava aguardando vaga disponível. E a gente entendeu isso. Só que a gente vai deixar no mesmo status de indeferir, só que com a opção: "Mãe recusou", por exemplo. É porque aí a gente pode ficar um pouco mais na mesma regra de status.

**Interlocutor 2:** É, mas a indeferida é...

**Interlocutor 1:** É indeferida default, é. Peguei, peguei.

**Paulinho:** É, a gente precisa ter o registro dessas indeferidas porque às vezes a mãe fez a inscrição e a gente indeferiu. A gente tentou entrar em contato e não conseguiu. E aí daqui três... daqui um mês a mãe liga aqui brava: "Ah, fiz a inscrição e até agora não apareceu!" Aí a gente: "Ah, tá, qual o seu nome?" A gente olha lá: "João". Aí o João tá lá na lista dos indeferidos e aí a gente explica pra mãe: "Olha, não tá na lista porque você mandou tal documento errado". Então isso é importante pra gente ter esse... ficar esse registro dos indeferidos.

**Interlocutor 2:** Beleza, beleza. O indeferido é bem tranquilo, então. É só manter essa rastreabilidade pra vocês, né?

**Paulinho:** Essa parte do cadastro, da lista de candidatos, dos indeferidos, do que já entrou... Eu acho que tá tranquilo. O problema mesmo é os aprovados.

**Interlocutor 1:** É. Vamos chegar... É que assim, a gente sempre pensou no caminho... Porque o caminho feliz, em teoria, vai ser mais tranquilo. Mas ó, só pra gente bater o martelo: então o indeferir ele vai servir tanto pra documento errado, que você vai sinalizar lá: "Documento errado", por exemplo, pode ser essa nomenclatura, aí você indefere a ficha. Então quando você buscar lá, vai tá lá a informação disso. Tanto pra uma mãe que desistiu no aguardando vaga disponível. Daí você vai sinalizar: "Mãe desistiu no meio do processo", um exemplo. A gente pode pensar nessa nomenclatura.

**Paulinho:** Ou "Mãe foi pra outra... pediu pra mudar a inscrição pra outra creche".

**Interlocutor 1:** Isso! Podemos pensar nisso aí.

**Paulinho:** Que isso é o que mais acontece.

**Interlocutor 1:** Aí, ó, maravilha. Porque isso aí vai tá tudo no indeferido, só que com subcategorias no indeferido, vamos dizer assim. Indeferido na documentação, indeferido na etapa do processo. Porque vai manter o indeferido do jeito que tá, só que daí a gente para de fazer o quê? Para de o Paulinho precisar ir em inscrições e indeferir, em vez de ele só pegar ali e indeferir por ali.

**Interlocutor 2:** Sabe uma coisa que é bem interessante que existe já na plataforma, só que a gente não tem... que tem as etapas da Central, ó: etapa da inscrição, etapa da inscrição efetuada, transferência... tem a etapa da lista de candidatos. A gente pode parar de olhar para o status e começar a lidar com as etapas.

**Interlocutor 1:** Sim, exatamente!

**Interlocutor 2:** Porque a inscrição que ela chega como indeferida, ela é uma, por exemplo, que não vai participar mais de etapa nenhuma e ela vai ter que ter o registro da etapa onde ela parou. Sabe? Ela parou, por exemplo, na etapa de lista de candidatos. Então já tem uma informação, mesmo que o responsável, por exemplo, tenha colocado uma observação insuficiente ou até mesmo nenhuma, a gente já tem a informação de que essa inscrição chegou a deixar de ser uma pré-inscrição, chegou na lista de candidatos. E assim dá para chegar por todas as etapas, tá certo?

**Interlocutor 1:** Qual que é a diferença do 'Indeferido' para o 'Recusadas'?

**Interlocutor 2:** Eu tava pensando agora, ontem...

**Interlocutor 1:** Ué, o 'Recusadas' pode ser o que a mãe recusou, cara! A gente não precisa nem mexer nisso.

**Interlocutor 2:** É, na verdade essa é a ação...

**Interlocutor 1:** Exatamente! Ele recusou na etapa do aguardando vaga disponível e o indeferido é quando você indefere a documentação.

**Paulinho:** Por exemplo, ela pode fazer parte da mesma situação, só que com uma diferença se foi recusada pela mãe ou se foi indeferido na hora da... pra matrícula. A gente nem precisa mexer com o indeferido no contexto geral só.

**Interlocutor 2:** Exatamente. É só a gente considerar que ela não vai participar mais de nenhuma etapa do processo. Parou ali.

**Interlocutor 1:** Porque a gente não mexe nem com o status. Ele recusou ali no aguardando vaga disponível.

**Paulinho:** Isso, parou ali, exatamente. Só vai caminhar novamente se a mãe fizer uma nova inscrição.

**Interlocutora 2:** Aí volta do zero.

**Paulinho:** É, isso, volta do zero. E aí fica o registro que essa mãe já... "Olha, essa mãe aqui já foi chamada uma vez e não quis a vaga", ou então: "A gente entrou em contato várias vezes e não conseguimos".

**Interlocutor 1:** Ó, porque então aqui já muda um pouco o jogo. A gente vai tratar a solicitação recusada na solicitação aprovada, vai aparecer? Não tem muito sentido. Mas assim: você conseguiu a vaga, deu tudo certo, e a mãe de última hora desistiu. Então aí você vai tratar ela como uma solicitação recusada, correto? E aí esse submódulo tem que aparecer na aprovada. Tem sentido?

**Interlocutor 2:** Sim, sim. É, a gente pode até criar uma separação mais clara entre as pré-inscrições e as inscrições. Entende? Porque... Não, espera aí que agora eu fiquei com uma dúvida séria aqui. Essa aprovada a gente tá considerando as aprovadas em pré-inscrição, as inscrições efetivas...

**Interlocutor 1:** Não. 'Solicitação Aprovada'?

**Interlocutor 2:** Solicitações aprovadas são as que passaram...

**Interlocutora 2:** Pela aprovação dele.

**Interlocutor 2:** Pela aprovação do Paulo. Passaram, elas ganharam a... a vaga.

**Interlocutor 1:** Fez a conferência, deu tudo certinho, aba 'Aguardando Vaga Disponível'...

**Interlocutor 2:** Tá, mas elas foram inseridas após aprovadas, então ela vai ter que carregar a etapa de aprovação. Passou para a aprovação.

**Interlocutor 1:** Não, não, mas calma, Djalma.

**Interlocutor 2:** Ela vai estar dentro das aprovadas.

**Interlocutor 1:** É porque a gente tá confundindo acho que a parte da aprovação do... 'Solicitação Aprovada'. Solicitação aprovada é que conseguiu a vaga, é o caminho feliz. Correto? Deu tudo certo.

**Paulinho:** Certo.

**Interlocutor 1:** E assim: por mais que a mãe recuse depois que ele conseguiu a vaga, ele conseguiu a vaga. O nome da criança vai exibir nessa solicitação aprovada, porque ele conseguiu essa vaga, só que a mãe recusou.

**Paulinho:** Certo.

**Interlocutor 2:** Ah, sim. Ah, isso... Ah, entendi.

**Interlocutor 1:** Continua lá. O recusado tem que aparecer.

**Paulinho:** É porque tem duas etapas que parecem, né? A etapa do deferimento, que é de deferir o aluno pra ir pra lista de espera, e a etapa da aprovação, que é quando consegue a vaga de fato na creche.

**Interlocutor 1:** É, essa aí a gente vai chegar nessa ainda, tanto que a gente conversou, a gente tá na metade ainda. Paulinho, depois que você aprova ali, que você clica ali na lista de candidatos e aprova, ele vai pra solicitação aprovada. E aí, qual que é a próxima jornada?

**Paulinho:** Aí tem que vir pra cá, né? 'Solicitações Aprovadas'... Aí digamos que a gente aprovou o Miguel, né? Que aquela Yonara lá era o Miguel, que até é o meu sobrinho, que mudou de escola. Então o Miguel, ele foi aprovado no dia 26, por exemplo...

**Interlocutor 1:** Tá. Isso aí é a data que você clica no botão lá?

**Paulinho:** É. Ou, por exemplo, se fosse hoje, por exemplo. Aí, na hora que eu cliquei lá no negocinho lá, o nome do Miguel veio pra cá, por exemplo.

**Interlocutora 2:** Uhum.

**Paulinho:** No horário e na data que eu fiz.

**Interlocutor 1:** Ele já compõe a lista de solicitação aprovada.

**Paulinho:** Exato. Não importa se depois a mãe vai desistir ou não, ele vai compor aqui a lista de solicitações aprovadas. Aí, por exemplo, eu chamei 15 crianças nessa semana, um exemplo. Aí fica lá registrado que eu chamei essas 15 dessa semana. Semana que vem eu chamo 70, na outra semana chamo 200. Aí no final do mês, quando chega no dia... por exemplo, no dia 30 de abril, que acho que caiu no final de semana, aí teve feriado, então eu fiquei de fazer a lista dos aprovados para mandar para o site do mês de abril até a... antes do início da segunda quinzena, ali dia 14. Então esse é o prazo que eu tenho para lançar os alunos que foram aprovados em abril. Então, o que que eu fazia? Eu vinha aqui no...

**Interlocutora 2:** No calendário.

**Paulinho:** No calendáriozinho aqui, aí colocava aqui: de 01/04 a 30/04.

**Interlocutor 1:** Que seria a data de aprovação.

**Paulinho:** É, a data de aprovação. Aí passa por esse processo aqui, que ele tá pensando, né? E aí, por exemplo, eu tenho... Todas as chamadas que eu faço, eu registro na... Deixa eu abrir a tabelinha pra você ver, né? De todas as chamadas. Eu faço uma tabela pra cada chamada e aí depois, no mês, eu somo lá quantas eu fiz. Por exemplo, nesse mês de abril eu contei 305. Na primeira vez que eu fiz aqui, tava dando 280, aí depois faltavam 500... É, 390, 500... Tipo, ele tava puxando outras... outros dados, outras coisas.

**Interlocutora 2:** Não, mas essa lista de convocação são as crianças que você aprovou, que ainda estão com interesse de continuar com a vaga e que tem a vaga disponível, e aí elas vão pra creche. Então o número não vai bater com a lista de solicitações aprovadas, né? Porque isso aqui entra a galera que desistiu, isso aqui tem a criança que ainda... que não tem mais interesse na vaga, não vai bater o número.

**Interlocutor 1:** É, na verdade... O número pode bater, só que ele vai pra outro lugar na plataforma. Então assim: se a gente condicionar que a impressão da solicitação aprovada ela vai contemplar os que deram certo, foi pro aguardando vaga disponível na inscrição, e também pelos recusados, que a mãe recusou depois de conseguir uma vaga, e isso contemplar a lista, beleza! Que a gente consegue fazer isso. Ela só não vai talvez exibir na mesma listagem no front aqui, ó.

**Interlocutora 2:** Sim. Mas aí não vai bater com o número dele.

**Interlocutor 1:** Vai bater! Porque se ele também considera que a mãe recusou uma vaga depois que ele conseguiu essa vaga, vai bater.

**Interlocutora 2:** Mas aí você não vai convocar, né? Se você viu que a mãe desistiu, por exemplo, ela não vai convocar.

**Interlocutor 1:** Ele vai lançar o nome da criança na aprovada.

**Interlocutora 2:** Não, vai aparecer aqui. Mas, por exemplo, a lista de convocação que você faz: a criança foi aprovada, a mãe manteve o interesse na vaga, surgiu a vaga na creche e aí você convocou pra fazer a matrícula. Não vão pensar assim?

**Paulinho:** É, na verdade a escola já fez a matrícula nesse espaço.

**Interlocutora 2:** Então é a mesma coisa a lista de solicitações aprovadas com essa lista que você publica?

**Paulinho:** É. Por exemplo: nesse mês de abril, a gente chamou 305 crianças. Então, o que que eu tinha sugerido? De pegar somente os dados das minhas aprovações. E como só eu que aprovo, então fica fácil de pegar da montagem dessa lista.

**Interlocutor 1:** Mas você fala da sua... extrair da plataforma?

**Paulinho:** É. Por exemplo, a lista aqui... Vamos só gerar uma lista só pra gente ver como que eu faço.

**Interlocutor 1:** É, porque o que eu quero deixar claro é que assim: a gente vai mexer na solicitação aprovada e se uma mãe recusar a vaga, ela vai ainda aparecer na solicitação aprovada. Porque você conseguiu essa vaga, só que a mãe recusou por qualquer outro motivo. O nome da criança ainda vai aparecer na solicitação aprovada, tem que aparecer.

**Paulinho:** É, porque ó, por exemplo: a gente chamou 10 crianças no dia 5 de abril. Beleza. Essas 10 crianças, elas têm que, no final do mês, lá no dia 30, por exemplo, ou no dia 2 de maio, não sei... quando fizer a pesquisa, essas 10 crianças, não importa se as 10 crianças se matricularam ou se as 10 crianças desistiram, elas têm que constar no registro da listagem de aprovados.

**Interlocutor 2:** A gente podia pensar assim: nessa publicação, o que que é importante? É as aprovadas, né? Elas terem registro de que elas contemplam uma vaga numa escola. Não é isso? Elas foram aprovadas. Então a gente pode bater aí que quando passa por aquele verdinho ali, que é o atual verdinho na lista de candidatos, ele passa pela etapa de aprovação e entra pra esse relatório. Então ele entra pra esse relatório na data X, que foi o dia da aprovação. O que acontece depois, aconteceu após essa etapa, entende? Esse relatório é um relatório de emissão dessa etapa do processo. Ela passou por ali, depois... depois é outra história.

**Paulinho:** A gente precisa comprovar que conseguiu a vaga. Quando o Ministério Público chega aqui e fala assim: "Ó, cadê a lista dos meninos que foram chamados no mês de abril?" Aí eu falo assim: "Ó, foram esses aqui".

**Interlocutor 1:** Maravilha. Fechou.

**Paulinho:** "Os 305", por exemplo.

**Interlocutor 1:** Maravilha. Então, após a solicitação aprovada, é o que você precisa ali. E após isso?

**Paulinho:** Então, eu preciso fazer duas listas: uma que é da lista de candidatos, é tranquilo, eu consigo fazer a lista dos candidatos sem problema...

*(Demonstrando na tela)*

**Paulinho:** Que são todos os que passaram pela sua primeira filtragem da documentação e deu tudo certo. Então, no final do mês, na sexta-feira, eu vou enviar essa lista aqui, que foram as crianças deferidas, que deu tudo certo, até o momento. Então até o momento, por exemplo, vamos supor se fosse hoje no final do mês, eu já ia fazer essa lista aqui com 295 inscrições deferidas. Aí a outra tabela que a gente pede, que é a de aprovados, no mesmo sentido ali, né? Com... dividido por creche e por berçário e maternal, né? Quantas crianças de berçário, quantas de maternal, bonitinho. A data da aprovação que foi feita a aprovação, a data de nascimento da criança... E é isso.

**Interlocutor 2:** É bem simples. Ó, dá pra gente contar até as etapas onde ela passa, ó: etapa da pré-inscrição feita pelo portal da comunidade; etapa de efetivação ou deferimento (se for indeferida, ela cai para as indeferidas); próxima etapa vai ser a etapa de aprovação, que a gente lista pela lista de candidatos (passou pela lista de candidatos, é aprovada); depois etapa de matrícula, efetivação. Vai dar quatro etapas. Se a gente puxar o tanto de botão que tem ali na tela, tem mais status do que essas quatro. Se eu não me engano, só para aprovada já tem mais de quatro status que a gente tá trazendo atualmente. Daí dá pra gente simplificar muito e atendendo, atendendo tudo certinho.

**Interlocutor 1:** Aí, ô Paulinho, depois da lista de aprovados, de solicitação aprovada, qual que é o caminho do diretor? Porque aqui fechou pra você, correto? Aqui é o que você tava precisando. Você não faz nenhuma mais movimentação ali nesses estudantes, né? Não precisa fazer mais nada. Bateu a listagem, fechou e é isso. E agora como é que é com o diretor lá? Próxima etapa com ele.

**Paulinho:** A próxima etapa, na hora que a gente faz o deferimento aqui... a gente vai lá no verdinho, né? Aí o que que eu faço? Eu mando a mensagem pro diretor e falo assim: "Olha, saiu pra você chamar... para suprir a vaga que você enviou pra gente". Então, um dia antes eu peço pra eles enviarem a quantidade de vagas. Mandou 30 vagas, aí eu vou e coloco os dois primeiros aqui, ainda fica 28 vagas disponíveis. Então fui lá, coloquei no aprovado, beleza. Aí quando coloca aprovado lá pro diretor da escola, vai aparecer o nome dele bonitinho e aí vai lá nas ações... Mas acho que não é nem ações, é naquele ações de inscrições. Aí o diretor vem aqui, ó...

**Interlocutor 1:** Não, porque o diretor ele muda o status! Ele muda o status lá no banco na lista. Ele tem essa opção de mudar.

**Paulinho:** Agora vocês vão entender: na última reunião que a gente conversou, de por exemplo fazer um link dos alunos que estão cadastrados na SED, que é aquela lista dos estudantes que vocês disponibilizaram pra gente, de todos os estudantes, porque ali é o momento que a criança já tá lá na creche. Fazendo isso, pegando daquela lista, a gente... ao invés de o diretor colocar aqui como matriculado, já aparecia que foi matriculado automaticamente.

**Interlocutor 1:** É, eu concordo contigo, isso aí é uma... é um gap que a gente tem na plataforma de não puxar a inscrição já e exibir ela aí. O que que a gente pode fazer, Paulinho? Feita essa jornada, o diretor vai na SED, faz a matrícula e a gente passa um crawler de madrugada, toda madrugada, batendo na SED pra ver se a matrícula foi feita. E pra você, exibir ali tipo uma sinalização. Pode ser uma tagzinha: 'Matriculado' ou tipo 'Não Matriculado'. Porque daí você pode puxar ali: "Putz, passou pela solicitação aprovada, sinalizei o diretor, eu vou puxar um filtro aqui: quem que ainda não foi matriculado dessas fichas minhas?" E a gente trazer esse resultado pra você. Porque daí a gente não condiciona o diretor a fazer essa atualização dentro da plataforma, que a gente sabe que não faz. E atualmente, cara, quanto mais ainda o problema maior ainda tá acontecendo: o diretor pode fazer... Vamos dizer que o diretor faça: ele acessa a ficha do estudante e ele pode mudar esse status. E esse status bagunça a lista de aprovados.

**Paulinho:** Se quiser tirar, pode tirar.

**Interlocutor 1:** É, a gente vai remover isso aí pro diretor. O diretor não precisa ter, o diretor tem que fazer na SED. E ele exibir pra você que tá certinho ali. Aí então quando você vir aqui numa solicitação aprovada, isso aqui a gente pode desenhar um pouquinho melhor ainda, tá? Pode exibir uma tagzinha: 'Matriculado' ou os que não tiver matriculado só. Porque daí você puxa um filtro e fala: "Pô, meu, o diretor da Cecília aqui, de três ele matriculou um. O que que houve?" Deu certo a jornada. Pra mim tá resolvido, só falta o diretor matricular.

**Paulinho:** Isso ilustra exatamente o que a gente tá passando com uma creche agora. A creche Sebastião, a gente mandou, por exemplo, 10 crianças na semana passada pra eles matricular. E dessas 10 crianças, sete... três desistiram e sete quiseram a vaga. Então eu não sei quais são essas sete. Enquanto ela não cadastrar, que não aparecer na SED pra mim, eu não sei quem são essas sete crianças. Então isso que você tá falando é perfeito, porque eu vou saber: "Opa, as sete que tá faltando, ela cadastrou duas". Então eu vou saber que a Maria e o João foram cadastrados.

**Interlocutor 1:** Me tira uma outra dúvida aqui agora, Paulinho: como que o diretor... ele acessa a plataforma pra ver o nome do estudante, tudo certinho? Então ele acessa pra saber quem que é o Miguel Anthony Gonçalves que ele precisa fazer o cadastro na SED. Ele se baseia pela plataforma nisso. Ele só não tá fazendo a ação de mudar o status, mas isso aí a gente vai tirar da mão dele pra ficar mais fácil. Legal. E se chega lá pro diretor e não dá certo? Tipo assim: a mãe desiste. Como que o diretor comunica você? Como que é feito esse processo? Porque assim: eu entendo que você aqui, você vai ter o controle de fazer isso, que é a solicitação recusada. Mas o diretor, ele comunica como pra você?

**Paulinho:** Não tem comunicação. A única comunicação agora vai ser... É assim: por exemplo, na semana passada ela mandou duas vagas, eu mandei duas crianças. Se as duas crianças não foram, aí ela devolve pra mim as duas vagas. Aí eu vou saber que essas duas vagas que eu chamei na semana passada não foram.

**Interlocutor 1:** E pode ser porque o diretor se esqueceu... Porque o mundo ideal, o caminho feliz, seria o diretor sinalizar ali na plataforma: "Ah, cara, desistiu da vaga", ou tipo assim: "Matriculou". Só que ele não faz isso. Aí o Paulinho fica cego. Então a gente vai pular a etapa do diretor e vai trazer o campo de matriculado das que você mandou pra ele. Aí só o único problema vai ser: mandei 10, três tão não matriculadas ainda. A gente vai ficar um pouco cego em saber o que aconteceu: se o diretor esqueceu ou se a mãe desistiu nesse meio-tempo. Aí essa comunicação que também... Entendeu? Porque você vai saber quem são os estudantes, aí você vai ter que talvez entrar em contato com ele...

**Interlocutor 2:** Outra coisa que me surgiu aqui: dentro da secretaria para os diretores, essa comunicação de vagas disponíveis por escola, como que eles fazem atualmente?

**Paulinho:** Um dia antes eu mando um formulário, um Forms pra eles. Eles me informam: tem três vagas de Berçário e cinco de Maternal. Aqui eu faço aquela tabelinha lá. E aí eu vejo quantas... Aí eu faço a quantidade de vagas que eles mandaram, vejo a quantidade de crianças que tá na lista de espera e aqui tem uma outra que são as que eu vou chamar de acordo com as vagas e com a quantidade que tem na fila. Aí eu chamo aqui.

**Interlocutor 2:** Essas ferramentas que vocês usam, seria interessante estar na plataforma?

**Interlocutor 1:** Esse 'Comunicar Vagas' que você tem aqui...

**Interlocutor 2:** Só que eu acho que ninguém nunca alimentou.

**Paulinho:** Então, tem esse daqui e tem o controle de vagas. Mas eu tenho a leve impressão de que isso não tá sendo usado.

**Interlocutor 1:** Isso aí seria mais pro diretor?

**Paulinho:** É, isso seria mais pro diretor.

**Interlocutor 1:** E você visualizar?

**Paulinho:** Eu visualizar, mas eu não... não confio na pessoa do diretor.

**Interlocutor 1:** Tá, mas a gente não consegue trazer essa informação?

**Interlocutor 2:** A gente pode botar assim uma dependência do controle de vagas pra matrícula. Por exemplo: ele vai efetuar a matrícula de um aluno... Tudo bem que isso é feito externo, né?

**Interlocutor 1:** É, mas a gente vai trazer pra plataforma. A gente tá propondo isso. Porque daí o que que a gente faz? Vamos dizer que a gente pega a base hoje e aí tem uma escola que tem duas turmas que têm duas vagas, essas duas turmas têm duas vagas. A gente trouxe hoje pra plataforma. A partir de agora, ele vai bater, vai matricular uma pra uma das turmas, ele vai retornar pra você que foi matriculado e aí no controle de vagas ele já pode vir debitando essa uma vaga. Pra você não depender do diretor te mandar essa análise. Eu acho que a gente pode pensar mais além nesse cenário. Porque daí o diretor não fica alimentando a plataforma, o diretor vira e mexe ele pode esquecer. A gente bate com o débito que ele tem de matrícula, então se ele fez uma matrícula hoje, amanhã essa turma tá com uma a menos já.

**Interlocutor 2:** Sim.

**Interlocutor 1:** Não precisa atualizar nada, você só vai visualizar. Você pode só ter um botão de impressão ali, uma tela mais bonitinha pra você ver quantas vagas tem. Eu acho justo a gente pensar nessa linha. A gente já vai trazer a informação da matrícula, então é só debitar de uma da turma que ele matriculou. A gente tem isso na plataforma, tem todos esses dados.

**Paulinho:** É perfeito, porque aí no caso a gente só condicionaria a capacidade da sala. Por exemplo: o Berçário A tem 20 vagas, sendo que 12 é disponível pra vaga de 7 horas e 8 de 12.

**Interlocutor 2:** E essas informações todas já vêm da SED também. A gente tem integração. Fecha muito bem isso aí.

**Interlocutor 1:** Porque daí o Paulinho não fica dependendo do diretor, o Paulinho vai conseguir consultar sempre que precisar. Não tem essa comunicação truncada por fora, que é um Forms que às vezes não dá certo.

**Paulinho:** É a única ferramenta que a gente tem assim... e a gente corre sempre o risco de eles mandar duas vagas a menos. Eles fazem isso.

**Interlocutor 1:** Aham. E às vezes até a turma que é uma turma de integral ali que o professor... Ele é mais responsável demais de um ali. Acho que você que me contou uma situação, né? Que eles colocam que não tão precisando de vaga pra o professor cuidar de menos crianças, né? Foi uma situação dessa que você trouxe uma vez? Então ele não fala que tá precisando de vaga aqui. Então nessa turma que tem cinco vagas, ele fala que tem uma, porque daí o responsável da sala vai trabalhar com menos crianças do que ele pode comportar. Isso aí é transparência também, da SED não vai ter esse problema se a gente trouxer. Um professor é responsável por quantas crianças, avezinhas?

**Paulinho:** No Maternal é 20 crianças e aí é dividido com mais uma ADI. Então no caso seriam 10... um adulto por 10 alunos, o outro adulto por 10 alunos, mas o professor é o responsável da sala.

**Interlocutor 1:** É, o diretor ele pode fechar essa turma falando: "Não, tem 15 crianças lá", e ele fala: "Não, não tem vagas aqui". Porque daí fica menos trabalho pra... Pode ser que aconteça.

**Interlocutor 2:** É, quando a turma comporta 30, por exemplo.

**Interlocutor 1:** Exatamente. E ele fala: "Não, aqui tá lotado já, cara. Eu tenho 15 crianças". A gente vai pegar isso aí também.

**Paulinho:** Pega porque aquele exemplo que eu dei da escola Sebastião: a menina não tá cadastrando as crianças. Tem sete lá para ela cadastrar e ela não cadastra. E eu não sei quem são essas crianças. Inclusive a gente ligou para ela hoje de manhã pedindo para ela cadastrar, porque o censo é até amanhã, né? O que tiver cadastrado na SED até amanhã... Amanhã o que tiver cadastrado na SED é o que vai estar no censo. Então, por exemplo, se vocês fizerem um... Vocês fazem isso de duas em duas horas, é isso?

**Interlocutor 1:** Isso, a gente tá no caminho de duas em duas horas.

**Paulinho:** Então no final do dia, à meia-noite, por exemplo, vai ser o que tá exato o que vai ser migrado pra SED. Pro censo, não tem jeito.

**Interlocutor 1:** Mas aí, no caso, você vai tirar pela plataforma?

**Paulinho:** É, a gente pode tirar pela plataforma o que tá na plataforma...

**Interlocutor 1:** É o que tá na SED. Eu vou até falar pro William rodar esse crawler manual, só pra gente... Amanhã, se for 8 horas que você vai precisar, que daí a gente roda já o manual ali 8 horas e a gente força essa atualização.

**Paulinho:** É porque no caso eles vão ter o dia inteiro pra cadastrar no novo envio.

**Interlocutor 1:** Sim, tranquilo. A gente vai atualizar, mas só pra caso... Você fala: "Pô, meu, às 18h eu vou enviar". Porque daí a gente força manual só pra não pegar num gap, entendeu?

**Paulinho:** Por exemplo, se cadastrarem 3 horas da tarde...

**Interlocutor 1:** E você tá precisando pras 4h, pode ser que ele... Aí a gente roda manual, força.

**Interlocutor 2:** Ou a gente só busca por data. Assim que atualizar, vai atualizando de duas em duas horas. Se na atualização das 2h da manhã houve uma atividade à 1h30, a gente vai desconsiderar, foi até a meia-noite do dia 26.

**Interlocutor 1:** Mas o Paulinho tá dizendo que amanhã eles vão mexer ainda, né?

**Paulinho:** É, amanhã até à meia-noite, por exemplo, pode ser que entre uma matrícula.

**Interlocutor 1:** Não, tranquilo. A gente vai estar sempre atualizando ali, Paulinho. Aí o que eu falei assim: eu pensei num cenário que você tá precisando desse documento pras 18h. Aí às 17h52 rola um cadastro na SED. Então até a gente rodar o crawler de novo, pode ser que a gente perca esse um cadastro. Então a gente vai fazer o quê? Às 18h eu vou falar pro dev: "Cara, roda manual, porque daí vai atualizar naquele momento o que tá na SED". Não, beleza. Fechou.

**Paulinho:** Porque às 19 horas, às 18 horas, eu peço pras meninas baixarem aquela lista dos estudantes todos. A gente coloca naquele programinha do Gabriel e aí ele faz a... Chega de notificação também e vocês também têm o registro do que foi cadastrado até amanhã.

**Interlocutor 1:** A gente vai estar sempre atualizando, mas é só questão de... Esse cenário específico pode acontecer.

**Paulinho:** Essa questão da vaga, de disponibilizar a vaga e de colocar qual o aluno que tá faltando fazer matrícula é interessante. E os alunos que cadastram na SED já vai aparecer lá que tá matriculado, a informação de que tá matriculado.

**Interlocutor 2:** A gente tá bem próximo disso, é só realmente a gente implementar agora. As ferramentas a gente já tem no sistema.

**Interlocutor 1:** É, a gente já tem os dados.

**Paulinho:** A gente tava só chegando nesse ponto pra simplificação.

**Interlocutor 1:** Exatamente.

**Interlocutor 2:** Sim, sim. É, a gente cometeu um erro na Central até agora, que foi assim: atender as necessidades trazendo mais coisa, quando na verdade... Você vê que a gente mapeou agora quatro etapas pro aluno tá matriculado. E olha só essa tela assim: se a gente contar quatro botões, a gente chega na lista de candidatos. Tem muito mais coisa, sabe? Esse muito mais coisa ainda tá engasgando pra...

**Interlocutor 1:** Mas foi o que eu falei: no começo da construção da Central de Vagas, eu não participei, acho que o Djalma também não... Foi só colocando mais coisa, empilhando mais coisa, empilhando mais coisa. A gente não tinha uma concepção: o que que é uma Central de Vagas? Como que é a Central de Vagas? Hoje a gente tem mais, mas ainda assim é viável a gente ter essa reunião pra enxugar mais.

**Interlocutor 2:** É muito bom que a gente tem assim, ó: a gente tem os dados de todas as inscrições até agora, sabe? A gente tem toda essa ação já dentro da plataforma, a gente já tem uma Central de Vagas, sabe? Agora a gente vai fazer esse esforço pra vida de vocês com a Central ser mais fácil mesmo, sabe? Trazer essas novidades também: controle de vagas, tudo, pra melhorar. Os relatórios também, deixar eles mais claros, mais fáceis de tá na mão de vocês aí no final do mês. Trabalhar em cima disso agora.

**Interlocutor 1:** Da minha parte aqui eu acho que eu tirei as dúvidas que eu tinha. Os outros módulos ali... Para mim o EJA, se eu não me engano, que a gente abriu uma aba à parte no Portal da Comunidade, então não é utilizado mais.

**Paulinho:** Foi, foi... Por exemplo, em agosto, lembra que a gente teve aquele espaço para matrícula dos alunos que estão precisando de vaga para o Pré I? E aí a gente tem essa ação, né, de uma semana e até o final do ano quem fizer a inscrição já se matricular no Pré I. Porque pode ser que tem criança na rede, que existe, que não fez a inscrição aqui, que seria a última etapa da creche, Maternal II.

**Interlocutor 1:** Mas vocês utilizam ainda?

**Paulinho:** Não, a gente não utilizou mais não. Foi só uma vez. Não funcionou porque as escolas tavam fazendo e tipo não tava alimentando. A gente cobrava: "Quantas matrículas vocês fizeram?" "Ah, olha, 20". Mas só tem duas cadastradas.

**Interlocutor 2:** É, não foi bem aderido, né? O pessoal não...

**Interlocutor 1:** Uma outra dúvida: e o 'Transferências'?

**Paulinho:** Também não... A gente não utiliza porque no final do ano a gente faz a ação de transferência entre creches. Então uma creche manda para outra de acordo com as vagas e aí a outra escola...

**Interlocutor 1:** Mas nada pela plataforma, tudo direto na SED?

**Paulinho:** É. O que vai aparecer daqui uns dias é aquela de 12 horas, né, que a gente já conversou lá...

**Interlocutor 1:** Sim, o que vem dos diretores lá, né? Isso aí é bem legal também.

**Paulinho:** Que aí esse de 12 horas é uma outra ação.

**Interlocutor 1:** Ela vai ser um pouquinho meio que apartada da Central ali, né? Ela não vai ter tipo lista de solicitação aprovada, vai ser uma lista própria dela, né? Essa aí tá tranquila.

**Paulinho:** Aí tem o quadro escolar... porque aqui tem todas as turmas, os alunos que estão cadastrados...

**Interlocutor 1:** A gente vai ter que... Eu vou ter que refazer o cronograma com o Gabriel, porque veio muita...

**Interlocutora 2:** É, mas o quadro ele tava bem mais para o final do ano, né? Agosto mais ou menos... Tinha uma refatoração grande para fazer.

**Interlocutor 1:** E provavelmente, Paulinho, a gente ainda vai atrasar um pouco porque eu vou mandar refazer um cronograma com o Gabriel. Veio bastante demandas urgentes, veio a questão dessa nova da Central de Vagas que a gente vai passar na frente, a do diretor também que vai aparecer aí. Então a gente vai dar uma postergada nela, mas eu vou passar um prazo certinho também. Mas é só porque tá vindo coisas à frente e a gente vai ter que ir atacando. Mas eu acredito que com essa nova parte da Central de Vagas ela vai matar um desenvolvimento que a gente tinha prometido lá, que era a questão de buscar por CPF, que eu tava meio assim... Mas eu acho que a gente pode fazer nesse esquema da matrícula. Você lembra que você tava querendo pesquisar pra ver se era matriculado lá na SED? Isso era um desenvolvimento que a gente tinha mapeado. A gente não vai fazer ele, a gente vai fazer mais simplificado aquilo ali. Você não vai precisar fazer nada, a gente vai trazer pronto pra você.

**Paulinho:** É, exatamente. Aí o que que eu ia precisar? Dessa lista de contemplados do mês de abril. Menos essa do mês de abril, se puder até amanhã...

**Interlocutor 2:** Matriculados?

**Paulinho:** Aprovados. Os que foram aprovados por mim no mês de abril.

**Interlocutor 2:** A gente tem um esquema... É que o número não tava batendo, né, Djalma? Tá dando 392.

**Interlocutor 1:** Então, mas aí, Djalma, a gente vai ter que... Tem que entender se teve alguma ação de alteração de status.

**Interlocutora 2:** E com certeza teve. Porque quando você filtra só o mês de abril, ele vai puxar tipo solicitação aprovada do começo de maio. A data que você viu, né? Eu mandei para eles também essa tela.

**Interlocutor 1:** O bug no filtro aí é de boa de resolver. Se for só isso o problema, tá de boa. O problema é quando mexe nos status.

**Interlocutor 2:** Como eu disse, todas as inscrições vocês têm aqui no sistema, a gente só precisa organizar elas.

**Interlocutor 1:** Você sabe, Djalma, se teve recusadas esse mês? Se o responsável tipo assim, ele chegou a recusar depois que conseguiu a vaga?

**Paulinho:** Sim, porque às vezes... Geralmente a gente manda tipo 30 crianças e só quatro querem. Então digamos que 15 foram recusadas e as outras...

**Interlocutor 1:** Pior que a gente tá dependendo do diretor fazer, hein? Por isso que o número não bate nunca. Porque se o diretor faz... Se o diretor faz errado, ele interfere na aprovada.

**Paulinho:** É. Por isso que eu tinha dado aquela sugestão de fazer a lista de acordo com as minhas aprovações.

**Interlocutor 1:** Mas vai ser isso! A gente vai tirar o diretor de fazer essa ação.

**Interlocutora 2:** Não, ele disse puxar o log dele para buscar quais crianças ele aprovou em tal período de tempo.

**Interlocutor 2:** Exato. Eu acho que os status realmente não vão bater, porque teve atualização.

**Interlocutor 1:** Ô Djalma, ele trouxe uma coisa que a gente pode usar: pegar o log dele e ver tudo que ele aprovou. E aí esse número vai bater. Porque daí a gente tira o diretor da jogada e ele tá fazendo o caminho de aprovar.

**Interlocutor 2:** Sim. Essa tela, essa aqui, ó: a lista externa de convocação. Se eu não me engano, ela traz os logs do Paulo já. Já foi feito um tratamento...

**Interlocutora 2:** E aí o número não bate?

**Interlocutor 2:** Não sei, isso a gente vai ter que ver agora. Mas de qualquer forma, vamos trabalhar em cima dela.

**Interlocutora 2:** Que foi isso que foi feito no ano passado, né?

**Paulinho:** Até acho que fevereiro... Teve uma lista que eu consegui fazer sozinho e deu certinho, bateu bonitinho. Não lembro qual foi, se foi a de fevereiro...

**Interlocutora 2:** Pode ter sido a de março, né?

**Paulinho:** É, porque a de março foi o que deu certo, acho que você enviou pra mim a de março. E a de abril que eu tô com problema, que era pra ter divulgado até o dia 15 de maio, por exemplo.

**Interlocutor 2:** Vamos trabalhar em cima dela já.

**Paulinho:** Porque acho que pra esse... mais rápido seria pegar o meu log.

**Interlocutor 1:** Você, esse mês, você lembra se você só aprovou mesmo ou você teve alguma alteração tipo de quando o pai entrou em contato contigo e desistiu?

**Paulinho:** É poucos.

**Interlocutor 1:** Dá pra puxar pelo log seu.

**Interlocutor 2:** Dá, tranquilo. Eu vou trabalhar nisso hoje: puxar pelo log do Paulo e os status... status iguais dessa tela aqui.

**Interlocutor 1:** A aprovação dele só. Ignora um pouco o status talvez. É, você vai trazer só o que 'Aguardando Vaga Disponível' e ele clicou lá.

**Paulinho:** Aqui foram 254 inscrições deferidas. Essa aqui é a lista de candidatos.

**Interlocutor 2:** Não, as solicitações aprovadas externa.

**Paulinho:** É essa aqui que eu fiz.

**Interlocutor 2:** É essa aqui? Não é não, essa aqui é o... Ah, não, essa aqui é... Vou ter que... Tá com erro aqui, ó. Vou trazer ela pra gente. Mas dá pra se basear pela 'Solicitações Aprovadas'. O status das aprovadas... ó, todos os logs trazem agora as aprovadas no mês de abril: 390.

**Paulinho:** Então, só que aí, quando a gente... ó, por exemplo: 4 de maio.

**Interlocutor 2:** Essa coluna aqui tem um detalhe nela: essa data de aprovação, ela pega a data da última mudança pra um status considerado aprovado.

**Interlocutor 1:** Então se o diretor mudou num outro período já bagunça.

**Interlocutor 2:** Esses 390, eles pegam por qualquer status de aprovação. Não é só o...

**Interlocutor 1:** Isso tá errado, isso aí tá errado porque assim, ó: vamos dizer que você aprovou uma criança esse mês. Vamos dizer que hoje é dia 29 e você aprovou uma criança. O diretor vai matricular dia 1º. Esse status vai alterar e ele vai sumir da lista do Paulinho de aprovação, porque o diretor... a gente tá bagunçando nisso. Então o caminho nesse momento pra gente resolver agora, até a gente atuar em tudo que a gente conversou hoje: puxa o log do Paulinho, solicitação aprovada do Paulinho e traz esse relatório à parte pra ele. Pra gente resolver agora do Paulinho. Porque tudo que a gente conversou hoje vai ser sanado nisso, não vai ter essa dor de cabeça mais. Só que até desenvolver, vai um tempo. Então o caminho mais rápido é puxar o log dele de aprovados.

**Paulinho:** Aí eu vou precisar a de hoje, de abril, pensando de 1º de abril a 30 de abril, e já vou pedir do próximo mês, de 1º de maio ao dia 29, sexta-feira... a 29 de maio. Aí esse só ficaria pronto na semana que vem.

**Interlocutor 1:** E lembrando, Djalma, que assim: tem que considerar qualquer mudança feita só pelo Paulinho. Se o diretor mudou, já vai bagunçar.

**Interlocutora 2:** E uma pergunta, Djalma: se a gente filtra só solicitação aprovada e aí na data de aprovação a gente desconsidera qualquer outra movimentação feita que também é considerada aprovada, deixa só aprovada... não atende? Você entende? Tipo, ele aprovou, o diretor foi lá e matriculou. Certo? Matriculado também tá dentro aqui dessa lista do front.

**Interlocutor 2:** Sim. Daí cai só vai ter as...

**Interlocutora 2:** Só aprovado! Porque é pra isso que serve a data de aprovação no filtro, né? O que foi aprovado de fato dentro... somente o que foi aprovado por ele.

**Interlocutor 2:** E todos os outros a gente vai desconsiderar, porque todos os outros status, se eu não me engano, caem pra uns cinco status que caem ali.

**Interlocutor 1:** Mas vamos por um cenário que o diretor recusa: a mãe ligou pro diretor e ele coloca ali, ele altera o status. Isso já alterou a lista. Mas foi aprovado! Daí prejudica isso aí.

**Interlocutora 2:** É isso que eu tô falando: foi aprovado, mas já alterou. Porque se ele aprova dia 29 e o diretor altera o status no dia 1º, já não entra na lista dele. Aí já dá a diferença que a gente tá batendo a cabeça pra entrar, você entende?

**Interlocutor 1:** Exatamente.

**Interlocutor 2:** Vai continuar listando. Mesmo assim a gente considera todos aqueles status. Provavelmente... assim, provavelmente não, com certeza: daqui a maioria das inscrições caem nessa data pelo primeiro status considerado aprovado, que é o aprovado lá da lista de candidatos ter sido na data.

**Interlocutora 2:** Até...

**Interlocutor 1:** Tá dando um valor acima? Tá dando 390 e ele chamou 305?

**Interlocutor 2:** É, porque pode ter outras inscrições que não passaram pela sua aprovação, mas ganharam status de aprovado.

**Interlocutor 1:** Não, isso aí não. É sempre o Paulinho que aprova. O que tem quase certeza que tá acontecendo é o quê: o Paulinho aprovou, passou o mês, o diretor foi lá e mudou o status pra aprovado e aí ele não tá considerando nessa lista... Quer dizer, tá considerando tudo, não só do mês que o Paulinho precisa, que é o que a gente tava conversando. Entende? Ele tá precisando de uma lista de abril.

**Interlocutor 2:** Não, mas aqui a primeira aprovação cai aqui. O primeiro log de aprovado cai pra cá.

**Interlocutor 1:** Então tá errado esse número. É o filtro da data ali então. Porque isso aí responde só à aprovação do Paulinho. Tem que responder só à aprovação do Paulinho.

**Paulinho:** Se vocês quiserem fazer uma... por exemplo, uma etapa: primeira etapa, aprovação do Paulinho, que é a minha aprovação...

**Interlocutor 1:** Ah, não. Com o que a gente propôs aqui hoje, vai resolver esse problema. Só que a gente tá pensando agora na lista emergencial. Mas é isso, Djalma. É a solicitação aprovada que o Paulinho fez.

**Interlocutor 2:** Então vou puxar uma, pessoal, com todos os que tiveram o primeiro log dentro da data de abril com a sua aprovação. O seu log de aprovado. E só. E trazer essa quantidade pra gente dar uma olhada.

**Interlocutor 1:** E ainda assim esse número pode não bater. Se não bater, a gente vai caçando até chegar no fechado ali, naquele grupo que passou pela sua mão. Não, acho que bate sim esse número. É pra bater, porque se ele deferiu e depois o responsável recusou, tem que considerar o deferimento primeiro dele ali. Tá certo, vai bater esse número.

**Paulinho:** Aí só lembrando a organização da lista: é por creche e por berçário, maternal...

**Interlocutor 1:** É, a gente segue no mesmo padrão ali.

**Interlocutor 2:** Show. Pessoal, anota isso em algum lugar pra gente já trabalhar nisso hoje.

**Interlocutor 1:** Sim, sim. Pô, isso aí é prioridade.

**Paulinho:** Eu me lembrei de uma coisa assim que eu acho interessante: aqui cada vez que eu faço uma... Por exemplo, nós estamos na 11ª chamada...

*(Interlocutora 3 / Josi retorna à sala)*

**Interlocutora 3 (Josi):** Olha, eu não fui ao shopping, hein? Eu almocei então. Eu sou senhorinha.

*(Risos)*

**Interlocutor 1:** Josi, só pra gente falar um pouquinho da agenda: a gente veio bem dedicado pra Central hoje e a gente também tem uma outra reunião no outro município. Mas a gente pode voltar num outro dia ou fazer de uma forma mais remota e daí a gente conversa com você. Só pra você também não ficar esperando, porque assim: eu falei, vou pegar o Paulinho hoje e falar: "Mano, hoje a gente vai conversar de tudo da Central pra parar de dar esse problema".

**Interlocutora 3:** Tá dando certo?

**Interlocutor 1:** Nossa, sim! Foi bem esclarecedor pra gente.

**Interlocutora 3:** Mas daí a gente já pode fazer uma agenda pra próxima semana então.

**Interlocutor 1:** Tá bom. Aí você prefere que seja presencial ou a gente pode fazer remoto?

**Interlocutora 3:** A gente pode fazer remoto. Ou na sexta-feira, se tiver tranquilo pra vocês.

**Interlocutor 1:** Fechou, aí eu vejo a minha agenda também.

**Interlocutora 3:** Daí me manda o dia que vocês podem e daí a gente faz remoto.

**Interlocutor 1:** Se quiser essa semana, remoto a gente consegue já.

**Interlocutora 2:** Era bom esperar o Gabriel voltar, não? Ele volta dia 5, não é?

**Interlocutor 2:** Gabriel volta dia 5.

**Interlocutora 3:** Mas não precisa o Gabriel. Não. Porque o que a gente precisa é resolver esses pontos de atribuição do módulo, que esses estão dando muito trabalho. A gente não consegue gerar relatório...

**Interlocutor 1:** Não, sim. Vamos fazer o mesmo atendimento que a gente tá fazendo aqui. Passando no ponto a ponto ali pra gente ver onde tá o gap e arrumar.

**Interlocutora 3:** Perfeito.

**Interlocutor 1:** Maravilha.

**Interlocutora 3:** Obrigada, gente. Tchau, tchau. Djalma, faça tudo bem, de verdade.

**Interlocutor 2:** Sou eu ao vivo!

*(Risos)*

**Interlocutor 2:** Quando desligarem o computador eu sumo, mas por enquanto eu tô aqui.

*(Despedidas da Interlocutora 3)*

**Paulinho:** Não, então, eu tava lembrando de uma situação aqui: por exemplo, a gente chama... Tô na 11ª chamada e a gente chamou, vamos supor, 50 alunos. Se assim que eu aprovar já aparecer os 50 alunos ali pra eu criar um PDF, por exemplo, pra guardar... Tem como fazer isso?

**Interlocutor 1:** Como assim? Não entendi.

**Paulinho:** Por exemplo: hoje eu vou chamar 100 crianças. Beleza. Aí na finalização de hoje, eu conseguir baixar o PDF dessas 100 crianças que eu chamei.

**Interlocutor 1:** Então, mas você aprovou 100 crianças hoje? É pra funcionar através do filtro! Do filtro de data de aprovação. É porque é o que eu falei: ele tá dando divergência por conta de que o diretor pode alterar, tá acontecendo um monte de divergência. Quando a gente começar a fechar isso aqui, se você alterar... aprovou 10 crianças hoje e puxar o filtro de hoje, tem que ter as 10 crianças. Porque isso aí é a consolidação dos dados. A gente não tá conseguindo consolidar o dado porque o diretor... A gente consolida o dado hoje, o diretor mexe amanhã, acabou a consolidação do dado. Entendeu? Mas isso vai resolver, com certeza que vai. Com essa nova manobra vai resolver.

**Interlocutora 2:** Porque daí ele já deixa salvo, né? E aí no final do mês só junta tudo.

**Interlocutor 1:** E ninguém vai mexer mais.

**Interlocutora 2:** E ninguém vai mexer.

**Interlocutor 1:** Gente, eu acho que da minha parte era isso. Foi bem esclarecedora a nossa conversa.

**Interlocutor 2:** Muito legal a gente parar pra trocar essa ideia, né? Pra ter um entendimento bem melhor de fato como que vocês precisam da Central. Muito legal. Agora vamos avançar pra executar.

**Interlocutor 1:** E a gente, qualquer dúvida no desenvolvimento, a gente vai mandando mensagem. Mas eu acho que aqui tá bem tranquilo, a gente conseguiu absorver bem aí a dor e a gente até tá pensando no caminho já a seguir.

**Interlocutor 2:** É, sim, foi bem legal. Já deu pra ter umas ideias também de novidades que tá faltando e dá pra gente colocar no sistema. Essa questão do controle de vagas do diretor aí... Muito bom. E também a questão de o aluno ser matriculado na SED e já aparecer...

**Interlocutor 1:** Isso já vai aparecer. Ele vai aparecer... Eu tô pensando em quê: na solicitação aprovada mesmo, só ter um filtrozinho ali, uma tagzinha pra você saber: matriculado, não matriculado. Que passou por você, foi aprovado, então agora tem esse caminho. Fechou.

**Paulinho:** Fechou. Aí eu só vou precisar mesmo daquela listinha do mês de abril.

**Interlocutor 1:** Sim, não, a gente vai corrigir isso aí.

**Interlocutor 2:** Beleza, eu vou trabalhar em cima dela hoje já.

**Interlocutor 1:** Eu acho interessante, só antes de a gente encerrar, fazer uma foto, se possível. Tranquilo? Só pra gente enriquecer a nossa ata. Você viu que foi bem densa a conversa?

*(Risos)*

**Interlocutor 1:** Ô, tira aí que o seu celular é... O Djalma tira, ele é bom em foto. Pra enriquecer a nossa ata com fotos.

**Interlocutora 2:** Aqui a gente não tem muita mania de tirar foto não.

*(Momento em que preparam e tiram a foto da reunião)*

**Interlocutor 2:** Eu desliguei esse celular... É esse de baixo aqui.

*(Cliques de foto e risos)*

**Interlocutora 2:** Você tava na foto que apareceu no Censo?

**Interlocutor 2:** Você me mostrou ele ao vivo!

**Interlocutora 2:** Te mostrei o Paulinho?

**Interlocutor 2:** É, você me mostrou que ele participou também.

**Interlocutora 2:** Agora vou chamar a outra diretoria.

**Interlocutor 1:** A gente alugou o Paulinho! Mas vai dar certo, Paulinho. Como eu falei: cara, aumentando o chamado, a gente viu que tava tendo problema, vamos sentar e vamos resolver.

**Paulinho:** Fechou. Obrigado pelo tempo, viu?

**Interlocutor 1:** Imagina, cara, a gente que agradece.

**Interlocutora 2:** Vai continuar aqui?

**Interlocutor 1:** Tchau. Agora ele vai até a saída, cara.

**Interlocutora 2:** Ah, vou levar! Para um homem que não pega água pra uma mulher, eu tenho que fazer de tudo, né?

**Interlocutor 1:** Foi eu que não peguei?

**Interlocutora 2:** Foi você!

*(Brincadeiras e risos ao fundo enquanto arrumam as coisas para sair)*

**Interlocutora 2:** Quer água?

**Interlocutor 1:** Ah, muito obrigado!

*(Passos e ruídos de saída da sala)*

**Interlocutora 2:** Foi bem tranquilo.

**Interlocutor 2:** Foi bem tranquilo, nossa, até entendi muito bem.

**Interlocutora 2:** A questão do status pra mim agora ficou bem mais clara. Acho que a gente tava misturando tudo.

**Interlocutor 2:** Separar os status não tava muito compreensível, sabe? É melhor pensar nas etapas que acontecem na ação, sabe? Igual tem... Você viu que são ações que separam as etapas? É uma ação do pessoal pra deferir...

**Interlocutora 2:** A gente olhar o log dele vai ter que fazer pela permissão, né?

**Interlocutor 2:** Essa é a melhor ideia. A gente pega o log da atividade. Sabe aqueles logs que aparecem...

*(Diálogo ao fundo com outra colaboradora)*

**Interlocutora 4:** Oi, tudo bem? Bem-vindo!

**Interlocutor 2:** Obrigado!

**Interlocutora 4:** Até agora a gente se viu só pela foto.

**Interlocutor 2:** Isso, eu mesmo! Prazer.

**Interlocutora 4:** Que legal! Não conhecia o pessoal, não conhecia ninguém, na verdade. Nem sei se conhecia pessoalmente.

**Interlocutora 2:** Como eu tava falando aqui: o indeferimento...

*(Conversas paralelas e ruídos de materiais)*

**Interlocutor 2:** Beleza, eu vou enviar um primeiro relatório com os logs da atividade. Eu acho que não é necessário pegar tudo...

**Interlocutora 2:** Ju!

**Interlocutor 2:** Vamos fazer esse primeiro teste...

*(Conversas distantes de despedida no corredor)*

**Interlocutora 2:** Você é o dev, né?

*(Risos)*

**Interlocutora 2:** Já almoçou?

**Interlocutor 2:** Já, já almocei.

**Interlocutora 2:** Deixa eu levar vocês aqui. Tchau, obrigada pela reunião.

**Interlocutor 2:** Tchau, tchau. Valeu.

*(Passos finais e encerramento da gravação)*


---

## 📊 Palavras de Maior Ocorrência nesta Sessão
- **Exemplo**: 63 ocorrências
- **Diretor**: 56 ocorrências
- **Vagas**: 48 ocorrências
- **Aprovada**: 45 ocorrências
- **Paulinho**: 40 ocorrências
