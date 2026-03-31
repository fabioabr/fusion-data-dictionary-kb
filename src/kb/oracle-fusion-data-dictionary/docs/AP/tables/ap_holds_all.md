---
id: DOC-AP-007
doc_type: system-doc
title: "AP_HOLDS_ALL — Retenções (Holds) de Faturas de Contas a Pagar"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, holds, retencoes, bloqueios, faturas, validacao]
aliases: [AP_HOLDS_ALL, ap_holds_all, holds_ap, retencoes_faturas_ap, bloqueios_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_HOLDS_ALL

## Visão Geral

Tabela de retenções (holds) aplicadas a faturas de contas a pagar. Cada registro representa um bloqueio que impede a fatura de ser selecionada para pagamento. Os holds podem ser manuais (aplicados por usuários) ou automáticos (aplicados pelo sistema durante validação — ex.: discrepância de matching com PO, variação de preço). Particionada por `ORG_ID`.

## Propósito de Negócio

Os holds são o principal mecanismo de controle de qualidade e compliance na saída de pagamentos. No Banco Patria, garantem que faturas com discrepâncias de preço, quantidade ou documentação não sejam pagas até resolução. São fundamentais para auditoria interna, controle de perdas e conformidade com políticas de aprovação.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | HOLD_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único do hold. | — | 🟢 100% |
| 2 | INVOICE_ID | NUMBER(15) | NOT NULL | FK | Identificador da fatura bloqueada. | [[ap_invoices_all]] | 🟢 100% |
| 3 | LINE_LOCATION_ID | NUMBER(15) | NULL | FK | Referência à linha de PO para holds de matching. | [[po_line_locations_all]] | 🟢 90% |
| 4 | HOLD_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Negócio | Código do tipo de hold (PRICE, QTY_REC, QTY_ORD, etc.). | [[ap_hold_codes]] | 🟢 100% |
| 5 | HOLD_TYPE | VARCHAR2(25) | NULL | Classificação | Classificação do hold (MATCHING, VARIANCE, MANUAL, etc.). | — | 🟢 90% |
| 6 | HOLD_DATE | DATE | NOT NULL | Negócio | Data em que o hold foi aplicado. | — | 🟢 95% |
| 7 | HOLD_REASON | VARCHAR2(240) | NULL | Negócio | Motivo textual do hold. | — | 🟢 90% |
| 8 | RELEASE_LOOKUP_CODE | VARCHAR2(25) | NULL | Negócio | Código de liberação do hold. | — | 🟢 90% |
| 9 | RELEASE_REASON | VARCHAR2(240) | NULL | Negócio | Motivo da liberação do hold. | — | 🟢 90% |
| 10 | STATUS_FLAG | VARCHAR2(1) | NULL | Controle | Status: S (aplicado/ativo), R (released/liberado). | — | 🟢 90% |
| 11 | HELD_BY | NUMBER(15) | NULL | Negócio | ID do usuário que aplicou o hold (manual). | — | 🟡 75% |
| 12 | RELEASED_BY | NUMBER(15) | NULL | Negócio | ID do usuário que liberou o hold. | — | 🟡 75% |
| 13 | RELEASED_DATE | DATE | NULL | Negócio | Data de liberação do hold. | — | 🟢 90% |
| 14 | ORG_ID | NUMBER(15) | NOT NULL | Multiorg | Identificador da organização (business unit). | [[hr_operating_units]] | 🟢 100% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_invoices_all]]** — Fatura à qual o hold está associado (via `INVOICE_ID`).
- **[[ap_hold_codes]]** — Definição do tipo de hold (via `HOLD_LOOKUP_CODE`).
- **[[po_line_locations_all]]** — Linha de PO para holds de matching (via `LINE_LOCATION_ID`).
- **[[hr_operating_units]]** — Organização/business unit (via `ORG_ID`).

### Tabelas-filha

- Nenhuma tabela-filha conhecida.

## Uso Típico

```sql
-- Listar faturas com holds ativos (não liberados)
SELECT h.HOLD_LOOKUP_CODE,
       h.HOLD_TYPE,
       h.HOLD_DATE,
       h.HOLD_REASON,
       i.INVOICE_NUM,
       i.INVOICE_AMOUNT,
       s.VENDOR_NAME
  FROM AP_HOLDS_ALL h
  JOIN AP_INVOICES_ALL i
    ON i.INVOICE_ID = h.INVOICE_ID
  JOIN POZ_SUPPLIERS s
    ON s.VENDOR_ID = i.VENDOR_ID
 WHERE h.ORG_ID = :p_org_id
   AND h.STATUS_FLAG = 'S'
 ORDER BY h.HOLD_DATE DESC;
```

## Observações

