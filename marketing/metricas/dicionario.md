# Dicionário de métricas e regras de atribuição

Toda métrica registrada em `registro.csv` usa o nome desta lista. Se precisar de uma nova, adicionar aqui.

## Investimento
| Métrica | Definição |
|---------|-----------|
| `invest_fee` | Fee mensal da agência (R$) |
| `invest_comissao` | Comissão de mídia da agência (R$) |
| `invest_meta` | Mídia paga Meta (R$), por cidade quando houver |
| `invest_google` | Mídia paga Google (R$) |
| `invest_off` | Rádio, outdoor, impresso (R$), por praça |
| `invest_producao` | Brindes, camisetas, gráfica, evento (R$) |
| `invest_total` | Soma de tudo no período |
| `mkt_pct_venda` | invest_total ÷ venda do período (%) |

## Alcance e engajamento (por canal)
| Métrica | Definição |
|---------|-----------|
| `alcance` | Contas únicas alcançadas no período |
| `impressoes` | Exibições totais |
| `frequencia` | impressoes ÷ alcance |
| `seguidores_liq` | Seguidores ganhos − perdidos |
| `interacoes` | Curtidas + comentários + compartilhamentos + salvamentos |
| `tx_engajamento` | interacoes ÷ alcance (%) |
| `visualizacoes_video` | Views de reels/vídeos |

## Resposta (por canal e cidade)
| Métrica | Definição |
|---------|-----------|
| `cliques_link` | Cliques em link (bio, anúncio, e-mail) |
| `ctr` | cliques ÷ impressoes (%) |
| `cpc` | invest ÷ cliques (R$) |
| `cpm` | invest ÷ impressoes × 1000 (R$) |
| `conversas` | Conversas iniciadas no WhatsApp a partir de anúncio/post (Meta) ou contadas pela loja |
| `custo_conversa` | invest ÷ conversas (R$) |
| `cadastros` | Novos cadastros (ChuvPontos, site, lista de evento) |
| `custo_cadastro` | invest ÷ cadastros (R$) |
| `orcamentos` | Orçamentos abertos no ERP no período (por loja) |
| `conv_orc_venda` | Orçamentos faturados ÷ orçamentos (%) |
| `pedidos_ecom` | Pedidos no e-commerce |
| `email_entregues`, `email_abertura`, `email_cliques` | Disparos de e-mail |

## Venda e base
| Métrica | Definição |
|---------|-----------|
| `venda` | Faturamento do período (R$), por loja |
| `baseline` | Venda esperada sem a ação: média das 4 semanas anteriores ajustada pelo mesmo período do ano anterior. Mostrar a conta. |
| `lift` | venda − baseline (R$) na janela da ação |
| `roas_incr` | lift ÷ invest da ação |
| `ticket_medio` | venda ÷ documentos |
| `clientes_novos` | Primeira compra no período |
| `clientes_reativados` | Compraram no período após ≥ 90 dias sem compra (profissional: ≥ 45 dias) |
| `clientes_ativos` | Compraram nos últimos N dias (N por perfil: profissional 45, doméstico 365) |
| `churn` | Ativos no período anterior que não compraram no atual (%) |
| `presentes_evento` | Pessoas presentes em evento |
| `como_conheceu_<canal>` | Respostas "como conheceu" por canal (pesquisa no PDV/cadastro) |

## Agência (entrega)
| Métrica | Definição |
|---------|-----------|
| `posts_planejados` / `posts_publicados` | Por mês |
| `relatorio_no_prazo` | 1 se o relatório chegou até o dia 5, 0 se não |
| `relatorio_por_cidade` | 1 se trouxe dado por cidade |
| `csv_entregue` | 1 se entregou export CSV do Meta/Google |

## Regras de atribuição (do mais confiável ao menos)
1. **Rastreável direto**: cupom/código, UTM, "como conheceu", conversa que virou orçamento com origem
   anotada. Vale como resultado do canal.
2. **Lift geográfico**: cidade com ação × cidade comparável sem ação, mesma janela. Vale como
   "provável".
3. **Lift temporal**: janela da ação × baseline da mesma loja. Vale como "indicativo"; citar o que
   mais pode ter mexido (feriado, preço, clima, sazonalidade).
4. **Correlação** (subiu alcance, subiu venda): não vale como resultado. Registrar como observação.

Toda medição diz qual nível usou. Métrica de vaidade (alcance, seguidores, curtidas) só entra no
painel acompanhada da métrica de resposta correspondente.

## Formato do `registro.csv`
`data,periodo,canal,campanha,cidade,metrica,valor,unidade,fonte,observacao`
- `data`: dia do registro (AAAA-MM-DD). `periodo`: `2026-09` (mês) ou `2026-10-10` (dia) ou `2026-W41`.
- `canal`: instagram, facebook, meta_ads, google_ads, whatsapp, ecommerce, chuvpontos, email, radio,
  outdoor, pdv, evento, agencia, total.
- `cidade`: prudente, assis, ourinhos, aracatuba, marilia, rondonopolis, todas.
- `valor`: número com ponto decimal. `unidade`: brl, n, pct, x.
- `fonte`: de onde veio (ex.: `NF Luz Própria set/26`, `print Instagram 29/09`, `relatório agência ago/26`).
