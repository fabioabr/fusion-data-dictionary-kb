---
id: DOC-HCM-617
doc_type: system-doc
title: "PER_ACTION_TYPES_TL — Tipos de Ação de RH (Traduções)"
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
  - action-types-tl
aliases:
  - PER_ACTION_TYPES_TL
  - per_action_types_tl
  - per-action-types-tl
  - tipos-de-ação-de-rh-(traduções)
  - per-action-types-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACTION_TYPES_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes dos tipos de ação de RH em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe tipos de ação no idioma do usuário.
- **Relatórios localizados** — suporte multilíngue.
- **Consistência** — tradução centralizada dos tipos de ação.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do tipo de ação | PER_ACTION_TYPES_B | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | ACTION_TYPE_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do tipo de ação | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_action_types_b]] — via `ACTION_TYPE_ID` (tabela base do tipo de aÃ§Ã£o de RH)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Tipos de ação em português
```sql
SELECT tl.ACTION_TYPE_ID, tl.ACTION_TYPE_NAME
FROM   PER_ACTION_TYPES_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `ACTION_TYPE_ID` + `LANGUAGE`.
- Sempre usar JOIN com a tabela _B para obter dados completos.
---

## 📚 Referências

- [Oracle Docs — PER_ACTION_TYPES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peractiontypestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
