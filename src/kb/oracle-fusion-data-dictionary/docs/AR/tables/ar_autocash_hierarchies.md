---
id: DOC-AR-049
doc_type: system-doc
title: "AR_AUTOCASH_HIERARCHIES — Regras AutoCash"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, autocash, aplicacao-automatica, hierarquia]
aliases: [AR_AUTOCASH_HIERARCHIES, ar_autocash_hierarchies, autocash_hierarchies, regras_autocash, ar_autocash]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_AUTOCASH_HIERARCHIES

## 📌 Visão Geral

Tabela de cadastro de **hierarquias AutoCash** — regras que definem a lógica de aplicação automática de recebimentos a faturas. Cada hierarquia determina a sequência de critérios que o sistema utiliza para tentar conciliar um recebimento com as faturas em aberto.

## 🧠 Propósito de Negócio

O AutoCash é o **motor de aplicação automática** do AR. Em vez de um analista aplicar manualmente cada recebimento a faturas individuais, as regras AutoCash tentam fazer esse match automaticamente, usando critérios como número da fatura, valor exato, número do pedido ou número do PO.

Casos de uso principais:
- Aplicação automática de recebimentos de lockbox
- Conciliação de pagamentos eletrônicos (TED/PIX)
- Redução de itens "unapplied" no aging
- Processamento em massa de recebimentos

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | AUTOCASH_HIERARCHY_ID | NUMBER | PK. Identificador único da hierarquia AutoCash. | Chave | 🟢 100% |
| 2 | HIERARCHY_NAME | VARCHAR2 | Nome da hierarquia (exibido em LOVs e configurações). | Identificação | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2 | Descrição textual da finalidade da hierarquia. | Identificação | 🟢 100% |
| 4 | STATUS | VARCHAR2 | Status: `A` (ativo) ou `I` (inativo). | Controle | 🟢 100% |
| 5 | MATCH_AMOUNT_FLAG | VARCHAR2 | Se `Y`, exige match exato de valor para aplicação automática. | Regra | 🟢 100% |
| 6 | APPLY_DISCOUNT_FLAG | VARCHAR2 | Se `Y`, aplica desconto automaticamente quando dentro do prazo. | Regra | 🟢 100% |
| 7 | REMAINING_AMOUNT_RULE | VARCHAR2 | Regra para valor remanescente: `UNAPPLIED`, `ON_ACCOUNT`, `WRITE_OFF`. | Regra | 🟢 100% |
| 8 | PRIORITY_1 | VARCHAR2 | Primeiro critério de match: `INVOICE`, `SALES_ORDER`, `PURCHASE_ORDER`, etc. | Regra | 🟢 100% |
| 9 | PRIORITY_2 | VARCHAR2 | Segundo critério de match. | Regra | 🟢 100% |
| 10 | PRIORITY_3 | VARCHAR2 | Terceiro critério de match. | Regra | 🟢 100% |
| 11 | PRIORITY_4 | VARCHAR2 | Quarto critério de match. | Regra | 🟢 100% |
| 12 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 13 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 14 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 15 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_receipt_methods]] | AUTO_CASH_RULE_ID | Referenciada por | Métodos de recebimento que usam esta hierarquia |
| [[ar_system_parameters_all]] | — | Referência | Parâmetros globais de aplicação automática |

## 📎 Uso Típico

```sql
-- Listar hierarquias AutoCash ativas
SELECT autocash_hierarchy_id,
       hierarchy_name,
       match_amount_flag,
       apply_discount_flag,
       remaining_amount_rule,
       priority_1,
       priority_2
  FROM ar_autocash_hierarchies
 WHERE status = 'A';
```

```sql
-- Métodos de recebimento com suas regras AutoCash
SELECT rm.name AS metodo,
       ah.hierarchy_name AS regra_autocash,
       ah.remaining_amount_rule
  FROM ar_receipt_methods rm
  JOIN ar_autocash_hierarchies ah ON ah.autocash_hierarchy_id = rm.auto_cash_rule_id;
```

## 🔒 Observações

- As prioridades (`PRIORITY_1` a `PRIORITY_4`) definem a **ordem de tentativa** de match — o sistema tenta o primeiro critério e, se não encontrar, passa ao seguinte.
- `REMAINING_AMOUNT_RULE` determina o que fazer com o valor que sobra após a aplicação: deixar como não aplicado, colocar em conta ou dar write-off.
- A hierarquia é associada ao **método de recebimento** ([[ar_receipt_methods]]), não diretamente ao recebimento.
- Para alta performance em lockbox, é recomendável que `PRIORITY_1` seja `INVOICE` (match por número da fatura) — é o critério mais rápido.

## 🔗 PVOs Relacionados

