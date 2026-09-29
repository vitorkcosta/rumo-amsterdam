#!/usr/bin/env python3
"""Lê uma exportação de conversa do WhatsApp (.txt ou .zip) e gera, na mesma pasta:

  <nome>.jsonl      uma mensagem por linha: data, hora, autor, texto, midia
  <nome>.resumo.md  período, mensagens por mês e por autor, mídia, telefones removidos

Telefones no texto viram [telefone]. Autores que são números (contato não salvo) viram
[contato-N], sempre o mesmo N para o mesmo número dentro do arquivo.

Uso:
  python3 marketing/ferramentas/whatsapp_export.py marketing/entradas/privado/whatsapp/<arquivo>.txt
  python3 marketing/ferramentas/whatsapp_export.py marketing/entradas/privado/whatsapp/<arquivo>.zip

Os arquivos de saída ficam em marketing/entradas/privado/ (fora do git). Nunca copiá-los para fora.
Formatos aceitos: iOS "[dd/mm/aaaa, hh:mm:ss] Nome: texto" e Android "dd/mm/aaaa hh:mm - Nome: texto".
"""
import io
import json
import re
import sys
import zipfile
from collections import Counter, OrderedDict
from pathlib import Path

LRM = "‎"
RE_IOS = re.compile(r"^‎?\[(\d{1,2}/\d{1,2}/\d{2,4}),? (\d{1,2}:\d{2}(?::\d{2})?)\] (.*)$")
RE_ANDROID = re.compile(r"^‎?(\d{1,2}/\d{1,2}/\d{2,4}),? (\d{1,2}:\d{2}) - (.*)$")
RE_PHONE = re.compile(
    r"(?<![\d/])(?:\+?\d{2,3}[\s.-]?)?(?:\(?\d{2}\)?[\s.-]?)?\d{4,5}[\s.-]\d{4}(?![\d/])"  # com separador
    r"|(?<![\d/])\+?\d{10,13}(?![\d/])"  # sequência crua de 10 a 13 dígitos (celular com DDD/DDI)
)
RE_AUTHOR_PHONE = re.compile(r"^\+?[\d\s().-]{8,}$")
RE_MEDIA = re.compile(
    r"(<anexo: ?[^>]+>|<attached: ?[^>]+>|\(arquivo anexado\)|\(file attached\)|"
    r"<Mídia oculta>|<Media omitted>|imagem ocultada|image omitted|vídeo omitido|video omitted|"
    r"áudio omitido|audio omitted|figurinha omitida|sticker omitted|documento omitido|document omitted)",
    re.I,
)


def norm_date(d):
    p = d.split("/")
    dd, mm, yy = int(p[0]), int(p[1]), int(p[2])
    if yy < 100:
        yy += 2000
    return f"{yy:04d}-{mm:02d}-{dd:02d}"


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as z:
            names = [n for n in z.namelist() if n.lower().endswith(".txt")]
            if not names:
                sys.exit("zip sem .txt dentro")
            names.sort(key=lambda n: (not n.startswith("_chat"), n))
            return z.read(names[0]).decode("utf-8", errors="replace")
    return path.read_text(encoding="utf-8", errors="replace")


def parse(text: str):
    msgs = []
    cur = None
    for raw in io.StringIO(text):
        line = raw.rstrip("\n").replace(LRM, "")
        m = RE_IOS.match(line) or RE_ANDROID.match(line)
        if m:
            if cur:
                msgs.append(cur)
            date, time, rest = m.group(1), m.group(2), m.group(3)
            if ": " in rest:
                author, body = rest.split(": ", 1)
            else:
                author, body = "[sistema]", rest
            cur = {"data": norm_date(date), "hora": time[:5], "autor": author.strip(), "texto": body}
        elif cur is not None:
            cur["texto"] += "\n" + line
    if cur:
        msgs.append(cur)
    return msgs


def anonymize(msgs):
    contatos = OrderedDict()
    removidos = 0
    for m in msgs:
        a = m["autor"]
        if RE_AUTHOR_PHONE.match(a):
            if a not in contatos:
                contatos[a] = f"[contato-{len(contatos) + 1}]"
            m["autor"] = contatos[a]
        m["texto"], n = RE_PHONE.subn("[telefone]", m["texto"])
        removidos += n
        m["midia"] = bool(RE_MEDIA.search(m["texto"]))
    return removidos, len(contatos)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    if "privado" not in src.parts:
        sys.exit("por segurança, o arquivo de origem precisa estar em marketing/entradas/privado/")
    msgs = parse(read_text(src))
    if not msgs:
        sys.exit("nenhuma mensagem reconhecida: formato diferente do esperado?")
    removidos, nao_salvos = anonymize(msgs)

    out_jsonl = src.with_suffix(".jsonl")
    with out_jsonl.open("w", encoding="utf-8") as f:
        for m in msgs:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")

    por_mes = Counter(m["data"][:7] for m in msgs)
    por_autor = Counter(m["autor"] for m in msgs)
    midia = sum(1 for m in msgs if m["midia"])
    linhas = [
        f"# Resumo da exportação: {src.name}",
        "",
        f"- Período: {msgs[0]['data']} a {msgs[-1]['data']}",
        f"- Mensagens: {len(msgs)} · com mídia: {midia} · telefones removidos do texto: {removidos} · contatos não salvos anonimizados: {nao_salvos}",
        f"- Saída: `{out_jsonl.name}` (uma mensagem por linha)",
        "",
        "## Mensagens por mês",
        "| Mês | Mensagens |",
        "|-----|-----------|",
    ]
    linhas += [f"| {k} | {v} |" for k, v in sorted(por_mes.items())]
    linhas += ["", "## Mensagens por autor (nome como está no WhatsApp)", "| Autor | Mensagens |", "|-------|-----------|"]
    linhas += [f"| {k} | {v} |" for k, v in por_autor.most_common()]
    out_md = src.with_suffix(".resumo.md")
    out_md.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"{len(msgs)} mensagens · {msgs[0]['data']} a {msgs[-1]['data']} · {out_jsonl} · {out_md}")


if __name__ == "__main__":
    main()
