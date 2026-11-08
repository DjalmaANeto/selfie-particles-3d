# Sessão de Terapia - 30/10/2026

## 🎧 Áudio da Sessão
![[Voz_261030_171203.mp3]]

## Metadados
- **Data Original:** 30/10/2026
- **Horário:** 17:12:03
- **Duração:** 118.0 minutos
- **Arquivo Original:** `Voz 261030_171203.m4a`

---

> **Nota de Contexto:** Embora o comando mencione "áudio de terapia", o conteúdo real do registro consiste em uma **reunião técnica de equipe de engenharia e produto de software**, focada em metodologia ágil, gestão de demandas, fluxo de homologação, testes e integração com ferramentas de Inteligência Artificial.

---

### 1. Resumo Geral da Sessão / Reunião

A reunião técnica tem como objetivo principal alinhar e reestruturar o fluxo de trabalho da equipe de desenvolvimento frente à adoção de ferramentas de Inteligência Artificial (como Claude/Claude Code e Gemini) e à gestão do ciclo de vida das tarefas. 

Durante o encontro, a equipe debate o problema da "poluição" da esteira do Trello causada pela proliferação de pequenas tarefas técnicas (*sub-issues* ou *sub-cards*) geradas tanto manualmente quanto pela IA. Isso tem gerado confusão na coluna de homologação, onde analistas e validadores de produto não conseguem testar partes isoladas de código ou infraestrutura. 

Propõe-se manter no Trello apenas cards em nível de negócio (**Épicos/Features completas**), enquanto o detalhamento técnico e a quebra de tarefas passam a ser geridos no **GitHub Projects/Issues**. Também são discutidas práticas para evitar Pull Requests (PRs) gigantescos sem perder a visão integrada do produto, a padronização de *skills* (prompts/agentes para a IA) e o fluxo correto de validação em homologação (*staging*) versus testes automatizados (unitários, regressão e *smoke tests*).

---

### 2. Principais Tópicos e Temas Abordados

* **Épicos vs. Sub-issues / Granularidade de Tarefas:** Definição da fronteira entre o que é regra de negócio (visão do cliente/validador) e o que é implementação técnica (código, refatoração de infraestrutura, alterações em banco de dados).
* **Gargalo no Fluxo de Homologação:** A problemática de mover tarefas intermediárias para homologação antes que uma funcionalidade completa esteja pronta para teste pelo usuário/QA.
* **Trello vs. GitHub Projects:** Proposta de transição do detalhamento técnico para o GitHub (usando *issues* e *sub-issues* nativas) e preservação do Trello para itens de alto nível e regras de negócio.
* **Padronização de *Skills* para Inteligência Artificial:** Desenvolvimento de comandos/prompts padronizados para guiar o Claude Code/Gemini a quebrar Épicos em tarefas executáveis sem inventar fluxos divergentes entre os desenvolvedores.
* **Pull Requests e Estratégia de Testes:** O equilíbrio entre criar PRs pequenos para facilitar revisões de código e manter a integridade funcional da aplicação por meio de testes unitários, testes de regressão e ambientes locais/containers (Docker).
* **Cultura de Equipe e "Pontinhos":** Discussão sobre métricas de produtividade, evitando que a pontuação incentive a fragmentação artificial de tarefas apenas para "bater meta".

---

### 3. Transcrição Completa Organizada por Interlocutor

**Gustavo:** ...arrumar, bi-bi-bi, bô-bô-bô. Todo esse contexto vocês vão precisar passar pra IA de vocês, usar o card do Vinícius como referência, pra que ela possa entender a necessidade de quantos cards eles vão precisar criar. Que é exatamente isso que o Paulo e que o Murilo estão fazendo. O Murilo criou o próprio roadmap dele lá. Você entendeu? O roadmap dele foi lá todo criadinho lá, tá todo dividido numa sequência lógica que ele entende essa sequência lógica. Entendeu? O que vai acabar acontecendo é: com o passar do tempo, os nossos cards, Vinícius, que é de estrutura de negócios, eles vão se tornar, eles vão ficar cada vez mais próximos de um Épico. E o dev com... usando a IA, usando o objetivo a ser desenvolvido do Épico, vai fracionar em quantas atividades forem necessárias para atingir aquele Épico.

**Vinícius:** Mas essas atividades são cards?

**Gustavo:** Isso.

**Vinícius:** Tá. Porque isso aí... e quando a gente entra agora na esteira, sei lá, pode ser que tenham dezessete cards novos que é um cada item desse relatório, tá ligado? Isso não dá uma poluída na esteira?

**Gustavo:** Dá uma poluída.

**Vinícius:** Isso não fica, tipo, um pouco mais confuso pra gente depois olhar? Tipo assim: "Putz, eu vou olhar em homologação agora". Aí tem lá um relatório pra homologar. Imagina que eu vou homologar esse relatório...

**Gustavo:** Uhum.

**Vinícius:** Só que desse relatório gerou quinze cards. Como é que a gente vai ficar olhando pra aquilo lá e falar: "Caralho, como é que eu testo isso aqui?"

**Outro Desenvolvedor:** É, aí entra naquele ponto que... Esse negócio é interessante, mas veja bem. Fiz uma mudança aqui, é uma mudança superestrutural, afeta tudo o que dá. Daí, nesse caso, quando chegar numa situação dessa que um card que a gente precisou, a gente vai ter que ver diversos lugares onde foi ter impacto, não vai ter como fugir. Porque se a gente for lá só clicar em imprimir, a gente só vai clicar em imprimir, mas...

**Vinícius:** Até aí tudo bem, mas eu entendo enquanto é uma... Mas enquanto é, tipo assim: "Putz, tô trocando um service, tô trocando alguma outra coisa", que é uma parte que não tem como a gente testar. Coisas que, tipo assim: "Ah, peguei uma coisa legada e tô fazendo", que é um trabalho que o desenvolvedor faz, pode levar duas, quatro, seis, oito horas fazendo, só que ele criou uma demanda pra isso, só que eu não consigo testar isso. É um exemplo. Mas eu tô falando que pode ser, tipo assim, vinte cards de uma tarefa, que podem ser vinte coisas legadas que estavam nessa tarefa.

**Gustavo:** Nós vamos migrar... nós vamos... Nós vamos migrar pra uma outra metodologia. O Trello vai ficar responsável só pela regra de negócios. Mas enquanto isso não acontece, nós vamos trabalhar no Trello da seguinte maneira. Hoje nós temos aqui o card que o Vinícius cria, certo? A estrutura do card que o Vinícius cria, ele é... como que é o nome lá? Título... Título, descrição...

**Participante:** Labels...

**Gustavo:** Isso, label...

**Participante:** A tag...

**Gustavo:** É, a tag... checklist... Beleza. Checklist, vamos colocar que o checklist é a User Story, beleza? Vamos colocar que o checklist é a User Story. Beleza. Tem algum caso que a User Story tá fora do checklist?

**Vinícius:** Não. Eu descrevo no card, na descrição, o que que é, e o checklist é só mais objetivo.

**Gustavo:** Isso, então beleza. Então o checklist tá todo voltado pro objetivo, certo?

**Vinícius:** Uhum.

**Gustavo:** Vocês concordam comigo que isso daqui é alto nível? Mas, ó: alto nível por quê? Porque ele não tá falando exatamente de código. E ele não tem que falar de código! Aqui ele tem que falar do objetivo, entendeu? Do... assim, do cliente final. Isso aqui é coisa assim mais... mais palpável, mais negócios. É mais sobre o negócio, beleza? Aí o que acontece? O que que acontece no card hoje? Isso aqui... chega lá... vamos dar um exemplo aqui, ó: um card aqui... "Criar..."

**Participante:** O que a gente fez na sexta-feira.

**Gustavo:** "...documento impresso do percentual de presença dos estudantes com nota baixa". Pra isso aqui acontecer, putz, cara... você vai ter que pegar, vai criar um relatório. Na hora que você for criar esse relatório, você vai ter que bater no serviço de presença, aí você vai bater no serviço de presença, você vai ter que depois bater no serviço de notas, aí você vai ter que ver primeiro quais são os alunos que estão com nota baixa, qual eu vou buscar a presença... Aí o que acontece? Chegou lá, não tem a funcionalidade, por exemplo, de você...

**Participante:** O que que é nota baixa?

**Gustavo:** É, você entendeu? Não tem essa funcionalidade do que que é nota baixa, vai precisar criar um outro serviço. E aí ele começa a tomar um... o negócio fica um rocambolesco. Aqui é onde começa a acontecer o quê? Baseado nisso aqui, vamos colocar que quem vai desenvolver isso aqui é o Enrico. O Enrico vai pegar, ele vai falar assim: "Ó..." Vamos supor que esse aqui é o card #1921. Ele vai chegar, o Enrico, vai colar lá o card e falar assim: "Ó, Claude, eu tô tentando... tô pra desenvolver essa demanda aqui, ó. E essa demanda aqui ela é uma demanda que eu preciso desenvolver e tal". Ele tá com o Claude Code na máquina, ele pode pedir pro Claude Code acessar as estruturas da plataforma, o Claude Code vai poder encontrar ali e falar assim: "Não, é só pegar isso aqui, isso aqui". Então o Claude já pode dar um norte ali pra ele, ou ele pode identificar que isso aqui é uma coisa complexa. Sendo isso aqui uma coisa complexa, isso aqui... sendo que isso aqui pode chegar até doze na escala, o que que ele vai fazer? Ele vai pegar isso aqui e vai olhar e vai ter uma sugestão: "Pô, espera aí, então vamos fazer o seguinte: o que que eu preciso fazer aqui?". Então, ó, eu vou precisar criar aqui os cards: um, pra poder fazer um método que lista os estudantes com presença baixa; dois, criar um repositório onde guarda os arquivos na página; três, criar relatório X; quatro, criar função de impressão...

**Dijas:** Ô Gu...

**Gustavo:** Oi?

**Dijas:** ...pra essas sub-issues que são criadas, a gente pode deixar o quê? Pra criar uma tag específica só pra identificar que isso não é uma coisa pra testar. Por quê? Porque o que eu tô enfrentando aqui com o pessoal dos municípios: o pessoal vem e fala assim: "Opa, tem uma demanda que tá aqui em homologação". Tá lá a tag de todos os municípios. Só que daí, mano, às vezes é muito dessas sub-issues que estão sendo feitas, tá ligado? E aí a pessoa: "Mano, como que eu testo isso?". Então fica causando um pouco de confusão no pessoal. Talvez se a gente colocar nessas sub-issues uma identificação de que seja tipo assim: "Ó, sei lá, desenvolvimento interno", alguma coisa do tipo.

**Gustavo:** Por que que tá a sub-issue na homologação?

**Dijas:** Ela tá indo pra homologação.

**Gustavo:** Por quê?

**Dijas:** Porque o desenvolvedor tá criando e tá indo pra lá.

