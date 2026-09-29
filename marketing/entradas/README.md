# Entradas

Tudo que entra no workspace, datado, uma por arquivo: `AAAA-MM-DD-<origem>-<tema>.md`
(modelo em `../modelos/entrada.md`). Origem: vitor, cris, luz-propria, erp, chuvpontos, meta, google, loja, outro.

- `dados/`: arquivos brutos **sem** dado pessoal (relatório agregado, export de mídia por cidade, PDF do ERP por loja).
- `privado/`: arquivos com nome, CPF, telefone, e-mail (CSV do ChuvPontos, listas para WhatsApp). **Fora do git.**
  Some quando a sessão na nuvem acaba; o que precisa durar vai para o Google Drive (pasta "Marketing Chuveirão").

O `.md` da entrada sempre existe, mesmo quando o bruto está em `privado/`: ele guarda o resumo agregado.

## Exportações do WhatsApp
Colocar os `.txt` ou `.zip` exportados em `privado/whatsapp/` e rodar `/marketing importar-whatsapp`
numa sessão no computador (o Claude na nuvem não alcança arquivos locais). O script
`../ferramentas/whatsapp_export.py` remove telefones e gera um resumo; a skill escreve só o agregado
em `entradas/AAAA-MM-DD-whatsapp-<grupo>.md`.
