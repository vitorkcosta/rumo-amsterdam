---
name: marketing
description: Marketing e prospecção do Chuveirão das Tintas. Use sempre que o Vitor falar de clientes, redes sociais, campanhas, ações nas lojas, mídia paga, Cris, Luz Própria, ChuvPontos, verba de marketing, ou trouxer qualquer dado, print, relatório ou recado sobre isso. Registra a entrada, atualiza a memória e aciona o agente certo.
argument-hint: "[registrar|status|importar-whatsapp|clientes|medir|estrategia|briefing-cris|briefing-agencia] <texto, arquivo ou link>"
---

# /marketing — porta de entrada do workspace

## Antes de tudo, sempre

1. Ler `marketing/contexto/negocio.md`, `publicos.md`, `equipe-e-parceiros.md`,
   `canais-e-calendario.md` e `fontes-de-dados.md`.
2. Ler `marketing/contexto/decisoes.md`, as últimas 30 linhas de `marketing/diario.md`
   e `marketing/metricas/painel.md`.
3. Se o Vitor trouxe algo novo (texto, print, link, arquivo, recado), **registrar primeiro**
   (modo `registrar`), depois fazer o que foi pedido.
4. Data de hoje: usar `date +%F` no Bash. Nunca chutar data.

Se o argumento não tiver um modo explícito, deduzir pelo pedido. Na dúvida entre dois modos,
executar os dois na ordem: registrar → clientes → medir → estrategia → briefing.

## Modos

### registrar
Entrada nova de qualquer origem (Vitor, Cris, Luz Própria, ERP, ChuvPontos, Meta, Google, evento).
1. Salvar em `marketing/entradas/AAAA-MM-DD-<origem>-<tema>.md` com o modelo `marketing/modelos/entrada.md`.
   Origem: `vitor`, `cris`, `luz-propria`, `erp`, `chuvpontos`, `meta`, `google`, `loja`, `outro`.
2. Arquivo bruto (CSV, PDF, XLSX): se não tem dado pessoal → `marketing/entradas/dados/`;
   se tem → `marketing/entradas/privado/` (fora do git) e o `.md` guarda só o resumo agregado.
   Link do Drive: registrar o link e o ID do arquivo no `.md`; ler pelo conector quando precisar.
3. Métricas mencionadas → acrescentar linhas em `marketing/metricas/registro.csv`
   (formato no cabeçalho do arquivo; vírgula como separador, ponto como decimal).
4. Fato durável (verba, equipe, canal, calendário, decisão, regra) → atualizar o arquivo certo em
   `marketing/contexto/` e, se for decisão, `decisoes.md`.
5. Acrescentar uma linha em `marketing/diario.md`: `AAAA-MM-DD | origem | resumo em uma frase | caminho`.
6. Responder em até 4 linhas: o que registrou, o que mudou no contexto, o que sugere fazer agora
   (ou "nada por enquanto").

### status
Sem acionar agente. Responder com:
- Onde estamos: 3 a 5 números do painel que importam (ou "painel sem dado de X").
- O que está aberto: decisões pendentes do Vitor, briefings sem resposta, entregas atrasadas da agência
  ou da Cris (ler `briefings/*/` e `decisoes.md`).
- Próximos 30 dias do calendário (`canais-e-calendario.md`).
- 3 ações recomendadas, cada uma com responsável.

### importar-whatsapp
Exportações de grupos do WhatsApp (agência, marketing interno) colocadas pelo Vitor em
`marketing/entradas/privado/whatsapp/` (.txt ou .zip). Roda numa sessão no computador dele.
1. Para cada arquivo: `python3 marketing/ferramentas/whatsapp_export.py <arquivo>`. Gera `.jsonl`
   (uma mensagem por linha, telefones removidos) e `.resumo.md` na mesma pasta. Ler o resumo primeiro.
2. Ler o `.jsonl` por mês (Bash/python), do mais recente para o mais antigo. Histórico grande: os últimos
   6 meses em detalhe, o resto em passagem rápida.
3. Escrever `marketing/entradas/AAAA-MM-DD-whatsapp-<grupo>.md` (grupo: `agencia` ou `mkt-interno`),
   **só agregado**: período e volume; participantes por papel (agência: nome e função, como já está em
   `contexto/equipe-e-parceiros.md`; internos: papel, ex. "gerente de Assis", sem sobrenome); linha do
   tempo por mês com decisões, entregas, peças e campanhas, problemas recorrentes, pedidos sem resposta;
   como cada grupo funciona (quem pede, quem aprova, tempo de resposta, tom). Nada de telefone, nome de
   cliente, valor por vendedor. Até ~300 linhas por grupo.
4. Atualizar `contexto/` com o que for durável (escopo real da agência, ritos, calendário executado,
   canais em uso, custos citados) e `contexto/decisoes.md` com as decisões encontradas (fonte:
   `whatsapp <grupo> AAAA-MM-DD`). Métricas citadas (alcance, cliques, cadastros, valores) vão para
   `metricas/registro.csv` com fonte `whatsapp <grupo>`.
5. Uma linha por grupo em `marketing/diario.md`. Depois, `status`.
Os arquivos em `privado/` nunca entram no git; conferir com `git status` antes de commitar.

### clientes → agente `leitor-de-clientes`
### medir → agente `analista-de-alcance`
### estrategia → agente `estrategista-de-comunicacao`
### briefing-cris e briefing-agencia → agente `diretor-de-marketing`

## Como acionar um agente

Usar a ferramenta Agent com `subagent_type` igual ao nome do agente. O prompt deve conter:
- o pedido do Vitor, literal;
- os caminhos das entradas relevantes (as que acabaram de ser registradas e as anteriores sobre o tema);
- o caminho de saída esperado (`marketing/analises/...` ou `marketing/briefings/...`);
- a instrução "leia o contexto em marketing/contexto antes de começar".

Pedidos compostos ("o que eu faço com isso?", "monta o plano do mês") seguem a cadeia
leitor (se há dados de clientes) → analista (se há métricas) → estrategista → diretor.
Cada agente lê a saída do anterior. Não pular etapa quando o dado existe; pular e dizer o que falta
quando não existe.

Depois de cada agente terminar, relatar ao Vitor em poucas linhas com o caminho do arquivo gerado
e o que precisa dele (decisão ou dado). Não colar o arquivo inteiro na resposta.

## Regras de resposta

- Liderar com a resposta. Sem preâmbulo, sem repetir o pedido.
- Número só quando muda a decisão, e em tabela curta.
- Terminar sempre com "Preciso de você:" seguido de decisão ou dado, ou "nada". O Vitor não quer ser
  gargalo: só entra ali verba nova, risco ou conflito com o comercial; o resto vai para a Cris, e a
  mensagem para ela já sai pronta para encaminhar. Antes de tudo, ler no Gmail `subject:[MKT]` e
  registrar o que a Cris mandou.
- Nunca inventar métrica. Sem dado → "sem dado" + quem fornece, o quê, até quando.
- Se o Vitor estiver errado (verba, prazo, expectativa de resultado), dizer na lata e propor o ajuste.
- Commit ao final quando houver arquivo novo ou alterado: `marketing: <o que mudou>`.