**Gustavo:** Tá indo pra homologação?

**Dijas:** Em homologação. Tem um caso que acontece: evitar PRs gigantes, que é o que eu tenho trabalhado essas semanas. Assim, é meio desumano dar um review numa PR de 100 mil linhas, tá ligado? Ou 10 mil linhas, impossível, desumano. Então, tipo assim, começa a entrar na lógica das issues. Essa issue gerou 50 arquivos, tá ligado? Já é uma boa cacetada ali pra dar uma atenção. Então ela tá em homologação enquanto eu reviso. Enquanto eu passo pra galera, a galera vai subir. Da homologação concluída, passou pra desenvolvimento...

**Gustavo:** Certo.

**Dijas:** Daí se resolve assim: essa sub-issue passou por esse processo. Então é um bloco que não ficou lá segurando e passou por esse processo.

**Gustavo:** Beleza.

**Dijas:** Acho que falta etiqueta pra isso mesmo.

**Gustavo:** Então, mas calma, calma, calma! Ó, eu vou trazer a proposta aqui pra vocês. Ó: o card, quando ele vier como uma regra de negócio, ele vai começar a ser Épico. Por quê? Existe funcionalidade dessas aqui que precisa de alguém testar pra avançar?

**Participante:** Não, mas é coisa interna, técnica, né?

**Dijas:** Mas o desenvolvedor sempre precisa ver o que aconteceu.

**Gustavo:** Então, mas como de ordem prática... como de ordem prática o mediador vai conseguir fazer um teste no método que você tá criando?

**Dijas:** É, não tem como.

**Gustavo:** É por isso que eu tô falando pra vocês. Cara, essa galerinha aqui, hoje, ela tá ficando lá na nossa esteira lá em homologação, entendeu? Por dois motivos: um motivo é o pessoal dar OK, que nem sempre eles vão dar OK; e o outro porque ele tá em homologação e alguém precisa jogar eles pra produção. Certo?

**Participante:** Para homologação concluída.

**Gustavo:** Exatamente. Que é homologação concluída em produção.

**Participante:** Não, é diferente. Homologação concluída é depois que eles validam a demanda e deu certo. Homologação concluída, o desenvolvedor pega e joga pra produção.

**Participante:** Tem que desmover o código também.

**Vinícius:** É, tá em homologação, aí o time vai lá e testa a funcionalidade: "Ah, não, deu tudo certo". Aí eles movem pra homologação concluída. Aí, a partir daí, o desenvolvedor responsável move pra produção.

**Gustavo:** Tá. Então beleza. Vamos fazer o seguinte, então. A gente tá aqui com essa dinâmica pra poder resolver. O que eu ia propor é: o card, quando vem com regra de negócio do cliente, ser Épico. Ele chega aqui, cai na mão do dev. O dev olha pro card Épico e, com a ajuda da IA, quebra essas tarefas em tarefas menores, palpáveis, pra esteira de desenvolvimento. Tudo o que é desenvolvido aqui, ele vai sendo implementado e aqui ele não passaria em homologação, ele já iria direto. Porque o único card que ficaria em homologação seria o Épico.

**Vinícius:** Que é o testável, né?

**Gustavo:** Que é o testável!

**Dijas:** Eu posso trazer um caso que aconteceu comigo? Justamente é como eu tenho trabalhado, usando a nossa esteira que já existia. Assim: por exemplo, teve um caso mesmo que, de uma reunião, eu, o Vinícius e a Pâmela, sobre atribuição, aquelas coisas que eu estava trabalhando, me deram duas semanas de trabalho pra uma task. Uma task que deu dezesseis cards. E foram dezesseis cards de um documento de plano de desenvolvimento que eu fiz enquanto a gente trocava ideias, em cima da ata deles lá. Então você vê o tanto de coisa que já tinha, tipo assim, encaminhando esses dezessete cards, tá ligado?

**Gustavo:** Sim.

**Vinícius:** Esses dezessete entrariam como sub-issues, né?

**Dijas:** Isso, seriam sub-cards. Nesse caso, eu acho que cai bem nessa, porque você vê: pô, duas semanas de desenvolvimento contra dezesseis cards. Faz sentido, tá ligado? Muitos cards ali eu mesmo dei o tempo de desenvolvimento de menos de duas horas, tá ligado? Então faz muito sentido assim. E outros eu vi que iam ser umas seis horas de trabalho assim. Daí eu falei: pô, faz muito sentido esses... e tudo ali era realmente um script pra rodar o negócio, tá ligado? Só que daí eu comecei a colocar: pô, esse daqui depende desse, então esse primeiro, certo? Beleza, seguindo a ordem. Só quando parou de depender, daí começou assim: pô, quatro em desenvolvimento ali no Claude, tá ligado? Daí eu falei: porra, tô com quatro cards em desenvolvimento. Eu vou dar review em um pra passar pra homologação, pro pessoal passar de homologação pra homologação concluída e ir pra dev... Daí eu falei: caralho, então, tipo assim, contra esses quatro que tá em desenvolvimento, eu vou ler um assim, tipo, nessas duas horas, tá ligado? Então o que que eu faço com esse card? Fico com quatro cards em desenvolvimento, com cinco, né, que eu já vou dar review em um... com cinco cards em desenvolvimento, ou eu coloco... vou passando eles um por um conforme o desenvolvimento, todos pra homologação? Eu optei por esse lado. Falei: pô, então beleza. Daí já mudei mesmo ali no Claude, quando ele terminar o código, ele me entrega a PR, eu vejo a PR, testo e tal, e ele coloca em homologação. Então no homolog já tá como se fosse em dev, sacou? E daí esse é o jeito que tá agora. Só que daí eu me deparei com esse lance mesmo: porra, então passei aqui quatro cards pra homologação pra Pâmela ver, que na real ou ela baixa o Postman e começa a mandar os negócios, ou ela não vai ter como ver isso aqui, tá ligado?

**Gustavo:** Exatamente.

**Dijas:** Daí esse é o ponto onde parei. Daí precisa dar uma... preciso pensar nisso aí.

**Gustavo:** Sim, é isso que nós estamos discutindo aqui.

**Outro Desenvolvedor:** Você fazia os Épicos e a gente criava ali os sub-cards disso e era anexado no Épico.

**Gustavo:** Exato!

**Outro Desenvolvedor:** A gente pode continuar nessa base...

**Gustavo:** É isso que eu tô... é isso que eu tô tentando trazer de volta.

**Vinícius:** Uma outra coisa também que eu acho que a gente precisa fazer é a questão que o Dijas comentou do "em desenvolvimento". Porque agora a gente olha ali no gráfico, aí eu pego lá: pô, Djalma. Aí o Djalma tá com cinco cards atribuídos, tá ligado? Como que fica isso?

**Participante:** Às vezes ele não rodou ainda o crawler lá pra atualizar aquela dashboard...

**Vinícius:** Não, muitas vezes tá mesmo! O Djalma esses dias tava com cinco demandas.

**Gustavo:** Mas, ó: usando a IA, usando a IA é possível trabalhar com mais de uma frente de desenvolvimento.

**Dijas:** É, eu acho que isso dá pra aceitar agora. Vários em dev.

**Participante:** Tem até aquela questão que você falou de coisas paralelas, às vezes coisas paralelas que é de melhoria, que a gente vem conversando sobre isso hoje de manhã. Porque hoje, agora sim, a gente tinha um código completamente personalizado e só de entrega de valor, mas entrega de engenharia muito pouca. Então a gente acaba tendo muita coisa de manutenção, justamente por causa desse escopo de trabalho. Agora que a gente tem a potência e a possibilidade de usar uma IA que vai fazer isso pra gente, poupar nosso tempo de trabalho ali de engenharia e colocar as coisas no eixo, a gente vai encontrar muito sub-assunto...

**Gustavo:** Que vão poder rodar em paralelo.

**Participante:** ...que vai poder pedir pra ela fazer. E aí não precisa ser documentado, porque a gente também é ganancioso e quer nosso pontinho no final do mês?

**Gustavo:** Não, exato! Mas assim: o pontinho, cara, o pontinho é igual chip, cara. É coisa que botaram na tua cabeça, mano. Não se preocupa com isso!

*(Risos na sala)*

**Dijas:** Eu comecei bem contra pontinho assim, e agora que eu tô vendo ele correr ali pelos cards...

**Gustavo:** Mas é interessante, é interessante. Mas o negócio do pontinho é que é assim: porra, mano, nós somos uma equipe que nós estamos juntos há muito tempo, nós somos colegas de trincheira assim, a gente já passou por muitas coisas, né? Uma coisa que eu vou pedir pra vocês, cara, é pra vocês não se iludirem com o pontinho. Não vai ter um parabéns pra quem fizer mais e não vai ter um corte pra quem fizer menos, tá ligado? É isso que eu tô falando pra vocês. Mas é uma coisa legal, esse negócio tipo assim, a treta saudável do Dijas com o Murilo ali, que o Murilo: "Tô passando você", o Dijas manda amolando o facão pra ele... Isso aí eu acho saudável, entendeu? Tudo bem. Mas assim, o que eu não quero que aconteça é, tipo assim, alguém chegar lá, inventar um monte de task só pra ganhar ponto, tá ligado? Isso aí ia ser foda.

**Gustavo:** Essas subtasks aqui, ó, antes que a gente avance: essas subtasks aqui, eu tenho o planejamento de mandar essas subtasks aqui pra serem gerenciadas pelo GitHub. Entendeu? Aí vocês vão parar de criar subtasks no Trello. O Trello, ele vai andar só com o card Épico.

**Vinícius:** O Trello não tem card e subcard? Ele tem anexos, né?

**Gustavo:** Ele tem... não, sub não, só anexo. Porque o que acontece: a minha ideia é criar essa estrutura toda de subtasks aqui, ficar lá no GitHub. O GitHub tem lá, o Murilo já me mostrou um monte de vezes essa funcionalidade...

**Dijas:** Eu fiz um no caseirão, cara, usando o Obsidian. Fiz essa estrutura que você tá fazendo.

**Vinícius:** Só que a partir do momento com essas subtasks que a gente tá gerando em cada demanda, não tá cabendo em homologação.

**Participante:** Eu tenho uma opinião sobre isso aí, tá ligado? Sou do time que cards que não precisam ser testados... eu discordo disso, tá ligado? Porque, por exemplo, toda alteração mexe no código. Seja ela técnica ou não. Eu atualizei, por exemplo, aqui a versão do PHP na tabela, tá ligado? Aí eu preciso que o Gabriel olhe. Vai no teste, entra no curso, tá com a fonte gigante? Tem que chamar a atividade e...

**Murilo:** Mas isso impacta a regra de negócios.

**Participante:** Eu tenho um caso sobre isso, tenho um caso sobre isso.

