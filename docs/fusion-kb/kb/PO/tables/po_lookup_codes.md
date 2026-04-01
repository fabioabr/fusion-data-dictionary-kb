---
id: DOC-PO-138
doc_type: system-doc
title: "PO_LOOKUP_CODES — Codigos de Lookup de Compras"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - lookups
  - configuracao
  - reference-data
aliases:
  - PO_LOOKUP_CODES
  - po_lookup_codes
  - po-lookup-codes
  - po-lookup
  - codigos-de-lookup-de-compras
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LOOKUP_CODES

## 📌 Visão Geral

Armazena os **codigos de lookup** (tabelas de referencia) do modulo Procurement. Listas de valores pre-definidos para campos codificados.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reference data:** Valores permitidos para campos.
- **Validacao:** Integridade referencial.
- **LOVs:** Listas de selecao.
- **Customizacao:** Valores adicionais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOOKUP_TYPE | VARCHAR2(25) | NOT NULL | PK | Tipo do lookup | — | 🟢 95% |
| 2 | LOOKUP_CODE | VARCHAR2(25) | NOT NULL | PK | Codigo | — | 🟢 95% |
| 3 | DISPLAYED_FIELD | VARCHAR2(80) | NULL | Descritivo | Valor exibido | — | 🟢 90% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao | — | 🟢 90% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Flag | Habilitado | — | 🟢 90% |
| 6 | INACTIVE_DATE | DATE | NULL | Status | Data de inativacao | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta identificada

### Tabelas-filha (FK de saída)
- Diversas tabelas PO referenciam esta tabela

---

## 📎 Uso Típico

### Valores de um lookup
```sql
SELECT LOOKUP_CODE, DISPLAYED_FIELD, DESCRIPTION
FROM   PO_LOOKUP_CODES
WHERE  LOOKUP_TYPE = :p_type AND ENABLED_FLAG = 'Y'
  AND  (INACTIVE_DATE IS NULL OR INACTIVE_DATE > SYSDATE);
```

---

## 🔒 Observações

- PK composta: `LOOKUP_TYPE` + `LOOKUP_CODE`.
- Tipos comuns: AUTHORIZATION STATUS, DOCUMENT TYPE, CLOSED CODE.
- Valores seeded nao devem ser alterados.

---

## 🔗 PVOs Relacionados

### [[agreementstatuspurchasinglookuppvo|AgreementStatusPurchasingLookupPVO]] (PO · BICC: 5/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | PoLookupCreationDate | — |
| DESCRIPTION | PoLookupDescription | ✅ |
| DISPLAYED_FIELD | PoLookupDisplayedField | ✅ |
| ENABLED_FLAG | PoLookupEnabledFlag | — |
| END_DATE_ACTIVE | PoLookupEndDateActive | — |
| LAST_UPDATE_DATE | PoLookupLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PoLookupLastUpdateLogin | — |
| LAST_UPDATED_BY | PoLookupLastUpdatedBy | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| PROGRAM_APPLICATION_ID | PoLookupProgramApplicationId | — |
| PROGRAM_ID | PoLookupProgramId | — |
| PROGRAM_UPDATE_DATE | PoLookupProgramUpdateDate | — |
| REQUEST_ID | PoLookupRequestId | — |

### [[contractfulagrlookup|ContractFulAgrLookup]] (OTHER · BICC: 15/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| DISPLAYED_FIELD | DisplayedField | ✅ |
| ENABLED_FLAG | EnabledFlag | ✅ |
| END_DATE_ACTIVE | EndDateActive | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| PROGRAM_APPLICATION_ID | ProgramApplicationId | ✅ |
| PROGRAM_ID | ProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | ✅ |
| REQUEST_ID | RequestId | ✅ |

### [[contractfullinelookup|ContractFulLineLookup]] (OTHER · BICC: 15/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| DISPLAYED_FIELD | DisplayedField | ✅ |
| ENABLED_FLAG | EnabledFlag | ✅ |
| END_DATE_ACTIVE | EndDateActive | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| PROGRAM_APPLICATION_ID | ProgramApplicationId | ✅ |
| PROGRAM_ID | ProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | ✅ |
| REQUEST_ID | RequestId | ✅ |

### [[contractfullookup|ContractFulLookup]] (OTHER · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | ✅ |
| DISPLAYED_FIELD | DisplayedField | — |
| ENABLED_FLAG | EnabledFlag | — |
| END_DATE_ACTIVE | EndDateActive | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| PROGRAM_APPLICATION_ID | ProgramApplicationId | — |
| PROGRAM_ID | ProgramId | — |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | — |
| REQUEST_ID | RequestId | — |