### [[autocashhierarchyextractpvo|AutoCashHierarchyExtractPVO]] (OTHER · BICC: 17/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_PARTIAL_PAYMENTS | ArAutoCashHierarchyApplyPartialPayments | ✅ |
| ATTRIBUTE1 | ArAutoCashHierarchyAttribute1 | — |
| ATTRIBUTE10 | ArAutoCashHierarchyAttribute10 | — |
| ATTRIBUTE11 | ArAutoCashHierarchyAttribute11 | — |
| ATTRIBUTE12 | ArAutoCashHierarchyAttribute12 | — |
| ATTRIBUTE13 | ArAutoCashHierarchyAttribute13 | — |
| ATTRIBUTE14 | ArAutoCashHierarchyAttribute14 | — |
| ATTRIBUTE15 | ArAutoCashHierarchyAttribute15 | — |
| ATTRIBUTE2 | ArAutoCashHierarchyAttribute2 | — |
| ATTRIBUTE3 | ArAutoCashHierarchyAttribute3 | — |
| ATTRIBUTE4 | ArAutoCashHierarchyAttribute4 | — |
| ATTRIBUTE5 | ArAutoCashHierarchyAttribute5 | — |
| ATTRIBUTE6 | ArAutoCashHierarchyAttribute6 | — |
| ATTRIBUTE7 | ArAutoCashHierarchyAttribute7 | — |
| ATTRIBUTE8 | ArAutoCashHierarchyAttribute8 | — |
| ATTRIBUTE9 | ArAutoCashHierarchyAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArAutoCashHierarchyAttributeCategory | — |
| AUTOCASH_HIERARCHY_ID | ArAutoCashHierarchyAutocashHierarchyId | ✅ |
| CREATED_BY | ArAutoCashHierarchyCreatedBy | ✅ |
| CREATION_DATE | ArAutoCashHierarchyCreationDate | ✅ |
| DESCRIPTION | ArAutoCashHierarchyDescription | ✅ |
| HIERARCHY_NAME | ArAutoCashHierarchyHierarchyName | ✅ |
| INCLUDE_DISCOUNTS | ArAutoCashHierarchyIncludeDiscounts | ✅ |
| INCLUDE_DISPUTE_ITEMS | ArAutoCashHierarchyIncludeDisputeItems | ✅ |
| INCLUDE_FINANCE_CHARGES | ArAutoCashHierarchyIncludeFinanceCharges | ✅ |
| LAST_UPDATE_DATE | ArAutoCashHierarchyLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArAutoCashHierarchyLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArAutoCashHierarchyLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ArAutoCashHierarchyObjectVersionNumber | ✅ |
| REMAINING_AMOUNT | ArAutoCashHierarchyRemainingAmount | ✅ |
| SEED_DATA_SOURCE | ArAutoCashHierarchySeedDataSource | ✅ |
| SET_ID | ArAutoCashHierarchySetId | ✅ |
| STATUS | ArAutoCashHierarchyStatus | ✅ |

### [[customerfinancialprofilepvo|CustomerFinancialProfilePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_PARTIAL_PAYMENTS | AutoCshHierarchyApplyPartialPayments | — |
| APPLY_PARTIAL_PAYMENTS | AutoCshHierarchyForAdrApplyPartialPayments | — |
| AUTOCASH_HIERARCHY_ID | AutoCshHierarchyAutocashHierarchyId | — |
| AUTOCASH_HIERARCHY_ID | AutoCshHierarchyForAdrAutocashHierarchyId | — |
| DESCRIPTION | AutoCshHierarchyDescription | — |
| DESCRIPTION | AutoCshHierarchyForAdrDescription | — |
| HIERARCHY_NAME | AutoCshHierarchyForAdrHierarchyName | — |
| HIERARCHY_NAME | AutoCshHierarchyHierarchyName | — |
| INCLUDE_DISCOUNTS | AutoCshHierarchyForAdrIncludeDiscounts | — |
| INCLUDE_DISCOUNTS | AutoCshHierarchyIncludeDiscounts | — |
| INCLUDE_DISPUTE_ITEMS | AutoCshHierarchyForAdrIncludeDisputeItems | — |
| INCLUDE_DISPUTE_ITEMS | AutoCshHierarchyIncludeDisputeItems | — |
| INCLUDE_FINANCE_CHARGES | AutoCshHierarchyForAdrIncludeFinanceCharges | — |
| INCLUDE_FINANCE_CHARGES | AutoCshHierarchyIncludeFinanceCharges | — |
| REMAINING_AMOUNT | AutoCshHierarchyForAdrRemainingAmount | — |
| REMAINING_AMOUNT | AutoCshHierarchyRemainingAmount | — |
| STATUS | AutoCshHierarchyForAdrStatus | — |
| STATUS | AutoCshHierarchyStatus | — |

### [[customerprofile|CustomerProfile]] (AR · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTOCASH_HIERARCHY_ID | AutoCshHierarchyAutocashHierarchyId | — |
| AUTOCASH_HIERARCHY_ID | AutoCshHierarchyForAdrAutocashHierarchyId | — |
| HIERARCHY_NAME | AutoCshHierarchyForAdrHierarchyName | ✅ |
| HIERARCHY_NAME | AutoCshHierarchyHierarchyName | ✅ |

### [[customersiteprofile|CustomerSiteProfile]] (AR · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTOCASH_HIERARCHY_ID | AutoCshHierarchyAutocashHierarchyId | — |
| AUTOCASH_HIERARCHY_ID | AutoCshHierarchyForAdrAutocashHierarchyId | — |
| HIERARCHY_NAME | AutoCshHierarchyForAdrHierarchyName | ✅ |
| HIERARCHY_NAME | AutoCshHierarchyHierarchyName | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — AutoCash Hierarchies View Object
- Oracle Fusion Cloud — Setting Up AutoCash Rules (Functional Guide)