**Gustavo:** Galera, ó: esse caso ele é resolvido da seguinte maneira: o pessoal... não é que o pessoal não vai testar. O pessoal não vai testar no subcard, eles vão testar no Épico! Entendeu? Porque daí vai vir o contexto todo pra ser testado.

**Vinícius:** O Dijas fez uma lá da questão do token. Isso aí precisa ser testado. Só que isso aí é uma coisa que, tipo assim, mano, tem um card pra isso que vai ser um Épico, tá ligado? O que a gente tá discutindo não é que eles não vão testar o Épico, eles vão testar lá. O relatório que eles vão imprimir com a porcentagem dos estudantes, eles têm que testar isso. Mas, mano, o que você fez ali pra gerar esse relatório, o componente que você atualizou, o bagulho que tava legado, como é que eles vão testar isso?

**Outro Desenvolvedor:** Ô Murilo, eu tenho um caso sobre isso, cara. Vamos supor que tá lá na parte de criação do curso. Então, cara, se eu não entrar ali como admin e fazer o teste, eu não vou saber o comportamento. Se eu não entrar como formador, também não vai ter...

**Vinícius:** Tá, mas dentro dessas sub-issues, o Épico qual que é? O Épico foi que agora precisa pegar e colocar ali um filtro, por exemplo, lá na parte de busca do curso. Esse era o problema. Quando o Murilo foi atacar, ele viu: "Ó, pra resolver isso aqui, eu vou ter que quebrar esse card em menores". Aí ele quebrou. Nessa que ele quebrou em cards menores, por mais que eu queira testar o Épico pra poder garantir a entrega, se eu não verificar cada passo que ele fez, vai dar ruim!

**Vinícius:** Não, é inviável a gente falar pro time testar dezessete sub-issues!

**Gustavo:** Não é isso, cara! É que, tipo assim, as sub-issues, elas são pra atender a issue principal.

**Vinícius:** Isso! A issue principal tem que testar! Ela estando 100%, isso aí o Épico tem que ser testado de cabo a rabo.

**Outro Desenvolvedor:** Falta uma descrição, tá ligado? Por exemplo, eu fiz a alteração do PHP na tabela. Qual que é a descrição, tipo assim, de um roteiro deles? Como que eles podem testar?

**Vinícius:** É, mas aí vai cair no looping de você ter que dar um roteiro pra eles testarem.

**Outro Desenvolvedor:** Não, mas não é muito bem assim. Veja bem, ó. O que até ia falar com vocês depois assim. Porque vamos supor: qualquer problema que eu vou entrar ali agora e vou descrever um card, eu sei o que eu preciso ter, digamos, nos meus cards quando eu tô controlando ali da transmissão ou até mesmo do Zeus, ou até mesmo no de gestão educacional. Por quê? Ó: eu montei uma estrutura: o card meu tem que ter isso aqui, coloca essas informações. Dessas informações, o meu próprio Claude, ou até mesmo o ChatGPT, já me dá o checklist. Então eu, por mais que independente do projeto que eu estou, se eu pego uma problemática, eu consigo criar um card dessa maneira. Se cada dev aqui começar a criar um card do jeito que quiser...

**Vinícius:** Não, essa é só o contexto...

**Gustavo:** Tá proibido criar card, mano! Criar card agora é com o Claude e só! Nem eu vou criar, ninguém vai criar.

**Participante:** Mas se ele não tiver o contexto, você vai ter que passar...

**Vinícius:** Mano, mas no caso dessas sub-issues, mano, isso aí são coisas que ele tem que atualizar no código, que não tem como eu testar, não tem como eu pegar e falar assim: "Putz..." Dá um exemplo bom aí, Diga, se você não conseguiu...

**Participante:** Não, o exemplo de código às vezes é de produto e o outro do... O Épico é sempre produto, é sempre negócio.

**Outro Desenvolvedor:** Por isso a atualização de PHP, caralho, ali é praticamente infraestrutura.

**Gustavo:** É, não tem nem...

**Participante:** Pega a métrica de todos...

**Gustavo:** Não tem nem regra de negócio ali.

**Participante:** Mas dá pra testar porque, se quebrar num lugar, vai quebrar tudo.

**Vinícius:** Ó, beleza. Eu peguei essa informação e entendi certinho. Mas a minha dúvida é: as sub-issues vão pra onde agora?

**Gustavo:** Então, eu também tô com essa dúvida, por isso que eu trouxe aqui pra gente.

**Vinícius:** Vão direto pra prod?

**Gustavo:** Ah, por mim, mano, enfiava um o dedo no cu do outro e falava: "Ah, foda-se essa porra!"

*(Risos na sala)*

**Dijas:** Eu tenho um blog... Porque poderia fazer o seguinte: essas sub-issues na verdade nem ficavam no Trello nada, iam direto pro GitHub.

**Gustavo:** Então, eu quero levar pro GitHub! Eu quero levar pro GitHub. A gente vai rodar um curto período com isso.

**Participante:** Mas como é que gera essa... esses cards dois ali? Vai ficar na camada da IA fazer isso?

**Gustavo:** É, a IA gera. Porque, cara, a ideia é a seguinte, ó: você pegar o card do Trello, colar lá no GitHub lá e falar pra ele quebrar aquelas tarefas lá, cara.

**Vinícius:** E esse é o mundo que a gente quer chegar...

**Dijas:** Cara, eu tenho uma observação sobre esses bagulhos que o usuário não testa, mas a gente testa como desenvolvedor. Teve um chamado que eu alterei um negócio, e pra resolver esse bagulho que o usuário não testa, eu tô fazendo o Claude rodar teste de regressão no sistema inteiro. Então assim: haja token, tá ligado? Mas aumentou o bagulho lá, tá dando certo.

**Participante:** Se o negócio tá usando...

**Dijas:** Daí eu peguei um caso, cara, onde a gente tem que abrir o bagulho e testar. Pegou... alterei um bagulho na Central de Vagas de um chamado. O chamado passou, deu pra galera: "Revisa aí e bora". Daí o Vinícius falou: "Mano, aqui, ó, esse bagulho aqui não tá devolvendo", tá ligado? E era um bagulho que no teste de regressão passava, tá ligado? Porque tava escrito do jeito que tinha que acontecer. E passou! Só que nenhum humano viu aquela parada, tá ligado? Do que eu testei, ia, tá ligado? Só que no bagulho de cima, do chamado que a tia tava reclamando, ela ia ler o bagulho de cima, ela não ia continuar pra baixo, tá ligado? Ia devolver o chamado. Então, tipo assim, tem que ter uma conferência da feature inteira sempre, tá ligado? Tipo assim, ou não?

**Vinícius:** Então, mas a feature inteira seria o nosso Épico! Porque assim, ô Dijas: isso é a regra de negócio, isso é o que tipo assim, a gente vai descrever o que que a gente espera da ferramenta. Descrevi o que eu espero da ferramenta. A pessoa vai lá e vai testar isso. Se você, mano, colocou um "cu de marreta" no código lá pra funcionar...

*(Risos)*

**Vinícius:** ...a pessoa não tem que testar isso, não consegue, tá ligado? Ela tem que testar o quê? A ferramenta que foi solicitada tá funcionando? Eu tô clicando, tô abrindo o relatório, o relatório tá baixando, tá apresentando as informações? Tá. Agora se você colocou lá, colocou no Blade que sei lá o quê, e criou uma sub-issue pra isso, tipo, mano...

**Dijas:** Não, mas isso o cara não vai testar. O cara não vai testar o endpoint novo que eu fiz. Só que lá vai tá escrito: "Atribuição: inscrição". O que que o cara vai ter que fazer? Uma inscrição de atribuição. Sei lá, tá falando assim: agora na API tal tal tal, ela diminuiu três milésimos de segundos e ficou roxa. Tipo assim, o cara não vai ver isso, tá ligado? Só que ele vai fazer uma inscrição de atribuição.

**Vinícius:** Então, mas aí é um Épico, a inscrição de atribuição!

**Dijas:** Não, mas é o card filho da atribuição inscrição, sacou?

**Gustavo:** Então, esse tipo de problema que você teve, o que vai cobrir isso é teste unitário.

**Dijas:** É, mas passou no teste unitário. Mas você tinha que testar tudo. O teste unitário, ele tava escrito pra passar. Ele tava escrito do jeito que tinha que ser. Só que quando você abria a tela, não era do jeito...

**Participante:** Mas aí é um problema de implementação. Às vezes a validação de front lá que era um campo de data e virou um texto...

**Gustavo:** Mas, ó, gente! A gente tá descendo num nível aqui, subindo num nível de discussão do sexo dos anjos. E não é isso que eu quero pra nossa reunião! A nossa reunião, a matriz dela, o ponto principal dela, o lastro principal dela é o seguinte: nós estamos com IA. Êêê, bacana! Agora, como é que nós vamos usar a IA da maneira correta? Não adianta ficar só na responsabilidade do Vinícius de ficar usando a IA pro Trello. Peço que vocês também usem a IA pra poder fazer essas coisas. Então, primeiro passo que eu quero combinar com vocês aqui: pegou um card de negócio novo pra ser desenvolvido, pegou um card grande assim... Pô, tá bom, tem um cardzinho ali que é criar um botão ali que alguém pediu, não precisa fazer isso. Mas pra um card que é grande, que vocês viram lá que é um cardzinho complexo, viu que bate numa regra de negócio que é complexa, tudo, mano, pede pro Claude olhar isso aqui, olhar a base de dados que vocês têm usando o Claude Code e verificar se pra fazer essa tarefa é complexa, não é, se tem algum problema na análise dele. Batendo essa análise, orienta ele, fala assim: "Ó, se tiver que quebrar esse card em mais atividades, quebra pra mim, por favor". E pede pra ele quebrar, né? E já colocar aqui já o card anexo. Aí o que acontece: ó, isso aqui virou um Épico! Vai lá, muda pra Épico quando fizer isso, entendeu? Pra que a gente possa saber... que nem o Dijas criou dezesseis cards lá. Esses dezesseis cards que ele criou, entendeu? Por a gente não tá com essa comunicação, na hora ali a gente ficou: "Putz, o que que tá acontecendo aqui?", você entendeu?

**Vinícius:** É, algum componente que você alterou, alguma coisa do código que não dava pra testar.

**Dijas:** Eu agora vou... brigão com isso, tipo assim...

**Gustavo:** Oi?

**Dijas:** Eu vou poder criar um card derivado desse?

**Gustavo:** Não, vai mexer no card principal.

**Dijas:** Tá escrito assim: "Atribuição: inscrição", ou "Atribuição: alocação", pensa que é uma task. Como que vai ser testado isso? Entrando na tela de atribuição alocação.

**Gustavo:** É, você pega, clica lá no card...

**Dijas:** Não...

**Gustavo:** Aí você põe anexar, aí você coloca a URL do card que você quer anexar e anexa. Fica linkado.

**Vinícius:** Mas a questão que eu ia dar...

