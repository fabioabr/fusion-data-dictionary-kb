---
id: DOC-HCM-212
doc_type: system-doc
title: "HRR_TMPL_ANLYT_BOX_LBLS_B — Labels de Box Analítico (Base)"
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
  - talent-review
  - analytics
  - box-labels
aliases:
  - HRR_TMPL_ANLYT_BOX_LBLS_B
  - hrr_tmpl_anlyt_box_lbls_b
  - labels-de-box-analítico-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_TMPL_ANLYT_BOX_LBLS_B

## 📌 Visão Geral

Tabela base dos **labels (rótulos)** das caixas em análises tipo 9-Box.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rótulos do 9-Box:** Configuração de labels.
- **Personalização:** Labels customizáveis.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BOX_LABEL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | ANALYTIC_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo analítico | [[hrr_tmpl_analytic_types_b]] | 🟢 85% |
| 3 | BOX_POSITION | NUMBER | NOT NULL | Identificação | Posição (1-9) | — | 🟡 80% |
| 4 | ROW_INDEX | NUMBER | NULL | Identificação | Índice da linha | — | 🟡 70% |
| 5 | COLUMN_INDEX | NUMBER | NULL | Identificação | Índice da coluna | — | 🟡 70% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 11 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_tmpl_analytic_types_b]] — via `ANALYTIC_TYPE_ID` (tipo analitico do rotulo de box)

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Labels do 9-Box
```sql
SELECT bl.BOX_LABEL_ID, bl.BOX_POSITION, bl.ROW_INDEX, bl.COLUMN_INDEX
FROM   HRR_TMPL_ANLYT_BOX_LBLS_B bl
WHERE  bl.ANALYTIC_TYPE_ID = :p_id;
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrr_tmpl_anlyt_box_lbls_tl]].
Posições 1-9 correspondem ao layout do 9-Box.

---

## 🔗 PVOs Relacionados

### [[boxlabellookuppvo|BoxLabelLookupPVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_BOX_LABEL_ID | AnalyticBoxLabelId | — |
| ANALYTIC_TYPE_ID | TmplAnylBoxLblPEOAnalyticTypeId | — |
| BOX_SEQUENCE | BoxSequence | ✅ |
| BUSINESS_GROUP_ID | TmplAnylBoxLblPEOBusinessGroupId | — |
| CREATED_BY | TmplAnylBoxLblPEOCreatedBy | — |
| CREATION_DATE | TmplAnylBoxLblPEOCreationDate | — |
| LAST_UPDATE_DATE | TmplAnylBoxLblPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TmplAnylBoxLblPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TmplAnylBoxLblPEOLastUpdatedBy | — |
| MODULE_ID | TmplAnylBoxLblPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TmplAnylBoxLblPEOObjectVersionNumber | — |

### [[nboxlabelpvo|NBoxLabelPVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANALYTIC_BOX_LABEL_ID | AnalyticBoxLabelId | — |
| ANALYTIC_TYPE_ID | TmplAnylBoxLblPEOAnalyticTypeId | — |
| BOX_SEQUENCE | BoxSequence | ✅ |
| BUSINESS_GROUP_ID | TmplAnylBoxLblPEOBusinessGroupId | — |
| CREATED_BY | TmplAnylBoxLblPEOCreatedBy | — |
| CREATION_DATE | TmplAnylBoxLblPEOCreationDate | — |
| LAST_UPDATE_DATE | TmplAnylBoxLblPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TmplAnylBoxLblPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TmplAnylBoxLblPEOLastUpdatedBy | — |
| MODULE_ID | TmplAnylBoxLblPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TmplAnylBoxLblPEOObjectVersionNumber | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
