# Rumo a Amsterdam

Site do ciclo de treino para a TCS Amsterdam Marathon (18/10/2026, meta 3:40:00).

Link fixo pra compartilhar — a página se atualiza sozinha, quem tem o link nunca
precisa de um endereço novo.

## Como funciona

```
conector Coros
      ↓
dados_hoje.json
      ↓
briefing_coros.py   (fonte no Google Drive)
      ↓
calculos.json       ← única fonte de números
      ↓
index.html          ← este repositório
      ↓
git push → GitHub Pages
```

A task agendada `briefing-coros-diario` roda todo dia às 06:30, regenera o
`index.html` e executa `./publicar.sh`.

## Publicar na mão

```bash
./publicar.sh "o que mudou"
```

## Privacidade

Página **não indexada**: `robots.txt` bloqueia tudo e o `index.html` traz
`<meta name="robots" content="noindex, nofollow, noarchive, noimageindex">`.
Buscadores não listam. Quem tiver o link, entra — não há senha.

## Arquivos

| Arquivo       | Papel                                                     |
|---------------|-----------------------------------------------------------|
| `index.html`  | O site inteiro: HTML, CSS e gráficos SVG, sem dependências |
| `robots.txt`  | Bloqueio de indexação                                      |
| `.nojekyll`   | Faz o GitHub Pages servir os arquivos sem processar        |
| `publicar.sh` | commit + push                                              |