**Gustavo:** Depois vocês vão ver. O Épico é os cards filhos, né?

**Dijas:** Sacou?

**Gustavo:** É, eu acho que... o que eu quero, a minha expectativa agora de orientar vocês a fazer isso é porque eu sei, eu tenho certeza, eu conheço vocês, cara, não é de hoje! O que que vai acontecer? Um vai anexar, outro vai colocar código, outro vai colocar o... "Ah, eu coloquei o primeiro nome", outro vai colocar... um vai criar a síntese... É, exatamente. Aí a gente vai entender isso aí, qual que é a melhor que ficou e vamos chegar e falar assim: "Ó, vamos fazer todo mundo esse".

**Dijas:** Cara, eu tenho um bagulho que eu acho que é um dos bagulhos mais sólidos assim que eu consigo trazer hoje, que é de criar card mesmo, tá ligado? Esse bagulho de ser, tipo assim: pô, teve uma reuniãozinha, tipo assim, ou teve uma ideia que foi trocada, virou uma demanda. Daquela coisa que troquei ideia, agora tem duas semanas de trabalho. Porra, duas semanas é muita coisa, tá ligado? Vai ser... vai ter... é tempo pra se fazer bastante coisa. Então vou criar os cards, vai ser criados cards. Bem beleza. Vou lá, crio os cards. Eu tô usando, na moral, o Gemini pra fazer isso, bota fé? Porque meu espírito muquirana me faz usar os tokens só pra código do Claude, tá ligado? Mas beleza. Daí beleza, tem o arquivo lá, coloquei lá na IA tal tal tal. Daí pra pegar as estimativas... se bem que isso aí eu já decidi que não vou usar, vou deixar no dia seguinte atualizar lá. Mas, por exemplo, pra criar o formato do card, tá ligado? De ter o formato que é nosso assim. Primeiro a IA tava criando uma parada, daí eu troquei ideia com o Vinícius e pedi pra ele me passar o exemplo, o card exemplo. Daí ele me passou o card exemplo e eu montei o layout. Agora tá saindo... você não viu, ó?

**Vinícius:** Não, não vi, porque eu vi aquele que você criou com AL.

**Dijas:** Ah, essa é a sigla, essa é a nomenclatura. Era de Atribuição Alocação, né?

**Vinícius:** É, então, nessa aí eu dei uma perdida. Mas isso aí, tipo assim, esses dezessete que já eram, são sub-issues?

**Dijas:** São sub-issues. Daria pra colocar sub.

**Vinícius:** E o principal é o...

**Dijas:** Sim! Mas então, o que eu queria trazer é que o que eu criei, na real, foi uma skill própria pra isso, tá ligado?

**Gustavo:** Exatamente! O que que eu vou fazer? Eu vou criar uma skill aqui do jeito que o meu modelo tá gerindo lá a esteira, e aí eu vou pedir pra ele criar uma skill aqui e vou passar essa skill pra vocês. Aí quando vocês forem criar o card, vocês sigam em cima dessa skill.

**Dijas:** Já tem várias skills, barra subagente, barra nomenclaturas lá...

**Participante:** É, mas nenhuma é nossa.

**Dijas:** É, que... mas tem as nossas que já tá em produção, que é o /orquestrador. Não sei se vocês tão usando. Se vocês derem um /orquestrador no Claude, ele vai... ele usa todos os... as nossas regras definidas em ponto... ponto Copilot e ponto Claude, que foi mergeado junto assim. Daí, mano, tá funcionando muito pica assim. Você coloca lá, ele monta: implementador...

**Gustavo:** Mas quem criou essa daí?

**Participante:** O Dijas também, né?

**Gustavo:** Não, foi o Felício que criou.

**Participante:** O Felício? Foi? Nem sabia.

**Gustavo:** Então, aí, ó. Vocês sabiam disso?

**Felício:** Tá em teste, mas não tá em produção.

**Dijas:** Cara, eu já alterei, já fiz o caralho...

**Felício:** Então, é... mexeram bastante. Tá em teste ainda, eu não divulguei não.

**Participante:** Eu criei uma pra criar card no Trello.

**Gustavo:** Aí, ó, viu? Você também criou!

**Dijas:** O esquema é fazer essa coleção de skills, cara. A gente colocar num repositório, alguma coisa...

**Vinícius:** É, e deixar uma padrão, porque cada um tá criando uma de um jeito.

*(Várias pessoas falando ao mesmo tempo sobre criar skills no Claude, chat e comandos paralelos)*

**Outro Desenvolvedor:** Se não, depois a própria equipe local lá na ponta vai se perder na hora de testar, porque vai estar escrito de outro jeito.

**Participante:** Tem que ser mais objetivo nisso, né? Não ter tantos e ter os principais, né? Criar card...

**Outro Desenvolvedor:** É, mas aí que tá. Esse negócio que a gente tá fazendo agora é legal porque volta a ter aquela esteira lá, aquela primeira skill aí, vamos supor, a skill do Trello, digamos assim, skill de card de Trello. Tendo essa skill lá toda a gente, quando vocês forem fazer, vai apontar nesse motor de regras que o Gustavo colocou. Então vai todo mundo estar usando o mesmo, então não vai ter o do Felício, não vai ter o do Enrico...

**Gustavo:** Vê se tem algum card a ser desenvolvido aí que tá ali pra gente poder entender o que cabe nessa esteira de Épico que alguém vai ter que desenvolver aí em breve.

**Participante:** Eu cheguei agora, tô entrando no meio da conversa aí, mas já que a gente tá falando disso, de card na tela e tudo mais, já não era melhor a gente passar a utilizar o Projects do GitHub?

**Gustavo:** É isso mesmo que nós estamos fazendo! O que que a gente tá fazendo aqui: nós estamos estabelecendo que os cards do Trello vão começar a ter o contexto mais Épico. E aí eu vou criar uma skill pra galera, só pra auxiliar a galera nesse período transitório, de fazer o quê? Ler o card Épico e a skill já vai granularizar, por exemplo, o que precisa ser desenvolvido com base no Épico. E aí, em breve, isso aqui, ele vai sair do Trello e já vai pro Projects. É pra gente ter, sei lá, uma, duas semanas pra gente preparar o ambiente do Projects, pra gente começar a colocar lá. Você entendeu?

*(Murilo e outros participantes mostram telas com exemplos de Épicos e quebra de tarefas criadas via IA)*

**Gustavo:** Isso aqui é um Épico, multi-temas, ó. Aí já tem o checklist, já estão os 20 e poucos aqui, tá vendo?

**Participante:** Ô Dijas, preciso do carregador...

**Gustavo:** Por que que tá tendo essa facilidade do Murilo? Porque aqui a gente não tá falando de regra de negócio, o Murilo tá sozinho no board. É igual o Paulo também.

**Vinícius:** Então, mas ó, o que que a gente já pode ir fazendo, mano, a partir da conversa ali: deixar essas sub-issues todas no Git, configurar esse ambiente ali e deixar o Trello só a regra de negócio.

**Gustavo:** É! Aí ficaria o multi-temas aqui em desenvolvimento, entendeu? Essas sub-issues não existiriam aqui, existiriam lá no GitHub.

**Vinícius:** Aí no... o Épico do multi-temas aqui no Trello vai ser o quê? Descrevendo o que que é que o Murilo tá fazendo pra gente conseguir testar depois. Tá ligado?

**Gustavo:** É.

**Vinícius:** Alto nível. Vai conversar lá: "Ó, quero um relatório de alunos".

**Gustavo:** É, exatamente.

**Vinícius:** Porque o que eu tô enfrentando ali agora de dor é, tipo assim: eu entrei em homologação, tem tipo 21 cards assim.

**Dijas:** Tá, mas deixa eu te falar a exemplificação desses cards em homologação. De dezesseis cards, estão em homologação coisa de oito cards, tá ligado? Esses oito cards são coisas simples mesmo assim: a responsiva na média lá, mas ainda não tem nada, não tava dando pra ser visualizado. Mas a questão... voltando para a homologação da atribuição: você já entrou e clicou no botão de homologação da atribuição?

**Vinícius:** Não. Mas você não acha que isso aí a gente teria que ter um Épico escrito "Atribuição: alocação", e aí a gente descreve?

**Participante:** Mas não seria melhor ter isso granularizado pra você só testar aquilo?

**Vinícius:** É, exatamente. E aí essas sub-issues não vão pra homologação.

**Dijas:** Cara, você vai pegar aquele bagulho da Central de Vagas, por exemplo. Tipo, como que começou essa esteira dessa sessão? Quando chegar aí o seu pontinho, já passou um pontinho, mandar pra produção. Você mandou pra produção, mas quando você clica no botão, a feature de cima não tá funcionando. Sacou?

**Vinícius:** Mas se a gente conversar, conversar, a gente não vai avançar nisso, mano. Eu acho que a gente tem que testar esse novo cenário de Git, tá ligado?

**Outro Desenvolvedor:** Gustavo, uma questão que a gente tá pecando, que eu acho que tá usando ferramenta errada: pra desenvolvimento, o Trello é a ferramenta que a gente tem pra acompanhar isso? Não é a mais adequada. Ela é só pra produto, talvez.

**Gustavo:** Não, não é. O Trello, ele dá pra usar, entendeu? Dá pra usar. É assim: depende de alguns objetivos, entendeu? Por exemplo: o Trello é uma ferramenta ótima pra gente poder pegar e tratar features a serem desenvolvidas. Só que o que acontece: o que eu sinto é que o Trello, ele tá resolvendo um pouco pra galera que tá na ponta e pouco pra galera que tá aqui. Entendeu? E a gente tava tentando fazer o quê? Agradar os dois lados. E não vai conseguir, você entendeu? Fazendo isso vai poluir muito. Eu ia fazer o teste com uma skill de criar no Trello os subcards, porque os subcards eu vejo que é uma coisa comum entre os devs, que é uma coisa que ajuda os devs. Mas não necessariamente que o Trello ia cuidar disso. Em algum momento a gente ia levar pro GitHub Projects, entendeu?

**Gustavo:** O Trello, agora que nós fomos pondo mais coisas nele, mas antes ele tava focado só na regra de negócio. Quando ele tava focado só na regra de negócio, era muito mais claro pro pessoal lá na ponta isso, entendeu? Agora, com esse monte de sub-issues, isso com certeza vai... vai embaçar a visão.

**Dijas:** No Trello você tem que se acostumar a clicar no botão, tá ligado? Eu acho que esse espaço também... Cara, não tem como eu passar, tipo assim, um mês sem atualizar nada, tá ligado? E atualizar tudo de uma vez. Mas tipo assim, com a IA torando o tempo... Dava pra fazer isso, mas tipo assim, você vê que o time não pega, tá ligado?

**Gustavo:** Então, mas ó...

