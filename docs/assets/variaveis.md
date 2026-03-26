---
description: "Variáveis globais para geração de documentos e apresentações HTML"
---

# Variáveis Globais

Dados centralizados usados pelas skills de geração (prs-writer, doc-writer, adr-writer, etc.).
Toda skill que gera output final (.md ou .html) DEVE ler este arquivo e substituir as variáveis correspondentes.

## Empresa

| Variável | Valor |
|----------|-------|
| `{{EMPRESA}}` | Patria Investimentos |
| `{{EMPRESA_SIGLA}}` | Patria |
| `{{AREA}}` | Arquitetura e Produtividade Corporativa |
| `{{TEAM}}` | Arquitetura |

## Autor / Responsável

| Variável | Valor |
|----------|-------|
| `{{AUTOR_NOME}}` | Fabio A. B. Rodrigues |
| `{{AUTOR_INICIAIS}}` | FABR |
| `{{AUTOR_CARGO}}` | Arquitetura e Produtividade Corporativa |
| `{{AUTOR_EMAIL}}` | fabio.rodrigues.consult@patria.com |

## Repositório

| Variável | Valor |
|----------|-------|
| `{{REPO_NOME}}` | patria-tech-docs |
| `{{REPO_PROJETO}}` | Discovery Oracle Fusion |
| `{{REPO_SERIE}}` | Data Dictioary |

## Logos (HTML)

| Variável | Valor |
|----------|-------|
| `{{LOGO_DARK_BASE64}}` | conteúdo de `src/assets/main/logos/logo-dark-base64.txt` |
| `{{LOGO_LIGHT_BASE64}}` | conteúdo de `src/assets/main/logos/logo-dark-base64.txt` |

> **Implementação no HTML:** vamos usar apenas o `.logo-dark` pois vamos manter apenas uma cor de cabeçalho/rodapé 

## Footer (HTML)

| Variável | Valor |
|----------|-------|
| `{{FOOTER_TEXTO}}` | {{EMPRESA}} · {{AREA}} |
| `{{FOOTER_AUTOR}}` | {{AUTOR_NOME}} |
| `{{FOOTER_CARGO}}` | {{AUTOR_CARGO}} |
| `{{FOOTER_SELO}}` | Criado por |
