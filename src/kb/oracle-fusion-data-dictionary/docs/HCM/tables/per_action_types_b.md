---
id: DOC-HCM-616
doc_type: system-doc
title: "PER_ACTION_TYPES_B — Tipos de Ação de RH (Base)"
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
  - tipos-acao
  - action-types
aliases:
  - PER_ACTION_TYPES_B
  - per_action_types_b
  - per-action-types-b
  - tipos-de-ação-de-rh-(base)
  - per-action-types-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACTION_TYPES_B

## 📌 Visão Geral

Armazena a definição dos **tipos de ação de RH**. Tipos agrupam ações relacionadas em categorias macro (ex.: Movimentação, Desligamento, Benefícios).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados principais do registro, independente de idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação de ações** — agrupa ações em categorias para organização e relatórios.
- **Configuração de workflow** — tipos de ação podem ter fluxos de aprovação distintos.
- **Segurança** — controle de acesso por tipo de ação.
- **Relatórios** — agrupamento de movimentações por tipo.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de ação | — | 🟢 95% |
| 2 | ACTION_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do tipo de ação | — | 🟢 90% |
| 3 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Status | Se o tipo está ativo (Y/N) | — | 🟢 85% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de classificação de tipos de ação.

### Tabelas-filha (FK de saída)
- [[per_action_types_tl]] — via `ACTION_TYPE_ID` (traduções do tipo de ação de RH)
- [[per_actions_b]] — via `ACTION_TYPE_ID` (ações deste tipo)

---

## 📎 Uso Típico

### Tipos de ação ativos
```sql
SELECT pat.ACTION_TYPE_ID, pat.ACTION_TYPE_CODE
FROM   PER_ACTION_TYPES_B pat
WHERE  pat.ACTIVE_FLAG = 'Y';
```

### Filtros comuns
- `ACTIVE_FLAG = 'Y'` — Tipos ativos
---

## 🔒 Observações

- Tabela base (_B) — textos traduzidos ficam na tabela _TL correspondente.
- Tipos de ação são a classificação mais alta na hierarquia de ações.
- Exemplos comuns: HIRE_TYPE, SEPARATION_TYPE, ASSIGNMENT_CHANGE_TYPE.
---

## 📚 Referências

- [Oracle Docs — PER_ACTION_TYPES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peractiontypesb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