**Dijas:** Só que daí tem outro processo: cara, subiu pra quebrar, quando dá uma linha de código, uma linha de código trava o negócio!

**Participante:** Mas aí tudo tem que ser testado...

**Dijas:** Eu testei e foi, daí passou por mim, o negócio tava plugado, tá ligado? A Pâmela não viu.

**Gustavo:** Então, mas ó, a gente vai ter que separar as coisas. A gente vai ter que parar de ficar nessa de que tudo é responsabilidade de todo mundo. A nossa esteira de desenvolvimento hoje é tudo responsabilidade de todo mundo, entendeu? Num certo nível. Cara, você vai numa mecânica, você vai lá e fala assim: "Ó, meu carro tá com problema". O cara fala assim: "Ó, isso aqui é a biela, a porca da parafuseta, essa borracha, é o..." Como é que o cara gosta de usar lá, o que tava falando no celular que deu problema lá no... cebolinha?

**Participante:** Cebolinha, é.

**Gustavo:** É o rotor de não sei o quê... Beleza. Você, cara, você como cliente, você até pode ser um curioso, uma pessoa que entende de veículo e entender o que o cara tá falando, mas beleza, você quer que arrume o carro. Fechou. O cara começa a trabalhar no carro, entendeu? É assim: terminou o serviço, ele fala aqui: "Ô, seu Gustavo, pode passar aqui e pegar o carro que ele tá pronto". Beleza, vou lá, vou pegar o carro, vou sair do carro... Tem uma taxa de acurácia, né? Uns 30% das vezes você vai pegar o carro que tá pronto, você sai, aí você tá chegando em casa, começa a ouvir um barulho. Aí você: "Pô, tô ouvindo um barulho aqui e tal", entendeu? Só que, antes de isso acontecer, o mecânico trabalhando no carro lá, enquanto ele tava trabalhando: meu, ele tava lá, tava com o carro ligado, ele acelerava: "Vrum, vrum!". Pra ver se não tava fazendo nenhum tipo de barulho. Tem os testes que são internos! A gente vai ter que começar a separar isso.

**Dijas:** Esses testes são os testes mais importantes pro bagulho funcionar. É igual eu disse: por que que eu tô defendendo um card que tenha esse teste pra Pâmela? Porque o que que ela vai fazer? Ela vai entrar, ela vai logar, ela vai abrir a atribuição, vai abrir a alocação. Chegou ali, cara, fechou, tá provado! Sacou? É esse lance. Você pegou o carro, você não vai lá no mecânico, você não vai estourar o cinto de segurança. Você vai abrir a porta, entrar, ligar. Ligou, acelera duas vezes...

**Gustavo:** Beleza, mas não acontece de você falar assim: "Beleza, testou aí? Então agora vai volta pra sua casa que sexta-feira eu te entrego o carro"? Não é assim, entendeu? É isso que eu quero que vocês entendam.

**Vinícius:** Mas você não acha que nesse cenário que você propôs, você não acha que tá errado alguma coisa antes ali? Você não acha que teria que ter o card de regra pra fazer esse teste que você tá falando? E não na sub-issue? Essa sub-issue tem que ser passada justamente por esses testes...

**Dijas:** Não, mas como faz o teste na prática? Esse teste que vocês estão falando é justamente o smoke test, tá ligado? Não é tipo assim: "Porra, a antena na API que tá escrita API/não sei o quê..."

**Vinícius:** Não, o smoke test a gente vai fazer pra dentro, mano. Não volta mais essa parada pra Pâmela!

**Dijas:** Não, mas se tiver na regra principal do card aqui no Trello, mano, é isso que eu tô falando! Porque pra eu testar a primeira etapa, você vai criar o processo de atribuição, você vai criar uma atribuição... E em algum momento você não vai fazer esse teste, cara?

**Participante:** Vou dar outro exemplo aqui, ó. Esse card aqui, por exemplo: "Atribuição: inscrição". Ó, isso aqui é um Épico.

*(Discussão sobre detalhes visuais, responsividade e formulários na tela)*

**Vinícius:** O que eu tô falando é que em algum momento a Pâmela, ela vai esbarrar na sua sub-issue e vai falar assim: "Hum, travei. Aqui eu travei". E aí, mano, não vai ser a sua sub-issue falando da API da puta que o pariu que ela vai olhar e falar: "Vou travar aqui". Ela vai testar e aí no Épico ela vai falar: "Dijas, ó, parei na etapa de alocação aqui e travei. Ó, apareceu esse erro pra mim aqui".

**Dijas:** Apareceu um erro. Então isso não vai pra produção, pelo amor de Deus!

**Vinícius:** Mas ninguém tá falando de ir pra produção a sua sub-issue! O que eu tô falando, Dijas, é que essa sub-issue tá indo pra homologação. Então hoje eu tenho 23 demandas em homologação. Só que muitos delas, mano, são sub-issues que não tem como testar! E o pessoal fica tipo assim: "Cara, o que que eu faço com isso? O que que eu faço com aquilo?". Entendeu?

**Dijas:** Um teste desse card...

**Vinícius:** Então isso aqui deveria ser um card da regra de negócio, Dijas! Onde a gente tivesse lá: atribuição, atribuição alocação, atribuição inscrição, atribuição pontuação... E aí, a partir desse teste no Trello da regra de negócio, ela comenta que deu ruim. E não na sub-issue!

**Outro Desenvolvedor:** Eu tenho um caso aqui: já concluí um item aqui no Épico, certo? Concluído. Fiz os testes aqui. Então, por exemplo, se eu tivesse só o Épico, onde que eu vou colocar ele? Vou colocar ele em concluído ou deixaria aqui?

**Gustavo:** Não, ele faz parte do quê?

**Outro Desenvolvedor:** Faz parte desse Épico aqui.

**Gustavo:** Então, quando esse aí tiver entregue, vai ser testado.

**Vinícius:** É, isso que eu tô falando. Em algum momento ele vai disparar o teste.

**Outro Desenvolvedor:** Mas se isso aqui der pra eu subir pra produção agora e não depender desses daqui?

**Gustavo:** Então ele é um Épico! Ele não faz parte do Épico.

**Vinícius:** Divide o card! Um card listagem e o outro criação. É isso que a gente faz! Listagem é uma coisa, criação é outra.

*(A equipe debate calorosamente sobre o "tamanho do grão", se uma listagem e um formulário de cadastro devem ser Épicos separados ou o mesmo Épico, e como isso impacta a entrega contínua)*

**Gustavo:** Pessoal, ó... vamos lá, vamos lá. Vocês não concordam comigo que o multi-temas ali, ele tá rodando, você tá fazendo, você fez uma funcionalidade ali e já entregou, beleza? Essa funcionalidade aí, quando for uma entrega parcial, ele faz parte do Épico ali, mas ele tá entregue e aí beleza, ele precisa de teste, entendeu? Beleza, ele vai ser testado quando o Épico for concluído! Porque se ele for...

**Participante:** Mas e se ele precisar de um teste de 1000 arquivos alterados pra ele testar tudo de uma vez?

**Gustavo:** Não, mas com certeza granularizar é importante. Só que o problema que nós estamos chegando aqui é exatamente isso: qual o tamanho do grão?

**Dijas:** É, cara, o grão é uma alteração, tá ligado?

**Vinícius:** Ó, vamos dizer um card que eu passei agora: é um CRUD. Create, read, update, delete. É um CRUD, sim? Eu posso chegar aqui e dividir... ou posso fazer um card só e entregar e falar: "Ó, Vini, testa tudo aí". Ou eu posso falar: "Não, vamos dividir, vamos testar separadinho. Ó, eu vou fazer só o criar e editar em um..." A gente até separou: "Não, eu fiz tudo junto porque eu achei que o grão criar e editar fazia parte da mesma coisa". Então eu criei um card. Um card criar e editar e um card listar. Daí dentro da listagem: "Pô, eu mandei lá, quero filtrar por nome". Daí eu não vou criar um outro card: "Filtrar por nome. Ah, agora eu quero filtrar por data", daí eu vou botar outro card "Filtrar por data".

**Gustavo:** Se não foi definido antes...

**Vinícius:** Se não foi definido antes, então vira um grão.

**Dijas:** A definição do Trello é que tem que criar um por um mesmo. O usuário tem que clicar, tem que navegar... O cara não vai analisar, tipo assim: "Porra, essa PI tal..." Não, ele vai clicar: "Quase cliquei no botão classe, tá verde. Pronto, cliquei". É diferente, tá ligado? O lance é que ele vai ver, ele vai considerar que isso aqui é alguma coisa se o card tiver diferente.

**Vinícius:** A feature que eu queria trazer, só pra finalizar essa parte da atribuição, que eu acho que agora ficou um pouquinho mais claro, é o quê: a gente tem atribuição sendo feita. Aí você falou: "Putz, eu tô fazendo atribuição, mano, e dentro dela saiu uma sub-issue que é atribuição alocação". A gente teria que ter o quê? Um Épico de alocação! Porque a partir do momento que você tá trabalhando nesse Épico, vai surgir um monte de sub-issue. E se na premissa você não sabe, tipo, você acredita que a Pâmela vai testar a alocação e ela vai enfrentar a barreira que você colocou na sub-issue, porque ela tá testando a alocação ali... Mas dentro da alocação...

**Gustavo:** Espera aí, espera aí, pessoal. Vamos lá. Ó: no Trello já tem, dá pra fazer. Tem o Épico da atribuição.

**Vinícius:** Grandão, atribuição.

**Gustavo:** Por que que não chama o Épico da alocação?

**Vinícius:** "Atribuição: alocação".

**Dijas:** Mas ele é Épico?

**Gustavo:** Mas é... Não, mas galera, assim: você tá trabalhando num processo de atribuição, que é um processo enorme, correto? E ele não tem diversas etapas? Por que que você vai criar um Épico de atribuição?

**Vinícius:** Então, mas é só pra gente ter um... A gente vai chegar no momento em que a gente vai tá trabalhando na atribuição alocação e você fala: "Putz, Vini, eu tô vendo que a atribuição alocação vai ter que criar um Épico".

**Dijas:** É, por isso é um bom caso, por causa disso mesmo. Atribuição, porra, entrega a atribuição...

**Participante:** Por que que não cria o Épico com o logo dentro da pasta?

**Gustavo:** Não, mano! Vocês tão viajando, cara! Tem que respeitar as coisas como elas estão trabalhando. Não dá pra ficar fácil. Então atribuição é o quê?

**Vinícius:** É "Atribuição: alocação", que é a etapa que você tá trabalhando agora. É o item que você tá trabalhando agora. É que a gente desceu mais uma camada. Então a gente vai trabalhar o quê? Agora você tá na alocação? "Atribuição: alocação", pá! E nisso aí vai ter vinte sub-issues, que é o que você criou. Aí na próxima etapa você vai pegar "Atribuição: pontuação". Dessa pontuação vai ter quinze sub-issues. Em algum momento a Pâmela vai esbarrar na sub-issue que você escreveu, testando isso. E ela vai falar assim...

