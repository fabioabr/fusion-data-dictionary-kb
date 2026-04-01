---
id: DOC-GL-009
doc_type: system-doc
title: "GL_DAILY_CONVERSION_TYPES — Tipos de Conversão Cambial Diária"
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
  - cambio
  - conversao
  - moeda
aliases:
  - GL_DAILY_CONVERSION_TYPES
  - gl_daily_conversion_types
  - tipos-conversao-cambial
  - daily-conversion-types
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_DAILY_CONVERSION_TYPES

## Visao Geral

Armazena os **tipos de conversão cambial** disponíveis para taxas de câmbio diárias no General Ledger. Cada registro define um tipo de taxa (Spot, Corporate, User, etc.) que pode ser utilizado na conversão de transações entre moedas. Esses tipos são referenciados pela tabela [[gl_daily_rates]] e por todas as transações multi-moeda do ERP.

> [!note] Tipos predefinidos
> O Oracle Fusion inclui tipos de conversão padrão como **Spot**, **Corporate** e **User**. A organização pode criar tipos adicionais conforme suas necessidades (ex: "BACEN" para taxa do Banco Central).

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Conversão de moedas:** Define quais tipos de taxa estão disponíveis para conversão de transações (AP, AR, GL).
- **Cotação diária:** Cada tipo pode ter taxas diferentes carregadas diariamente na [[gl_daily_rates]].
- **Política cambial:** Permite definir tipos corporativos (taxa interna) vs. tipos de mercado (spot).
- **Relatórios multi-moeda:** Referência para revalorizações e translations de saldos.
- **Integração:** Tipos de conversão são usados por todos os módulos financeiros (AP, AR, FA, etc.).

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONVERSION_TYPE | VARCHAR2(30) | NOT NULL | PK | Código do tipo de conversão (ex: Spot, Corporate, User) | — | 🟢 95% |
| 2 | USER_CONVERSION_TYPE | VARCHAR2(30) | NOT NULL | Identificação | Nome amigável do tipo de conversão | — | 🟢 95% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do tipo de conversão | — | 🟢 90% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o tipo está ativo (Y/N) | — | 🟢 85% |
| 5 | ATTRIBUTE1–5 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis | — | 🟡 70% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟡 70% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Sistema | Controle de versionamento otimista (locking) | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta — esta é uma tabela de configuração raiz.

### Tabelas-filha (FK de saída)
- [[gl_daily_rates]] — via `CONVERSION_TYPE` (taxas de câmbio diárias associadas)

---

## Uso Tipico

### Listar tipos de conversão ativos
```sql
SELECT dct.CONVERSION_TYPE, dct.USER_CONVERSION_TYPE,
       dct.DESCRIPTION
FROM   GL_DAILY_CONVERSION_TYPES dct
WHERE  dct.ENABLED_FLAG = 'Y'
ORDER BY dct.USER_CONVERSION_TYPE;
```

