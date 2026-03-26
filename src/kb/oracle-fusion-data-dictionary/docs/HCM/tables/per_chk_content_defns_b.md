---
id: DOC-HCM-643
doc_type: system-doc
title: "PER_CHK_CONTENT_DEFNS_B — Definições de Conteúdo de Checklist (Base)"
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
  - checklists
  - content-definitions
aliases:
  - PER_CHK_CONTENT_DEFNS_B
  - per_chk_content_defns_b
  - per-chk-content-defns-b
  - definições-de-conteúdo-de-checklist-(base)
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

# PER_CHK_CONTENT_DEFNS_B

## 📌 Visão Geral

Armazena as **definições de conteúdo** utilizadas em checklists. Define os tipos e estruturas de conteúdo disponíveis para configuração de templates de checklist.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados principais do registro, independente de idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de tipos de conteúdo** — padroniza os conteúdos disponíveis para checklists.
- **Configuração** — define a estrutura dos itens de conteúdo.
- **Reutilização** — permite compartilhar definições de conteúdo entre múltiplos checklists.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHK_CONTENT_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador único da definição | — | 🟢 90% |
| 2 | CONTENT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código do tipo de conteúdo | — | 🟢 85% |
| 3 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Status | Se a definição está ativa (Y/N) | — | 🟢 85% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de definições de conteúdo.

### Tabelas-filha (FK de saída)
- [[per_chk_content_defns_tl]] — via `CHK_CONTENT_DEFN_ID` (traduÃ§Ãµes da definiÃ§Ã£o de conteÃºdo de checklist)

---

## 📎 Uso Típico

### Definições de conteúdo ativas
```sql
SELECT pccd.CHK_CONTENT_DEFN_ID, pccd.CONTENT_TYPE_CODE
FROM   PER_CHK_CONTENT_DEFNS_B pccd
WHERE  pccd.ACTIVE_FLAG = 'Y';
```

### Filtros comuns
- `ACTIVE_FLAG = 'Y'` — Definições ativas
---

## 🔒 Observações

- Tabela base (_B) — textos traduzidos ficam na tabela _TL correspondente.
- Define os tipos de conteúdo reutilizáveis nos templates de checklist.
---

## 📚 Referências

- [Oracle Docs — PER_CHK_CONTENT_DEFNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perchkcontentdefnsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