**Dijas:** Eu entendi, faz sentido essa modificação que você falou. Só quero fazer um apontamento: cara, a gente vai continuar testando coisas depois de milhares de alterações de código que foi pra produção? Assim, eu vou ir botando granularizado, tá ligado? Só que o usuário vai ver lá depois de milhares de alterações.

**Gustavo:** Então, mas aí é onde a gente tem que ganhar maturidade. Um produto, ele tem que ser entregue pro usuário quando ele estiver completo!

**Dijas:** Tá, mas e quem é que vai continuar... eu vou continuar com toda a carga de teste até ser entregue?

**Vinícius:** Não, quando tá no homolog a gente faz o teste! Aí é a hora que o time, eu, a gente faz o teste local da jornada inteira. Atribuição está na alocação, pontuação e documentos? Beleza, você tá entregando etapa por etapa. Assim que você falar: "Finalizei atribuição", a gente vai bombar a atribuição ali e vai testar ela do zero, mano!

**Dijas:** Beleza, faz sentido. A Pâmela vai ver de fato depois de milhares de ciclos de alterações.

**Vinícius:** O produto completo!

**Dijas:** Ela vai testar o produto completo, a feature. Só que eu vou trabalhar de forma granularizada, alterações menores que é na minha parte. Beleza, entreguei uma alteração, testei no meu ambiente, foi OK. Vocês vão ver quando? O Vinícius vai ver quando? Porque o que eu fiz...

**Vinícius:** Vai ser no tamanho da granularização. Quando você subiu uma homologação, você entregou uma etapa e falou assim: "Mano, terminei a etapa".

**Gustavo:** Exatamente.

**Vinícius:** A gente tem que fazer isso. Mas a gente tá conversando agora...

**Gustavo:** Não, mas ó: o ponto é esse. Vocês vão ter que acertar no tamanho do Épico. Vocês sabem que tudo pode ser Épico, mano. Que nem quando a gente tava fazendo a formação, o Gabriel colocou "Universos", mano. O Universo! Você entendeu? Podia ser literalmente tudo. Entendeu? Se pode ser literalmente tudo, sabe quando isso vai concluir? Nunca! Você entendeu?

**Dijas:** E aí tem que pensar também, cara: o Vinícius vai clicar no botão da alocação toda vez que eu subir uma sub-issue lá no Trello? Daí o que que você vai tá fazendo durante o dia?

**Vinícius:** Na verdade você tem que fazer o quê: a alocação gerou dez sub-issues. Vamos propor assim: você tá resolvendo, cinco, seis, sete, oito... Quando der dez sub-issues que você falou "entreguei a alocação", você vai movimentar e falar: "Vini, tô treinando a alocação agora".

**Dijas:** Mas a cada PR é uma sub-issue, não dá pra testar sub-issue!

**Gustavo:** Não, o teste da sub-issue é você que faz! Aí quando você sobe pra homologação...

**Vinícius:** Aí em homologação a gente vai testar a regra de negócio.

**Participante:** E isso melhora o nosso posicionamento ali.

**Vinícius:** O seu homolog lá de demandas suas... outro dia você falou: "Tô com nove demandas em homolog, são sub-issues, mano". Eu não sei testar ali, eu não sei, tá ligado? Se a gente tivesse aquele lá, arruma o botão de notificação... Não, você tem que entregar todas as sub-issues da alocação, aí eu testo a alocação, mano! É isso que eu tô falando. Você tem que entregar por etapas. Dependendo da sua etapa tiver dez, uma, vinte, trinta sub-issues, eu preciso testar a sua etapa. A etapa alocação tem que testar. Entendeu? A partir dali, e não as trinta sub-issues que você colocou lá, mano.

**Gustavo:** Ô Dijas, você imagina... você imagina que isso aqui é uma mecânica, Dijas. Você tá plainando um cabeçote de um carro que fundiu o cabeçote. Você tá colocando lá, mano, você como mecânico tem que testar todas as válvulas, entendeu? Faz parte do seu trabalho, você entendeu? O cliente, que no caso, sei lá, sou eu, deixei o carro lá, eu vou fazer o teste final, que é pegar o carro, sair andando com ele. Aí tá envolvendo as válvulas, o freio, o câmbio, tudo, você entendeu? Esse é o Épico. O Épico é arrumar o carro.

**Dijas:** Mas o Vinícius não é o nosso cliente.

**Gustavo:** Lógico que é! Cliente interno.

**Vinícius:** Tem duas coisas pra gente separar: o que que é PR, tamanho de PR e o que que é tamanho de card para entrega. Quanto menor a PR, melhor. Vinte e duas PRs é melhor do que uma PR de 22 vezes. Concordo contigo. O problema é que o card é diferente, eles não conseguem homologar cada PR. Eles vão homologar cada melhoria que você fez ali, entendeu?

**Dijas:** E se eles não testarem...

**Vinícius:** Mas aí eu acho que... aí que tá. O que eles vão testar, eles vão testar o card. A gente tá falando: quem vai testar é cliente. O cliente não tem que saber se é uma PR, se são oito PRs. Ele tem que saber uma funcionalidade funcionando. E funcionalidade é listar, é criar o processo. Entendeu? Agora: "Ah, eu criei, depois a outra PR foi permissão, a outra PR mudei o ML..."

**Dijas:** Eu tenho um caso aqui: de um item aqui do Épico, certo? Concluído. Fiz os testes aqui. Então, por exemplo, se eu fosse só o Épico, onde que eu vou colocar o Épico? Vou colocar em concluído ou deixaria aqui?

**Vinícius:** Não, ele faz parte do quê? Faz parte desse Épico aqui? Então, quando esse aí tiver entregue, vai ser testado.

**Outro Desenvolvedor:** Mas e se isso aqui der pra eu subir pra produção agora e não depender desse daqui?

**Vinícius:** Então divide o card! Um card listagem e o outro criação. É isso que a gente faz!

**Gustavo:** Pessoal, ó, vamos lá, vamos lá. Vocês não concordam comigo que o multi-temas ali, ele tá rodando, você tá fazendo, você fez uma funcionalidade ali e já entregou, beleza? Essa funcionalidade aí, quando for uma entrega parcial, ele faz parte do Épico ali, mas ele tá entregue e aí beleza, ele precisa de teste. Ele vai ser testado quando o Épico for concluído!

**Participante:** Mas ele acabou de falar que foram 1000 arquivos alterados pra ele testar...

**Gustavo:** Não, com certeza granularizar é importante. Só que o problema que nós estamos chegando aqui é exatamente isso: qual o tamanho do grão?

**Vinícius:** Cara, o grão é uma alteração. É um CRUD: create, read, update, delete. Eu posso chegar aqui e dividir, ou posso fazer um card só e falar: "Ó, Vini, testa tudo aí". Ou eu posso falar: "Não, vamos dividir, vamos testar separadinho".

**Dijas:** A definição do Trello é que tem que ter um fluxo mesmo. O usuário tem que clicar, tem que navegar... O cara não vai analisar na API tal... Não, ele vai clicar: "Quase cliquei no botão, tá verde. Pronto, cliquei".

**Vinícius:** A parte da atribuição que eu acho que agora ficou um pouquinho mais claro: a gente tem atribuição sendo feita. Aí você falou: "Putz, tô fazendo atribuição e dentro dela saiu uma sub-issue de alocação". A gente teria que ter o quê? Um Épico de alocação! Porque a partir do momento que você tá trabalhando nesse Épico, vai surgir um monte de sub-issues. Você acredita que a Pâmela vai testar a alocação e ela vai enfrentar a barreira que você colocou na sub-issue, porque ela tá testando a alocação ali.

**Gustavo:** No Trello dá pra fazer. Tem o Épico da atribuição.

**Vinícius:** Grandão, atribuição.

**Gustavo:** E como chama o Épico da alocação?

**Vinícius:** "Atribuição: alocação".

**Gustavo:** Mas ele é Épico?

**Vinícius:** É! Você tá trabalhando num processo de atribuição, que é um processo enorme, correto? E ele não tem diversas etapas?

**Gustavo:** Por que que você vai criar um Épico de atribuição?

**Vinícius:** Então, mas é só pra gente ter... A gente vai chegar no momento em que a gente vai tá trabalhando na atribuição alocação e você fala: "Putz, Vini, tô vendo que a atribuição alocação vai ter que criar um Épico".

**Dijas:** Mas por isso é um bom caso, por causa disso mesmo. Atribuição, porra, entregar atribuição...

**Gustavo:** Por que que não cria o Épico logo dentro da pasta? Vocês tão viajando, cara! Tem que respeitar as coisas como elas estão trabalhando.

**Vinícius:** "Atribuição: alocação", que é a etapa que você tá trabalhando agora. É o item que você tá trabalhando agora. É que a gente desceu mais uma camada. Então a gente vai trabalhar o quê? Agora você tá na alocação? "Atribuição: alocação", pá! E nisso aí vai ter vinte sub-issues, que é o que você criou. Aí na próxima etapa você vai pegar "Atribuição: pontuação". Dessa pontuação vai ter quinze sub-issues. Em algum momento a Pâmela vai esbarrar na sub-issue que você escreveu testando isso.

**Dijas:** Eu entendi, só quero fazer um apontamento, cara: a gente vai continuar testando coisas depois de milhares de alterações no código? Assim, eu vou ir botando granularizado, tá ligado? Só que o usuário vai ver lá depois de milhares de alterações.

**Gustavo:** Então, mas aí é onde a gente tem que ganhar maturidade. Um produto, ele tem que ser entregue pro usuário quando ele tiver completo!

**Dijas:** Tá, mas e quem é que vai continuar... eu vou continuar com toda a carga de teste até ser entregue?

**Vinícius:** Não, quando tá no homolog a gente faz o teste! Aí é a hora que o time, eu, a gente faz o teste local da jornada inteira. Atribuição está na alocação, pontuação e documentos? Beleza, você tá entregando etapa por etapa. Assim que você falar: "Finalizei atribuição", a gente vai bombar a atribuição ali e vai testar ela do zero, mano!

**Dijas:** Beleza, faz sentido. A Pâmela vai ver de fato depois de milhares de ciclos de alterações.

**Vinícius:** O produto completo!

**Gustavo:** O Épico, né?

**Dijas:** É, a feature. Só que eu vou trabalhar de forma granularizada, alterações menores que é na minha parte. Beleza, entreguei uma alteração, testei no meu ambiente, foi OK. Vocês vão ver quando? O Vinícius vai ver quando? Porque o que eu fiz...

**Vinícius:** Vai ser no tamanho da granularização. Quando você subiu uma homologação, você entregou uma etapa e falou assim: "Mano, terminei a etapa".

**Gustavo:** Exatamente.

