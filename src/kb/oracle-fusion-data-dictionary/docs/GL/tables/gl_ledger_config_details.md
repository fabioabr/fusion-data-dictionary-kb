---
id: DOC-GL-028
doc_type: system-doc
title: "GL_LEDGER_CONFIG_DETAILS — Detalhes de Configuração dos Ledgers"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - ledger-config
  - configuracao
  - setup
aliases:
  - GL_LEDGER_CONFIG_DETAILS
  - gl_ledger_config_details
  - config-ledger
  - ledger-configuration
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_LEDGER_CONFIG_DETAILS

## 📌 Visão Geral

Armazena os **detalhes de configuração dos ledgers** no General Ledger. Esta tabela complementa [[gl_ledgers]] com informações granulares sobre a configuração de cada ledger, incluindo detalhes de secondary ledgers, reporting currencies e opções de configuração avançada. Cada registro representa um detalhe específico dentro de uma configuração de ledger.

> [!note] Tabela de configuração avançada
> Esta tabela contém detalhes granulares da configuração do ledger. Modificações diretas não são recomendadas — usar a UI do Oracle Fusion (Accounting Configuration).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Setup de ledgers:** Armazena parâmetros de configuração detalhados para cada ledger.
- **Multi-book:** Configuração da relação entre primary e secondary ledgers.
- **Reporting currencies:** Detalhes de configuração de moedas de reporte (ALC).
- **Subledger Accounting:** Parâmetros de método contábil por ledger.
- **Auditoria de setup:** Verificação de como cada ledger foi configurado.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONFIGURATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da configuração | — | 🟢 90% |
| 2 | CONFIGURATION_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador do detalhe de configuração | — | 🟡 80% |
| 3 | OBJECT_ID | NUMBER(18) | NOT NULL | FK | ID do objeto associado (ledger, reporting currency etc.) | [[gl_ledgers]] | 🟡 80% |
| 4 | OBJECT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de objeto: PRIMARY, SECONDARY, ALC | — | 🟡 80% |
| 5 | SETUP_STEP_CODE | VARCHAR2(30) | NULL | Classificação | Código do passo de setup (ex: ASSIGN_LEGAL_ENTITIES, ASSIGN_BALANCING_SEGMENT_VALUES) | — | 🟡 75% |
| 6 | NEXT_SETUP_STEP_CODE | VARCHAR2(30) | NULL | Classificação | Próximo passo de setup na sequência | — | 🟡 70% |
| 7 | CONFIGURATION_STATUS_CODE | VARCHAR2(30) | NULL | Controle | Status da configuração: NOT_STARTED, IN_PROGRESS, COMPLETED | — | 🟡 75% |
| 8 | ACCOUNTING_METHOD_CODE | VARCHAR2(30) | NULL | Classificação | Método contábil atribuído (Standard Accrual etc.) | — | 🟡 80% |
| 9 | ACCOUNTING_METHOD_TYPE_CODE | VARCHAR2(30) | NULL | Classificação | Tipo do método contábil | — | 🟡 75% |
| 10 | CURRENCY_CODE | VARCHAR2(15) | NULL | Classificação | Moeda associada a este detalhe de configuração | — | 🟡 80% |
| 11 | CHART_OF_ACCOUNTS_ID | NUMBER(18) | NULL | FK | ID do plano de contas associado | — | 🟡 80% |
| 12 | PERIOD_SET_NAME | VARCHAR2(15) | NULL | FK | Nome do calendário contábil | — | 🟡 80% |
| 13 | PERIOD_TYPE | VARCHAR2(15) | NULL | Classificação | Tipo de período (Month) | — | 🟡 75% |
| 14 | MAX_ROLL_FWD_PERIOD_NUM | NUMBER | NULL | Controle | Número máximo de períodos para roll forward | — | 🟡 65% |
| 15 | SOURCE_LEDGER_ID | NUMBER(18) | NULL | FK | ID do ledger de origem (para secondary/ALC) | [[gl_ledgers]] | 🟡 80% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `OBJECT_ID` / `SOURCE_LEDGER_ID` (ledger configurado)

