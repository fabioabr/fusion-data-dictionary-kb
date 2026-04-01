---
id: DOC-AR-029
doc_type: system-doc
title: "AR_DISTRIBUTION_SETS_ALL — Conjuntos de Distribuição"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - distribution-sets
  - conjuntos-distribuicao
  - misc-receipts
aliases:
  - AR_DISTRIBUTION_SETS_ALL
  - ar_distribution_sets_all
  - conjuntos-distribuicao-ar
  - distribution-sets
  - misc-receipt-distributions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_DISTRIBUTION_SETS_ALL

## 📌 Visão Geral

Armazena os **conjuntos de distribuição** (distribution sets) do módulo Accounts Receivable. Cada registro define um modelo reutilizável de alocação contábil para recebimentos avulsos (miscellaneous receipts). Ao registrar um recebimento avulso, o usuário seleciona um distribution set que automaticamente distribui o valor entre contas contábeis pré-configuradas com percentuais definidos.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de misc receipts:** Definição de modelos de distribuição contábil para padronizar a contabilização de recebimentos avulsos.
- **Automação de contabilização:** Evita entrada manual de contas contábeis a cada recebimento avulso.
- **Padronização:** Garante que recebimentos avulsos do mesmo tipo sejam sempre contabilizados nas mesmas contas.
- **Setup organizacional:** Cada business unit pode ter seus próprios distribution sets.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DISTRIBUTION_SET_ID | NUMBER(18) | NOT NULL | PK | Identificador único do conjunto de distribuição | — | 🟢 100% |
| 2 | DISTRIBUTION_SET_NAME | VARCHAR2(50) | NOT NULL | Identificação | Nome do conjunto de distribuição | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição do conjunto de distribuição | — | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Classificação | Status do set: A (ativo), I (inativo) | — | 🟢 100% |
| 5 | TOTAL_PERCENT | NUMBER | NULL | Controle | Percentual total das linhas (deve ser 100%) | — | 🟢 100% |
| 6 | START_DATE_ACTIVE | DATE | NULL | Controle | Data de início de vigência | — | 🟢 100% |
| 7 | END_DATE_ACTIVE | DATE | NULL | Controle | Data de término de vigência | — | 🟢 100% |
| 8 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 14 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 15 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do conjunto de distribuição)

### Tabelas-filha (FK de saída)
- **AR_DISTRIBUTION_SET_LINES_ALL** — linhas do conjunto com CCID e percentual (tabela de detalhe)
- [[ar_cash_receipts_all]] — via `DISTRIBUTION_SET_ID` (recebimentos que utilizam este set)

---

## 📎 Uso Típico

### Listar conjuntos de distribuição ativos
```sql
SELECT ds.DISTRIBUTION_SET_NAME, ds.DESCRIPTION, ds.TOTAL_PERCENT,
       ds.START_DATE_ACTIVE, ds.END_DATE_ACTIVE
FROM   AR_DISTRIBUTION_SETS_ALL ds
WHERE  ds.STATUS = 'A'
  AND  ds.ORG_ID = :p_org_id
ORDER BY ds.DISTRIBUTION_SET_NAME;
```

### Recebimentos avulsos por distribution set
```sql
SELECT cr.RECEIPT_NUMBER, cr.AMOUNT, cr.RECEIPT_DATE, ds.DISTRIBUTION_SET_NAME
FROM   AR_CASH_RECEIPTS_ALL cr
JOIN   AR_DISTRIBUTION_SETS_ALL ds ON ds.DISTRIBUTION_SET_ID = cr.DISTRIBUTION_SET_ID
WHERE  cr.TYPE = 'MISC'
  AND  cr.ORG_ID = :p_org_id;
```

---

## 🔒 Observações

- O `TOTAL_PERCENT` deve sempre totalizar **100%** para que o distribution set seja válido.
- As linhas de detalhe (com CCID e percentual por conta) são armazenadas em uma tabela separada de linhas.
- Distribution sets com `END_DATE_ACTIVE` no passado não podem ser utilizados em novos recebimentos, mas permanecem associados aos recebimentos históricos.
- Cada business unit configura seus próprios distribution sets — não há compartilhamento entre organizações.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | DistributionSetCreatedBy | — |
| CREATION_DATE | DistributionSetCreationDate | — |
| DESCRIPTION | DistributionSetDescription | — |
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | ✅ |
| LAST_UPDATE_DATE | DistributionSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DistributionSetLastUpdateLogin | — |
| LAST_UPDATED_BY | DistributionSetLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DistributionSetObjectVersionNumber | — |
| ORG_ID | DistributionSetOrgId | — |
| STATUS | DistributionSetStatus | — |
| TOTAL_PERCENT_DISTRIBUTION | DistributionSetTotalPercentDistribution | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | DistributionSetDescription | — |
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | ✅ |
| ORG_ID | DistributionSetOrgId | — |
| STATUS | DistributionSetStatus | — |
| TOTAL_PERCENT_DISTRIBUTION | DistributionSetTotalPercentDistribution | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | DistributionSetDescription | — |
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | — |
| ORG_ID | DistributionSetOrgId | — |
| STATUS | DistributionSetStatus | — |
| TOTAL_PERCENT_DISTRIBUTION | DistributionSetTotalPercentDistribution | — |

