# Este repositório

Duas coisas independentes convivem aqui:

1. **Site da maratona** (`index.html`, `publicar.sh`, `robots.txt`, `.nojekyll`). É gerado pela task
   `briefing-coros-diario` e publicado no GitHub Pages. Tarefas de marketing não tocam nesses arquivos.
2. **Workspace de marketing e prospecção do Chuveirão das Tintas** (`marketing/`), com agentes em
   `.claude/agents/` e a skill `/marketing` em `.claude/skills/marketing/`. Serve para ler clientes,
   medir alcance de redes/campanhas/ações, montar estratégia e direcionar a Cris (marketing interno)
   e a Luz Própria (agência).

Guia humano do workspace: `marketing/README.md`.

## Regras para qualquer tarefa de marketing

- Idioma: português do Brasil, direto, sem preâmbulo. Liderar com a resposta.
- **Sempre** ler antes de agir: `marketing/contexto/*.md`, as últimas entradas de `marketing/diario.md`,
  `marketing/contexto/decisoes.md` e `marketing/metricas/painel.md`.
- Tudo que o Vitor trouxer (print, relatório, CSV, decisão, recado da Cris, proposta da agência) vira
  uma entrada em `marketing/entradas/` e uma linha em `marketing/diario.md`. Fatos duráveis (verba,
  equipe, canal, calendário, decisão) atualizam o arquivo certo em `marketing/contexto/`.
- **Este repositório é público.** Nunca gravar CPF, telefone, e-mail pessoal, endereço, lista nominal
  de clientes ou de funcionários, nem dados de vendedor individual. Só agregados. Dados nominais ficam
  no Google Drive (pasta "Marketing Chuveirão") ou em `marketing/entradas/privado/` (ignorado pelo git).
- Nunca enviar e-mail, WhatsApp, criar evento ou arquivo no Drive em nome do Vitor sem ele pedir
  explicitamente nessa conversa. Rascunhos vão para `marketing/briefings/`.
- Nunca inventar métrica. Sem dado: escrever "sem dado" e dizer quem fornece, o quê e até quando.
- Não rodar `publicar.sh` em tarefas de marketing (ele faz `git add -A` e push direto na `main`).
  Commits de marketing usam o prefixo `marketing:` e vão para a branch da sessão.
- Fontes externas (Drive, Gmail) e como consultá-las: `marketing/contexto/fontes-de-dados.md`.

## Agentes e skill

| Nome | Quando usar |
|------|-------------|
| `/marketing` (skill) | Porta de entrada. Registra entradas, mostra status e aciona o agente certo. |
| `leitor-de-clientes` | Dados de clientes (ChuvPontos, ERP, listas ativos/inativos): quem compra, quem parou, quem reativar, segmentação. |
| `analista-de-alcance` | Medir redes sociais, campanhas, mídia paga, eventos e ações. Mantém o painel e o registro de métricas. |
| `estrategista-de-comunicacao` | Transformar leituras e métricas em estratégia, plano de campanha, prospecção e alocação de verba. |
| `diretor-de-marketing` | Briefings, planos semanais, cobranças e pautas para a Cris e para a Luz Própria. Rascunhos de mensagens para o Vitor enviar. |
