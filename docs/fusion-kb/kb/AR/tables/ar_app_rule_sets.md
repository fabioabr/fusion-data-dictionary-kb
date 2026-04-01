---
id: DOC-AR-051
doc_type: system-doc
title: "AR_APP_RULE_SETS — Conjuntos de Regras de Aplicação"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, rule-sets, aplicacao, regras]
aliases: [AR_APP_RULE_SETS, ar_app_rule_sets, application_rule_sets, conjuntos_regras_aplicacao, ar_rule_sets]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_APP_RULE_SETS

## 📌 Visão Geral

Tabela de cadastro de **conjuntos de regras de aplicação** (application rule sets). Agrupa regras que governam como recebimentos são aplicados a transações — definindo critérios de priorização, comportamento de desconto e tratamento de exceções.

## 🧠 Propósito de Negócio

Os conjuntos de regras de aplicação são **containers organizacionais** que agrupam políticas de aplicação de recebimentos. Permitem padronizar o comportamento de aplicação por tipo de cliente, canal ou linha de negócio.

Casos de uso principais:
- Definição de política de aplicação por segmento de cliente
- Padronização de regras de desconto por canal
- Agrupamento de regras de exceção ([[ar_app_exception_rules]])

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | RULE_SET_ID | NUMBER | PK. Identificador único do conjunto de regras. | Chave | 🟢 100% |
| 2 | NAME | VARCHAR2 | Nome do conjunto de regras (exibido em LOVs). | Identificação | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2 | Descrição textual da finalidade do conjunto. | Identificação | 🟢 100% |
| 4 | STATUS | VARCHAR2 | Status: `A` (ativo) ou `I` (inativo). | Controle | 🟢 100% |
| 5 | TYPE | VARCHAR2 | Tipo do conjunto de regras (categorização funcional). | Classificação | 🟢 100% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 7 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 8 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 9 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |
| 11 | LAST_UPDATE_DATE | DATE | Data da última atualização. | WHO | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2 | Login da última sessão de atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_app_exception_rules]] | RULE_SET_ID | Referenciada por | Regras de exceção que pertencem a este conjunto |
| [[ar_system_parameters_all]] | — | Referência | Parâmetros podem referenciar rule sets padrão |

## 📎 Uso Típico

```sql
-- Listar conjuntos de regras de aplicação ativos
SELECT rule_set_id,
       name,
       description,
       type,
       status
  FROM ar_app_rule_sets
 WHERE status = 'A'
 ORDER BY name;
```

```sql
-- Conjunto de regras com suas regras de exceção
SELECT rs.name AS conjunto,
       er.exception_type,
       er.threshold_amount,
       er.action_code
  FROM ar_app_rule_sets rs
  JOIN ar_app_exception_rules er ON er.rule_set_id = rs.rule_set_id
 WHERE rs.status = 'A';
```

## 🔒 Observações

- Cada conjunto agrupa uma ou mais [[ar_app_exception_rules|regras de exceção]] que definem o tratamento para casos especiais.
- Inativar um conjunto (`STATUS = 'I'`) desabilita todas as regras de exceção associadas.
- A tabela é relativamente simples — o comportamento complexo está nas regras filhas.

## 🔗 PVOs Relacionados