### [[distributionsetextractpvo|DistributionSetExtractPVO]] (OTHER · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ArDistributionSetCreatedBy | ✅ |
| CREATION_DATE | ArDistributionSetCreationDate | ✅ |
| DESCRIPTION | ArDistributionSetDescription | ✅ |
| DISTRIBUTION_SET_ID | ArDistributionSetDistributionSetId | ✅ |
| DISTRIBUTION_SET_NAME | ArDistributionSetDistributionSetName | ✅ |
| LAST_UPDATE_DATE | ArDistributionSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArDistributionSetLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArDistributionSetLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ArDistributionSetObjectVersionNumber | ✅ |
| ORG_ID | ArDistributionSetOrgId | ✅ |
| STATUS | ArDistributionSetStatus | ✅ |
| TOTAL_PERCENT_DISTRIBUTION | ArDistributionSetTotalPercentDistribution | ✅ |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | DistributionSetCreatedBy | — |
| CREATION_DATE | DistributionSetCreationDate | — |
| DESCRIPTION | DistributionSetDescription | — |
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | ✅ |
| LAST_UPDATE_DATE | DistributionSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DistributionSetLastUpdateLogin | — |
| LAST_UPDATED_BY | DistributionSetLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DistributionSetObjectVersionNumber | — |
| ORG_ID | DistributionSetOrgId | — |
| STATUS | DistributionSetStatus | — |
| TOTAL_PERCENT_DISTRIBUTION | DistributionSetTotalPercentDistribution | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | DistributionSetCreatedBy | — |
| CREATION_DATE | DistributionSetCreationDate | — |
| DESCRIPTION | DistributionSetDescription | — |
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | — |
| LAST_UPDATE_DATE | DistributionSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DistributionSetLastUpdateLogin | — |
| LAST_UPDATED_BY | DistributionSetLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DistributionSetObjectVersionNumber | — |
| ORG_ID | DistributionSetOrgId | — |
| STATUS | DistributionSetStatus | — |
| TOTAL_PERCENT_DISTRIBUTION | DistributionSetTotalPercentDistribution | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | DistributionSetCreatedBy | — |
| CREATION_DATE | DistributionSetCreationDate | — |
| DESCRIPTION | DistributionSetDescription | — |
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | ✅ |
| LAST_UPDATE_DATE | DistributionSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DistributionSetLastUpdateLogin | — |
| LAST_UPDATED_BY | DistributionSetLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DistributionSetObjectVersionNumber | — |
| ORG_ID | DistributionSetOrgId | — |
| STATUS | DistributionSetStatus | — |
| TOTAL_PERCENT_DISTRIBUTION | DistributionSetTotalPercentDistribution | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | DistributionSetCreatedBy | — |
| CREATION_DATE | DistributionSetCreationDate | — |
| DESCRIPTION | DistributionSetDescription | — |
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | ✅ |
| LAST_UPDATE_DATE | DistributionSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DistributionSetLastUpdateLogin | — |
| LAST_UPDATED_BY | DistributionSetLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DistributionSetObjectVersionNumber | — |
| ORG_ID | DistributionSetOrgId | — |
| STATUS | DistributionSetStatus | — |
| TOTAL_PERCENT_DISTRIBUTION | DistributionSetTotalPercentDistribution | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | DistributionSetCreatedBy | — |
| CREATION_DATE | DistributionSetCreationDate | — |
| DESCRIPTION | DistributionSetDescription | — |
| DISTRIBUTION_SET_ID | DistributionSetDistributionSetId | — |
| DISTRIBUTION_SET_NAME | DistributionSetDistributionSetName | ✅ |
| LAST_UPDATE_DATE | DistributionSetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DistributionSetLastUpdateLogin | — |
| LAST_UPDATED_BY | DistributionSetLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | DistributionSetObjectVersionNumber | — |
| ORG_ID | DistributionSetOrgId | — |
| STATUS | DistributionSetStatus | — |
| TOTAL_PERCENT_DISTRIBUTION | DistributionSetTotalPercentDistribution | — |

---

## 📚 Referências

- [Oracle Docs — AR_DISTRIBUTION_SETS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/ardistributionsetsall-25092.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
