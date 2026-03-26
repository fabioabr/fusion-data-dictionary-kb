---
id: DOC-HCM-383
doc_type: system-doc
title: "HWM_TM_REC_GRP_USAGES — Usos de Grupos de Registros de Tempo"
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
  - time-management
  - record-group-usage
  - uso-grupo-registros
aliases:
  - HWM_TM_REC_GRP_USAGES
  - hwm_tm_rec_grp_usages
  - hwm-tm-rec-grp-usages
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REC_GRP_USAGES

## 📌 Visão Geral

Armazena as **associações entre grupos de registros e seus usos** (usages) no módulo Time Management. Define como cada grupo de registros de tempo é utilizado no processamento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Associação grupo-uso:** vincula grupos de registros a contextos de utilização.
- **Configuração de processamento:** define regras de uso por grupo.
- **Rastreabilidade:** permite auditar como cada grupo foi utilizado.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REC_GRP_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do uso | — | 🟡 70% |
| 2 | REC_GRP_ID | NUMBER(18) | NOT NULL | FK | Grupo de registros associado | HWM_TM_REC_GRP | 🟡 70% |
| 3 | USAGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de uso do grupo | — | 🟡 60% |
| 4 | USAGE_CONTEXT | VARCHAR2(240) | NULL | Dados | Contexto de utilização | — | 🟡 55% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_tm_rec_grp]] — via `REC_GRP_ID` (grupo de registros de tempo do uso)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Típico

### Usos de um grupo de registros
```sql
SELECT u.REC_GRP_USAGE_ID, u.USAGE_TYPE, u.USAGE_CONTEXT
FROM   HWM_TM_REC_GRP_USAGES u
WHERE  u.REC_GRP_ID = :p_grp_id;
```

### Filtros comuns
- `REC_GRP_ID = :p_grp_id — Filtrar por grupo`

---

## 🔒 Observações

- Tabela de associação entre grupos e seus contextos de uso.
- Utilizada internamente pelo engine de Time Management.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_REC_GRP_USAGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrecgrpusages.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
