---
id: DOC-HCM-609
doc_type: system-doc
title: "PER_ACCRUAL_PLANS_TL — Planos de Acumulação (Traduções)"
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
  - absence-management
  - traducoes
  - accrual-plans-tl
aliases:
  - PER_ACCRUAL_PLANS_TL
  - per_accrual_plans_tl
  - per-accrual-plans-tl
  - planos-de-acumulação-(traduções)
  - per-accrual-plans-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACCRUAL_PLANS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições dos planos de acumulação em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — permite exibir planos de accrual no idioma do usuário.
- **Self-service multilíngue** — colaboradores veem nomes de planos traduzidos.
- **Relatórios localizados** — suporte a relatórios em idiomas específicos.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCRUAL_PLAN_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do plano de acumulação | PER_ACCRUAL_PLANS_B | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | ACCRUAL_PLAN_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do plano | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(600) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_accrual_plans_b]] — via `ACCRUAL_PLAN_ID` (tabela base do plano de acÃºmulo)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Planos de accrual em português
```sql
SELECT tl.ACCRUAL_PLAN_ID, tl.ACCRUAL_PLAN_NAME, tl.DESCRIPTION
FROM   PER_ACCRUAL_PLANS_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `ACCRUAL_PLAN_ID` + `LANGUAGE`.
- Sempre usar JOIN com a tabela _B para obter dados completos do plano.
---

## 📚 Referências

- [Oracle Docs — PER_ACCRUAL_PLANS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peraccrualplanstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
