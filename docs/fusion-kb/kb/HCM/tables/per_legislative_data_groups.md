---
id: DOC-HCM-673
doc_type: system-doc
title: "PER_LEGISLATIVE_DATA_GROUPS — Grupos de Dados Legislativos"
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
  - ldg
  - legislative-data-groups
aliases:
  - PER_LEGISLATIVE_DATA_GROUPS
  - per_legislative_data_groups
  - per-legislative-data-groups
  - grupos-de-dados-legislativos
  - per-legislative-data
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_LEGISLATIVE_DATA_GROUPS

## 📌 Visão Geral

Armazena os **grupos de dados legislativos (LDG)** que definem o contexto legal/trabalhista no Oracle HCM. Cada LDG agrupa dados sob uma legislação específica e uma moeda, sendo a base para segmentação legal de dados de payroll e RH.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Segmentação legal** — agrupa entidades sob uma legislação específica.
- **Moeda** — define a moeda principal para dados financeiros do grupo.
- **Payroll** — cada payroll está associado a um LDG.
- **Multi-legislação** — suporta operações em múltiplos países com legislações diferentes.
- **Compliance** — garante que regras corretas sejam aplicadas por jurisdição.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do LDG | — | 🟢 95% |
| 2 | LEGISLATION_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da legislação (BR, US, etc.) | — | 🟢 95% |
| 3 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Configuração | Moeda do grupo (BRL, USD, etc.) | — | 🟢 90% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do LDG | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de grupos legislativos.

### Tabelas-filha (FK de saída)
- [[per_legislative_data_groups_tl]] — via `LEGISLATIVE_DATA_GROUP_ID` (traduções do grupo de dados legislativos)

---

## 📎 Uso Típico

### Grupos de dados legislativos
```sql
SELECT pldg.LEGISLATIVE_DATA_GROUP_ID, pldg.NAME,
       pldg.LEGISLATION_CODE, pldg.CURRENCY_CODE
FROM   PER_LEGISLATIVE_DATA_GROUPS pldg
ORDER BY pldg.LEGISLATION_CODE;
```

### Filtros comuns
- `LEGISLATION_CODE = 'BR'` — LDG para legislação brasileira
---

## 🔒 Observações

- O LDG é um conceito central no Oracle HCM — define o contexto legal e de moeda.
- Cada payroll deve estar associado a um LDG.
- No Brasil, tipicamente há um LDG com `LEGISLATION_CODE = 'BR'` e `CURRENCY_CODE = 'BRL'`.
- Operações multinacionais terão múltiplos LDGs (um por país/legislação).
---

## 🔗 PVOs Relacionados

### [[legislativedatagrouppvo|LegislativeDataGroupPVO]] (GL · BICC: 8/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | LegislativeDataGroupPEOBusinessGroupId | — |
| COST_ALLOCATION_ID_FLEX_NUM | LegislativeDataGroupPEOCostAllocationIdFlexNum | ✅ |
| CREATED_BY | LegislativeDataGroupPEOCreatedBy | ✅ |
| CREATION_DATE | LegislativeDataGroupPEOCreationDate | ✅ |
| DEFAULT_CURRENCY_CODE | LegislativeDataGroupPEODefaultCurrencyCode | ✅ |
| LAST_UPDATE_DATE | LegislativeDataGroupPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LegislativeDataGroupPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LegislativeDataGroupPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislativeDataGroupPEOLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | ✅ |
| OBJECT_VERSION_NUMBER | LegislativeDataGroupPEOObjectVersionNumber | — |

### [[payrollruncosting|PayrollRunCosting]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COST_ALLOCATION_ID_FLEX_NUM | LdgPEOCostAllocationIdFlexNum | — |
| LEGISLATIVE_DATA_GROUP_ID | LdgPEOLegislativeDataGroupId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[prepaymentcosting|PrePaymentCosting]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COST_ALLOCATION_ID_FLEX_NUM | LdgPEOCostAllocationIdFlexNum | — |
| LEGISLATIVE_DATA_GROUP_ID | LdgPEOLegislativeDataGroupId | — |

---

## 📚 Referências

- [Oracle Docs — PER_LEGISLATIVE_DATA_GROUPS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perlegislativedatagroups.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
