#!/bin/bash
# Publica o dashboard atualizado no GitHub Pages.
# Uso: ./publicar.sh            -> mensagem automática com a data
#      ./publicar.sh "texto"    -> mensagem de commit customizada
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -f index.html ]; then
  echo "erro: index.html não encontrado em $(pwd)" >&2
  exit 1
fi

MSG="${1:-briefing $(date +%d/%m/%Y)}"

git add -A

if git diff --cached --quiet; then
  echo "nada mudou — nada a publicar."
  exit 0
fi

git commit -q -m "$MSG"

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "commit feito, mas o remote 'origin' ainda não foi configurado."
  echo "o site NÃO foi atualizado. configure o GitHub e rode ./publicar.sh de novo."
  exit 2
fi

if ! git push -q origin main; then
  echo "commit feito, mas o push falhou (rede ou credencial)."
  echo "o site NÃO foi atualizado." >&2
  exit 3
fi

echo "publicado: $MSG"
echo "no ar em ~1 min."