### [[destinationtypepurchasinglookuppvo|DestinationTypePurchasingLookupPVO]] (PO · BICC: 6/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | PoLookupCreationDate | — |
| DESCRIPTION | PoLookupDescription | ✅ |
| DISPLAYED_FIELD | PoLookupDisplayedField | ✅ |
| ENABLED_FLAG | PoLookupEnabledFlag | — |
| END_DATE_ACTIVE | PoLookupEndDateActive | ✅ |
| LAST_UPDATE_DATE | PoLookupLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PoLookupLastUpdateLogin | — |
| LAST_UPDATED_BY | PoLookupLastUpdatedBy | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| PROGRAM_APPLICATION_ID | PoLookupProgramApplicationId | — |
| PROGRAM_ID | PoLookupProgramId | — |
| PROGRAM_UPDATE_DATE | PoLookupProgramUpdateDate | — |
| REQUEST_ID | PoLookupRequestId | — |

### [[orderstatuspurchasinglookuppvo|OrderStatusPurchasingLookupPVO]] (PO · BICC: 5/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | PoLookupCreationDate | — |
| DESCRIPTION | PoLookupDescription | ✅ |
| DISPLAYED_FIELD | PoLookupDisplayedField | ✅ |
| ENABLED_FLAG | PoLookupEnabledFlag | — |
| END_DATE_ACTIVE | PoLookupEndDateActive | — |
| LAST_UPDATE_DATE | PoLookupLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PoLookupLastUpdateLogin | — |
| LAST_UPDATED_BY | PoLookupLastUpdatedBy | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| PROGRAM_APPLICATION_ID | PoLookupProgramApplicationId | — |
| PROGRAM_ID | PoLookupProgramId | — |
| PROGRAM_UPDATE_DATE | PoLookupProgramUpdateDate | — |
| REQUEST_ID | PoLookupRequestId | — |

### [[payoncodepurchasinglookuppvo|PayOnCodePurchasingLookupPVO]] (PO · BICC: 5/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | PoLookupCreationDate | — |
| DESCRIPTION | PoLookupDescription | ✅ |
| DISPLAYED_FIELD | PoLookupDisplayedField | — |
| ENABLED_FLAG | PoLookupEnabledFlag | — |
| END_DATE_ACTIVE | PoLookupEndDateActive | ✅ |
| LAST_UPDATE_DATE | PoLookupLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PoLookupLastUpdateLogin | — |
| LAST_UPDATED_BY | PoLookupLastUpdatedBy | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| PROGRAM_APPLICATION_ID | PoLookupProgramApplicationId | — |
| PROGRAM_ID | PoLookupProgramId | — |
| PROGRAM_UPDATE_DATE | PoLookupProgramUpdateDate | — |
| REQUEST_ID | PoLookupRequestId | — |

### [[poinvmatchoptionpurchasinglookuppvo|PoInvMatchOptionPurchasingLookupPVO]] (PO · BICC: 5/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | PoLookupCreationDate | — |
| DESCRIPTION | PoLookupDescription | ✅ |
| DISPLAYED_FIELD | PoLookupDisplayedField | — |
| ENABLED_FLAG | PoLookupEnabledFlag | — |
| END_DATE_ACTIVE | PoLookupEndDateActive | ✅ |
| LAST_UPDATE_DATE | PoLookupLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PoLookupLastUpdateLogin | — |
| LAST_UPDATED_BY | PoLookupLastUpdatedBy | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| PROGRAM_APPLICATION_ID | PoLookupProgramApplicationId | — |
| PROGRAM_ID | PoLookupProgramId | — |
| PROGRAM_UPDATE_DATE | PoLookupProgramUpdateDate | — |
| REQUEST_ID | PoLookupRequestId | — |

### [[rolepurchasinglookuppvo|RolePurchasingLookupPVO]] (PO · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | PoLookupCreationDate | — |
| DESCRIPTION | PoLookupDescription | — |
| DISPLAYED_FIELD | PoLookupDisplayedField | ✅ |
| ENABLED_FLAG | PoLookupEnabledFlag | — |
| END_DATE_ACTIVE | PoLookupEndDateActive | — |
| LAST_UPDATE_DATE | PoLookupLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PoLookupLastUpdateLogin | — |
| LAST_UPDATED_BY | PoLookupLastUpdatedBy | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| PROGRAM_APPLICATION_ID | PoLookupProgramApplicationId | — |
| PROGRAM_ID | PoLookupProgramId | — |
| PROGRAM_UPDATE_DATE | PoLookupProgramUpdateDate | — |
| REQUEST_ID | PoLookupRequestId | — |

---

## 📚 Referências

- [Oracle Docs — PO_LOOKUP_CODES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/polookupcodess-10195.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
