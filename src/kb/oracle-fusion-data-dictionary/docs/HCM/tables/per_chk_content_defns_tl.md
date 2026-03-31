---
id: DOC-HCM-644
doc_type: system-doc
title: "PER_CHK_CONTENT_DEFNS_TL — Definições de Conteúdo de Checklist (Traduções)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - workforce-management
  - traducoes
  - content-defns-tl
aliases:
  - PER_CHK_CONTENT_DEFNS_TL
  - per_chk_content_defns_tl
  - per-chk-content-defns-tl
  - definições-de-conteúdo-de-checklist-(traduções)
  - per-chk-content-defn
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CHK_CONTENT_DEFNS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes das definições de conteúdo de checklist em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe definições de conteúdo no idioma do usuário.
- **Consistência** — tradução centralizada das definições.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHK_CONTENT_DEFN_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da definição | PER_CHK_CONTENT_DEFNS_B | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | CONTENT_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido da definição | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_chk_content_defns_b]] — via `CHK_CONTENT_DEFN_ID` (tabela base da definição de conteúdo de checklist)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Definições de conteúdo em português
```sql
SELECT tl.CHK_CONTENT_DEFN_ID, tl.CONTENT_NAME
FROM   PER_CHK_CONTENT_DEFNS_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `CHK_CONTENT_DEFN_ID` + `LANGUAGE`.
---

## 📚 Referências

- [Oracle Docs — PER_CHK_CONTENT_DEFNS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perchkcontentdefnstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
