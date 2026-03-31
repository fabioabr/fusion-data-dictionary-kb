---
id: DOC-AP-006
doc_type: system-doc
title: "AP_DISTRIBUTION_SETS_ALL — Conjuntos de Distribuição Contábil de AP"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, distribution-sets, distribuicao-contabil, contabilidade]
aliases: [AP_DISTRIBUTION_SETS_ALL, ap_distribution_sets_all, distribution_sets_ap, conjuntos_distribuicao_ap, dist_sets_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_DISTRIBUTION_SETS_ALL

## Visão Geral

Tabela de conjuntos de distribuição contábil predefinidos para faturas de contas a pagar. Cada registro define um template de alocação contábil que pode ser aplicado a faturas, distribuindo automaticamente valores entre contas contábeis conforme percentuais configurados. Particionada por `ORG_ID`.

## Propósito de Negócio

Os conjuntos de distribuição eliminam a necessidade de informar manualmente as contas contábeis em cada fatura, padronizando e acelerando a entrada de documentos. No Banco Patria, são utilizados para despesas recorrentes (aluguel, serviços de TI, consultorias) onde a alocação contábil segue um padrão fixo entre centros de custo ou contas do plano de contas.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DISTRIBUTION_SET_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único do conjunto de distribuição. | — | 🟢 100% |
| 2 | DISTRIBUTION_SET_NAME | VARCHAR2(50) | NOT NULL | Negócio | Nome do conjunto de distribuição. | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Negócio | Descrição do conjunto de distribuição. | — | 🟢 95% |
| 4 | TOTAL_PERCENT_DISTRIBUTION | NUMBER | NULL | Negócio | Percentual total de distribuição (deve somar 100%). | — | 🟢 90% |
| 5 | INACTIVE_DATE | DATE | NULL | Controle | Data de inativação do conjunto. | — | 🟢 90% |
| 6 | ORG_ID | NUMBER(15) | NOT NULL | Multiorg | Identificador da organização (business unit). | [[hr_operating_units]] | 🟢 100% |
| 7 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto de flexfield descritivo. | — | 🟢 90% |
| 8 | ATTRIBUTE1 | VARCHAR2(150) | NULL | DFF | Atributo descritivo flexível 1. | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 10 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[hr_operating_units]]** — Organização/business unit (via `ORG_ID`).

### Tabelas-filha

- **[[ap_distribution_set_lines_all]]** — Linhas individuais do conjunto com contas contábeis e percentuais (1:N via `DISTRIBUTION_SET_ID`).

## Uso Típico

```sql
-- Listar conjuntos de distribuição ativos com seus percentuais
SELECT ds.DISTRIBUTION_SET_NAME,
       ds.DESCRIPTION,
       ds.TOTAL_PERCENT_DISTRIBUTION,
       dsl.LINE_NUMBER,
       dsl.PERCENT_DISTRIBUTION,
       dsl.DIST_CODE_COMBINATION_ID
  FROM AP_DISTRIBUTION_SETS_ALL ds
  JOIN AP_DISTRIBUTION_SET_LINES_ALL dsl
    ON dsl.DISTRIBUTION_SET_ID = ds.DISTRIBUTION_SET_ID
 WHERE ds.ORG_ID = :p_org_id
   AND (ds.INACTIVE_DATE IS NULL OR ds.INACTIVE_DATE > SYSDATE)
 ORDER BY ds.DISTRIBUTION_SET_NAME, dsl.LINE_NUMBER;
```

## Observações

- O `TOTAL_PERCENT_DISTRIBUTION` deve somar 100% para que o conjunto seja válido.
- Conjuntos inativos (`INACTIVE_DATE` no passado) não aparecem nas LOVs de seleção durante entrada de faturas.
- Cada linha do conjunto aponta para uma combinação contábil (`DIST_CODE_COMBINATION_ID` em `GL_CODE_COMBINATIONS`).

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle BICC — AP Distribution Subject Area Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | DistributionSetCreatedBy | — |
| CREATION_DATE | DistributionSetCreationDate | — |
| DESCRIPTION | DistributionSetDescription | — |
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | — |
| INACTIVE_DATE | DistributionSetInactiveDate | — |
| LAST_UPDATE_DATE | DistributionSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DistributionSetLastUpdateLogin | — |
| LAST_UPDATED_BY | DistributionSetLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DistributionSetObjectVersionNumber | — |
| ORG_ID | DistributionSetOrgId | — |
| TOTAL_PERCENT_DISTRIBUTION | DistributionSetTotalPercentDistribution | — |

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| ORG_ID | DistributionSetOrgId | ✅ |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_ID | DistributionSetLineDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | ✅ |
| DISTRIBUTION_SET_NAME | DistributionSetLineDistributionSetName | ✅ |
| ORG_ID | DistributionSetLineOrgId | — |
| ORG_ID | DistributionSetOrgId | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| LAST_UPDATE_DATE | DistributionSetLastUpdateDate | ✅ |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_ID | DistributionSetLineDistributionSetId | — |
| LAST_UPDATE_DATE | DistributionSetLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | DistributionSetLineLastUpdateDate | ✅ |

### [[suppliersiteassignmentspvo|SupplierSiteAssignmentsPVO]] (PO · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ApDistributionSetsAllCreatedBy | ✅ |
| CREATION_DATE | ApDistributionSetsAllCreationDate | ✅ |
| DESCRIPTION | ApDistributionSetsAllDescription | ✅ |
| DISTRIBUTION_SET_ID | ApDistributionSetsAllDistributionSetId | ✅ |
| DISTRIBUTION_SET_NAME | ApDistributionSetsAllDistributionSetName | ✅ |
| INACTIVE_DATE | ApDistributionSetsAllInactiveDate | ✅ |
| LAST_UPDATE_DATE | ApDistributionSetsAllLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApDistributionSetsAllLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ApDistributionSetsAllLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ApDistributionSetsAllObjectVersionNumber | ✅ |
| ORG_ID | ApDistributionSetsAllOrgId | ✅ |
| TOTAL_PERCENT_DISTRIBUTION | ApDistributionSetsAllTotalPercentDistribution | ✅ |
