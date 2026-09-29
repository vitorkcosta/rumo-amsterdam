# Fontes de dados e como acessar

Os conectores Google Drive e Gmail ficam disponíveis nas sessões do Claude Code do Vitor.
Só leitura por padrão; escrita (criar arquivo, enviar e-mail) só com pedido explícito na conversa.

## Google Drive

| O que | Onde | Como buscar |
|-------|------|-------------|
| Planejamento de marketing digital da Luz Própria (44 slides: público, posicionamento, editorias, campanhas, mídia) | Google Slides `1Phw4McGE68kLBSvSVJCPFgaMcd7Ftzkc1sPIJAmDq14` | `read_file_content` com o ID |
| Planejamento anual (cronograma + verba) | Google Sheets `1D7dua6PQRDkdCgGA_b5kAijxuGwtJUrUvKlFEMOabEA` | idem |
| Peças (PSD) da agência | pasta "PSD's Chuveirão" `14edTx-Ywwg-Wjf-Gg7lJz37ri8_cZjCz`, subpasta "Campanhas" | `search_files` com `parentId` |
| Relatórios diários do ERP (PDF: vendas diárias por empresa, evolução de vendas por vendedor/cliente, metas, ticket/conversão, margem, inadimplência, fluxo de caixa) | pasta "Chuveirão das Tintas - Relatórios Diários" `1IYdzyLR65kWezrJSH3K8JDQUmWhap_Tq` (e cópias em `16CjAm3CHm8zkVy2AiOvLDlUEtHa7XXxX`) | `search_files`: `parentId = '<id>' and title contains 'EVOLUCAO'` ou `'VENDAS_DIARIAS'` |
| Pasta do workspace para dados nominais (a criar quando precisar) | "Marketing Chuveirão" | criar só com pedido do Vitor |

Consulta genérica: `fullText contains 'Chuveirão' and title contains '<termo>'`.

## Gmail

| O que | Consulta |
|-------|----------|
| Tudo da agência | `from:luzpropria.com` |
| Faturamento (fee + comissão) | `from:financeiro@luzpropria.com subject:Faturamento` |
| Mídia Meta/Google (boletos, NFs) | `from:luzpropria.com (boleto OR NF) (meta OR google)` |
| Relatórios e planejamento da agência | `from:luzpropria.com (relatório OR planejamento OR cronograma)` |
| Relatórios do ChuvPontos (CSV ativos/inativos/nunca compraram) | `from:contato@chuveiraodastintas.com.br (ChuvPontos OR relatório)` |
| Painel comercial do ERP (agente do Vitor) | `subject:"[Agente] Painel Chuveirão"` |
| Briefing diário do Vitor (contém recados da Cris e decisões) | `subject:"[Agente] Briefing"` |
| Recados de marketing internos | `Cris marketing` ou `festa dos pintores` |

Anexos de e-mail: o conector lista `attachments` no `get_thread`; para ler o conteúdo, pedir ao Vitor
para salvar no Drive ou colar aqui.

## ERP Citel
Relatórios chegam por e-mail/Drive em PDF. Os úteis para marketing: **Evolução de Vendas** (por
vendedor ou por cliente, 7 meses, por empresa), **Vendas Diárias por Empresa**, **Metas por Vendedor**,
**Ticket e Conversão** (orçamento → faturado). Pedir a TI (Denilson) um export CSV de clientes com:
código, tipo PF/PJ, atividade, cidade, loja, vendedor, data da primeira e da última compra, valor 12
meses, quantidade de compras 12 meses, linha principal. Sem nome/CPF para o repositório.

## ChuvPontos
CSVs `relatorio_clientes_ativos`, `relatorio_clientes_inativos` e "nunca compraram" (via contato@).
Colunas ainda não catalogadas: o `leitor-de-clientes` documenta na primeira leitura.

## Plataformas de mídia (acesso é da agência)
Meta Business Suite e Google Ads. Pedir export mensal CSV por campanha e por cidade: investimento,
impressões, alcance, cliques, conversas iniciadas, custo por resultado. Pedir acesso de leitura
para o Vitor **(decisão pendente)**.

## O que ainda não existe
Google Analytics/plataforma do site (**confirmar**), contagem de conversas do WhatsApp por loja,
campo "como conheceu" no cadastro, cupons por canal. Ver `metricas/dicionario.md`.
