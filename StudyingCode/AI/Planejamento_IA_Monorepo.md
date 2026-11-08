# Planejamento e Estratégias para Gestão de Monorepos Legados com IA

Estratégias Avançadas para Gestão de Monorepos Legados

Contexto e Desafios Técniocos

• Estratégias para Gestão de Monorepos Legados em Grande Escala

• Abordagem Técnica e Operacional

• Rag

• Mcp

• Fine tunning

• Lidar com um monorepo legado nessa escala (milhões de arquivos no total, ~100k por projeto, misturando Angular, Laravel, PHP puro e JS puro) impõe desafios severos de limite de contexto, ruído de busca, consumo de tokens e risco de regressão.

• Como você já possui um harness inicial e skills de boas práticas mapeadas, o foco agora é otimizar a arquitetura de contexto, isolamento de escopo e automação de validação.

• Abaixo está a estratégia recomendada dividida em Estratégia de Operação no Dia a Dia e Próximos Passos de Evolução:

• ───

Práticas Operacionais e Escalonamento

• Estratégia de Operação no Dia a Dia

• A. Escopo Local vs. Raiz (Workspace Scoping)

• Nunca abra a CLI na raiz de milhões de arquivos para tarefas pontuais:

• Se a tarefa for alterar um componente Angular, abra o terminal e a sessão diretamente dentro de /apps/frontend-angular.

Otimização de Escopo e Filtragem

• Se for alterar uma API Laravel, abra dentro de /apps/api-laravel.

• Exceção (tarefas cross-app): Quando precisar criar/alterar um contrato entre API e Front, defina explicitamente no início do prompt apenas os 2 subdiretórios envolvidos.

• Ignorar agressivamente o ruído: Configure o .ignore / .claudeignore / .gitignore em cada subprojeto e na raiz para excluir pastas pesadas que o agente não deve indexar ou ler: vendor/, node_modules/, storage/framework/, storage/logs/, dist/, .angular/cache/, dumps de banco e builds legados.

Estrutura e Documentação

• Organização Modular de Documentação Técnica

• B. Hierarquia de Instruções (Modular Context Layering)

• Evite concentrar todas as regras em um único arquivo de instrução no topo: Raiz (/CLAUDE.md ou /GEMINI.md): Deve conter apenas o mapa geral do repositório (quais apps existem, portas locais, convenções de commits e comandos de orquestração).

Configurações Técnicas e Padronização

• Subdiretórios de Projetos (/apps/portal-angular/CLAUDE.md, /apps/api-laravel/CLAUDE.md): Versão exata da linguagem/framework (ex: PHP 8.1 vs PHP 7.4; Angular 14 vs 17).

• Como rodar lint e testes desse projeto

• Configuração Técnica e Fluxo de Trabalho do Agente

• específico (php artisan test --filter=..., npm run lint).

• Padrões de arquitetura daquele app (ex: "Aqui usamos Actions em vez de Services", "Não use signals, use RxJS BehaviorSubjects legados").

Diretrizes de Execução e Segurança de Código

• C. Fluxo de Execução: Pesquisa Cirúrgica → Plano → Mudança

• Diretrizes para Execução Segura e Pesquisa de Código

• Proibir buscas cegas recursivas: Instrua o agente a buscar por símbolos/rotas ou usar ferramentas de busca rápida (como ripgrep) restritas ao subdiretório de interesse.

• Exigir Plano de Análise de Impacto (Blast Radius): Em código legado com PHP e JS puro, funções globais e acoplamento oculto são comuns.

• O agente deve listar onde uma função/classe é referenciada antes de alterá-la.

Estruturação de Mapeamento Técnico

• Implementação de Documentação e Mapas de Código

• Próximos Passos para Elevar a Estratégia de IA

• Passo 1: Construir Mapas de Arquitetura e Contratos ("Codebase Maps")

• Crie e mantenha pequenos arquivos de metadados em Markdown nos projetos-chave:

• API Endpoints Map: Um índice conciso das rotas e controladores do Laravel/PHP puro.

• Data Model Map: Resumo das tabelas principais e modelos Eloquent.

Otimização de Fluxos e Especialização em Sistemas Legados

• Otimização de Arquitetura e Fluxos Automatizados

• Dependency Matrix: Mapeamento de quais apps front-end dependem de quais back-ends.

• > Benefício: O modelo lê esses resumos em ~2.000 tokens e localiza o arquivo exato sem precisar rodar grep em 100.000 arquivos.

• Passo 2: Criar Skills Especializadas para Legado

• Adicione skills customizadas voltadas para os problemas reais do legado:

• Skill legacy-blast-radius: Analisa referências cruzadas de funções/arquivos PHP procedurais e variáveis globais JS antes de propor refatoração.

Habilidades Especializadas do Agente

• Skill strangler-pattern-refactor: Orienta o agente a nunca reescrever do zero, mas a encapsular código legado procedural com classes/interfaces modernas e testes antes de refatorar.

• Skill contract-validator: Dada uma alteração em uma rota Laravel, verifica se os services TypeScript/Angular que a consomem sofreram quebra de tipagem.

Estabelecendo Ciclos de Feedback e Verificação

• Passo 3: Fechar o Ciclo de Validação Automática (Linters e Testes Rápidos)

• O maior ganho de maturidade em desenvolvimento assistido por IA é fechar o ciclo de feedback autônomo:

• Validação de Código e Práticas de Teste

• Verificação Estática: Garanta que o agente saiba rodar checagens rápidas pós-edição: Laravel: php -l {arquivo} (sintaxe imediata) e vendor/bin/phpstan analyse {arquivo}.

• Angular/TS: npx tsc --noEmit ou npx eslint {arquivo}.

• TDD / Reprodução Empírica: Instrua o agente a criar primeiro um teste unitário ou script de reprodução que falhe antes de corrigir um bug no código legado, validando a correção em seguida.

Delegação de Funções e Fluxo de Trabalho

• Passo 4: Implementar Sub-agentes / Separação de Papéis

• Separe o fluxo mental do agente:

• Investigador/Arquiteto: Lê os mapas, localiza o problema e desenha a estratégia (read-only).

• Implementador: Focado exclusivamente em aplicar a alteração cirúrgica no arquivo alvo.

• Revisor: Valida se a mudança não introduziu código moderno incompatível com a versão de produção (ex: usar sintaxe do PHP 8.2 em um PHP 7.4).

Boas Práticas de Organização e Validação

• Resumo do Próximo Movimento Recomendado

• Audite os arquivos de ignore para blindar o agente contra diretórios mortos/temporários.

• Organização Estrutural

• Mova as regras do harness para arquivos locais em cada subprojeto, mantendo a raiz enxuta.

• Eficiência em Testes e Validação

• Documente os comandos de teste e lint cirúrgicos (por arquivo) no harness de cada subprojeto para que o agente valide suas próprias alterações sem rodar suítes pesadas de milhões de linhas.

• ✦ Direto ao ponto: A estratégia primordial é o MCP

Prioridades e Estratégias de Desenvolvimento

• combinado com um RAG voltado para código.

• O Fine-tuning é a menor das suas prioridades (e provavelmente um desperdício de recursos neste momento).

• E respondendo à sua última pergunta logo de início: Não, você não precisa fazer tudo isso agora.

• Tentar implementar RAG próprio do zero e Fine-tuning ao mesmo tempo é uma armadilha de sobre-engenharia.

• Abaixo está o detalhamento prático de cada estratégia, como executá-las e o que realmente compensa fazer hoje.

Análise Comparativa e Implementação

• ───

• Comparativo: Qual é primordial para 1 milhão de arquivos?

• ┌─────────┬───────────┬────────────┬──────────┐

• │ Estraté │ Papel no │ Prioridade │ Recomend │

• │ gia │ seu │ │ ação │

• │ │ Monorepo │ │ │

• │ │ Legado │ │ │

• ├─────────┼───────────┼────────────┼──────────┤

• │ MCP │ Dá "mãos │ 1º │ Continue │

• │ │ e olhos │ (Imediato) │ usando e │

• │ │ em tempo │ │ refinand │

• │ │ real" ao │ │ o. O MCP │

• │ │ agente │ │ é o │

