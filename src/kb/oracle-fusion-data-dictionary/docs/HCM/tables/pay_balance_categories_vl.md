---
id: DOC-HCM-553
doc_type: system-doc
title: "PAY_BALANCE_CATEGORIES_VL — Categorias de Saldo (View Localizada)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - balance-categories-vl
  - view-localizada
  - pay-bal-cat-vl
aliases:
  - PAY_BALANCE_CATEGORIES_VL
  - pay_balance_categories_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_BALANCE_CATEGORIES_VL

## 📌 Visão Geral

**View localizada** (`_VL`) que combina `PAY_BALANCE_CATEGORIES_F` com `PAY_BALANCE_CATEGORIES_TL` no idioma da sessao do usuario. Facilita consultas sem necessidade de join explicito com a tabela de traducao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas simplificadas de categorias de saldo com traducao
- Uso em LOVs (List of Values) de interfaces
- Relatorios no idioma do usuario

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BALANCE_CATEGORY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da categoria | --- | 🟢 95% |
| 2 | CATEGORY_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome da categoria no idioma da sessao | --- | 🟢 90% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- --- View, sem filhas diretas

---

## 📎 Uso Típico

### Categorias de saldo com nome traduzido
```sql
SELECT vl.BALANCE_CATEGORY_ID, vl.CATEGORY_NAME
FROM   PAY_BALANCE_CATEGORIES_VL vl
WHERE  SYSDATE BETWEEN vl.EFFECTIVE_START_DATE AND vl.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Esta eh uma view (VL = View Localizada), nao uma tabela fisica.
- Retorna automaticamente o nome no idioma da sessao do usuario.
- Preferir esta view para consultas que necessitem nome traduzido.

---

## 🔗 PVOs Relacionados

### [[balancecategoriespvo|BalanceCategoriesPVO]] (GL · BICC: 83/83)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BALANCE_CATEGORY_ID | BalanceCategoriesPEOBalanceCategoryId | ✅ |
| BASE_BALANCE_CATEGORY_ID | BalanceCategoriesPEOBaseBalanceCategoryId | ✅ |
| BASE_CATEGORY_NAME | BalanceCategoriesPEOBaseCategoryName | ✅ |
| CREATED_BY | BalanceCategoriesPEOCreatedBy | ✅ |
| CREATION_DATE | BalanceCategoriesPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | BalanceCategoriesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | BalanceCategoriesPEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | BalanceCategoriesPEOEnterpriseId | ✅ |
| LAST_UPDATE_DATE | BalanceCategoriesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BalanceCategoriesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BalanceCategoriesPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | BalanceCategoriesPEOLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | BalanceCategoriesPEOLegislativeDataGroupId | ✅ |
| MODULE_ID | BalanceCategoriesPEOModuleId | ✅ |
| OBJECT_VERSION_NUMBER | BalanceCategoriesPEOObjectVersionNumber | ✅ |
| PBC_INFORMATION1 | BalanceCategoriesPEOPbcInformation1 | ✅ |
| PBC_INFORMATION10 | BalanceCategoriesPEOPbcInformation10 | ✅ |
| PBC_INFORMATION11 | BalanceCategoriesPEOPbcInformation11 | ✅ |
| PBC_INFORMATION12 | BalanceCategoriesPEOPbcInformation12 | ✅ |
| PBC_INFORMATION13 | BalanceCategoriesPEOPbcInformation13 | ✅ |
| PBC_INFORMATION14 | BalanceCategoriesPEOPbcInformation14 | ✅ |
| PBC_INFORMATION15 | BalanceCategoriesPEOPbcInformation15 | ✅ |
| PBC_INFORMATION16 | BalanceCategoriesPEOPbcInformation16 | ✅ |
| PBC_INFORMATION17 | BalanceCategoriesPEOPbcInformation17 | ✅ |
| PBC_INFORMATION18 | BalanceCategoriesPEOPbcInformation18 | ✅ |
| PBC_INFORMATION19 | BalanceCategoriesPEOPbcInformation19 | ✅ |
| PBC_INFORMATION2 | BalanceCategoriesPEOPbcInformation2 | ✅ |
| PBC_INFORMATION20 | BalanceCategoriesPEOPbcInformation20 | ✅ |
| PBC_INFORMATION21 | BalanceCategoriesPEOPbcInformation21 | ✅ |
| PBC_INFORMATION22 | BalanceCategoriesPEOPbcInformation22 | ✅ |
| PBC_INFORMATION23 | BalanceCategoriesPEOPbcInformation23 | ✅ |
| PBC_INFORMATION24 | BalanceCategoriesPEOPbcInformation24 | ✅ |
| PBC_INFORMATION25 | BalanceCategoriesPEOPbcInformation25 | ✅ |
| PBC_INFORMATION26 | BalanceCategoriesPEOPbcInformation26 | ✅ |
| PBC_INFORMATION27 | BalanceCategoriesPEOPbcInformation27 | ✅ |
| PBC_INFORMATION28 | BalanceCategoriesPEOPbcInformation28 | ✅ |
| PBC_INFORMATION29 | BalanceCategoriesPEOPbcInformation29 | ✅ |
| PBC_INFORMATION3 | BalanceCategoriesPEOPbcInformation3 | ✅ |
| PBC_INFORMATION30 | BalanceCategoriesPEOPbcInformation30 | ✅ |
| PBC_INFORMATION4 | BalanceCategoriesPEOPbcInformation4 | ✅ |
| PBC_INFORMATION5 | BalanceCategoriesPEOPbcInformation5 | ✅ |
| PBC_INFORMATION6 | BalanceCategoriesPEOPbcInformation6 | ✅ |
| PBC_INFORMATION7 | BalanceCategoriesPEOPbcInformation7 | ✅ |
| PBC_INFORMATION8 | BalanceCategoriesPEOPbcInformation8 | ✅ |
| PBC_INFORMATION9 | BalanceCategoriesPEOPbcInformation9 | ✅ |
| PBC_INFORMATION_CATEGORY | BalanceCategoriesPEOPbcInformationCategory | ✅ |
| PBC_INFORMATION_DATE1 | BalanceCategoriesPEOPbcInformationDate1 | ✅ |
| PBC_INFORMATION_DATE10 | BalanceCategoriesPEOPbcInformationDate10 | ✅ |
| PBC_INFORMATION_DATE11 | BalanceCategoriesPEOPbcInformationDate11 | ✅ |
| PBC_INFORMATION_DATE12 | BalanceCategoriesPEOPbcInformationDate12 | ✅ |
| PBC_INFORMATION_DATE13 | BalanceCategoriesPEOPbcInformationDate13 | ✅ |
| PBC_INFORMATION_DATE14 | BalanceCategoriesPEOPbcInformationDate14 | ✅ |
| PBC_INFORMATION_DATE15 | BalanceCategoriesPEOPbcInformationDate15 | ✅ |
| PBC_INFORMATION_DATE2 | BalanceCategoriesPEOPbcInformationDate2 | ✅ |
| PBC_INFORMATION_DATE3 | BalanceCategoriesPEOPbcInformationDate3 | ✅ |
| PBC_INFORMATION_DATE4 | BalanceCategoriesPEOPbcInformationDate4 | ✅ |
| PBC_INFORMATION_DATE5 | BalanceCategoriesPEOPbcInformationDate5 | ✅ |
| PBC_INFORMATION_DATE6 | BalanceCategoriesPEOPbcInformationDate6 | ✅ |
| PBC_INFORMATION_DATE7 | BalanceCategoriesPEOPbcInformationDate7 | ✅ |
| PBC_INFORMATION_DATE8 | BalanceCategoriesPEOPbcInformationDate8 | ✅ |
| PBC_INFORMATION_DATE9 | BalanceCategoriesPEOPbcInformationDate9 | ✅ |
| PBC_INFORMATION_NUMBER1 | BalanceCategoriesPEOPbcInformationNumber1 | ✅ |
| PBC_INFORMATION_NUMBER10 | BalanceCategoriesPEOPbcInformationNumber10 | ✅ |
| PBC_INFORMATION_NUMBER11 | BalanceCategoriesPEOPbcInformationNumber11 | ✅ |
| PBC_INFORMATION_NUMBER12 | BalanceCategoriesPEOPbcInformationNumber12 | ✅ |
| PBC_INFORMATION_NUMBER13 | BalanceCategoriesPEOPbcInformationNumber13 | ✅ |
| PBC_INFORMATION_NUMBER14 | BalanceCategoriesPEOPbcInformationNumber14 | ✅ |
| PBC_INFORMATION_NUMBER15 | BalanceCategoriesPEOPbcInformationNumber15 | ✅ |
| PBC_INFORMATION_NUMBER16 | BalanceCategoriesPEOPbcInformationNumber16 | ✅ |
| PBC_INFORMATION_NUMBER17 | BalanceCategoriesPEOPbcInformationNumber17 | ✅ |
| PBC_INFORMATION_NUMBER18 | BalanceCategoriesPEOPbcInformationNumber18 | ✅ |
| PBC_INFORMATION_NUMBER19 | BalanceCategoriesPEOPbcInformationNumber19 | ✅ |
| PBC_INFORMATION_NUMBER2 | BalanceCategoriesPEOPbcInformationNumber2 | ✅ |
| PBC_INFORMATION_NUMBER20 | BalanceCategoriesPEOPbcInformationNumber20 | ✅ |
| PBC_INFORMATION_NUMBER3 | BalanceCategoriesPEOPbcInformationNumber3 | ✅ |
| PBC_INFORMATION_NUMBER4 | BalanceCategoriesPEOPbcInformationNumber4 | ✅ |
| PBC_INFORMATION_NUMBER5 | BalanceCategoriesPEOPbcInformationNumber5 | ✅ |
| PBC_INFORMATION_NUMBER6 | BalanceCategoriesPEOPbcInformationNumber6 | ✅ |
| PBC_INFORMATION_NUMBER7 | BalanceCategoriesPEOPbcInformationNumber7 | ✅ |
| PBC_INFORMATION_NUMBER8 | BalanceCategoriesPEOPbcInformationNumber8 | ✅ |
| PBC_INFORMATION_NUMBER9 | BalanceCategoriesPEOPbcInformationNumber9 | ✅ |
| SAVE_RUN_BALANCE_ENABLED | BalanceCategoriesPEOSaveRunBalanceEnabled | ✅ |
| USER_CATEGORY_NAME | BalanceCategoriesPEOUserCategoryName | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_BALANCE_CATEGORIES_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paybalancecategoriesvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
