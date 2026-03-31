---
id: DOC-HCM-048
doc_type: system-doc
title: "BEN_PER_BILL_INFO_F — Informações de Cobrança por Pessoa"
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
  - benefits
  - info-cobranca-pessoa
  - person-bill-info
aliases:
  - BEN_PER_BILL_INFO_F
  - ben_per_bill_info_f
  - info-cobranca-pessoa
  - person-bill-info
  - ben-per-bill-info
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PER_BILL_INFO_F

## 📌 Visão Geral

Armazena as **informações de cobrança** por pessoa para o sistema de billing de benefícios (endereço de cobrança, método de pagamento preferencial, etc.).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Dados de cobrança:** Informações específicas de billing por participante.
- **Método de pagamento:** Preferências de pagamento do colaborador.
- **Correspondência:** Endereço para envio de boletos/extratos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador | [[per_all_people_f]] | 🟡 80% |
| 3 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 4 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 5 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 6 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (quando aplicável)

### Tabelas-filha (FK de saída)
- Consultar documentação Oracle para tabelas-filha específicas.

---

## 📎 Uso Típico

### Consulta de informações de cobrança por pessoa
```sql
SELECT * FROM BEN_PER_BILL_INFO_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Informações de Cobrança por Pessoa).

---

## 🔗 PVOs Relacionados

### [[billchargedetailspvo|BillChargeDetailsPVO]] (HCM · BICC: 16/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | AddressLine1 | ✅ |
| ADDRESS_LINE2 | AddressLine2 | ✅ |
| ADDRESS_LINE3 | AddressLine3 | ✅ |
| ADDRESS_LINE4 | AddressLine4 | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| CITY | City | ✅ |
| COMMENTS | Comments1 | ✅ |
| CONFIG_CHAR_1 | ConfigChar12 | — |
| CONFIG_CHAR_2 | ConfigChar22 | — |
| CONFIG_CHAR_3 | ConfigChar32 | — |
| CONFIG_CHAR_4 | ConfigChar42 | — |
| CONFIG_CHAR_5 | ConfigChar52 | — |
| CONFIG_DATE_1 | ConfigDate12 | — |
| CONFIG_DATE_2 | ConfigDate22 | — |
| CONFIG_DATE_3 | ConfigDate32 | — |
| CONFIG_DATE_4 | ConfigDate42 | — |
| CONFIG_DATE_5 | ConfigDate52 | — |
| CONFIG_NUM_1 | ConfigNum12 | — |
| CONFIG_NUM_2 | ConfigNum22 | — |
| CONFIG_NUM_3 | ConfigNum32 | — |
| CONFIG_NUM_4 | ConfigNum42 | — |
| CONFIG_NUM_5 | ConfigNum52 | — |
| COUNTRY | Country | ✅ |
| CREATED_BY | CreatedBy2 | — |
| CREATION_DATE | CreationDate2 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PBI_ATTRIBUTE1 | PbiAttribute1 | — |
| PBI_ATTRIBUTE10 | PbiAttribute10 | — |
| PBI_ATTRIBUTE2 | PbiAttribute2 | — |
| PBI_ATTRIBUTE3 | PbiAttribute3 | — |
| PBI_ATTRIBUTE4 | PbiAttribute4 | — |
| PBI_ATTRIBUTE5 | PbiAttribute5 | — |
| PBI_ATTRIBUTE6 | PbiAttribute6 | — |
| PBI_ATTRIBUTE7 | PbiAttribute7 | — |
| PBI_ATTRIBUTE8 | PbiAttribute8 | — |
| PBI_ATTRIBUTE9 | PbiAttribute9 | — |
| PBI_ATTRIBUTE_CATEGORY | PbiAttributeCategory | — |
| PBI_ATTRIBUTE_DATE1 | PbiAttributeDate1 | — |
| PBI_ATTRIBUTE_DATE2 | PbiAttributeDate2 | — |
| PBI_ATTRIBUTE_DATE3 | PbiAttributeDate3 | — |
| PBI_ATTRIBUTE_DATE4 | PbiAttributeDate4 | — |
| PBI_ATTRIBUTE_DATE5 | PbiAttributeDate5 | — |
| PBI_ATTRIBUTE_NUMBER1 | PbiAttributeNumber1 | — |
| PBI_ATTRIBUTE_NUMBER2 | PbiAttributeNumber2 | — |
| PBI_ATTRIBUTE_NUMBER3 | PbiAttributeNumber3 | — |
| PBI_ATTRIBUTE_NUMBER4 | PbiAttributeNumber4 | — |
| PBI_ATTRIBUTE_NUMBER5 | PbiAttributeNumber5 | — |
| PER_ACCT_NUM | PerAcctNum1 | ✅ |
| PER_BILL_INFO_ID | PerBillInfoId1 | — |
| PERSON_ID | PersonId1 | — |
| PREF_COMM_MODE | PrefCommMode | — |
| PRMRY_EMAIL_ID | PrmryEmailId | ✅ |
| PRMRY_MAIL_ADDRESS_ID | PrmryMailAddressId | ✅ |
| STATE | State | ✅ |
| STOP_BILL_FLAG | StopBillFlag | ✅ |
| ZIP_CODE | ZipCode | ✅ |

### [[billchargespvo|BillChargesPVO]] (HCM · BICC: 15/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | AddressLine1 | ✅ |
| ADDRESS_LINE2 | AddressLine2 | ✅ |
| ADDRESS_LINE3 | AddressLine3 | ✅ |
| ADDRESS_LINE4 | AddressLine4 | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CITY | City | ✅ |
| COMMENTS | Comments1 | ✅ |
| CONFIG_CHAR_1 | ConfigChar11 | — |
| CONFIG_CHAR_2 | ConfigChar21 | — |
| CONFIG_CHAR_3 | ConfigChar31 | — |
| CONFIG_CHAR_4 | ConfigChar41 | — |
| CONFIG_CHAR_5 | ConfigChar51 | — |
| CONFIG_DATE_1 | ConfigDate11 | — |
| CONFIG_DATE_2 | ConfigDate21 | — |
| CONFIG_DATE_3 | ConfigDate31 | — |
| CONFIG_DATE_4 | ConfigDate41 | — |
| CONFIG_DATE_5 | ConfigDate51 | — |
| CONFIG_NUM_1 | ConfigNum11 | — |
| CONFIG_NUM_2 | ConfigNum21 | — |
| CONFIG_NUM_3 | ConfigNum31 | — |
| CONFIG_NUM_4 | ConfigNum41 | — |
| CONFIG_NUM_5 | ConfigNum51 | — |
| COUNTRY | Country | ✅ |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PBI_ATTRIBUTE1 | PbiAttribute1 | — |
| PBI_ATTRIBUTE10 | PbiAttribute10 | — |
| PBI_ATTRIBUTE2 | PbiAttribute2 | — |
| PBI_ATTRIBUTE3 | PbiAttribute3 | — |
| PBI_ATTRIBUTE4 | PbiAttribute4 | — |
| PBI_ATTRIBUTE5 | PbiAttribute5 | — |
| PBI_ATTRIBUTE6 | PbiAttribute6 | — |
| PBI_ATTRIBUTE7 | PbiAttribute7 | — |
| PBI_ATTRIBUTE8 | PbiAttribute8 | — |
| PBI_ATTRIBUTE9 | PbiAttribute9 | — |
| PBI_ATTRIBUTE_CATEGORY | PbiAttributeCategory | — |
| PBI_ATTRIBUTE_DATE1 | PbiAttributeDate1 | — |
| PBI_ATTRIBUTE_DATE2 | PbiAttributeDate2 | — |
| PBI_ATTRIBUTE_DATE3 | PbiAttributeDate3 | — |
| PBI_ATTRIBUTE_DATE4 | PbiAttributeDate4 | — |
| PBI_ATTRIBUTE_DATE5 | PbiAttributeDate5 | — |
| PBI_ATTRIBUTE_NUMBER1 | PbiAttributeNumber1 | — |
| PBI_ATTRIBUTE_NUMBER2 | PbiAttributeNumber2 | — |
| PBI_ATTRIBUTE_NUMBER3 | PbiAttributeNumber3 | — |
| PBI_ATTRIBUTE_NUMBER4 | PbiAttributeNumber4 | — |
| PBI_ATTRIBUTE_NUMBER5 | PbiAttributeNumber5 | — |
| PER_ACCT_NUM | PerAcctNum1 | — |
| PER_BILL_INFO_ID | PerBillInfoId1 | — |
| PERSON_ID | PersonId1 | — |
| PREF_COMM_MODE | PrefCommMode | — |
| PRMRY_EMAIL_ID | PrmryEmailId | ✅ |
| PRMRY_MAIL_ADDRESS_ID | PrmryMailAddressId | ✅ |
| STATE | State | ✅ |
| STOP_BILL_FLAG | StopBillFlag | ✅ |
| ZIP_CODE | ZipCode | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_PER_BILL_INFO_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benperbillinfof.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