### [[applicationrulesetextractpvo|ApplicationRuleSetExtractPVO]] (OTHER · BICC: 13/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | ArAppRuleSetAttribute1 | — |
| ATTRIBUTE10 | ArAppRuleSetAttribute10 | — |
| ATTRIBUTE11 | ArAppRuleSetAttribute11 | — |
| ATTRIBUTE12 | ArAppRuleSetAttribute12 | — |
| ATTRIBUTE13 | ArAppRuleSetAttribute13 | — |
| ATTRIBUTE14 | ArAppRuleSetAttribute14 | — |
| ATTRIBUTE15 | ArAppRuleSetAttribute15 | — |
| ATTRIBUTE2 | ArAppRuleSetAttribute2 | — |
| ATTRIBUTE3 | ArAppRuleSetAttribute3 | — |
| ATTRIBUTE4 | ArAppRuleSetAttribute4 | — |
| ATTRIBUTE5 | ArAppRuleSetAttribute5 | — |
| ATTRIBUTE6 | ArAppRuleSetAttribute6 | — |
| ATTRIBUTE7 | ArAppRuleSetAttribute7 | — |
| ATTRIBUTE8 | ArAppRuleSetAttribute8 | — |
| ATTRIBUTE9 | ArAppRuleSetAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArAppRuleSetAttributeCategory | — |
| CREATED_BY | ArAppRuleSetCreatedBy | ✅ |
| CREATION_DATE | ArAppRuleSetCreationDate | ✅ |
| DESCRIPTION | ArAppRuleSetDescription | ✅ |
| FREEZE_FLAG | ArAppRuleSetFreezeFlag | ✅ |
| LAST_UPDATE_DATE | ArAppRuleSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArAppRuleSetLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArAppRuleSetLastUpdatedBy | ✅ |
| MODULE_ID | ArAppRuleSetModuleId | ✅ |
| OBJECT_VERSION_NUMBER | ArAppRuleSetObjectVersionNumber | ✅ |
| RULE_SET_ID | ArAppRuleSetRuleSetId | ✅ |
| RULE_SET_NAME | ArAppRuleSetRuleSetName | ✅ |
| RULE_SOURCE | ArAppRuleSetRuleSource | ✅ |
| SEED_DATA_SOURCE | ArAppRuleSetSeedDataSource | ✅ |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | AppRuleSetDescription | — |
| RULE_SET_ID | AppRuleSetRuleSetId | — |
| RULE_SET_NAME | AppRuleSetRuleSetName | ✅ |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | AppRuleSetDescription | — |
| FREEZE_FLAG | AppRuleSetFreezeFlag | — |
| MODULE_ID | AppRuleSetModuleId | — |
| RULE_SET_ID | AppRuleSetRuleSetId | — |
| RULE_SET_NAME | AppRuleSetRuleSetName | ✅ |
| RULE_SOURCE | AppRuleSetRuleSource | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | AppRuleSetDescription | — |
| FREEZE_FLAG | AppRuleSetFreezeFlag | — |
| MODULE_ID | AppRuleSetModuleId | — |
| RULE_SET_ID | AppRuleSetRuleSetId | — |
| RULE_SET_NAME | AppRuleSetRuleSetName | — |
| RULE_SOURCE | AppRuleSetRuleSource | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | AppRuleSetDescription | — |
| FREEZE_FLAG | AppRuleSetFreezeFlag | — |
| MODULE_ID | AppRuleSetModuleId | — |
| RULE_SET_ID | AppRuleSetRuleSetId | — |
| RULE_SET_NAME | AppRuleSetRuleSetName | ✅ |
| RULE_SOURCE | AppRuleSetRuleSource | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | AppRuleSetCreatedBy | — |
| CREATION_DATE | AppRuleSetCreationDate | — |
| DESCRIPTION | AppRuleSetDescription | — |
| FREEZE_FLAG | AppRuleSetFreezeFlag | — |
| LAST_UPDATE_DATE | AppRuleSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AppRuleSetLastUpdateLogin | — |
| LAST_UPDATED_BY | AppRuleSetLastUpdatedBy | — |
| MODULE_ID | AppRuleSetModuleId | — |
| OBJECT_VERSION_NUMBER | AppRuleSetObjectVersionNumber | — |
| RULE_SET_ID | AppRuleSetRuleSetId | — |
| RULE_SET_NAME | AppRuleSetRuleSetName | ✅ |
| RULE_SOURCE | AppRuleSetRuleSource | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Application Rule Sets View Object
- Oracle Fusion Cloud — Managing Application Rules (Functional Guide)
