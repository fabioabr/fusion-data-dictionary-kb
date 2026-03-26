---
id: DOC-AP-003
doc_type: system-doc
title: "AP_BATCHES_ALL — Lotes de Faturas de Contas a Pagar"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, batches, lotes, faturas, invoices]
aliases: [AP_BATCHES_ALL, ap_batches_all, batches_ap, lotes_faturas_ap, invoice_batches]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_BATCHES_ALL

## Visão Geral

Tabela de lotes (batches) de faturas de contas a pagar. Cada registro representa um agrupamento lógico de faturas inseridas em conjunto no sistema, permitindo controle de entrada, validação e rastreamento em bloco. A tabela é particionada por organização (`ORG_ID`), seguindo o padrão `_ALL` do Oracle Fusion.

## Propósito de Negócio

Os lotes de faturas facilitam a entrada em massa de documentos de fornecedores, permitindo validação e aprovação em grupo. No Banco Patria, os batches são usados para processar volumes de notas fiscais de fornecedores de serviços e produtos, garantindo rastreabilidade do processo de entrada e controle de totais por lote.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BATCH_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único do lote. | — | 🟢 100% |
| 2 | BATCH_NAME | VARCHAR2(50) | NOT NULL | Negócio | Nome do lote de faturas. | — | 🟢 100% |
| 3 | BATCH_DATE | DATE | NOT NULL | Negócio | Data do lote. | — | 🟢 95% |
| 4 | INVOICE_COUNT | NUMBER(15) | NULL | Negócio | Quantidade de faturas no lote (controle). | — | 🟢 90% |
| 5 | INVOICE_TOTAL | NUMBER | NULL | Negócio | Valor total das faturas do lote (controle). | — | 🟢 90% |
| 6 | ACTUAL_INVOICE_COUNT | NUMBER(15) | NULL | Negócio | Contagem real de faturas inseridas. | — | 🟡 75% |
| 7 | ACTUAL_INVOICE_TOTAL | NUMBER | NULL | Negócio | Valor real totalizado das faturas inseridas. | — | 🟡 75% |
| 8 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NULL | Negócio | Código da moeda das faturas do lote. | [[fnd_currencies]] | 🟢 90% |
| 9 | PAYMENT_CURRENCY_CODE | VARCHAR2(15) | NULL | Negócio | Código da moeda de pagamento. | [[fnd_currencies]] | 🟡 75% |
| 10 | ORG_ID | NUMBER(15) | NOT NULL | Multiorg | Identificador da organização (business unit). | [[hr_operating_units]] | 🟢 100% |
| 11 | HOLD_LOOKUP_CODE | VARCHAR2(25) | NULL | Controle | Código de hold aplicado ao lote. | — | 🟡 70% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 13 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[hr_operating_units]]** — Organização/business unit (via `ORG_ID`).
- **[[fnd_currencies]]** — Moeda das faturas e pagamentos (via `INVOICE_CURRENCY_CODE`, `PAYMENT_CURRENCY_CODE`).

### Tabelas-filha

- **[[ap_invoices_all]]** — Faturas pertencentes ao lote (via `BATCH_ID`).

## Uso Típico

```sql
-- Listar lotes com contagem e valor total de faturas
SELECT ab.BATCH_NAME,
       ab.BATCH_DATE,
       ab.INVOICE_COUNT,
       ab.INVOICE_TOTAL,
       ab.ACTUAL_INVOICE_COUNT,
       ab.ACTUAL_INVOICE_TOTAL
  FROM AP_BATCHES_ALL ab
 WHERE ab.ORG_ID = :p_org_id
   AND ab.BATCH_DATE >= TRUNC(SYSDATE) - 90
 ORDER BY ab.BATCH_DATE DESC;
```

## Observações

- Os campos `INVOICE_COUNT` / `INVOICE_TOTAL` são valores de controle informados na criação do lote; `ACTUAL_*` são calculados pelo sistema.
- Diferenças entre totais de controle e reais indicam faturas pendentes de inserção ou exclusão.
- Tabela particionada por `ORG_ID` — sempre filtrar por organização em consultas.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle BICC — AP Invoice Batches Subject Area Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