**Vinícius:** A gente tem que fazer isso.

**Gustavo:** Não, mas ó: o ponto é esse. Vocês vão ter que acertar no tamanho do Épico. Porque vocês sabem que tudo pode ser Épico, mano. Que nem quando a gente tava fazendo a formação, o Gabriel colocou "Universos", mano. O Universo! Podia ser literalmente tudo, entendeu? Se pode ser literalmente tudo, sabe quando isso vai concluir? Nunca!

**Dijas:** E aí tem que pensar também, cara: o Vinícius vai clicar no botão da alocação toda vez que eu subir uma sub-issue lá no Trello? Daí o que que você vai tá fazendo durante o dia?

**Vinícius:** Na verdade você tem que fazer o quê: a alocação gerou dez sub-issues. Você tá resolvendo, cinco, seis, sete, oito... Quando der dez sub-issues que você falou "entreguei a alocação", você vai movimentar e falar: "Vini, tô treinando a alocação agora".

**Dijas:** Mas a cada PR é uma sub-issue, não dá pra testar sub-issue!

**Gustavo:** Não, o teste da sub-issue é você que faz! Aí quando você sobe pra homologação...

**Vinícius:** Aí em homologação a gente vai testar a regra de negócio.

**Dijas:** No seu homolog lá de demandas suas... você mesmo falou: "Tô com nove demandas em homolog, são sub-issues, mano". Eu não sei testar ali, eu não sei, tá ligado? Se a gente tivesse aquele lá, arruma o botão de notificação... Não, você tem que entregar todas as sub-issues da alocação, aí eu testo a alocação, mano! É isso que eu tô falando. Você tem que entregar por etapas. Dependendo da sua etapa tiver dez, uma, vinte, trinta sub-issues, eu preciso testar a sua etapa. A etapa alocação tem que testar. Entendeu? A partir dali, e não as trinta sub-issues que você colocou lá, mano.

**Gustavo:** Ô Dijas, você imagina que isso aqui é uma mecânica. Você tá plainando um cabeçote de um carro que fundiu o cabeçote. Você tá colocando lá, mano, você como mecânico tem que testar todas as válvulas, entendeu? Faz parte do seu trabalho. O cliente, que no caso, sei lá, sou eu, deixei o carro lá, eu vou fazer o teste final, que é pegar o carro, sair andando com ele. Aí tá envolvendo as válvulas, o freio, o câmbio, tudo. Esse é o Épico. O Épico é arrumar o carro.

**Dijas:** Mas o Vinícius não é o nosso cliente.

**Gustavo:** Lógico que é! Cliente interno.

**Vinícius:** Tem duas coisas pra gente separar: o que que é PR, tamanho de PR e o que que é tamanho de card para entrega. Quanto menor a PR, melhor. Vinte e duas PRs é melhor do que uma PR de 22 vezes. Concordo contigo. O problema é que o card é diferente, eles não conseguem homologar cada PR. Eles vão homologar cada melhoria que você fez ali, entendeu?

**Dijas:** E se eles não testarem...

**Vinícius:** O que eles vão testar, eles vão testar o card. Quem vai testar é cliente. O cliente não tem que saber se é uma PR, se são oito PRs. Ele tem que saber uma funcionalidade funcionando. E funcionalidade é listar, é criar o processo. Entendeu? Agora: "Ah, eu criei, depois a outra PR foi permissão, a outra PR mudei o ML..."

**Participante:** Eu tenho uma dúvida: quando eu crio uma PR pequena, aí eu testo ali. Mas aí no teste funcional não vai ter como testar essa PR de sub-issue.

**Vinícius:** Tudo bem, vai voltar depois pra isso.

**Participante:** Mas aí é retrabalho!

**Vinícius:** Ué, mano, mas eu não consigo barrar uma funcionalidade porque você não testou as pequenas!

**Dijas:** Eu criei um teste que roda todas as PRs, tá ligado? Testei, agora é só você testar essa porra. Você vai botar homolog, beleza? Você não colocou produção. Quando você terminar todas as suas sub-issues, você falou: "Vini, vai pra homolog, testa aí". Aí eu vou testar.

**Gustavo:** O que tá faltando pra gente é um ambiente de staging.

**Vinícius:** É! Que aí não é o homolog que a gente vai testar depois de pronto. O staging é pra testar...

**Dijas:** É o que eu venho esperando: tá bom o suficiente pra ser testado. Sabe o que vai acontecer sempre, Dijas? Eu vou tá testando a sua alocação lá e: "Putz, Dijas, peguei um BO aqui na sua alocação". Aí você fala: "Caralho, é uma sub-issue que eu escrevi". Ele testou a sub-issue sem querer! Você entendeu?

**Dijas:** Cara, se você, tipo assim: pô, tem isso daqui, cara. Isso daqui é de cabeçalho, não sei o quê, não sei o quê. Uma vez que você tá com isso aqui, a sub-issue não existe mais.

**Vinícius:** Mano, eu não preciso ver a sub-issue!

**Gustavo:** Isso!

**Vinícius:** Se hoje tiver que homologar... Mano, mas a gente tem um cenário que o Paulo falou: eu sou o cliente interno de vocês, mano! O que vocês fazem aqui em qualquer parte do processo, eu testo, mano! Tem coisa que eu não consigo mesmo, mas processos cadastrais, mano, eu testo de ponta a ponta isso aí, mano, e volto a demanda.

**Gustavo:** E olha que é uma bosta aquele processo, hein?

**Vinícius:** É, e o problema talvez seja dividir o Épico em entregáveis. O Épico do tipo de tudo lá: o Épico é o grande, o definitivo. Isso aqui não vamos esperar ficar pronto o mundo inteiro, o Épico inteiro. Mas, mano, essa treta que a gente tá tendo agora é porque tá criando sub-issue a partir da IA, porque não tinha isso, mano! Você tá criando uma briga que não tinha essa briga!

**Dijas:** Claro, só que isso não existia antes. Como que ela funcionava? Você tá se apegando com a realidade ou você ficava esperando entregar um bagulho de sexta-feira, ia pra casa, sumia, voltava depois de um mês com o bagulho bugado?

**Vinícius:** Não, não tem nada a ver o que você falou. Vamos voltar no começo do ano como que era feito? No começo do ano tinha essa sub-issue que vocês estavam gerando? Como que a gente testava a sub-issue no começo do ano sem essa tecnologia que a gente tá agora? Não tinha sub-issue, era uma demanda que a gente entregava no final.

**Dijas:** Exatamente, o método não mudou, acelerou!

**Vinícius:** Não, você não tinha essa sub-issue.

**Dijas:** Então eu continuava desenvolvendo o Épico na sombra ali, tá ligado? Na fé. Você ia confiando em mim que eu tava desenvolvendo as sub-issues.

**Gustavo:** Eu acho que o caminho que a gente tá discutindo é o melhor caminho possível.

**Vinícius:** Mano, quando toda mudança que entra na plataforma o cliente chia, você vai deixar essa mudança na cara do usuário? Não! Cria um controle de issue e PR. A issue pra mim é o pedaço do produto. Ali é o que o usuário ia fazer. De repente tá falando assim: "Ó, mas aqui tem um problema de permissão aqui que tá muito aberto e todo mundo pode ver essa tela". Mano, não é o que o usuário vai fazer. Eu vou ter que criar uma sub-issue do que eu tô fazendo? Cria outro card e depois resolve!

*(Discussões paralelas sobre Docker, containers travando, permissões e branches de desenvolvimento)*

**Gustavo:** Atenção, pessoal! Atenção, atenção. O que que nós vamos fazer agora pra gente fazer em conjunto? Eu vou criar uma skill e vocês, como desenvolvedores, vão usar essa skill. Essa skill, ela vai estar trazendo todo o contexto de conhecimento que eu venho utilizando pra poder fazer os motores de regras, tudo o que eu venho aprendendo até agora. Eu não sei qual vai ser o resultado disso, mas eu vou pedir pra vocês pra que vocês testem, pra gente testar junto, a gente vai ver como se comporta pra ver se é isso mesmo, tá? Mas o objetivo que a gente quer alcançar aqui, qual é? É pegar um card Épico, bateu lá um card que é grande, a skill vai identificar... vai bater lá no card, vai analisar a tarefa, vai aproveitar pra... é importante que esteja com a base do código instalada na máquina pro Claude poder olhar, e ele vai startar o processo com o agente, vai olhar, vai ajudar a entender se é uma tarefa complexa ou não. Sendo uma tarefa complexa, que vai um pouco além daquele objetivo, ele vai criar subtasks. Entendeu? Essas subtasks, elas vão ser criadas agora no Trello mesmo, pra gente entender se esse formato vai funcionar, se eu não tô viajando, se eu não entendi tudo errado, você entendeu? Por isso que eu vou pedir a ajuda de vocês. Isso aqui funcionando, porque assim, eu tenho uma grande esperança de que vai funcionar legal, porque o Dijas, aqueles dezesseis cards que ele criou lá: AL tal, AL isso, AL aquilo... O que que aconteceu? Ele criou a essência da criação dos cards, tá corretíssima!

**Dijas:** É, eu fiz exatamente o que você... Você foi falando o plano, eu peguei e fiz.

**Gustavo:** É! Quando eu vi seus cards, eu entendi tudo. Só que o que acontece: o AL, o que que aquele AL significa?

**Dijas:** Alocação. E ele é filho de atribuição.

**Gustavo:** Então, você tá vendo? A gente precisa padronizar essas escritas, essas informações. A minha intenção é isso: é a gente fazer uma coisa padronizada, que fique inteligível pra todos, entendeu? Que a gente siga essa mesma metodologia. Se der certo isso que a gente vai rodar aí nas próximas semanas, na próxima semana e na outra talvez, a gente faz o quê? Monta o ambiente no GitHub e começa a fazer lá, entendeu? Aí vamos dar a skill pra fazer o quê? Em vez de criar esses cards no Trello, cria esses cards no GitHub!

**Vinícius:** É, adiciona issue, né?

**Gustavo:** E linka tudo lá! Você entendeu?

**Vinícius:** Ô Gu, só pra complementar essa parte: essas demandas, essas sub-issues que estão sendo criadas no Trello atualmente, não joga ela em homolog.

**Participante:** Eu tava falando pro Dijas aqui exatamente sobre isso: que tipo, no Trello não dá pra você criar sub-cards de outros cards, né? Fica um monte de card jogado. Por isso que o GitHub eu acho que seria melhor pra gente já iniciar, tá ligado? Porque você consegue criar uma issue e as outras vão virando sub daquela.

**Gustavo:** É, então vamos fazer o seguinte: eu vou criar a skill, a gente faz um teste controlado com algumas pessoas aqui enquanto a gente prepara o ambiente. Vocês me ajudam a preparar esse ambiente.

**Dijas:** Dá pra fazer hoje!

**Vinícius:** Deixar a regra de negócio no Trello e essas sub-issues no Git, mano.

