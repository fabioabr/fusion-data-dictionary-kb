---
id: DOC-HCM-611
doc_type: system-doc
title: "PER_ACTIONS_TL — Ações de RH (Traduções)"
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
  - actions-tl
aliases:
  - PER_ACTIONS_TL
  - per_actions_tl
  - per-actions-tl
  - ações-de-rh-(traduções)
  - per-actions-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACTIONS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições das ações de RH em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe ações no idioma do usuário.
- **Self-service multilíngue** — colaboradores e gestores veem ações traduzidas.
- **Relatórios localizados** — suporte a relatórios em múltiplos idiomas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da ação | PER_ACTIONS_B | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | ACTION_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido da ação | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(600) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_actions_b]] — via `ACTION_ID` (tabela base da ação de RH)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Ações em português
```sql
SELECT tl.ACTION_ID, tl.ACTION_NAME
FROM   PER_ACTIONS_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `ACTION_ID` + `LANGUAGE`.
- Sempre usar JOIN com a tabela _B para obter dados completos.
---

## 📚 Referências

- [Oracle Docs — PER_ACTIONS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peractionstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