### Verificar se existe tipo corporativo
```sql
SELECT dct.CONVERSION_TYPE, dct.USER_CONVERSION_TYPE
FROM   GL_DAILY_CONVERSION_TYPES dct
WHERE  dct.CONVERSION_TYPE = 'Corporate'
  AND  dct.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Tipos ativos
- `CONVERSION_TYPE = 'Spot'` — Taxa spot (mercado)
- `CONVERSION_TYPE = 'Corporate'` — Taxa corporativa (interna)
- `CONVERSION_TYPE = 'User'` — Taxa definida pelo usuário na transação

---

## Observacoes

- Os tipos **Spot**, **Corporate** e **User** são predefinidos pelo Oracle e não devem ser removidos.
- O tipo **User** é especial — permite que o usuário informe a taxa manualmente na transação, sem depender de taxas carregadas na [[gl_daily_rates]].
- Tipos customizados (ex: "BACEN", "ECB") podem ser criados para representar fontes específicas de cotação.
- O `CONVERSION_TYPE` é o código interno (usado em joins), enquanto `USER_CONVERSION_TYPE` é o nome exibido na interface.
- Todos os módulos financeiros (AP, AR, FA, Projects) referenciam esta tabela para conversão de moedas em transações.

---

## Referencias

- [Oracle Docs — GL_DAILY_CONVERSION_TYPES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gldailyconversiontypes-25080.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 4/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | CashDailyConversionTypeConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | CashDailyConversionTypeCreatedBy | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | CashDailyConversionTypeCreationDate | ✅ |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | CashDailyConversionTypeDescription | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | CashDailyConversionTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | CashDailyConversionTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | CashDailyConversionTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | CashDailyConversionTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | CashDailyConversionTypeFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | CashDailyConversionTypeFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | CashDailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CashDailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | CashDailyConversionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | CashDailyConversionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | CashDailyConversionTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | CashDailyConversionTypeSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | CashDailyConversionTypeUserConversionType | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | CashDailyConversionTypeUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[awardednegotiationresponselinepvo|AwardedNegotiationResponseLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeResHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| DESCRIPTION | DailyConversionTypeResHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeResHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeResHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeResHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeResHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeResHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeResHdrFemTimeframe | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeNegoHdrObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeResHdrObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeResHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeResHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConversionTypeResHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeResHdrUserOverrideCrossRateFlag | — |

### [[balanceactivitypvo|BalanceActivityPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ConversionType | — |
| OBJECT_VERSION_NUMBER | GLDailyConversionTypeObjectVersionNumber | — |
| USER_CONVERSION_TYPE | UserConversionType | — |

### [[bankaccountpvo|BankAccountPVO]] (OTHER · BICC: 4/72)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | BankExcRateTypeConversionType | — |
| CONVERSION_TYPE | GlCurExcRateTypeConversionType | — |
| CONVERSION_TYPE | ReconFrnBankXrateDateTypeConversionType | — |
| CONVERSION_TYPE | ReconFrnBankXrateTypeConversionType | — |
| CREATED_BY | BankExcRateTypeCreatedBy | — |
| CREATED_BY | GlCurExcRateTypeCreatedBy | — |
| CREATED_BY | ReconFrnBankXrateDateTypeCreatedBy | — |
| CREATED_BY | ReconFrnBankXrateTypeCreatedBy | — |
| CREATION_DATE | BankExcRateTypeCreationDate | — |
| CREATION_DATE | GlCurExcRateTypeCreationDate | — |
| CREATION_DATE | ReconFrnBankXrateDateTypeCreationDate | — |
| CREATION_DATE | ReconFrnBankXrateTypeCreationDate | — |
| DESCRIPTION | BankExcRateTypeDescription | — |
| DESCRIPTION | GlCurExcRateTypeDescription | — |
| DESCRIPTION | ReconFrnBankXrateDateTypeDescription | — |
| DESCRIPTION | ReconFrnBankXrateTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | BankExcRateTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | GlCurExcRateTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | ReconFrnBankXrateDateTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | ReconFrnBankXrateTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | BankExcRateTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | GlCurExcRateTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | ReconFrnBankXrateDateTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | ReconFrnBankXrateTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | BankExcRateTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | GlCurExcRateTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | ReconFrnBankXrateDateTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | ReconFrnBankXrateTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | BankExcRateTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | GlCurExcRateTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | ReconFrnBankXrateDateTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | ReconFrnBankXrateTypeFemRateTypeCode | — |
| FEM_SCENARIO | BankExcRateTypeFemScenario | — |
| FEM_SCENARIO | GlCurExcRateTypeFemScenario | — |
| FEM_SCENARIO | ReconFrnBankXrateDateTypeFemScenario | — |
| FEM_SCENARIO | ReconFrnBankXrateTypeFemScenario | — |
| FEM_TIMEFRAME | BankExcRateTypeFemTimeframe | — |
| FEM_TIMEFRAME | GlCurExcRateTypeFemTimeframe | — |
| FEM_TIMEFRAME | ReconFrnBankXrateDateTypeFemTimeframe | — |
| FEM_TIMEFRAME | ReconFrnBankXrateTypeFemTimeframe | — |
| LAST_UPDATE_DATE | BankExcRateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | GlCurExcRateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReconFrnBankXrateDateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReconFrnBankXrateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BankExcRateTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | GlCurExcRateTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReconFrnBankXrateDateTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReconFrnBankXrateTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | BankExcRateTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | GlCurExcRateTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | ReconFrnBankXrateDateTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | ReconFrnBankXrateTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | BankExcRateTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | GlCurExcRateTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReconFrnBankXrateDateTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReconFrnBankXrateTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | BankExcRateTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | GlCurExcRateTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | ReconFrnBankXrateDateTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | ReconFrnBankXrateTypePivotCurrencyCode | — |
| SECURITY_FLAG | BankExcRateTypeSecurityFlag | — |
| SECURITY_FLAG | GlCurExcRateTypeSecurityFlag | — |
| SECURITY_FLAG | ReconFrnBankXrateDateTypeSecurityFlag | — |
| SECURITY_FLAG | ReconFrnBankXrateTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | BankExcRateTypeUserConversionType | — |
| USER_CONVERSION_TYPE | GlCurExcRateTypeUserConversionType | — |
| USER_CONVERSION_TYPE | ReconFrnBankXrateDateTypeUserConversionType | — |
| USER_CONVERSION_TYPE | ReconFrnBankXrateTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | BankExcRateTypeUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | GlCurExcRateTypeUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | ReconFrnBankXrateDateTypeUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | ReconFrnBankXrateTypeUserOverrideCrossRateFlag | — |

### [[bankstatementlineavailabilitypvo|BankStatementLineAvailabilityPVO]] (OTHER · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | RateTypeConversionType | — |
| CREATED_BY | RateTypeCreatedBy | — |
| CREATION_DATE | RateTypeCreationDate | — |
| DESCRIPTION | RateTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | RateTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | RateTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | RateTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | RateTypeFemRateTypeCode | — |
| FEM_SCENARIO | RateTypeFemScenario | — |
| FEM_TIMEFRAME | RateTypeFemTimeframe | — |
| LAST_UPDATE_DATE | RateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RateTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | RateTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | RateTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | RateTypePivotCurrencyCode | — |
| SECURITY_FLAG | RateTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | RateTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | RateTypeUserOverrideCrossRateFlag | — |

### [[bankstatementlinespvo|BankStatementLinesPVO]] (OTHER · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | RateTypeConversionType | — |
| CREATED_BY | RateTypeCreatedBy | — |
| CREATION_DATE | RateTypeCreationDate | — |
| DESCRIPTION | RateTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | RateTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | RateTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | RateTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | RateTypeFemRateTypeCode | — |
| FEM_SCENARIO | RateTypeFemScenario | — |
| FEM_TIMEFRAME | RateTypeFemTimeframe | — |
| LAST_UPDATE_DATE | RateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RateTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | RateTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | RateTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | RateTypePivotCurrencyCode | — |
| SECURITY_FLAG | RateTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | RateTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | RateTypeUserOverrideCrossRateFlag | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[contractheadercurrentp|ContractHeaderCurrentP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ContractHeaderInvConvRatePEOConversionType | — |
| CONVERSION_TYPE | ContractHeaderRevConvRatePEOConversionType | — |
| DESCRIPTION | ContractHeaderInvConvRatePEODescription | — |
| DESCRIPTION | ContractHeaderRevConvRatePEODescription | — |
| OBJECT_VERSION_NUMBER | ContractHeaderInvConvRatePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ContractHeaderRevConvRatePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ContractHeaderInvConvRatePEOUserConversionType | — |
| USER_CONVERSION_TYPE | ContractHeaderRevConvRatePEOUserConversionType | — |

### [[contractheaderlinesall|ContractHeaderLinesAll]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ContractHeaderInvConvRatePEOConversionType | — |
| CONVERSION_TYPE | ContractHeaderRevConvRatePEOConversionType | — |
| DESCRIPTION | ContractHeaderInvConvRatePEODescription | — |
| DESCRIPTION | ContractHeaderRevConvRatePEODescription | — |
| OBJECT_VERSION_NUMBER | ContractHeaderInvConvRatePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ContractHeaderRevConvRatePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ContractHeaderInvConvRatePEOUserConversionType | — |
| USER_CONVERSION_TYPE | ContractHeaderRevConvRatePEOUserConversionType | — |

### [[contractheaderlinesallunsec|ContractHeaderLinesAllUnsec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ContractHeaderInvConvRatePEOConversionType | — |
| CONVERSION_TYPE | ContractHeaderRevConvRatePEOConversionType | — |
| DESCRIPTION | ContractHeaderInvConvRatePEODescription | — |
| DESCRIPTION | ContractHeaderRevConvRatePEODescription | — |
| OBJECT_VERSION_NUMBER | ContractHeaderInvConvRatePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ContractHeaderRevConvRatePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ContractHeaderInvConvRatePEOUserConversionType | — |
| USER_CONVERSION_TYPE | ContractHeaderRevConvRatePEOUserConversionType | — |

### [[contractheaderlinesp|ContractHeaderLinesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ContractHeaderInvConvRatePEOConversionType | — |
| CONVERSION_TYPE | ContractHeaderRevConvRatePEOConversionType | — |
| DESCRIPTION | ContractHeaderInvConvRatePEODescription | — |
| DESCRIPTION | ContractHeaderRevConvRatePEODescription | — |
| OBJECT_VERSION_NUMBER | ContractHeaderInvConvRatePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ContractHeaderRevConvRatePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ContractHeaderInvConvRatePEOUserConversionType | — |
| USER_CONVERSION_TYPE | ContractHeaderRevConvRatePEOUserConversionType | — |

### [[contractheaderlinesrefp|ContractHeaderLinesRefP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ContractHeaderInvConvRatePEOConversionType | — |
| CONVERSION_TYPE | ContractHeaderRevConvRatePEOConversionType | — |
| DESCRIPTION | ContractHeaderInvConvRatePEODescription | — |
| DESCRIPTION | ContractHeaderRevConvRatePEODescription | — |
| OBJECT_VERSION_NUMBER | ContractHeaderInvConvRatePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ContractHeaderRevConvRatePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ContractHeaderInvConvRatePEOUserConversionType | — |
| USER_CONVERSION_TYPE | ContractHeaderRevConvRatePEOUserConversionType | — |

### [[contractheaderp|ContractHeaderP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ContractHeaderInvConvRatePEOConversionType | — |
| CONVERSION_TYPE | ContractHeaderRevConvRatePEOConversionType | — |
| DESCRIPTION | ContractHeaderInvConvRatePEODescription | — |
| DESCRIPTION | ContractHeaderRevConvRatePEODescription | — |
| OBJECT_VERSION_NUMBER | ContractHeaderInvConvRatePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ContractHeaderRevConvRatePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ContractHeaderInvConvRatePEOUserConversionType | — |
| USER_CONVERSION_TYPE | ContractHeaderRevConvRatePEOUserConversionType | — |

### [[contractheaderrefp|ContractHeaderRefP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ContractHeaderInvConvRatePEOConversionType | — |
| CONVERSION_TYPE | ContractHeaderRevConvRatePEOConversionType | — |
| DESCRIPTION | ContractHeaderInvConvRatePEODescription | — |
| DESCRIPTION | ContractHeaderRevConvRatePEODescription | — |
| OBJECT_VERSION_NUMBER | ContractHeaderInvConvRatePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ContractHeaderRevConvRatePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ContractHeaderInvConvRatePEOUserConversionType | — |
| USER_CONVERSION_TYPE | ContractHeaderRevConvRatePEOUserConversionType | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 2/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | CurConvTypeConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | CurConvTypeDescription | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber6 | — |
| PIVOT_CURRENCY_CODE | CurConvTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | CurConvTypeUserConversionType | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[customerprofile|CustomerProfile]] (AR · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | GlConvTypeConversionType | — |
| ENABLE_CROSS_RATE_FLAG | GlConvTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | GlConvTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | GlConvTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | GlConvTypeFemRateTypeCode | — |
| FEM_SCENARIO | GlConvTypeFemScenario | — |
| FEM_TIMEFRAME | GlConvTypeFemTimeframe | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | GlConvTypePivotCurrencyCode | — |
| SECURITY_FLAG | GlConvTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | GlConvTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | GlConvTypeUserOverrideCrossRateFlag | — |

### [[customersiteprofile|CustomerSiteProfile]] (AR · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | GlConvTypeConversionType | — |
| ENABLE_CROSS_RATE_FLAG | GlConvTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | GlConvTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | GlConvTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | GlConvTypeFemRateTypeCode | — |
| FEM_SCENARIO | GlConvTypeFemScenario | — |
| FEM_TIMEFRAME | GlConvTypeFemTimeframe | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | GlConvTypePivotCurrencyCode | — |
| SECURITY_FLAG | GlConvTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | GlConvTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | GlConvTypeUserOverrideCrossRateFlag | — |

### [[dailyconversiontypeextractpvo|DailyConversionTypeExtractPVO]] (OTHER · BICC: 13/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | DailyConversionTypeAttribute1 | — |
| ATTRIBUTE10 | DailyConversionTypeAttribute10 | — |
| ATTRIBUTE11 | DailyConversionTypeAttribute11 | — |
| ATTRIBUTE12 | DailyConversionTypeAttribute12 | — |
| ATTRIBUTE13 | DailyConversionTypeAttribute13 | — |
| ATTRIBUTE14 | DailyConversionTypeAttribute14 | — |
| ATTRIBUTE15 | DailyConversionTypeAttribute15 | — |
| ATTRIBUTE2 | DailyConversionTypeAttribute2 | — |
| ATTRIBUTE3 | DailyConversionTypeAttribute3 | — |
| ATTRIBUTE4 | DailyConversionTypeAttribute4 | — |
| ATTRIBUTE5 | DailyConversionTypeAttribute5 | — |
| ATTRIBUTE6 | DailyConversionTypeAttribute6 | — |
| ATTRIBUTE7 | DailyConversionTypeAttribute7 | — |
| ATTRIBUTE8 | DailyConversionTypeAttribute8 | — |
| ATTRIBUTE9 | DailyConversionTypeAttribute9 | — |
| ATTRIBUTE_CATEGORY | DailyConversionTypeAttributeCategory | — |
| CONVERSION_TYPE | DailyConversionTypeConversionType | ✅ |
| CREATED_BY | DailyConversionTypeCreatedBy | ✅ |
| CREATION_DATE | DailyConversionTypeCreationDate | ✅ |
| DESCRIPTION | DailyConversionTypeDescription | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | ✅ |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | ✅ |

### [[dailyconversiontypepvo|DailyConversionTypePVO]] (OTHER · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | DailyConversionTypeAttribute1 | — |
| ATTRIBUTE10 | DailyConversionTypeAttribute10 | — |
| ATTRIBUTE11 | DailyConversionTypeAttribute11 | — |
| ATTRIBUTE12 | DailyConversionTypeAttribute12 | — |
| ATTRIBUTE13 | DailyConversionTypeAttribute13 | — |
| ATTRIBUTE14 | DailyConversionTypeAttribute14 | — |
| ATTRIBUTE15 | DailyConversionTypeAttribute15 | — |
| ATTRIBUTE2 | DailyConversionTypeAttribute2 | — |
| ATTRIBUTE3 | DailyConversionTypeAttribute3 | — |
| ATTRIBUTE4 | DailyConversionTypeAttribute4 | — |
| ATTRIBUTE5 | DailyConversionTypeAttribute5 | — |
| ATTRIBUTE6 | DailyConversionTypeAttribute6 | — |
| ATTRIBUTE7 | DailyConversionTypeAttribute7 | — |
| ATTRIBUTE8 | DailyConversionTypeAttribute8 | — |
| ATTRIBUTE9 | DailyConversionTypeAttribute9 | — |
| ATTRIBUTE_CATEGORY | DailyConversionTypeAttributeCategory | — |
| CONVERSION_TYPE | DailyConversionTypeConversionType | ✅ |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[dailyratepvo|DailyRatePVO]] (GL · BICC: 7/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | GlDailyConversionTypesConversionType | ✅ |
| CREATED_BY | GlDailyConversionTypesCreatedBy | ✅ |
| CREATION_DATE | GlDailyConversionTypesCreationDate | ✅ |
| DESCRIPTION | GlDailyConversionTypesDescription | ✅ |
| ENABLE_CROSS_RATE_FLAG | GlDailyConversionTypesEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | GlDailyConversionTypesEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | GlDailyConversionTypesFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | GlDailyConversionTypesFemRateTypeCode | — |
| FEM_SCENARIO | GlDailyConversionTypesFemScenario | — |
| FEM_TIMEFRAME | GlDailyConversionTypesFemTimeframe | — |
| LAST_UPDATE_DATE | GlDailyConversionTypesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlDailyConversionTypesLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GlDailyConversionTypesLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | GlDailyConversionTypesObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | GlDailyConversionTypesPivotCurrencyCode | — |
| SECURITY_FLAG | GlDailyConversionTypesSecurityFlag | — |
| USER_CONVERSION_TYPE | GlDailyConversionTypesUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | GlDailyConversionTypesUserOverrideCrossRateFlag | — |

### [[disbursementheaderpvo|DisbursementHeaderPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ExchangeRateTypeConversionType | — |
| USER_CONVERSION_TYPE | ExchangeRateTypeUserConversionType | ✅ |

### [[distributioninitlinepvo|DistributionInitLinePVO]] (OTHER · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[distributionrectlinepvo|DistributionRectLinePVO]] (OTHER · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 3/54)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | InvoiceConversionTypeConversionType | — |
| CONVERSION_TYPE | PaymentConversionTypeConversionType | — |
| CONVERSION_TYPE | RateTypeConversionType | — |
| CREATED_BY | InvoiceConversionTypeCreatedBy | — |
| CREATED_BY | PaymentConversionTypeCreatedBy | — |
| CREATED_BY | RateTypeCreatedBy | — |
| CREATION_DATE | InvoiceConversionTypeCreationDate | — |
| CREATION_DATE | PaymentConversionTypeCreationDate | — |
| CREATION_DATE | RateTypeCreationDate | — |
| DESCRIPTION | InvoiceConversionTypeDescription | — |
| DESCRIPTION | PaymentConversionTypeDescription | — |
| DESCRIPTION | RateTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | InvoiceConversionTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | PaymentConversionTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | RateTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | InvoiceConversionTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | PaymentConversionTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | RateTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | InvoiceConversionTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | PaymentConversionTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | RateTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | InvoiceConversionTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | PaymentConversionTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | RateTypeFemRateTypeCode | — |
| FEM_SCENARIO | InvoiceConversionTypeFemScenario | — |
| FEM_SCENARIO | PaymentConversionTypeFemScenario | — |
| FEM_SCENARIO | RateTypeFemScenario | — |
| FEM_TIMEFRAME | InvoiceConversionTypeFemTimeframe | — |
| FEM_TIMEFRAME | PaymentConversionTypeFemTimeframe | — |
| FEM_TIMEFRAME | RateTypeFemTimeframe | — |
| LAST_UPDATE_DATE | InvoiceConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvoiceConversionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PaymentConversionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RateTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | InvoiceConversionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | PaymentConversionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | RateTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | InvoiceConversionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PaymentConversionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RateTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | InvoiceConversionTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | PaymentConversionTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | RateTypePivotCurrencyCode | — |
| SECURITY_FLAG | InvoiceConversionTypeSecurityFlag | — |
| SECURITY_FLAG | PaymentConversionTypeSecurityFlag | — |
| SECURITY_FLAG | RateTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | InvoiceConversionTypeUserConversionType | — |
| USER_CONVERSION_TYPE | PaymentConversionTypeUserConversionType | — |
| USER_CONVERSION_TYPE | RateTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | InvoiceConversionTypeUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | PaymentConversionTypeUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | RateTypeUserOverrideCrossRateFlag | — |

### [[expensepvo|ExpensePVO]] (OTHER · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | GlDailyConversionTypesConversionType | — |
| CREATED_BY | GlDailyConversionTypesCreatedBy | — |
| CREATION_DATE | GlDailyConversionTypesCreationDate | — |
| DESCRIPTION | GlDailyConversionTypesDescription | — |
| ENABLE_CROSS_RATE_FLAG | GlDailyConversionTypesEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | GlDailyConversionTypesEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | GlDailyConversionTypesFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | GlDailyConversionTypesFemRateTypeCode | — |
| FEM_SCENARIO | GlDailyConversionTypesFemScenario | — |
| FEM_TIMEFRAME | GlDailyConversionTypesFemTimeframe | — |
| LAST_UPDATE_DATE | GlDailyConversionTypesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlDailyConversionTypesLastUpdateLogin | — |
| LAST_UPDATED_BY | GlDailyConversionTypesLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | GlDailyConversionTypesObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | GlDailyConversionTypesPivotCurrencyCode | — |
| SECURITY_FLAG | GlDailyConversionTypesSecurityFlag | — |
| USER_CONVERSION_TYPE | GlDailyConversionTypesUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | GlDailyConversionTypesUserOverrideCrossRateFlag | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | RateTypeConversionType | — |
| CREATED_BY | RateTypeCreatedBy | — |
| CREATION_DATE | RateTypeCreationDate | — |
| DESCRIPTION | RateTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | RateTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | RateTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | RateTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | RateTypeFemRateTypeCode | — |
| FEM_SCENARIO | RateTypeFemScenario | — |
| FEM_TIMEFRAME | RateTypeFemTimeframe | — |
| LAST_UPDATE_DATE | RateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RateTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | RateTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | RateTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | RateTypePivotCurrencyCode | — |
| SECURITY_FLAG | RateTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | RateTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | RateTypeUserOverrideCrossRateFlag | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[invoicedistributionpvo|InvoiceDistributionPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ContCurrInvRateTypePEOConversionType | — |
| CONVERSION_TYPE | LedgerCurrInvRateTypePEOConversionType | — |
| CONVERSION_TYPE | ProjCurrInvRateTypePEOConversionType | — |
| DESCRIPTION | ContCurrInvRateTypePEODescription | — |
| DESCRIPTION | LedgerCurrInvRateTypePEODescription | — |
| DESCRIPTION | ProjCurrInvRateTypePEODescription | — |

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | InvoiceConversionTypeConversionType | — |
| USER_CONVERSION_TYPE | InvoiceConversionTypeUserConversionType | ✅ |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | InvoiceConversionTypeConversionType | — |
| USER_CONVERSION_TYPE | InvoiceConversionTypeUserConversionType | ✅ |

### [[journalentrylinepvo|JournalEntryLinePVO]] (GL · BICC: 1/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ConversionTypeXlalineConversionType | — |
| CONVERSION_TYPE | DailyConvConversionType | — |
| DESCRIPTION | ConversionTypeXlalineDescription | ✅ |
| DESCRIPTION | DailyConvDescription | — |
| ENABLE_CROSS_RATE_FLAG | ConversionTypeXlalineEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConvEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | ConversionTypeXlalineEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConvEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | ConversionTypeXlalineFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConvFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | ConversionTypeXlalineFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConvFemRateTypeCode | — |
| FEM_SCENARIO | ConversionTypeXlalineFemScenario | — |
| FEM_SCENARIO | DailyConvFemScenario | — |
| FEM_TIMEFRAME | ConversionTypeXlalineFemTimeframe | — |
| FEM_TIMEFRAME | DailyConvFemTimeframe | — |
| OBJECT_VERSION_NUMBER | ConversionTypeXlalineObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | ConversionTypeXlalinePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConvPivotCurrencyCode | — |
| SECURITY_FLAG | ConversionTypeXlalineSecurityFlag | — |
| SECURITY_FLAG | DailyConvSecurityFlag | — |
| USER_CONVERSION_TYPE | ConversionTypeXlalineUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConvUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | ConversionTypeXlalineUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConvUserOverrideCrossRateFlag | — |

### [[journalheaderpvo|JournalHeaderPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ConversionTypeConversionType | — |
| DESCRIPTION | ConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | ConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | ConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | ConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | ConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | ConversionTypeFemScenario | — |
| FEM_TIMEFRAME | ConversionTypeFemTimeframe | — |
| OBJECT_VERSION_NUMBER | CreatedByPersonNameObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | LastUpdatedByPersonNameObjectVersionNumber2 | — |
| PIVOT_CURRENCY_CODE | ConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | ConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | ConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | ConversionTypeUserOverrideCrossRateFlag | — |

### [[journallinepvo|JournalLinePVO]] (GL · BICC: 1/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ConversionTypeConversionType | — |
| CONVERSION_TYPE | ConversionTypeLineConversionType | — |
| DESCRIPTION | ConversionTypeDescription | — |
| DESCRIPTION | ConversionTypeLineDescription | — |
| ENABLE_CROSS_RATE_FLAG | ConversionTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | ConversionTypeLineEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | ConversionTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | ConversionTypeLineEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | ConversionTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | ConversionTypeLineFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | ConversionTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | ConversionTypeLineFemRateTypeCode | — |
| FEM_SCENARIO | ConversionTypeFemScenario | — |
| FEM_SCENARIO | ConversionTypeLineFemScenario | — |
| FEM_TIMEFRAME | ConversionTypeFemTimeframe | — |
| FEM_TIMEFRAME | ConversionTypeLineFemTimeframe | — |
| OBJECT_VERSION_NUMBER | ConversionTypeLineObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CreatedByPersonNameObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | LastUpdatedByPersonNameObjectVersionNumber2 | — |
| PIVOT_CURRENCY_CODE | ConversionTypeLinePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | ConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | ConversionTypeLineSecurityFlag | — |
| SECURITY_FLAG | ConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | ConversionTypeLineUserConversionType | ✅ |
| USER_CONVERSION_TYPE | ConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | ConversionTypeLineUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | ConversionTypeUserOverrideCrossRateFlag | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 4/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CONVERSION_TYPE | ReceiptDailyRateConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATED_BY | ReceiptDailyRateCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| CREATION_DATE | ReceiptDailyRateCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| DESCRIPTION | ReceiptDailyRateDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | ReceiptDailyRateEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | ReceiptDailyRateEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | ReceiptDailyRateFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | ReceiptDailyRateFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_SCENARIO | ReceiptDailyRateFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| FEM_TIMEFRAME | ReceiptDailyRateFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptDailyRateLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptDailyRateLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptDailyRateLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptDailyRateObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | ReceiptDailyRatePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| SECURITY_FLAG | ReceiptDailyRateSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_CONVERSION_TYPE | ReceiptDailyRateUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | ReceiptDailyRateUserOverrideCrossRateFlag | — |

### [[negdocumentnegotiationlinepvo|NegDocumentNegotiationLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |

### [[negdocumentsourcingnegotiationandtemplatepvo|NegDocumentSourcingNegotiationAndTemplatePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeNegoHdrObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |

### [[negdocumentsourcingsupplierinviteepvo|NegDocumentSourcingSupplierInviteePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |

### [[negotiationawardacceptancepvo|NegotiationAwardAcceptancePVO]] (PO · BICC: 25/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | ✅ |
| CONVERSION_TYPE | DailyConversionTypeResHdrConversionType | ✅ |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | ✅ |
| DESCRIPTION | DailyConversionTypeResHdrDescription | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeResHdrEnableCrossRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeResHdrEnforceInverseRateFlag | ✅ |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | ✅ |
| FEM_ENABLED_FLAG | DailyConversionTypeResHdrFemEnabledFlag | ✅ |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | ✅ |
| FEM_RATE_TYPE_CODE | DailyConversionTypeResHdrFemRateTypeCode | ✅ |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | ✅ |
| FEM_SCENARIO | DailyConversionTypeResHdrFemScenario | ✅ |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | ✅ |
| FEM_TIMEFRAME | DailyConversionTypeResHdrFemTimeframe | ✅ |
| OBJECT_VERSION_NUMBER | DailyConversionTypeNegoHdrObjectVersionNumber | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypeResHdrPivotCurrencyCode | ✅ |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | ✅ |
| SECURITY_FLAG | DailyConversionTypeResHdrSecurityFlag | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeResHdrUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeResHdrUserOverrideCrossRateFlag | ✅ |

### [[negotiationcollaborationteampvo|NegotiationCollaborationTeamPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeNegoHdrObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |

### [[negotiationpricetierpvo|NegotiationPriceTierPVO]] (PO · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | ✅ |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | ✅ |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | ✅ |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | ✅ |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | ✅ |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | ✅ |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | ✅ |

### [[negotiationresponsecostfactorpvo|NegotiationResponseCostFactorPVO]] (PO · BICC: 36/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | ✅ |
| CONVERSION_TYPE | DailyConversionTypeResHdrConversionType | ✅ |
| CREATED_BY | DailyConversionTypeNegoHdrCreatedBy | ✅ |
| CREATED_BY | DailyConversionTypeResHdrCreatedBy | ✅ |
| CREATION_DATE | DailyConversionTypeNegoHdrCreationDate | ✅ |
| CREATION_DATE | DailyConversionTypeResHdrCreationDate | ✅ |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | ✅ |
| DESCRIPTION | DailyConversionTypeResHdrDescription | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeResHdrEnableCrossRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeResHdrEnforceInverseRateFlag | ✅ |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | ✅ |
| FEM_ENABLED_FLAG | DailyConversionTypeResHdrFemEnabledFlag | ✅ |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | ✅ |
| FEM_RATE_TYPE_CODE | DailyConversionTypeResHdrFemRateTypeCode | ✅ |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | ✅ |
| FEM_SCENARIO | DailyConversionTypeResHdrFemScenario | ✅ |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | ✅ |
| FEM_TIMEFRAME | DailyConversionTypeResHdrFemTimeframe | ✅ |
| LAST_UPDATE_DATE | DailyConversionTypeNegoHdrLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | DailyConversionTypeResHdrLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeNegoHdrLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeResHdrLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | DailyConversionTypeNegoHdrLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | DailyConversionTypeResHdrLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | DailyConversionTypeNegoHdrObjectVersionNumber | ✅ |
| OBJECT_VERSION_NUMBER | DailyConversionTypeResHdrObjectVersionNumber | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypeResHdrPivotCurrencyCode | ✅ |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | ✅ |
| SECURITY_FLAG | DailyConversionTypeResHdrSecurityFlag | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeResHdrUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeResHdrUserOverrideCrossRateFlag | ✅ |

### [[negotiationresponsepricetierpvo|NegotiationResponsePriceTierPVO]] (PO · BICC: 26/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | ✅ |
| CONVERSION_TYPE | DailyConversionTypeResHdrConversionType | ✅ |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | ✅ |
| DESCRIPTION | DailyConversionTypeResHdrDescription | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeResHdrEnableCrossRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeResHdrEnforceInverseRateFlag | ✅ |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | ✅ |
| FEM_ENABLED_FLAG | DailyConversionTypeResHdrFemEnabledFlag | ✅ |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | ✅ |
| FEM_RATE_TYPE_CODE | DailyConversionTypeResHdrFemRateTypeCode | ✅ |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | ✅ |
| FEM_SCENARIO | DailyConversionTypeResHdrFemScenario | ✅ |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | ✅ |
| FEM_TIMEFRAME | DailyConversionTypeResHdrFemTimeframe | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypeResHdrPivotCurrencyCode | ✅ |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | ✅ |
| SECURITY_FLAG | DailyConversionTypeResHdrSecurityFlag | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeResHdrUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeResHdrUserOverrideCrossRateFlag | ✅ |

### [[negotiationresponsepurchaseorderlinepvo|NegotiationResponsePurchaseOrderLinePVO]] (PO · BICC: 1/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeResHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| DESCRIPTION | DailyConversionTypeResHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeResHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeResHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeResHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeResHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeResHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeResHdrFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeNegoHdrLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeNegoHdrLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeNegoHdrLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeNegoHdrObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeResHdrObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeResHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeResHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConversionTypeResHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeResHdrUserOverrideCrossRateFlag | — |

### [[negotiationresponserequirementandattributepvo|NegotiationResponseRequirementAndAttributePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeResHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| DESCRIPTION | DailyConversionTypeResHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeResHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeResHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeResHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeResHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeResHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeResHdrFemTimeframe | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeResHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeResHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConversionTypeResHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeResHdrUserOverrideCrossRateFlag | — |

### [[negotiationsupplieracknowledgementpvo|NegotiationSupplierAcknowledgementPVO]] (PO · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | ✅ |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | ✅ |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | ✅ |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | ✅ |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | ✅ |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | ✅ |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | ✅ |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ExchangeRateTypeConversionType | — |
| USER_CONVERSION_TYPE | ExchangeRateTypeUserConversionType | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 9/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | BankRateTypeConversionType | — |
| CONVERSION_TYPE | ClearedExchangeRateTypeConversionType | — |
| CONVERSION_TYPE | ExchangeRateTypeConversionType | — |
| CONVERSION_TYPE | ExchangeRateTypeInvPaymentConversionType | — |
| CONVERSION_TYPE | InvoiceConversionTypeConversionType | — |
| CONVERSION_TYPE | MaturityExchangeRateTypeConversionType | — |
| CONVERSION_TYPE | PaymentConversionTypeConversionType | — |
| CONVERSION_TYPE | PmtRateTypeConversionType | — |
| LAST_UPDATE_DATE | BankRateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ClearedExchangeRateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ExchangeRateTypeInvPaymentLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ExchangeRateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | InvoiceConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MaturityExchangeRateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PmtRateTypeLastUpdateDate | ✅ |
| USER_CONVERSION_TYPE | ExchangeRateTypeUserConversionType | ✅ |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 3/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeScheduleConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATED_BY | DailyConversionTypeScheduleCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| CREATION_DATE | DailyConversionTypeScheduleCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| DESCRIPTION | DailyConversionTypeScheduleDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeScheduleEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeScheduleEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeScheduleFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeScheduleFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeScheduleFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeScheduleFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | DailyConversionTypeScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | DailyConversionTypeScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | DailyConversionTypeScheduleLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeScheduleObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeSchedulePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeScheduleSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeScheduleUserConversionType | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeScheduleUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 4/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DistconversionTypeConversionType | — |
| CONVERSION_TYPE | PrepayClrExchangeRateTypeConversionType | — |
| CONVERSION_TYPE | PrepayExchangeRateTypeConversionType | — |
| CONVERSION_TYPE | PrepayPayExchangeRateTypeConversionType | — |
| LAST_UPDATE_DATE | DistconversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PrepayClrExchangeRateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PrepayExchangeRateTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PrepayPayExchangeRateTypeLastUpdateDate | ✅ |

### [[project|Project]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | GlDailyConversionTypesConversionType | — |
| DESCRIPTION | GlDailyConversionTypesDescription | — |
| OBJECT_VERSION_NUMBER | GlDailyConversionTypesObjectVersionNumber | — |

### [[projectexec|ProjectExec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | GlDailyConversionTypesConversionType | — |
| DESCRIPTION | GlDailyConversionTypesDescription | — |
| OBJECT_VERSION_NUMBER | GlDailyConversionTypesObjectVersionNumber | — |

### [[projectplanlinebudgetpvo|ProjectPlanLineBudgetPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | PcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PcRevRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcRevRateTypeForPlanOptnConversionType | — |
| DESCRIPTION | PcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PcRevRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcRevRateTypeForPlanOptnDescription | — |
| USER_CONVERSION_TYPE | PcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PcRevRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcRevRateTypeForPlanOptnUserConversionType | — |

### [[projectplanlinedetailbudgetpvo|ProjectPlanLineDetailBudgetPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | PcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PcRevRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcRevRateTypeForPlanOptnConversionType | — |
| DESCRIPTION | PcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PcRevRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcRevRateTypeForPlanOptnDescription | — |
| USER_CONVERSION_TYPE | PcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PcRevRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcRevRateTypeForPlanOptnUserConversionType | — |

### [[projectplanlineforecastpvo|ProjectPlanLineForecastPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | PcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PcRevRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcRevRateTypeForPlanOptnConversionType | — |
| DESCRIPTION | PcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PcRevRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcRevRateTypeForPlanOptnDescription | — |
| USER_CONVERSION_TYPE | PcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PcRevRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcRevRateTypeForPlanOptnUserConversionType | — |

### [[projectplanversionbudgetpvo|ProjectPlanVersionBudgetPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | PcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PcRevRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcRevRateTypeForPlanOptnConversionType | — |
| DESCRIPTION | PcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PcRevRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcRevRateTypeForPlanOptnDescription | — |
| USER_CONVERSION_TYPE | PcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PcRevRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcRevRateTypeForPlanOptnUserConversionType | — |

### [[projectplanversionforecastpvo|ProjectPlanVersionForecastPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | PcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PcRevRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcRevRateTypeForPlanOptnConversionType | — |
| DESCRIPTION | PcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PcRevRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcRevRateTypeForPlanOptnDescription | — |
| USER_CONVERSION_TYPE | PcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PcRevRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcRevRateTypeForPlanOptnUserConversionType | — |

### [[projectrefpvo|ProjectRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | GlDailyConversionTypesConversionType | — |
| DESCRIPTION | GlDailyConversionTypesDescription | — |
| OBJECT_VERSION_NUMBER | GlDailyConversionTypesObjectVersionNumber | — |

### [[projectview|ProjectView]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | GlDailyConversionTypesConversionType | — |
| DESCRIPTION | GlDailyConversionTypesDescription | — |
| OBJECT_VERSION_NUMBER | GlDailyConversionTypesObjectVersionNumber | — |

### [[projplanlinedetailforecastpvo|ProjPlanLineDetailForecastPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | PcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PcRevRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcCostRateTypeForPlanOptnConversionType | — |
| CONVERSION_TYPE | PfcRevRateTypeForPlanOptnConversionType | — |
| DESCRIPTION | PcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PcRevRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcCostRateTypeForPlanOptnDescription | — |
| DESCRIPTION | PfcRevRateTypeForPlanOptnDescription | — |
| USER_CONVERSION_TYPE | PcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PcRevRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcCostRateTypeForPlanOptnUserConversionType | — |
| USER_CONVERSION_TYPE | PfcRevRateTypeForPlanOptnUserConversionType | — |

### [[rateadjustmentpvo|RateAdjustmentPVO]] (AR · BICC: 4/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | NewExcRateConversionType | — |
| CONVERSION_TYPE | OldExcRateConversionType | — |
| CREATED_BY | NewExcRateCreatedBy | — |
| CREATED_BY | OldExcRateCreatedBy | — |
| CREATION_DATE | NewExcRateCreationDate | — |
| CREATION_DATE | OldExcRateCreationDate | — |
| DESCRIPTION | NewExcRateDescription | — |
| DESCRIPTION | OldExcRateDescription | — |
| ENABLE_CROSS_RATE_FLAG | NewExcRateEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | OldExcRateEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | NewExcRateEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | OldExcRateEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | NewExcRateFemEnabledFlag | — |
| FEM_ENABLED_FLAG | OldExcRateFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | NewExcRateFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | OldExcRateFemRateTypeCode | — |
| FEM_SCENARIO | NewExcRateFemScenario | — |
| FEM_SCENARIO | OldExcRateFemScenario | — |
| FEM_TIMEFRAME | NewExcRateFemTimeframe | — |
| FEM_TIMEFRAME | OldExcRateFemTimeframe | — |
| LAST_UPDATE_DATE | NewExcRateLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OldExcRateLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NewExcRateLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OldExcRateLastUpdateLogin | — |
| LAST_UPDATED_BY | NewExcRateLastUpdatedBy | — |
| LAST_UPDATED_BY | OldExcRateLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | NewExcRateObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OldExcRateObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | NewExcRatePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | OldExcRatePivotCurrencyCode | — |
| SECURITY_FLAG | NewExcRateSecurityFlag | — |
| SECURITY_FLAG | OldExcRateSecurityFlag | — |
| USER_CONVERSION_TYPE | NewExcRateUserConversionType | ✅ |
| USER_CONVERSION_TYPE | OldExcRateUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | NewExcRateUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | OldExcRateUserOverrideCrossRateFlag | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 3/59)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConvCashDistConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeScheduleConversionType | — |
| CONVERSION_TYPE | ExchConvTypeConversionType | — |
| CREATED_BY | DailyConvCashDistCreatedBy | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATED_BY | DailyConversionTypeScheduleCreatedBy | — |
| CREATION_DATE | DailyConvCashDistCreationDate | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| CREATION_DATE | DailyConversionTypeScheduleCreationDate | — |
| DESCRIPTION | DailyConvCashDistDescription | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| DESCRIPTION | DailyConversionTypeScheduleDescription | — |
| DESCRIPTION | ExchConvTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConvCashDistEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeScheduleEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConvCashDistEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeScheduleEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConvCashDistFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeScheduleFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConvCashDistFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeScheduleFemRateTypeCode | — |
| FEM_SCENARIO | DailyConvCashDistFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeScheduleFemScenario | — |
| FEM_TIMEFRAME | DailyConvCashDistFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeScheduleFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConvCashDistLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | DailyConversionTypeScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConvCashDistLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | DailyConversionTypeScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConvCashDistLastUpdatedBy | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | DailyConversionTypeScheduleLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConvCashDistObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeScheduleObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PIVOT_CURRENCY_CODE | DailyConvCashDistPivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeSchedulePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | ExchConvTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConvCashDistSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeScheduleSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConvCashDistUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConversionTypeScheduleUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_CONVERSION_TYPE | ExchConvTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConvCashDistUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeScheduleUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 5/59)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConvCashDistConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeScheduleConversionType | — |
| CONVERSION_TYPE | ExchConvTypeConversionType | — |
| CREATED_BY | DailyConvCashDistCreatedBy | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATED_BY | DailyConversionTypeScheduleCreatedBy | — |
| CREATION_DATE | DailyConvCashDistCreationDate | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| CREATION_DATE | DailyConversionTypeScheduleCreationDate | — |
| DESCRIPTION | DailyConvCashDistDescription | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| DESCRIPTION | DailyConversionTypeScheduleDescription | — |
| DESCRIPTION | ExchConvTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConvCashDistEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeScheduleEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConvCashDistEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeScheduleEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConvCashDistFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeScheduleFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConvCashDistFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeScheduleFemRateTypeCode | — |
| FEM_SCENARIO | DailyConvCashDistFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeScheduleFemScenario | — |
| FEM_TIMEFRAME | DailyConvCashDistFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeScheduleFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConvCashDistLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | DailyConversionTypeScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConvCashDistLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | DailyConversionTypeScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConvCashDistLastUpdatedBy | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | DailyConversionTypeScheduleLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConvCashDistObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeScheduleObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PIVOT_CURRENCY_CODE | DailyConvCashDistPivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeSchedulePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | ExchConvTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConvCashDistSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeScheduleSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConvCashDistUserConversionType | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeScheduleUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_CONVERSION_TYPE | ExchConvTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConvCashDistUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeScheduleUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[receipthistorydistributionpvo|ReceiptHistoryDistributionPVO]] (AR · BICC: 4/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CONVERSION_TYPE | HistoryDailyRateConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATED_BY | HistoryDailyRateCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| CREATION_DATE | HistoryDailyRateCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| DESCRIPTION | HistoryDailyRateDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | HistoryDailyRateEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | HistoryDailyRateEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_ENABLED_FLAG | HistoryDailyRateFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | HistoryDailyRateFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_SCENARIO | HistoryDailyRateFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| FEM_TIMEFRAME | HistoryDailyRateFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | HistoryDailyRateLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | HistoryDailyRateLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | HistoryDailyRateLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | HistoryDailyRateObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | HistoryDailyRatePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| SECURITY_FLAG | HistoryDailyRateSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_CONVERSION_TYPE | HistoryDailyRateUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | HistoryDailyRateUserOverrideCrossRateFlag | — |

### [[receipthistorypvo|ReceiptHistoryPVO]] (AR · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConvTypeConversionType | — |
| CREATED_BY | DailyConvTypeCreatedBy | — |
| CREATION_DATE | DailyConvTypeCreationDate | — |
| DESCRIPTION | DailyConvTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConvTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConvTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConvTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConvTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConvTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConvTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConvTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConvTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConvTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConvTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConvTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConvTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConvTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConvTypeUserOverrideCrossRateFlag | — |

### [[revenuedistributionpvo|RevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ContCurrRevRateTypePEOConversionType | — |
| CONVERSION_TYPE | LedgerCurrRateTypePEOConversionType | — |
| CONVERSION_TYPE | ProjCurrRateTypePEOConversionType | — |
| DESCRIPTION | ContCurrRevRateTypePEODescription | — |
| DESCRIPTION | LedgerCurrRateTypePEODescription | — |
| DESCRIPTION | ProjCurrRateTypePEODescription | — |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[sourcingcostfactorpvo|SourcingCostFactorPVO]] (PO · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | ✅ |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | ✅ |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | ✅ |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | ✅ |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | ✅ |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | ✅ |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | ✅ |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | ✅ |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | ✅ |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | ✅ |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | ✅ |

### [[sourcingobjectivenegotiationpvo|SourcingObjectiveNegotiationPVO]] (PO · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ProgramDailyConversionTypePEOConversionType | — |
| DESCRIPTION | ProgramDailyConversionTypePEODescription | — |
| OBJECT_VERSION_NUMBER | ProgramDailyConversionTypePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ProgramDailyConversionTypePEOUserConversionType | ✅ |

### [[sourcingprogramheaderpvo|SourcingProgramHeaderPVO]] (PO · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ProgramDailyConversionTypePEOConversionType | — |
| DESCRIPTION | ProgramDailyConversionTypePEODescription | — |
| OBJECT_VERSION_NUMBER | ProgramDailyConversionTypePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ProgramDailyConversionTypePEOUserConversionType | ✅ |

### [[sourcingprogramobjectivepvo|SourcingProgramObjectivePVO]] (PO · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ProgramDailyConversionTypePEOConversionType | — |
| DESCRIPTION | ProgramDailyConversionTypePEODescription | — |
| OBJECT_VERSION_NUMBER | ProgramDailyConversionTypePEOObjectVersionNumber | — |
| USER_CONVERSION_TYPE | ProgramDailyConversionTypePEOUserConversionType | ✅ |

### [[sourcingrequirementandattributepvo|SourcingRequirementAndAttributePVO]] (PO · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeNegoHdrLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeNegoHdrLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeNegoHdrLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeNegoHdrObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |

### [[subledgerjournaldistributionpvo|SubledgerJournalDistributionPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | ConversionTypeXlalineConversionType | — |
| CONVERSION_TYPE | DailyConvConversionType | — |
| DESCRIPTION | ConversionTypeXlalineDescription | — |
| DESCRIPTION | DailyConvDescription | — |
| ENABLE_CROSS_RATE_FLAG | ConversionTypeXlalineEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConvEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | ConversionTypeXlalineEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConvEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | ConversionTypeXlalineFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConvFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | ConversionTypeXlalineFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConvFemRateTypeCode | — |
| FEM_SCENARIO | ConversionTypeXlalineFemScenario | — |
| FEM_SCENARIO | DailyConvFemScenario | — |
| FEM_TIMEFRAME | ConversionTypeXlalineFemTimeframe | — |
| FEM_TIMEFRAME | DailyConvFemTimeframe | — |
| OBJECT_VERSION_NUMBER | ConversionTypeXlalineObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| PIVOT_CURRENCY_CODE | ConversionTypeXlalinePivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConvPivotCurrencyCode | — |
| SECURITY_FLAG | ConversionTypeXlalineSecurityFlag | — |
| SECURITY_FLAG | DailyConvSecurityFlag | — |
| USER_CONVERSION_TYPE | ConversionTypeXlalineUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConvUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | ConversionTypeXlalineUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConvUserOverrideCrossRateFlag | — |

### [[transactionbatchpvo|TransactionBatchPVO]] (OTHER · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactioninitheaderpvo|TransactionInitHeaderPVO]] (OTHER · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | ✅ |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[transactionrectheaderpvo|TransactionRectHeaderPVO]] (OTHER · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeConversionType | — |
| CREATED_BY | DailyConversionTypeCreatedBy | — |
| CREATION_DATE | DailyConversionTypeCreationDate | — |
| DESCRIPTION | DailyConversionTypeDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeFemTimeframe | — |
| LAST_UPDATE_DATE | DailyConversionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DailyConversionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | DailyConversionTypeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypePivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeUserOverrideCrossRateFlag | — |

### [[unlockednegotiationresponseheaderpvo|UnlockedNegotiationResponseHeaderPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeResHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| DESCRIPTION | DailyConversionTypeResHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeResHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeResHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeResHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeResHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeResHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeResHdrFemTimeframe | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeNegoHdrObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeResHdrObjectVersionNumber | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeResHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeResHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConversionTypeResHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeResHdrUserOverrideCrossRateFlag | — |

### [[unlockednegotiationresponselinepvo|UnlockedNegotiationResponseLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONVERSION_TYPE | DailyConversionTypeNegoHdrConversionType | — |
| CONVERSION_TYPE | DailyConversionTypeResHdrConversionType | — |
| DESCRIPTION | DailyConversionTypeNegoHdrDescription | — |
| DESCRIPTION | DailyConversionTypeResHdrDescription | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrEnableCrossRateFlag | — |
| ENABLE_CROSS_RATE_FLAG | DailyConversionTypeResHdrEnableCrossRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeNegoHdrEnforceInverseRateFlag | — |
| ENFORCE_INVERSE_RATE_FLAG | DailyConversionTypeResHdrEnforceInverseRateFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeNegoHdrFemEnabledFlag | — |
| FEM_ENABLED_FLAG | DailyConversionTypeResHdrFemEnabledFlag | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeNegoHdrFemRateTypeCode | — |
| FEM_RATE_TYPE_CODE | DailyConversionTypeResHdrFemRateTypeCode | — |
| FEM_SCENARIO | DailyConversionTypeNegoHdrFemScenario | — |
| FEM_SCENARIO | DailyConversionTypeResHdrFemScenario | — |
| FEM_TIMEFRAME | DailyConversionTypeNegoHdrFemTimeframe | — |
| FEM_TIMEFRAME | DailyConversionTypeResHdrFemTimeframe | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeNegoHdrObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DailyConversionTypeResHdrObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeNegoHdrPivotCurrencyCode | — |
| PIVOT_CURRENCY_CODE | DailyConversionTypeResHdrPivotCurrencyCode | — |
| SECURITY_FLAG | DailyConversionTypeNegoHdrSecurityFlag | — |
| SECURITY_FLAG | DailyConversionTypeResHdrSecurityFlag | — |
| USER_CONVERSION_TYPE | DailyConversionTypeNegoHdrUserConversionType | — |
| USER_CONVERSION_TYPE | DailyConversionTypeResHdrUserConversionType | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeNegoHdrUserOverrideCrossRateFlag | — |
| USER_OVERRIDE_CROSS_RATE_FLAG | DailyConversionTypeResHdrUserOverrideCrossRateFlag | — |