### Tabelas-filha (FK de saída)
- [[gl_ledgers]] — via `CONFIGURATION_ID` (ledgers que usam esta configuração)

---

## 📎 Uso Típico

### Listar configurações de ledgers
```sql
SELECT lcd.CONFIGURATION_ID,
       lcd.OBJECT_TYPE_CODE,
       gl.NAME AS ledger_name,
       lcd.CONFIGURATION_STATUS_CODE,
       lcd.ACCOUNTING_METHOD_CODE,
       lcd.CURRENCY_CODE
FROM   GL_LEDGER_CONFIG_DETAILS lcd
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = lcd.OBJECT_ID
ORDER BY lcd.CONFIGURATION_ID, lcd.OBJECT_TYPE_CODE;
```

### Verificar status de setup dos ledgers
```sql
SELECT lcd.CONFIGURATION_ID,
       gl.NAME AS ledger_name,
       lcd.SETUP_STEP_CODE,
       lcd.CONFIGURATION_STATUS_CODE
FROM   GL_LEDGER_CONFIG_DETAILS lcd
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = lcd.OBJECT_ID
WHERE  lcd.CONFIGURATION_STATUS_CODE != 'COMPLETED'
ORDER BY lcd.CONFIGURATION_ID;
```

### Filtros comuns
- `OBJECT_TYPE_CODE = 'PRIMARY'` — Configuração do primary ledger
- `OBJECT_TYPE_CODE = 'SECONDARY'` — Configuração de secondary ledgers
- `CONFIGURATION_STATUS_CODE = 'COMPLETED'` — Configurações finalizadas
- `CONFIGURATION_STATUS_CODE != 'COMPLETED'` — Configurações pendentes

---

## 🔒 Observações

- Esta tabela é gerada e mantida pelo wizard de Accounting Configuration do Oracle Fusion — não deve ser alterada diretamente.
- Cada `CONFIGURATION_ID` agrupa todos os detalhes de uma configuração de ledger (primary + secondary + ALC).
- O `SETUP_STEP_CODE` indica qual etapa do wizard gerou cada registro — útil para debugging de problemas de configuração.
- `SOURCE_LEDGER_ID` é preenchido apenas para secondary ledgers e reporting currencies, indicando o primary ledger de origem.
- Alterações na configuração de um ledger em produção são operações de alto impacto e devem ser planejadas com cuidado.

---

## 🔗 PVOs Relacionados

### [[ledgerconfigdetailextractpvo|LedgerConfigDetailExtractPVO]] (OTHER · BICC: 15/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONFIGURATION_ID | GLConfigDetailsConfigurationId | ✅ |
| CREATED_BY | GLConfigDetailsCreatedBy | ✅ |
| CREATION_DATE | GLConfigDetailsCreationDate | ✅ |
| LAST_UPDATE_DATE | GLConfigDetailsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GLConfigDetailsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GLConfigDetailsLastUpdatedBy | ✅ |
| NEXT_ACTION_CODE | GLConfigDetailsNextActionCode | ✅ |
| OBJECT_ID | GLConfigDetailsObjectId | ✅ |
| OBJECT_NAME | GLConfigDetailsObjectName | ✅ |
| OBJECT_TYPE_CODE | GLConfigDetailsObjectTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | GLConfigDetailsObjectVersionNumber | ✅ |
| SETUP_STEP_CODE | GLConfigDetailsSetupStepCode | ✅ |
| STATUS_CODE | GLConfigDetailsStatusCode | ✅ |
| TAX_DEFAULT_LE_FLAG | GLConfigDetailsTaxDefaultLeFlag | ✅ |
| TIME_ZONE_DEFAULT_LE_FLAG | GLConfigDetailsTimeZoneDefaultLeFlag | ✅ |