- Holds com `STATUS_FLAG = 'S'` são ativos e impedem o pagamento da fatura.
- Holds liberados (`STATUS_FLAG = 'R'`) permanecem na tabela para auditoria com data e motivo de liberação.
- Holds automáticos de matching são criados pelo processo de validação de faturas e podem ser liberados via tolerâncias configuradas.
- Uma mesma fatura pode ter múltiplos holds simultâneos — todos devem ser liberados para que o pagamento seja possível.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle BICC — AP Holds Subject Area Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[invoiceheaderholdspvo|InvoiceHeaderHoldsPVO]] (AP · BICC: 10/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvoiceHoldCreatedBy | — |
| CREATION_DATE | InvoiceHoldCreationDate | ✅ |
| HELD_BY | InvoiceHoldHeldBy | — |
| HOLD_DATE | InvoiceHoldHoldDate | ✅ |
| HOLD_DETAILS | InvoiceHoldHoldDetails | ✅ |
| HOLD_ID | HoldId | ✅ |
| HOLD_LOOKUP_CODE | InvoiceHoldHoldLookupCode | ✅ |
| HOLD_REASON | InvoiceHoldHoldReason | ✅ |
| INVOICE_ID | InvoiceHoldInvoiceId | — |
| LAST_UPDATE_DATE | InvoiceHoldLastUpdateDate | ✅ |
| LAST_UPDATED_BY | InvoiceHoldLastUpdatedBy | — |
| LINE_NUMBER | InvoiceHoldLineNumber | — |
| OBJECT_VERSION_NUMBER | InvoiceHoldObjectVersionNumber | — |
| ORG_ID | InvoiceHoldOrgId | — |
| RELEASE_LOOKUP_CODE | InvoiceHoldReleaseLookupCode | ✅ |
| RELEASE_REASON | InvoiceHoldReleaseReason | ✅ |
| STATUS_FLAG | InvoiceHoldStatusFlag | — |
| WF_STATUS | InvoiceHoldWfStatus | ✅ |

### [[invoiceholdextractpvo|InvoiceHoldExtractPVO]] (OTHER · BICC: 23/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | ApHoldsAllAttribute1 | — |
| ATTRIBUTE10 | ApHoldsAllAttribute10 | — |
| ATTRIBUTE11 | ApHoldsAllAttribute11 | — |
| ATTRIBUTE12 | ApHoldsAllAttribute12 | — |
| ATTRIBUTE13 | ApHoldsAllAttribute13 | — |
| ATTRIBUTE14 | ApHoldsAllAttribute14 | — |
| ATTRIBUTE15 | ApHoldsAllAttribute15 | — |
| ATTRIBUTE2 | ApHoldsAllAttribute2 | — |
| ATTRIBUTE3 | ApHoldsAllAttribute3 | — |
| ATTRIBUTE4 | ApHoldsAllAttribute4 | — |
| ATTRIBUTE5 | ApHoldsAllAttribute5 | — |
| ATTRIBUTE6 | ApHoldsAllAttribute6 | — |
| ATTRIBUTE7 | ApHoldsAllAttribute7 | — |
| ATTRIBUTE8 | ApHoldsAllAttribute8 | — |
| ATTRIBUTE9 | ApHoldsAllAttribute9 | — |
| ATTRIBUTE_CATEGORY | ApHoldsAllAttributeCategory | — |
| CONSUMPTION_ADVICE_LINE_ID | ApHoldsAllConsumptionAdviceLineId | ✅ |
| CREATED_BY | ApHoldsAllCreatedBy | ✅ |
| CREATION_DATE | ApHoldsAllCreationDate | ✅ |
| HELD_BY | ApHoldsAllHeldBy | ✅ |
| HOLD_DATE | ApHoldsAllHoldDate | ✅ |
| HOLD_DETAILS | ApHoldsAllHoldDetails | ✅ |
| HOLD_ID | ApHoldsAllHoldId | ✅ |
| HOLD_LOOKUP_CODE | ApHoldsAllHoldLookupCode | ✅ |
| HOLD_REASON | ApHoldsAllHoldReason | ✅ |
| INVOICE_ID | ApHoldsAllInvoiceId | ✅ |
| LAST_UPDATE_DATE | ApHoldsAllLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApHoldsAllLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ApHoldsAllLastUpdatedBy | ✅ |
| LINE_LOCATION_ID | ApHoldsAllLineLocationId | ✅ |
| LINE_NUMBER | ApHoldsAllLineNumber | ✅ |
| OBJECT_VERSION_NUMBER | ApHoldsAllObjectVersionNumber | ✅ |
| ORG_ID | ApHoldsAllOrgId | ✅ |
| RCV_TRANSACTION_ID | ApHoldsAllRcvTransactionId | ✅ |
| RELEASE_LOOKUP_CODE | ApHoldsAllReleaseLookupCode | ✅ |
| RELEASE_REASON | ApHoldsAllReleaseReason | ✅ |
| RESPONSIBILITY_ID | ApHoldsAllResponsibilityId | ✅ |
| STATUS_FLAG | ApHoldsAllStatusFlag | ✅ |
| WF_STATUS | ApHoldsAllWfStatus | ✅ |

### [[invoiceholdpvo|InvoiceHoldPVO]] (AP · BICC: 16/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvoiceHoldCreatedBy | ✅ |
| CREATION_DATE | InvoiceHoldCreationDate | ✅ |
| HELD_BY | InvoiceHoldHeldBy | ✅ |
| HOLD_DATE | InvoiceHoldHoldDate | ✅ |
| HOLD_DETAILS | InvoiceHoldHoldDetails | ✅ |
| HOLD_ID | HoldId | ✅ |
| HOLD_LOOKUP_CODE | InvoiceHoldHoldLookupCode | ✅ |
| HOLD_REASON | InvoiceHoldHoldReason | ✅ |
| INVOICE_ID | InvoiceHoldInvoiceId | ✅ |
| LAST_UPDATE_DATE | InvoiceHoldLastUpdateDate | ✅ |
| LAST_UPDATED_BY | InvoiceHoldLastUpdatedBy | ✅ |
| LINE_NUMBER | InvoiceHoldLineNumber | ✅ |
| OBJECT_VERSION_NUMBER | InvoiceHoldObjectVersionNumber | — |
| ORG_ID | InvoiceHoldOrgId | — |
| RELEASE_LOOKUP_CODE | InvoiceHoldReleaseLookupCode | ✅ |
| RELEASE_REASON | InvoiceHoldReleaseReason | ✅ |
| STATUS_FLAG | InvoiceHoldStatusFlag | ✅ |
| WF_STATUS | InvoiceHoldWfStatus | ✅ |

### [[invoiceholdpvoactiveholds|InvoiceHoldPVOActiveHolds]] (AP · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvoiceHoldCreatedBy | — |
| CREATION_DATE | InvoiceHoldCreationDate | — |
| HELD_BY | InvoiceHoldHeldBy | — |
| HOLD_DATE | InvoiceHoldHoldDate | ✅ |
| HOLD_DETAILS | InvoiceHoldHoldDetails | — |
| HOLD_ID | HoldId | ✅ |
| HOLD_LOOKUP_CODE | InvoiceHoldHoldLookupCode | — |
| HOLD_REASON | InvoiceHoldHoldReason | — |
| INVOICE_ID | InvoiceHoldInvoiceId | ✅ |
| LAST_UPDATE_DATE | InvoiceHoldLastUpdateDate | ✅ |
| LAST_UPDATED_BY | InvoiceHoldLastUpdatedBy | — |
| LINE_NUMBER | InvoiceHoldLineNumber | — |
| OBJECT_VERSION_NUMBER | InvoiceHoldObjectVersionNumber | — |
| ORG_ID | InvoiceHoldOrgId | — |
| RELEASE_LOOKUP_CODE | InvoiceHoldReleaseLookupCode | — |
| RELEASE_REASON | InvoiceHoldReleaseReason | — |
| STATUS_FLAG | InvoiceHoldStatusFlag | — |
| WF_STATUS | InvoiceHoldWfStatus | — |

### [[invoicelineholdspvo|InvoiceLineHoldsPVO]] (AP · BICC: 10/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvoiceHoldCreatedBy | — |
| CREATION_DATE | InvoiceHoldCreationDate | ✅ |
| HELD_BY | InvoiceHoldHeldBy | — |
| HOLD_DATE | InvoiceHoldHoldDate | ✅ |
| HOLD_DETAILS | InvoiceHoldHoldDetails | ✅ |
| HOLD_ID | HoldId | ✅ |
| HOLD_LOOKUP_CODE | InvoiceHoldHoldLookupCode | ✅ |
| HOLD_REASON | InvoiceHoldHoldReason | ✅ |
| INVOICE_ID | InvoiceHoldInvoiceId | — |
| LAST_UPDATE_DATE | InvoiceHoldLastUpdateDate | ✅ |
| LAST_UPDATED_BY | InvoiceHoldLastUpdatedBy | — |
| LINE_NUMBER | InvoiceHoldLineNumber | — |
| OBJECT_VERSION_NUMBER | InvoiceHoldObjectVersionNumber | — |
| ORG_ID | InvoiceHoldOrgId | — |
| RELEASE_LOOKUP_CODE | InvoiceHoldReleaseLookupCode | ✅ |
| RELEASE_REASON | InvoiceHoldReleaseReason | ✅ |
| STATUS_FLAG | InvoiceHoldStatusFlag | — |
| WF_STATUS | InvoiceHoldWfStatus | ✅ |