• │ │ (ler AST, │ │ canal de │

• │ │ rodar │ │ ação. │

• │ │ linters, │ │ │

• │ │ consultar │ │ │

• │ │ banco, │ │ │

Análise de Ferramentas de IA

• RAG de Código | Dá "memória de navegação em escala" sem estourar a janela de contexto.

• 2º (Curto prazo) | Essencial quando o grep tradicional ficar lento ou você precisar achar fluxos conceituais.

• Fine-Tuning | Ajusta "estilo e sintaxe" nos pesos do modelo.

• 3º (Desnecessário) | Não faça agora. Não resolve o problema de localizar arquivos em 1 milhão de itens e gera alucinações.

Limitações e Casos de Uso do Fine-Tuning

• Por que Fine-Tuning NÃO é recomendado agora?

• O que o Fine-tuning faz bem: Ensinar um formato específico de saída (ex: um JSON muito customizado) ou um framework proprietário interno que não existe na internet.

Limitações do Fine-Tuning em Código

• O que ele NÃO faz: Ele não funciona como banco de dados.

• Você não faz fine-tuning para o modelo "decorar" o código de 1 milhão de arquivos.

• O modelo vai alucinar nomes de variáveis, misturar versões e inventar arquivos que não existem.

• Problema de obsolescência: Assim que alguém commitar alterações no PHP ou no Angular, seus pesos treinados ficam desatualizados.

• Conclusão: Modelos de ponta atuais já conhecem profundamente PHP, Laravel, Angular e TypeScript.

• O seu problema não é de inteligência do modelo, é de recuperação do arquivo certo.

Implementação Estruturada de RAG

• Como fazer um RAG Preciso para Código (Code RAG)

• Fazer RAG de texto comum (cortar o código a cada 500 caracteres e gerar vetores) falha miseravelmente em código legado, pois corta funções no meio e perde declarações de classes e imports.

• Para código em larga escala, o RAG precisa ser estruturado e híbrido:

• Passo A: Chunking Sintático com AST (Tree-sitter)

• Em vez de quebrar por quantidade de linhas:

• Use parsers de sintaxe (como a biblioteca

Processamento e Estruturação de Dados

• Tree-sitter, disponível para PHP, JS e TypeScript).

• Cada chunk deve ser uma unidade lógica completa: uma classe inteira, um método, uma função isolada ou uma definição de rota.

• Guarde metadados em cada chunk: caminho do arquivo, namespace, docblock/comentários e lista de dependências (use, import).

Otimização da Busca Híbrida

• Passo B: Busca Híbrida (BM25 Lexical + Vetores Semânticos)

• Busca Lexical (BM25 / Ripgrep): Essencial para código.

• Quando o agente procura pelo método exato calcularDescontoLegado(), a busca por palavras-chave exatas é imbatível.

• Busca Vetorial (Embeddings de Código): Útil para intenções conceituais (ex: "onde fica a regra de autenticação do token antigo?").

• Use modelos de embedding otimizados para código (ex: text-embedding-3-small da OpenAI ou modelos abertos como jina-embeddings-code).

• Reranking: Um modelo leve de rerank (ex: Cohere Rerank ou BGE-Reranker) pega os 20 melhores resultados e seleciona apenas os 3 mais relevantes para o prompt do agente.

Configuração da Infraestrutura MCP

• Passo C: Expor o RAG via Servidor MCP

• A forma mais limpa de integrar esse RAG ao Claude Code ou Gemini CLI:

• Crie um servidor MCP local simples (em Node.js ou Python).

Implementação de Ferramentas e Funcionalidades

• Defina tools no MCP, como: search_codebase(query, app_scope): Busca vetorial/híbrida no índice.

• find_symbol_definition(symbol_name): Encontra onde uma classe/função foi declarada.

• f

ind_callers(function_name): Identifica quem
chama aquela função no legado.
1. O agente chama essa ferramenta autonomamente
apenas quando não souber onde um arquivo está.

───

4. O que é necessário para AGORA? (Roteiro em 3
Passos)

Fase 1: O "RAG dos Pobres" com MCP (Sem
infraestrutura nova)
Antes de construir bancos vetoriais (Qdrant,
Pinecone, Chroma):
1. MCP de Busca Rápida: Garanta que seu ambiente
tenha MCPs que usem ripgrep (rg) e fd. O ripgrep
busca em 100k arquivos em frações de segundo.
2. MCP com Ctags / Universal-Ctags: Gere um arquivo
de índice de símbolos (tags) nos projetos PHP e
JS. Um MCP simples que lê esse arquivo acha
qualquer função ou classe instantaneamente sem
custo de tokens.

Fase 2: RAG Automatizado (Ferramentas Prontas)
Se a busca por texto não bastar para entender fluxos
complexos:
• Em vez de programar um pipeline de RAG do zero,
avalie ferramentas que já fazem indexação de
grafos de código (ex: plugins/MCPs do Greptile,
Sourcegraph/Cody, ou Aider com repo-map via
ctags).

Fase 3: Fine-Tuning
• Descarte. Foque o tempo e orçamento em melhorar
os testes unitários do código legado, o harness
de validação e a qualidade dos seus servidores
MCP.



Não usa o Claude Code sem esses 5 plugins aqui...
1. Carthographer (Mapa de projeto para economizar tokens)
2. Claude Code Setup (Recomenda plugins e limpa contexto)
3. Cloud Man (Sistema de memória entre sessões)
4. Head Room (Compressão de contexto)
5. Omni Router (Fallback de provedores de IA)