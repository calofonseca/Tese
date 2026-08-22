# Relatório de revisão da voz autoral — Tese de Doutoramento v11

## Objetivo

Esta revisão transformou o texto de um *working draft* muito bem estruturado, mas ainda marcado pelo diálogo de planeamento com uma IA, numa versão de leitura com voz autoral consistente. A estrutura científica, a terminologia e as cautelas justificadas foram preservadas. Foram removidos o metadiscurso editorial, as justificações repetidas da organização, a antecipação constante de objeções e as instruções dirigidas a um futuro redator.

A revisão não inventa resultados. Quando faltam números, versões, autoria, figuras ou evidência operacional, essa lacuna permanece no projeto anotado e não é mascarada no texto limpo.

## Dois modos de leitura

### `main.tex` — versão limpa de leitura

- prosa em estilo final de tese;
- sem caixas `Draft note`;
- sem `[TBD]` visíveis;
- sem tabelas de resultados ainda vazias;
- sem instruções de produção das figuras;
- placeholders visuais neutros, mantendo apenas a legenda e a posição prevista;
- 220 páginas A4.

### `main-annotated.tex` — versão de trabalho e auditoria

- mantém as notas de evidência;
- mostra os campos `[TBD]`;
- mantém os *result ledgers* ainda por preencher;
- mostra as fontes necessárias e a função de cada figura;
- preserva a lista de verificações de implementação, autoria e deployment;
- 222 páginas A4.

## Principais alterações de escrita

### 1. O objeto científico passou a abrir os parágrafos

Parágrafos que começavam por `This chapter`, `The purpose`, `The thesis`, ou por uma explicação editorial da estrutura foram reescritos para começar pelo sistema, método, problema, resultado ou evidência.

Exemplo de movimento:

```text
Antes:
This chapter deliberately begins with the architecture rather than with a mathematical formulation.

Depois:
EnergAIze provides the common architecture within which the controller families,
experimental services, and operational lifecycle are integrated.
```

### 2. As contribuições são apresentadas afirmativamente

Construções do tipo `The contribution is not X; it is Y` foram substituídas por uma declaração direta de Y. A fronteira da claim continua presente, mas aparece no parágrafo de scope ou limitações, depois de a contribuição estar clara.

### 3. As discussões de planeamento foram retiradas da tese

Frases que comparavam narrativas alternativas — por exemplo, explicar que os métodos anteriores não eram fracassos ou justificar por que o Chapter 3 começa pela arquitetura — foram condensadas em afirmações científicas diretas. A história cumulativa permanece, mas já não é apresentada como resposta a uma dúvida editorial.

### 4. As instruções ao futuro redator foram separadas da prosa

Expressões como:

- `the final result should report...`;
- `the final chapter must state...`;
- `this table is to be populated...`;
- `final values require audit...`;

foram movidas para a versão anotada ou convertidas em descrições científicas no presente. O apêndice de reprodutibilidade passou de uma lista de instruções para uma descrição autoral dos requisitos e artefactos de reprodução.

### 5. O ritmo ficou menos previsível

Foram reduzidas enumerações simétricas, construções defensivas repetidas e cadeias de `first/second/third` quando uma relação causal era mais natural. Mantiveram-se listas onde são adequadas: definições, protocolos, taxonomias, métricas e estados do lifecycle.

### 6. Exemplos e termos estáveis foram preservados

A revisão manteve o estilo pretendido pelo autor:

- explicação intuitiva antes da formalização;
- exemplos recorrentes de EVs, baterias, edifícios e comunidades;
- inglês formal sem complexidade desnecessária;
- uso consistente de `agent`, `asset`, `controller`, `policy`, `policy set`, `Scalability`, `Deployability`, `Safety` e `Robustness`;
- linha narrativa contínua entre capítulos.

## Auditoria heurística da voz

Contagens aproximadas no texto extraído do PDF:

| Padrão | v10 | v11 limpa |
|---|---:|---:|
| `This chapter` | 26 | 1 |
| `The purpose` | 10 | 0 |
| `This distinction` | 13 | 2 |
| `The contribution is not` | 6 | 0 |
| `Draft note.` | 19 | 0 |
| `[TBD]` | 148 | 0 |
| `Working mapping` | 2 | 0 |
| `to be populated` | 4 | 0 |
| `Provisional findings` | 2 | 0 |
| `rather than` | 105 | 82 |
| `does not` | 99 | 80 |

As duas ocorrências restantes de `This distinction` e a ocorrência de `This chapter` são usos naturais dentro de argumentos concretos, não sinalização editorial repetida.

## Alterações específicas por parte da tese

### Front matter

- declaração de coautoria convertida para voz no presente;
- tabela de outputs com coluna `Status`, em vez de `Working status`;
- separação entre publicações concluídas e manuscritos ou contribuições em preparação;
- versão limpa sem instruções de auditoria visíveis.

### Chapter 1

- matriz RQ–evidência deixou de ser designada `working`;
- estrutura das contribuições apresentada diretamente;
- artefactos descritos como parte da investigação, não como uma lista futura.

### Chapter 4

- tabela de performance apresentada como medição de engenharia no estado auditado;
- observação manual de memória explicitamente excluída das claims comparativas;
- instruções para futura repetição removidas da prosa limpa.

### Chapters 5–7

- tabelas ainda vazias de comparação e ablação mantidas apenas no PDF anotado;
- texto limpo preserva o argumento e os protocolos sem mostrar células sem evidência;
- secção `Claim Discipline` do TI-MARL passou a `Results, Scope, and Contribution to the Research Questions`;
- findings provisórios do lifecycle passaram para a camada anotada;
- contribuição de lifecycle expressa afirmativamente como extensão semântica de MLOps/RLOps para policy sets coordenados.

### Chapter 8

- percentagens de estudos distintos são interpretadas segundo o respetivo nível de evidência, sem instruções dirigidas ao redator;
- o ledger de auditoria operacional permanece apenas na versão anotada;
- a contribuição da validação real é formulada positivamente como evidência integrada sobre interfaces, dados, recursos, fallback e lifecycle.

### Appendix A

- passou de “o apêndice final deverá incluir...” para uma descrição científica dos elementos necessários à reprodução;
- claims, manifests, configurações, estatística, resultados negativos, lifecycle e arquivo são apresentados como partes do registo de reprodutibilidade.

## Validação técnica

- versão limpa: 220 páginas A4;
- versão anotada: 222 páginas A4;
- compilação com pdfLaTeX e Biber;
- 96 chaves bibliográficas utilizadas;
- nenhuma citação ou referência interna indefinida;
- nenhum erro LaTeX;
- nenhum aviso `Overfull` no log final;
- PDFs não encriptados, textuais e abertos com `pypdf`;
- todas as 220 páginas da versão limpa foram renderizadas e revistas através de folhas de contacto;
- páginas representativas e zonas alteradas foram inspecionadas em alta resolução.

## O que continua em aberto

A prosa está agora em estilo de autor, mas a tese não está cientificamente pronta para submissão enquanto faltarem:

- números finais e intervalos de incerteza;
- versões congeladas dos algoritmos e do simulador;
- ablações e cenários integrados do TI-MARL;
- auditoria *as built* do EnergAIze e do lifecycle;
- classificação exata de cada demonstrador e respetiva autoridade de atuação;
- datas, durações, incidentes e hardware de deployment;
- atribuição detalhada de autoria;
- estado final dos artigos, repositórios, datasets e releases;
- substituição dos placeholders por figuras verificadas.

Esses elementos são problemas de evidência e conclusão científica, não de voz. A versão anotada mantém-nos localizados sem contaminar a leitura da versão limpa.
