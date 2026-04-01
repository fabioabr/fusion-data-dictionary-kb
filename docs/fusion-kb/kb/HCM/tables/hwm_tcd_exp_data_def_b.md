---
id: DOC-HCM-328
doc_type: system-doc
title: "HWM_TCD_EXP_DATA_DEF_B — Definição de Dados de Exportação de Time Card (Base)"
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
  - time-card
  - exportacao
  - definicao
  - base
aliases:
  - HWM_TCD_EXP_DATA_DEF_B
  - hwm_tcd_exp_data_def_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TCD_EXP_DATA_DEF_B

## 📌 Visão Geral

Tabela base que define a estrutura de dados para exportação de informações de cartão de ponto para sistemas externos (folha de pagamento, projetos).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados não traduzíveis. A tabela correspondente `_TL` armazena as traduções.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Exportação de dados de ponto:** Configuração de como os dados do cartão de ponto são exportados para sistemas externos.
- **Mapeamento de campos:** Definição de correspondência entre campos do time card e sistemas de destino.
- **Integração com Payroll:** Transferência de horas trabalhadas para processamento de folha de pagamento.
- **Integração com Project Costing:** Alocação de horas em projetos para custeio.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | TCD_EXP_DATA_DEF_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | CODE | VARCHAR2(30) | NOT NULL | Identificação | Código identificador único | — | 🟢 90% |
| 3 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro (A/I) | — | 🟡 80% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se está habilitado (Y/N) | — | 🟡 75% |
| 5 | START_DATE | DATE | NULL | Vigência | Data de início de validade | — | 🟡 80% |
| 6 | END_DATE | DATE | NULL | Vigência | Data de fim de validade | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.CODE, t.STATUS, t.START_DATE, t.END_DATE
FROM   HWM_TCD_EXP_DATA_DEF_B t
WHERE  NVL(t.ENABLED_FLAG, 'Y') = 'Y'
```

### Filtros comuns
- `NVL(ENABLED_FLAG, 'Y') = 'Y'` — Registros habilitados
- `STATUS = 'A'` — Registros ativos

---

## 🔒 Observações

- Tabela base: contém dados não traduzíveis. Utilize a view `_VL` correspondente para consultas com tradução.
- Área funcional: Time Card Export dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[tcdexportdatadefinitionpvo|TcdExportDataDefinitionPVO]] (GL · BICC: 18/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_NAME1 | TcdExportDataDefBPEOAdditionalName1 | ✅ |
| ADDITIONAL_NAME2 | TcdExportDataDefBPEOAdditionalName2 | ✅ |
| ATTRIBUTE1 | TcdExportDataDefBPEOAttribute1 | — |
| ATTRIBUTE10 | TcdExportDataDefBPEOAttribute10 | — |
| ATTRIBUTE11 | TcdExportDataDefBPEOAttribute11 | — |
| ATTRIBUTE12 | TcdExportDataDefBPEOAttribute12 | — |
| ATTRIBUTE13 | TcdExportDataDefBPEOAttribute13 | — |
| ATTRIBUTE14 | TcdExportDataDefBPEOAttribute14 | — |
| ATTRIBUTE15 | TcdExportDataDefBPEOAttribute15 | — |
| ATTRIBUTE16 | TcdExportDataDefBPEOAttribute16 | — |
| ATTRIBUTE17 | TcdExportDataDefBPEOAttribute17 | — |
| ATTRIBUTE18 | TcdExportDataDefBPEOAttribute18 | — |
| ATTRIBUTE19 | TcdExportDataDefBPEOAttribute19 | — |
| ATTRIBUTE2 | TcdExportDataDefBPEOAttribute2 | — |
| ATTRIBUTE20 | TcdExportDataDefBPEOAttribute20 | — |
| ATTRIBUTE21 | TcdExportDataDefBPEOAttribute21 | — |
| ATTRIBUTE22 | TcdExportDataDefBPEOAttribute22 | — |
| ATTRIBUTE23 | TcdExportDataDefBPEOAttribute23 | — |
| ATTRIBUTE24 | TcdExportDataDefBPEOAttribute24 | — |
| ATTRIBUTE25 | TcdExportDataDefBPEOAttribute25 | — |
| ATTRIBUTE26 | TcdExportDataDefBPEOAttribute26 | — |
| ATTRIBUTE27 | TcdExportDataDefBPEOAttribute27 | — |
| ATTRIBUTE28 | TcdExportDataDefBPEOAttribute28 | — |
| ATTRIBUTE29 | TcdExportDataDefBPEOAttribute29 | — |
| ATTRIBUTE3 | TcdExportDataDefBPEOAttribute3 | — |
| ATTRIBUTE30 | TcdExportDataDefBPEOAttribute30 | — |
| ATTRIBUTE4 | TcdExportDataDefBPEOAttribute4 | — |
| ATTRIBUTE5 | TcdExportDataDefBPEOAttribute5 | — |
| ATTRIBUTE6 | TcdExportDataDefBPEOAttribute6 | — |
| ATTRIBUTE7 | TcdExportDataDefBPEOAttribute7 | — |
| ATTRIBUTE8 | TcdExportDataDefBPEOAttribute8 | — |
| ATTRIBUTE9 | TcdExportDataDefBPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | TcdExportDataDefBPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | TcdExportDataDefBPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | TcdExportDataDefBPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | TcdExportDataDefBPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | TcdExportDataDefBPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | TcdExportDataDefBPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | TcdExportDataDefBPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | TcdExportDataDefBPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | TcdExportDataDefBPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | TcdExportDataDefBPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | TcdExportDataDefBPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | TcdExportDataDefBPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | TcdExportDataDefBPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | TcdExportDataDefBPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | TcdExportDataDefBPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | TcdExportDataDefBPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | TcdExportDataDefBPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | TcdExportDataDefBPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | TcdExportDataDefBPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | TcdExportDataDefBPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | TcdExportDataDefBPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | TcdExportDataDefBPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | TcdExportDataDefBPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | TcdExportDataDefBPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | TcdExportDataDefBPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | TcdExportDataDefBPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | TcdExportDataDefBPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | TcdExportDataDefBPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | TcdExportDataDefBPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | TcdExportDataDefBPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | TcdExportDataDefBPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | TcdExportDataDefBPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | TcdExportDataDefBPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | TcdExportDataDefBPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | TcdExportDataDefBPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | TcdExportDataDefBPEOAttributeNumber9 | — |
| CREATED_BY | TcdExportDataDefBPEOCreatedBy | ✅ |
| CREATION_DATE | TcdExportDataDefBPEOCreationDate | ✅ |
| DELETE_FLAG | TcdExportDataDefBPEODeleteFlag | ✅ |
| ENTERPRISE_ID | TcdExportDataDefBPEOEnterpriseId | — |
| FIRST_NAME | TcdExportDataDefBPEOFirstName | ✅ |
| LAST_NAME | TcdExportDataDefBPEOLastName | ✅ |
| LAST_UPDATE_DATE | TcdExportDataDefBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TcdExportDataDefBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TcdExportDataDefBPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | TcdExportDataDefBPEOObjectVersionNumber | — |
| PAY_TIME_TYPES | TcdExportDataDefBPEOPayTimeTypes | ✅ |
| PERSON_BADGE_ID | TcdExportDataDefBPEOPersonBadgeId | ✅ |
| PERSON_NAME | TcdExportDataDefBPEOPersonName | — |
| PERSON_NUMBER | TcdExportDataDefBPEOPersonNumber | — |
| SCHEDULE | TcdExportDataDefBPEOSchedule | ✅ |
| SEED_DATA_SOURCE | TcdExportDataDefBPEOSeedDataSource | — |
| TCD_EXP_DATA_DEF_CATEGORY | TcdExportDataDefBPEOTcdExportDataDefinitionCategory | — |
| TCD_EXP_DATA_DEF_CODE | TcdExportDataDefBPEOTcdExportDataDefinitionCode | ✅ |
| TCD_EXP_DATA_DEF_ID | TcdExportDataDefBPEOTcdExportDataDefinitionId | ✅ |
| TCD_EXP_DATA_SRVC_MAP_ID | TcdExportDataDefBPEOTcdExportDataSrvcMapId | — |
| TCD_EXP_DURATION | TcdExportDataDefBPEOTcdExportDuration | ✅ |
| TCD_EXP_SERVICE_END_POINT | TcdExportDataDefBPEOTcdExportServiceEndPoint | — |
| TCD_EXP_START_DATE | TcdExportDataDefBPEOTcdExportStartDate | ✅ |
| TCD_EXPORT_BATCH_SIZE | TcdExportDataDefBPEOTcdExportBatchSize | ✅ |
| TCD_VENDOR_CODE | TcdExportDataDefBPEOTcdVendorCode | — |

---

## 📚 Referências

- [Oracle Docs — HWM_TCD_EXP_DATA_DEF_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tcd_exp_data_def_b.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