### [[legalentitybalancingsegmentvaluespvo|LegalEntityBalancingSegmentValuesPVO]] (GL · BICC: 5/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONFIGURATION_ID | ConfigurationId | ✅ |
| CONFIGURATION_ID | LeLedgerConfigDtlsConfigurationId | — |
| CREATED_BY | GlLedgerConfigDetailsCreatedBy | — |
| CREATED_BY | LeLedgerConfigDtlsCreatedBy | — |
| LAST_UPDATE_LOGIN | GlLedgerConfigDetailsLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | LeLedgerConfigDtlsLastUpdateLogin | — |
| LAST_UPDATED_BY | GlLedgerConfigDetailsLastUpdatedBy | — |
| LAST_UPDATED_BY | LeLedgerConfigDtlsLastUpdatedBy | — |
| NEXT_ACTION_CODE | GlLedgerConfigDetailsNextActionCode | — |
| NEXT_ACTION_CODE | LeLedgerConfigDtlsNextActionCode | — |
| OBJECT_ID | LeLedgerConfigDtlsObjectId | ✅ |
| OBJECT_ID | ObjectId | ✅ |
| OBJECT_NAME | GlLedgerConfigDetailsObjectName | — |
| OBJECT_NAME | LeLedgerConfigDtlsObjectName | — |
| OBJECT_TYPE_CODE | LeLedgerConfigDtlsObjectTypeCode | — |
| OBJECT_TYPE_CODE | ObjectTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | GlLedgerConfigDetailsObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | LeLedgerConfigDtlsObjectVersionNumber | — |
| SETUP_STEP_CODE | LeLedgerConfigDtlsSetupStepCode | — |
| SETUP_STEP_CODE | SetupStepCode | ✅ |
| STATUS_CODE | GlLedgerConfigDetailsStatusCode | — |
| STATUS_CODE | LeLedgerConfigDtlsStatusCode | — |
| TAX_DEFAULT_LE_FLAG | GlLedgerConfigDetailsTaxDefaultLeFlag | — |
| TAX_DEFAULT_LE_FLAG | LeLedgerConfigDtlsTaxDefaultLeFlag | — |
| TIME_ZONE_DEFAULT_LE_FLAG | GlLedgerConfigDetailsTimeZoneDefaultLeFlag | — |
| TIME_ZONE_DEFAULT_LE_FLAG | LeLedgerConfigDtlsTimeZoneDefaultLeFlag | — |

### [[legalentityprimaryledgerpvo|LegalEntityPrimaryLedgerPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONFIGURATION_ID | GlLedConfDetConfigurationId | — |
| NEXT_ACTION_CODE | GlLedConfDetNextActionCode | — |
| OBJECT_ID | GlLedConfDetObjectId | — |
| OBJECT_NAME | GlLedConfDetObjectName | — |
| OBJECT_TYPE_CODE | GlLedConfDetObjectTypeCode | — |
| SETUP_STEP_CODE | GlLedConfDetSetupStepCode | — |
| STATUS_CODE | GlLedConfDetStatusCode | — |
| TAX_DEFAULT_LE_FLAG | GlLedConfDetTaxDefaultLeFlag | — |
| TIME_ZONE_DEFAULT_LE_FLAG | GlLedConfDetTimeZoneDefaultLeFlag | — |

### [[legalentitypvo|LegalEntityPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONFIGURATION_ID | GlLedConfDetConfigurationId | — |
| NEXT_ACTION_CODE | GlLedConfDetNextActionCode | — |
| OBJECT_ID | GlLedConfDetObjectId | — |
| OBJECT_NAME | GlLedConfDetObjectName | — |
| OBJECT_TYPE_CODE | GlLedConfDetObjectTypeCode | — |
| SETUP_STEP_CODE | GlLedConfDetSetupStepCode | — |
| STATUS_CODE | GlLedConfDetStatusCode | — |
| TAX_DEFAULT_LE_FLAG | GlLedConfDetTaxDefaultLeFlag | — |
| TIME_ZONE_DEFAULT_LE_FLAG | GlLedConfDetTimeZoneDefaultLeFlag | — |

---

## 📚 Referências

- [Oracle Docs — GL_LEDGER_CONFIG_DETAILS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glledgerconfigdetails.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
