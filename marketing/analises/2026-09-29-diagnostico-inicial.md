# Diagnóstico inicial e primeiros 30 dias

- **Data:** 2026-09-29 · **Insumos:** planejamento digital e cronograma anual da Luz Própria (Drive),
  NFs e e-mails da agência (Gmail), painel comercial de 18/09, recados da Cris no briefing de 25/09.
- **Nível de confiança:** o que está aqui é o que dá para afirmar sem nenhum relatório de resultado
  em mãos. Marcado: **M** medido · **E** estimado · **—** sem dado.

## Resultado em uma linha
Hoje o Chuveirão gasta ~R$ 5,1 mil/mês fixos com a agência (M) mais mídia e off (E: R$ 20 a 55 mil/mês
pelo cronograma) sem nenhuma métrica de resposta ligada a cidade ou canal: não dá para dizer o que
cada real produziu. Primeiro trabalho é instrumentar, e a festa dos pintores de 10/10 é a primeira
ação a nascer medida.

## O que existe e está bom
- Planejamento da agência tem base decente: 4 personas, posicionamento, 3 editorias, 12 campanhas
  mensais, mídia comprada **por cidade** (isso permite medir por loja). Cronograma anual com verba.
- ChuvPontos gera lista de ativos, inativos e "nunca compraram": base pronta para leitura e reativação.
- ERP produz evolução de vendas por cliente e por vendedor, ticket e conversão orçamento→venda:
  dá para ligar campanha a venda por loja.
- Existe uma pessoa interna (Cris) com acesso à ponta (gerentes, WhatsApp das lojas, eventos).

## O que falta (por ordem de custo de corrigir)
1. **Nenhum relatório de resultado no repositório ou no Gmail** desde o de fevereiro (apresentado em
   reunião, sem arquivo). Não se sabe alcance, cliques, conversas nem custo por conversa de nenhum mês. (—)
2. **Valor da mídia Meta e Google não consolidado**: boletos e NFs existem no Gmail, mas ninguém soma. (—)
3. **Sem origem no cadastro**: ChuvPontos e orçamento não perguntam "como conheceu". Sem isso, rádio,
   outdoor e evento ficam sem atribuição. (—)
4. **Sem contagem de conversas no WhatsApp por loja**: o objetivo dos anúncios é conversa, e a loja
   não conta. (—)
5. **Sem UTM nem cupom por canal.** (—)
6. **Vitor sem acesso de leitura ao Meta Business e Google Ads.** Depende da agência para tudo. (—)
7. **Verba dividida igual por cidade** (R$ 900 cada no cenário 1) enquanto as lojas têm tamanhos e
   gaps muito diferentes (Ourinhos e CMC bem abaixo da meta em set/26; Araçatuba e Assis acima). (E)
8. **B2B sem plano**: o planejamento da agência é só B2C e profissional; construtora, indústria,
   condomínio e imobiliária dependem de prospecção ativa que ninguém dirige. (—)

## Primeiros 30 dias (29/09 a 29/10)

| # | Ação | Dono | Prazo | Como medir |
|---|------|------|-------|------------|
| 1 | **Festa dos pintores e das crianças (10/10; Araçatuba 17/10) nasce medida**: meta de cadastros no ChuvPontos por loja, lista de presença, código `PINTOR10` válido 30 dias, venda de pintores 30 dias após × baseline. Briefing para a Cris esta semana. | diretor → Cris | plano até 02/10; conferência 06/10 | cadastros, presentes, resgates do código, lift de venda por loja |
| 2 | **Pedir à Luz Própria o relatório de agosto e setembro** no formato do workspace (por cidade e campanha, CSV do Meta e do Google) e o valor de mídia realizado por mês desde jan/26. | diretor → Vitor envia | pedido até 01/10; entrega até 05/10 | `relatorio_no_prazo`, `csv_entregue` |
| 3 | **Ler a base do ChuvPontos** (CSVs de ago/26 no Gmail): ativos/inativos/nunca compraram por loja, quanto vale reativar, lista de pintores para o evento. | Vitor salva CSV em `entradas/privado/` ou no Drive → leitor-de-clientes | até 03/10 | análise em `analises/` |
| 4 | **Instrumentar barato**: "como conheceu" no cadastro do app e no orçamento; contagem semanal de conversas do WhatsApp por loja (Cris pede aos gerentes); UTM em toda peça; cupom por canal off. | Cris + agência + TI | 15/10 | existência dos campos; primeiro registro semanal |
| 5 | **Campanha de aniversário (out/nov, 2 × R$ 50 mil off + digital)**: definir objetivo e meta por cidade antes de liberar verba; dividir mídia por gap de loja, não em partes iguais; briefing formal. | estrategista → diretor → Vitor aprova | estratégia até 06/10; briefing até 08/10 | conversas, cadastros, lift por cidade |
| 6 | **Acesso de leitura** ao Meta Business e Google Ads para o Vitor. | Vitor pede à Glauce | 10/10 | acesso ativo |
| 7 | **Comunicação de preço pós-01/10** alinhada com o comercial (repasse do ICMS-ST): uma mensagem só para profissional e para consumidor; agência não pode anunciar preço velho. | Vitor + comercial → Cris/agência | 01/10 | peças conferidas |

## Decisões que preciso do Vitor
1. Aprova exigir da agência relatório até o dia 5, por cidade, com CSV? (proposta em `decisoes.md`)
2. Aprova condicionar a verba de aniversário (R$ 100 mil off) a meta por cidade definida antes?
3. Confirma: Cris é o contato do dia a dia com a agência? Quem tem acesso ao ChuvPontos (relatórios)?
4. Confirma o que está ativo: Google Ads (Max Performance/Shopping), e-mail marketing, Mercado Livre,
   analytics do site.
5. Quer que eu leia os CSVs do ChuvPontos de agosto agora? (precisa salvar os anexos no Drive ou colar
   aqui; ficam em `entradas/privado/`, fora do git).

## Preciso de você
Itens 1 a 5 acima. Sem o item 5 e o relatório da agência, a próxima rodada continua sem número.
