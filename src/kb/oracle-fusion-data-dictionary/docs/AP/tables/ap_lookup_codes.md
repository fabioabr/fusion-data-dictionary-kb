---
id: DOC-AP-017
doc_type: system-doc
title: "AP_LOOKUP_CODES — Tabela de Lookup do Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - lookup
  - dominio-valores
  - codigos
aliases:
  - AP_LOOKUP_CODES
  - ap_lookup_codes
  - lookup-ap
  - codigos-ap
  - dominio-valores-ap
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_LOOKUP_CODES

## 📌 Visão Geral

Armazena os **códigos de lookup** (domínio de valores) do módulo Accounts Payable. Cada registro representa um par tipo/código com sua descrição, controlando listas de valores válidos para campos como tipo de fatura, grupo de pagamento, tipo de hold, tipo de distribuição e outros. É a tabela de referência para decodificação de códigos usados em diversas tabelas do módulo AP.

> [!note] Lookup legado
> No Oracle Fusion, muitos lookups migraram para `FND_LOOKUP_VALUES` / `FND_LOOKUPS`. Entretanto, `AP_LOOKUP_CODES` ainda é utilizada para lookups específicos do módulo AP herdados do Oracle EBS ou mantidos por compatibilidade.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Validação de domínio:** Garante que campos codificados contenham apenas valores válidos (ex: tipos de fatura, grupos de pagamento).
- **Decodificação em relatórios:** Tradução de códigos internos para descrições legíveis ao usuário.
- **Configuração de listas de valores (LOV):** Alimenta picklists na interface do usuário.
- **Extensibilidade:** Permite adicionar novos valores de lookup sem alterar estrutura de tabelas.
- **Integração e migração:** Referência obrigatória para mapeamento de valores entre sistemas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOOKUP_TYPE | VARCHAR2(25) | NOT NULL | PK | Tipo do lookup (agrupa valores relacionados) | — | 🟢 100% |
| 2 | LOOKUP_CODE | VARCHAR2(25) | NOT NULL | PK | Código do valor dentro do tipo | — | 🟢 100% |
| 3 | DISPLAYED_FIELD | VARCHAR2(80) | NULL | Descrição | Descrição exibida ao usuário (display name) | — | 🟢 100% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição | Descrição detalhada do código | — | 🟢 100% |
| 5 | INACTIVE_DATE | DATE | NULL | Controle | Data de inativação (NULL = ativo) | — | 🟢 100% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indica se o código está habilitado (Y/N) | — | 🟡 75% |
| 7 | START_DATE_ACTIVE | DATE | NULL | Controle | Data de início de vigência | — | 🟡 75% |
| 8 | END_DATE_ACTIVE | DATE | NULL | Controle | Data de fim de vigência | — | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma — tabela de referência raiz.

### Tabelas-filha (FK de saída)
- [[ap_invoices_all]] — via `INVOICE_TYPE_LOOKUP_CODE` (tipo: INVOICE TYPE)
- [[ap_invoices_all]] — via `PAY_GROUP_LOOKUP_CODE` (tipo: PAY GROUP)
- [[ap_invoice_lines_all]] — via `LINE_TYPE_LOOKUP_CODE` (tipo: INVOICE DISTRIBUTION TYPE)
- [[ap_invoice_distributions_all]] — via `LINE_TYPE_LOOKUP_CODE` (tipo: INVOICE DISTRIBUTION TYPE)
- Diversas outras tabelas AP que referenciam campos `*_LOOKUP_CODE`

---

## 📎 Uso Típico

### Listar tipos de fatura disponíveis
```sql
SELECT alc.LOOKUP_CODE, alc.DISPLAYED_FIELD, alc.DESCRIPTION
FROM   AP_LOOKUP_CODES alc
WHERE  alc.LOOKUP_TYPE = 'INVOICE TYPE'
  AND  (alc.INACTIVE_DATE IS NULL OR alc.INACTIVE_DATE > SYSDATE)
ORDER BY alc.DISPLAYED_FIELD;
```

### Decodificar tipo de fatura em relatório
```sql
SELECT ai.INVOICE_NUM, ai.INVOICE_AMOUNT,
       alc.DISPLAYED_FIELD AS tipo_fatura
FROM   AP_INVOICES_ALL ai
JOIN   AP_LOOKUP_CODES alc
  ON   alc.LOOKUP_TYPE = 'INVOICE TYPE'
  AND  alc.LOOKUP_CODE = ai.INVOICE_TYPE_LOOKUP_CODE
WHERE  ai.ORG_ID = :p_org_id;
```

### Lookup types comuns
- `INVOICE TYPE` — Tipos de fatura (STANDARD/CREDIT/DEBIT/PREPAYMENT)
- `INVOICE DISTRIBUTION TYPE` — Tipos de distribuição (ITEM/TAX/FREIGHT)
- `PAY GROUP` — Grupos de pagamento
- `HOLD CODE` — Tipos de hold/retenção
- `NLS TRANSLATION` — Traduções

---

## 🔒 Observações

- A PK composta é `LOOKUP_TYPE` + `LOOKUP_CODE`.
- O campo `INACTIVE_DATE` controla a vigência: registros com data futura ou NULL estão ativos.
- No Oracle Fusion, a tendência é usar `FND_LOOKUP_VALUES` para novos lookups; `AP_LOOKUP_CODES` é mantida para compatibilidade com lookups legados do módulo AP.
- Não confundir com `FND_LOOKUPS` (view) ou `FND_LOOKUP_VALUES_B/TL` (tabelas base do FND).
- Novos valores de lookup podem ser adicionados via configuração sem necessidade de desenvolvimento.

---

## 🔗 PVOs Relacionados

### [[invoicepaymentlookuppvo|InvoicePaymentLookupPVO]] (AP · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | Description | ✅ |
| DISPLAYED_FIELD | DisplayedField | ✅ |
| ENABLED_FLAG | EnabledFlag | — |
| END_DATE_ACTIVE | EndDateActive | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |

### [[invoicetypelookuppvo|InvoiceTypeLookupPVO]] (AP · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | Description | ✅ |
| DISPLAYED_FIELD | DisplayedField | ✅ |
| ENABLED_FLAG | EnabledFlag | — |
| END_DATE_ACTIVE | EndDateActive | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |

### [[paymentmethodlookuppvo|PaymentMethodLookupPVO]] (AP · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | Description | — |
| DISPLAYED_FIELD | DisplayedField | — |
| ENABLED_FLAG | EnabledFlag | — |
| END_DATE_ACTIVE | EndDateActive | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |

### [[reconsummarylinelookuppvo|ReconSummaryLineLookupPVO]] (AP · BICC: 4/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | Description | — |
| DISPLAYED_FIELD | DisplayedField | ✅ |
| ENABLED_FLAG | EnabledFlag | ✅ |
| END_DATE_ACTIVE | EndDateActive | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| START_DATE_ACTIVE | StartDateActive | — |

### [[sourcelookuppvo|SourceLookupPVO]] (AP · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | Description | ✅ |
| DISPLAYED_FIELD | DisplayedField | ✅ |
| ENABLED_FLAG | EnabledFlag | — |
| END_DATE_ACTIVE | EndDateActive | — |
| LOOKUP_CODE | LookupCode | ✅ |
| LOOKUP_TYPE | LookupType | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |

---

## 📚 Referências

- [Oracle Docs — AP_LOOKUP_CODES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/aplookupcodes-10024.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
