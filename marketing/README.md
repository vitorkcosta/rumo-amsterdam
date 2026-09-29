# Marketing e Prospecção — Chuveirão das Tintas

Workspace de agentes para: ler os clientes, medir o alcance e o resultado de redes sociais,
campanhas e ações, montar estratégia e direcionar a **Cris** (marketing interno) e a
**Luz Própria** (agência). Tudo que o Vitor for colocando aqui vira memória para as próximas rodadas.

## Como usar (no Claude Code, neste repositório)

Fale normalmente ou use a skill:

```
/marketing registrar  <cole o texto, o print, o link do Drive ou o caminho do arquivo>
/marketing status
/marketing importar-whatsapp                     -> lê exportações em entradas/privado/whatsapp/ (sessão local)
/marketing clientes   <pergunta ou arquivo>      -> agente leitor-de-clientes
/marketing medir      <campanha, mês ou canal>   -> agente analista-de-alcance
/marketing estrategia <tema>                     -> agente estrategista-de-comunicacao
/marketing briefing-cris <tema>                  -> agente diretor-de-marketing
/marketing briefing-agencia <tema>               -> agente diretor-de-marketing
```

Exemplos:
- "registra: a Cris confirmou que a festa dos pintores é 10/10, Araçatuba 17/10, sorteio só com o app"
- "mede a campanha de setembro com esse relatório da Luz Própria" (cole o link do Drive)
- "quem parou de comprar em Ourinhos nos últimos 90 dias?" (anexe o CSV do ChuvPontos ou o PDF do ERP)
- "monta o briefing da campanha de aniversário para a Luz Própria com verba de R$ 50 mil off + digital"
- "plano da semana para a Cris"

## Mapa das pastas

| Pasta / arquivo | O que é |
|-----------------|---------|
| `contexto/negocio.md` | O que é o Chuveirão, lojas, posicionamento, tom de voz, e-commerce, ChuvPontos, ERP |
| `contexto/publicos.md` | Públicos e personas (doméstico, pintores, oficinas, piscineiros, B2B) |
| `contexto/equipe-e-parceiros.md` | Vitor, Cris, Luz Própria (escopo, time, custos, ritos), fornecedores de mídia |
| `contexto/canais-e-calendario.md` | Canais, verba planejada, calendário anual, campanhas mensais, eventos |
| `contexto/fontes-de-dados.md` | Onde estão os dados (Drive, Gmail, ERP, ChuvPontos, agência) e como buscar |
| `contexto/decisoes.md` | Registro de decisões (o que foi decidido, por quem, quando) |
| `diario.md` | Linha do tempo de tudo que entrou (append-only) |
| `entradas/` | Entradas brutas datadas. `dados/` para CSV sem PII; `privado/` fica fora do git |
| `metricas/dicionario.md` | Definição de cada métrica e regras de atribuição |
| `metricas/painel.md` | Painel mensal (funil por canal, por cidade, base de clientes, ações, agência) |
| `metricas/registro.csv` | Registro linha a linha de todas as métricas coletadas |
| `analises/` | Saídas dos agentes: leituras de clientes, medições, estratégias |
| `briefings/cris/` | Planos semanais, checklists e mensagens para a Cris |
| `briefings/luz-propria/` | Briefings de campanha, pautas de reunião, cobranças e feedback para a agência |
| `modelos/` | Modelos que os agentes usam para gerar cada tipo de documento |
| `ferramentas/` | Scripts de apoio (ex.: leitor de exportação do WhatsApp) |

## Ritmo sugerido

- **Diário/quando surgir**: `registrar` qualquer coisa nova (print, recado da Cris, e-mail da agência).
- **Semanal (segunda)**: `status` + `briefing-cris` para a semana.
- **Mensal (até dia 10)**: `medir` o mês anterior com o relatório da Luz Própria + export do Meta/Google;
  depois `estrategia` do mês seguinte e `briefing-agencia`.
- **Antes de cada campanha/evento**: `briefing-agencia` ou `briefing-cris` com meta numérica e forma de medir.
- **Depois**: `medir` com o modelo de pós-campanha.

## Privacidade

O repositório é público. Aqui só entram agregados. Listas com nome, CPF, telefone ou e-mail ficam no
Google Drive ou em `entradas/privado/` (ignorado pelo git). Os agentes já sabem disso.
