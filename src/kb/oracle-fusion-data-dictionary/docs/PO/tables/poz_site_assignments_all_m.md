---
id: DOC-PO-086
doc_type: system-doc
title: "POZ_SITE_ASSIGNMENTS_ALL_M — Atribuições de Sites de Fornecedores"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - supplier-sites
  - site-assignments
  - procurement-bu
aliases:
  - POZ_SITE_ASSIGNMENTS_ALL_M
  - poz_site_assignments_all_m
  - atribuicoes-site-fornecedor
  - site-assignments
  - supplier-site-bu-assignment
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SITE_ASSIGNMENTS_ALL_M

## Visão Geral

Armazena as **atribuições de sites de fornecedores a business units (BUs) e funções de procurement**. Cada registro vincula um site de fornecedor a uma BU específica com um propósito funcional (compras, pagamentos, ou ambos), controlando onde e como o site pode ser utilizado em transações de procurement.

> [!note] Sufixos _ALL_M
> O sufixo `_ALL` indica dados de **todas as business units** (multi-org). O sufixo `_M` indica tabela **merge** (suporta operações de merge/upsert no ETL).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Atribuição de sites a BUs:** Controla em quais business units cada site de fornecedor pode ser utilizado.
- **Segregação funcional:** Define se o site é usado para compras (Purchasing), pagamentos (Payment), ou ambos.
- **Pedidos de compra:** Validação de que o site está atribuído à BU do pedido antes da criação de POs.
- **Contas a pagar:** Validação de que o site está habilitado para pagamento na BU da fatura.
- **Multi-org:** Permite que um mesmo fornecedor tenha configurações diferentes por BU.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SITE_ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da atribuição de site | — | 🟡 75% |
| 2 | VENDOR_SITE_ID | NUMBER(18) | NOT NULL | FK | Identificador do site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 85% |
| 3 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 85% |
| 4 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit de atribuição | [[hr_all_organization_units_f]] | 🟢 85% |
| 5 | PROCUREMENT_BU_ID | NUMBER(18) | NULL | FK | BU de procurement associada | [[hr_all_organization_units_f]] | 🟡 70% |
| 6 | PURCHASING_FLAG | VARCHAR2(1) | NOT NULL | Configuração | Site habilitado para compras (Y/N) | — | 🟡 75% |
| 7 | PAYMENT_FLAG | VARCHAR2(1) | NOT NULL | Configuração | Site habilitado para pagamentos (Y/N) | — | 🟡 75% |
| 8 | PRIMARY_PAY_SITE_FLAG | VARCHAR2(1) | NULL | Configuração | Site primário de pagamento (Y/N) | — | 🟡 70% |
| 9 | INACTIVE_DATE | DATE | NULL | Vigência | Data de inativação do assignment | — | 🟡 70% |
| 10 | BILL_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Localização de cobrança (Bill-To) | [[hr_locations_all_f_vl]] | 🟡 65% |
| 11 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Localização de entrega (Ship-To) | [[hr_locations_all_f_vl]] | 🟡 65% |
| 12 | LIABILITY_DISTRIBUTION | VARCHAR2(240) | NULL | Contabilidade | Distribuição contábil de passivo | — | 🟡 60% |
| 13 | PREPAY_DISTRIBUTION | VARCHAR2(240) | NULL | Contabilidade | Distribuição contábil de antecipação | — | 🟡 60% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor da atribuição de site à BU)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[hr_all_organization_units_f]] — via `ORG_ID` e `PROCUREMENT_BU_ID` (business unit à qual o site do fornecedor é atribuído)

### Tabelas relacionadas

---

## Uso Típico

### Sites atribuídos a uma BU específica
```sql
SELECT sa.VENDOR_ID, sa.VENDOR_SITE_ID,
       sa.PURCHASING_FLAG, sa.PAYMENT_FLAG,
       sa.PRIMARY_PAY_SITE_FLAG
FROM   POZ_SITE_ASSIGNMENTS_ALL_M sa
WHERE  sa.ORG_ID = :p_org_id
  AND  (sa.INACTIVE_DATE IS NULL OR sa.INACTIVE_DATE > SYSDATE);
```

### Sites habilitados para compras de um fornecedor
```sql
SELECT sa.VENDOR_SITE_ID, sa.ORG_ID,
       sa.PURCHASING_FLAG, sa.PAYMENT_FLAG
FROM   POZ_SITE_ASSIGNMENTS_ALL_M sa
WHERE  sa.VENDOR_ID = :p_vendor_id
  AND  sa.PURCHASING_FLAG = 'Y'
  AND  (sa.INACTIVE_DATE IS NULL OR sa.INACTIVE_DATE > SYSDATE);
```

---

## Observações

- Um site de fornecedor pode estar atribuído a **múltiplas BUs**, cada uma com configurações diferentes de purchasing/payment.
- O campo `PRIMARY_PAY_SITE_FLAG` indica o site padrão de pagamento quando o fornecedor tem múltiplos sites na mesma BU.
- Sites com `INACTIVE_DATE` no passado não são elegíveis para novas transações, mas transações existentes permanecem válidas.
- A combinação `VENDOR_SITE_ID + ORG_ID` deve ser única (um site só pode ter uma atribuição por BU).
- As distribuições contábeis (`LIABILITY_DISTRIBUTION`, `PREPAY_DISTRIBUTION`) definem as contas default para lançamentos AP.

---

## Referências

- [Oracle Docs — POZ_SITE_ASSIGNMENTS_ALL_M](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
