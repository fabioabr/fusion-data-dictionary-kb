---
id: DOC-AR-056
doc_type: system-doc
title: "AR_LOOKUPS — Valores de Lookup do Contas a Receber"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, lookups, dominio-valores, referencia]
aliases: [AR_LOOKUPS, ar_lookups, ar_lookup_values, lookups_ar, valores_lookup_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_LOOKUPS

## 📌 Visão Geral

View (ou tabela) que centraliza os **valores de lookup** específicos do módulo Accounts Receivable. Lookups são listas de valores de domínio (domain values) utilizadas em campos codificados — status, tipos, categorias, flags — em todo o AR.

## 🧠 Propósito de Negócio

Os lookups são o **dicionário de códigos** do AR. Cada campo codificado (ex: status de uma fatura, tipo de ajuste, método de remessa) referencia um lookup que traduz o código interno em um significado legível para o usuário.

Casos de uso principais:
- Decodificação de campos codificados em relatórios
- Validação de valores permitidos em interfaces
- Customização de listas de valores (LOVs) na UI
- Referência para migrações e integrações

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | LOOKUP_TYPE | VARCHAR2 | PK composta. Tipo do lookup (agrupador de valores). Ex: `INVOICE_TRX_TYPE`, `RECEIPT_STATUS`. | Chave | 🟢 100% |
| 2 | LOOKUP_CODE | VARCHAR2 | PK composta. Código do valor dentro do tipo. Ex: `INV`, `CM`, `DM`. | Chave | 🟢 100% |
| 3 | MEANING | VARCHAR2 | Significado legível do código (exibido na UI). Ex: "Invoice", "Credit Memo". | Identificação | 🟢 100% |
| 4 | DESCRIPTION | VARCHAR2 | Descrição detalhada do valor do lookup. | Identificação | 🟢 100% |
| 5 | ENABLED_FLAG | VARCHAR2 | Indica se o valor está habilitado: `Y`/`N`. | Controle | 🟢 100% |
| 6 | START_DATE_ACTIVE | DATE | Data de início de vigência do valor. | Vigência | 🟢 100% |
| 7 | END_DATE_ACTIVE | DATE | Data de fim de vigência (nulo = sem expiração). | Vigência | 🟢 100% |
| 8 | TAG | VARCHAR2 | Tag auxiliar para classificação ou filtragem. | Classificação | 🟢 100% |
| 9 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 10 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 11 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 12 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ra_customer_trx_all]] | Diversos campos de status/tipo | Referência | Transações usam lookup codes |
| [[ar_adjustments_all]] | STATUS, TYPE | Referência | Ajustes usam lookup codes |
| [[ar_cash_receipts_all]] | STATUS | Referência | Recebimentos usam lookup codes |
| [[fnd_lookup_values]] | LOOKUP_TYPE + LOOKUP_CODE | Origem | View base do framework de lookups |

## 📎 Uso Típico

```sql
-- Listar todos os valores de um tipo de lookup
SELECT lookup_code,
       meaning,
       description,
       enabled_flag
  FROM ar_lookups
 WHERE lookup_type = :p_lookup_type
   AND enabled_flag = 'Y'
 ORDER BY lookup_code;
```

```sql
-- Decodificar status de transação em relatório
SELECT ct.trx_number,
       al.meaning AS status_descricao
  FROM ra_customer_trx_all ct
  JOIN ar_lookups al ON al.lookup_type = 'INVOICE_TRX_STATUS'
                    AND al.lookup_code = ct.status_trx
 WHERE ct.org_id = :p_org_id;
```

## 🔒 Observações

- `AR_LOOKUPS` é tipicamente uma **view** sobre `FND_LOOKUP_VALUES` filtrada para lookups do módulo AR — não é uma tabela física independente.
- Lookup types comuns no AR: `INVOICE_TRX_TYPE`, `RECEIPT_STATUS`, `ADJUSTMENT_TYPE`, `PAYMENT_TERM_TYPE`, `APPROVAL_STATUS`.
- Valores com `ENABLED_FLAG = 'N'` não aparecem em LOVs na interface, mas podem existir em registros históricos.
- O campo `TAG` é utilizado para filtragem contextual — por exemplo, filtrar lookup values que se aplicam apenas a determinados tipos de transação.
- Em migrações, é fundamental validar que os lookup codes utilizados nos dados de origem existem no ambiente de destino.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — AR Lookups View Object
- Oracle Fusion Cloud — Managing Lookup Types (Setup Guide)