**Gustavo:** O Trello, ele vai andar só com o card Épico.

**Vinícius:** Eu pensei em deixar no Trello, tipo assim, só realmente o passo a passo do que precisa ser validado em relação ao Épico.

**Gustavo:** É, exatamente.

**Vinícius:** No produto Trello, e sub-issues, coisas que vocês mudaram, refatoraram, código legado, deixa no Git, mano!

**Dijas:** Eu tenho um robô de notificação pro... que é justamente a regressão.

*(Murilo compartilha a tela mostrando sua esteira no Claude e no GitHub)*

**Gustavo:** Olha aí, o Murilo, ele criou um esquema aqui... Tá vendo o seu Alagoas lá que você criou um monte de cards? O Murilo já pôs etapa, tá vendo, ó? Muito da hora, mano! Entendeu, ó? Mostra aí um card aí, Murilo. Ó, esse aqui é o Épico: multi-temas, ó. Aí já tem o checklist, já são os vinte e poucos aqui, tá vendo?

**Murilo:** Aí eu vou trabalhando aqui, né? Pá!

**Gustavo:** Por que que tá tendo essa facilidade do Murilo? Porque aqui a gente não tá falando de regra de negócio, o Murilo tá sozinho no board. É igual o Paulo também.

**Vinícius:** Então, mas ó: o que que a gente já pode ir fazendo, mano, a partir da conversa ali: deixar essas sub-issues todas no Git, configurar esse ambiente ali e deixar o Trello só a regra de negócio.

**Gustavo:** É, aí ficaria o multi-temas aqui em desenvolvimento, entendeu? Essas sub-issues não existiriam aqui, existiriam lá no GitHub. E no Épico aqui no Trello vai ser o quê? Descrevendo o que que é que o Murilo tá fazendo pra gente conseguir testar depois.

**Vinícius:** É, tá ligado? Alto nível. Vai conversar lá: "Ó, quero um relatório de alunos".

**Dijas:** De dezesseis cards, estão em homologação coisa de oito cards, tá ligado? Esses oito cards são coisas simples mesmo assim: a responsiva na média lá... Você já entrou e clicou no botão de homologação da atribuição?

**Vinícius:** Não. Mas você não acha que isso aí a gente teria que ter um Épico escrito "Atribuição: alocação"?

**Participante:** Mas não seria melhor ter isso granularizado pra você só testar aquilo?

**Vinícius:** É, exatamente. E aí essas sub-issues não vão pra homologação.

*(O grupo retoma o debate sobre branches, deploys simultâneos em containers e como testar o frontend quando o backend ainda está sendo alterado)*

**Participante:** Acho que uma questão que a gente tá pecando, que eu acho que tá usando ferramenta errada: pra desenvolvimento, o Trello é a ferramenta que a gente tem pra acompanhar isso? Não é a mais adequada. Ela é só pra produto, talvez.

**Gustavo:** Não, não é. O Trello dá pra usar, entendeu? Dá pra usar. É assim: depende de alguns objetivos. Por exemplo, o Trello é uma ferramenta ótima pra gente poder pegar e tratar features a serem desenvolvidas. Só que o que acontece: o que eu sinto é que o Trello, ele tá resolvendo um pouco pra galera que tá na ponta e pouco pra galera que tá aqui. Entendeu? E a gente tava tentando fazer o quê? Agradar os dois lados. E não vai conseguir! Fazendo isso vai poluir muito. Eu ia fazer o teste com uma skill de criar no Trello os sub-cards, porque os sub-cards eu vejo que é uma coisa comum entre os devs, que é uma coisa que ajuda os devs. Mas não necessariamente que o Trello ia cuidar disso. Em algum momento a gente ia levar pro GitHub Projects, entendeu?

**Gustavo:** Quando o Trello tava focado só na regra de negócio, era muito mais claro pro pessoal lá na ponta isso, entendeu? Agora, com esse monte de sub-issues, isso com certeza vai embaçar a visão.

**Dijas:** No Trello você tem que se acostumar a clicar no botão, tá ligado? Eu acho que esse espaço também... Cara, não tem como eu passar um mês sem atualizar nada e atualizar tudo de uma vez. Mas tipo assim, com a IA torando o tempo... Dava pra fazer isso, mas você vê que o time não pega, tá ligado?

**Gustavo:** A gente vai ter que separar as coisas. A gente vai ter que parar de ficar nessa de que tudo é responsabilidade de todo mundo. A nossa esteira de desenvolvimento hoje é tudo responsabilidade de todo mundo, num certo nível. Tem os testes que são internos! A gente vai ter que começar a separar isso.

**Dijas:** Esses testes são os testes mais importantes pro bagulho funcionar. É igual eu disse: por que que eu tô defendendo um card que tenha esse teste pra Pâmela? Porque o que que ela vai fazer? Ela vai entrar, vai logar, vai abrir a atribuição, vai abrir a alocação. Chegou ali, cara, fechou, tá provado! Sacou? É esse lance. Você não vai lá no mecânico estourar o cinto de segurança. Você vai abrir a porta, entrar, ligar. Ligou, acelera duas vezes...

**Gustavo:** Beleza, mas não acontece de você falar assim: "Beleza, testou aí? Então agora volta pra sua casa que sexta-feira eu te entrego o carro"? Não é assim, entendeu?

**Vinícius:** O smoke test a gente vai fazer pra dentro, mano. Não volta mais essa parada pra Pâmela!

**Dijas:** Não, mas se tiver na regra principal do card aqui no Trello, mano, é isso que eu tô falando!

**Vinícius:** Em algum momento a Pâmela vai esbarrar na sua sub-issue e vai falar assim: "Hum, travei". E aí ela vai testar e no Épico ela vai falar: "Dijas, parei na etapa de alocação aqui e travei. Apareceu esse erro pra mim aqui".

**Dijas:** Apareceu um erro. Então isso não vai pra produção, pelo amor de Deus!

**Vinícius:** Mas ninguém tá falando de ir pra produção a sua sub-issue! O que eu tô falando é que essa sub-issue tá indo pra homologação. Então hoje eu tenho 23 demandas em homologação, só que muitas delas são sub-issues que não tem como testar.

**Gustavo:** O produto tem que ser entregue pro usuário quando ele tiver completo!

**Dijas:** Tá, mas eu vou continuar com toda a carga de teste até ser entregue?

**Vinícius:** Não! Quando tá no homolog a gente faz o teste, a jornada inteira. Assim que você falar "finalizei atribuição", a gente vai bombar a atribuição ali e vai testar ela do zero.

**Dijas:** Beleza, faz sentido. A Pâmela vai ver de fato depois de milhares de ciclos de alterações o produto completo.

**Vinícius:** O produto completo!

**Gustavo:** Isso, exato.

**Dijas:** E aí o Vinícius vai ver quando? Porque o que eu fiz...

**Vinícius:** Vai ser no tamanho da granularização. Quando você subiu uma homologação, você entregou uma etapa e falou assim: "Mano, terminei a etapa". A gente tem que fazer isso.

**Gustavo:** Vocês vão ter que acertar no tamanho do Épico. Porque tudo pode ser Épico. Se for aberto demais, nunca vai concluir.

**Vinícius:** A alocação gerou dez sub-issues. Você tá resolvendo... Quando der dez sub-issues que você falou "entreguei a alocação", você vai movimentar e falar: "Vini, tô entregando a alocação agora".

**Dijas:** É que a cada PR é uma sub-issue, não dá pra testar sub-issue.

**Gustavo:** O teste da sub-issue é o dev que faz. Aí quando sobe pra homologação, testa a regra de negócio.

**Vinícius:** E só pra te falar uma coisa, Dijas: no seu homolog lá, você mesmo falou: "Tô com nove demandas em homolog, são sub-issues". Eu não sei testar ali! Você tem que entregar todas as sub-issues da alocação, aí eu testo a alocação, mano! É isso que eu tô falando. Você tem que entregar por etapas.

**Gustavo:** O cliente vai fazer o teste final, que é pegar o carro e sair andando com ele. Envolve válvulas, freio, câmbio, tudo. Esse é o Épico: arrumar o carro.

**Vinícius:** Tem duas coisas pra gente separar: tamanho de PR e tamanho de card para entrega. Quanto menor a PR, melhor. O problema é que o card é diferente, eles não conseguem homologar cada PR. Eles vão homologar a funcionalidade pronta.

**Gustavo:** A discussão levou a gente pro ponto de que o cliente olhando o sistema quer ver o que ele pediu entregue.

**Vinícius:** Essa treta que a gente tá tendo agora é porque tá criando sub-issue a partir da IA, porque não tinha isso antes.

**Dijas:** Claro, só que isso não existia antes. Antes a gente entregava tudo no final do mês, e se viesse quebrado, vinha quebrado tudo junto.

**Gustavo:** A gente tem que evoluir da planilha de 300 linhas que a gente usava no passado para um fluxo moderno, sem perder a organização.

**Vinícius:** E no Trello, como que vai testar as PRs? Vai chegar PR pra eu aprovar, como que eu vou saber se posso aprovar ou não sem saber como testar?

**Gustavo:** A gente pode fazer o seguinte: smoke test pra todo mundo, cara.

**Dijas:** O Paulo montou um smoke test pro Zeus. Precisava ver se se aplica. Porque se tudo funcionar como a gente tá planejando, vai gerar cada vez mais código e vai ficar humanamente impossível pro Felício revisar e pra Pâmela conferir tudo na mão.

**Vinícius:** Então esse processo tem que ser automatizado também.

**Gustavo:** Semana que vem, no começo da semana, na terça ou quarta-feira no máximo, vamos fazer a nossa reunião de novo pra gente falar sobre o Harness agora. Falar sobre orquestrador, falar sobre essas coisas, mano. Eu tenho um sonho aqui que é o seguinte: alguém pega a subtask, a partir dessa subtask joga no Claude e a partir dali já começa todo o código.

**Dijas:** Eu já tô fazendo isso meio que na encolha. Pra mim no que eu tô fazendo, se der bosta quem corrige sou eu, tá ligado?

**Gustavo:** Mas vamos falar sobre esse mundo hipotético na próxima reunião.

**Vinícius:** Eu consegui agora no meu ambiente subir duas, três branches simultâneas. Eu consigo rodar três sessões diferentes no Claude e trabalhar em branches separadas.

**Dijas:** Pô, você pode botar quatro, seis tasks ao mesmo tempo, tá ligado?

**Vinícius:** Mas dá pra gente usar no back-end e no front-end separado.

*(A equipe finaliza a discussão fazendo piadas sobre o cansaço do dia, combinando de tomar café e fumar um cigarro antes de voltar para o código)*

**Gustavo:** Vou deixar vocês discutirem mais um pouco, vou fumar um cigarro e vou voltar. Fechou?

**Equipe:** Fechou, bora!
