---
id: DOC-AR-034
doc_type: system-doc
title: "AR_COLLECTORS — Cobradores de Contas a Receber"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, cobradores, cobranca, collectors]
aliases: [AR_COLLECTORS, ar_collectors, collectors_ar, cobradores_ar, collector]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_COLLECTORS

## 📌 Visão Geral

Tabela de cadastro de cobradores (collectors) responsáveis pela gestão de contas a receber. Cada cobrador pode ser associado a perfis de clientes, determinando quem é responsável por acompanhar e cobrar saldos em aberto.

## 🧠 Propósito de Negócio

Os cobradores são peças centrais no processo de cobrança do Accounts Receivable. Cada perfil de cliente pode ser atribuído a um cobrador específico, que será responsável por monitorar os recebíveis, executar ações de cobrança e negociar com clientes inadimplentes. A tabela permite mapear cobradores a funcionários ou recursos do sistema.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | COLLECTOR_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do cobrador. | PK | 🟢 100% |
| 2 | NAME | VARCHAR2(30) | NOT NULL | Nome do cobrador. | Negócio | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição do cobrador. | Negócio | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Status ativo/inativo (A = Ativo, I = Inativo). | Controle | 🟢 100% |
| 5 | EMPLOYEE_ID | NUMBER(15) | NULL | FK para tabela de funcionários (HCM). | FK | 🟢 100% |
| 6 | RESOURCE_ID | NUMBER(15) | NULL | Identificador do recurso associado (JTF Resources). | FK | 🟢 100% |
| 7 | RESOURCE_TYPE | VARCHAR2(30) | NULL | Tipo do recurso (ex.: RS_EMPLOYEE, RS_GROUP). | Classificação | 🟢 100% |
| 8 | ALIAS | VARCHAR2(30) | NULL | Nome alternativo para o cobrador. | Negócio | 🟡 75% |
| 9 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 11 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 13 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **HZ_CUSTOMER_PROFILES** — Perfis de clientes associados ao cobrador (via `COLLECTOR_ID`).
- **[[ar_dispute_history]]** — Disputas podem ser gerenciadas pelo cobrador atribuído ao cliente.

## 📎 Uso Típico

```sql
-- Listar cobradores ativos com contagem de clientes atribuídos
SELECT c.COLLECTOR_ID,
       c.NAME,
       COUNT(cp.CUST_ACCOUNT_PROFILE_ID) AS total_clientes
  FROM AR_COLLECTORS c
  LEFT JOIN HZ_CUSTOMER_PROFILES cp
    ON cp.COLLECTOR_ID = c.COLLECTOR_ID
 WHERE c.STATUS = 'A'
 GROUP BY c.COLLECTOR_ID, c.NAME
 ORDER BY total_clientes DESC;
```

## 🔒 Observações

- Cobradores são compartilhados entre business units (não possuem `ORG_ID`).
- A associação com `EMPLOYEE_ID` permite rastrear o funcionário responsável no HCM.
- `RESOURCE_ID` e `RESOURCE_TYPE` integram com o framework JTF Resources do Oracle.

## 🔗 PVOs Relacionados

### [[collectorextractpvo|CollectorExtractPVO]] (OTHER · BICC: 18/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIAS | ArCollectorAlias | ✅ |
| ATTRIBUTE1 | ArCollectorAttribute1 | — |
| ATTRIBUTE10 | ArCollectorAttribute10 | — |
| ATTRIBUTE11 | ArCollectorAttribute11 | — |
| ATTRIBUTE12 | ArCollectorAttribute12 | — |
| ATTRIBUTE13 | ArCollectorAttribute13 | — |
| ATTRIBUTE14 | ArCollectorAttribute14 | — |
| ATTRIBUTE15 | ArCollectorAttribute15 | — |
| ATTRIBUTE2 | ArCollectorAttribute2 | — |
| ATTRIBUTE3 | ArCollectorAttribute3 | — |
| ATTRIBUTE4 | ArCollectorAttribute4 | — |
| ATTRIBUTE5 | ArCollectorAttribute5 | — |
| ATTRIBUTE6 | ArCollectorAttribute6 | — |
| ATTRIBUTE7 | ArCollectorAttribute7 | — |
| ATTRIBUTE8 | ArCollectorAttribute8 | — |
| ATTRIBUTE9 | ArCollectorAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArCollectorAttributeCategory | — |
| COLLECTOR_ID | ArCollectorCollectorId | ✅ |
| CREATED_BY | ArCollectorCreatedBy | ✅ |
| CREATION_DATE | ArCollectorCreationDate | ✅ |
| DESCRIPTION | ArCollectorDescription | ✅ |
| EMPLOYEE_ID | ArCollectorEmployeeId | ✅ |
| INACTIVE_DATE | ArCollectorInactiveDate | ✅ |
| LAST_UPDATE_DATE | ArCollectorLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArCollectorLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArCollectorLastUpdatedBy | ✅ |
| NAME | ArCollectorName | ✅ |
| OBJECT_VERSION_NUMBER | ArCollectorObjectVersionNumber | ✅ |
| RESOURCE_ID | ArCollectorResourceId | ✅ |
| RESOURCE_TYPE | ArCollectorResourceType | ✅ |
| SEED_DATA_SOURCE | ArCollectorSeedDataSource | ✅ |
| SET_ID | ArCollectorSetId | ✅ |
| STATUS | ArCollectorStatus | ✅ |
| TELEPHONE_NUMBER | ArCollectorTelephoneNumber | ✅ |

### [[customerfinancialprofilepvo|CustomerFinancialProfilePVO]] (AR · BICC: 2/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIAS | CollectorsAlias | — |
| COLLECTOR_ID | CollectorsCollectorId | — |
| CREATED_BY | CollectorsCreatedBy | — |
| CREATION_DATE | CollectorsCreationDate | — |
| DESCRIPTION | CollectorsDescription | — |
| EMPLOYEE_ID | CollectorsEmployeeId | — |
| INACTIVE_DATE | CollectorsInactiveDate | — |
| LAST_UPDATE_DATE | CollectorsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CollectorsLastUpdateLogin | — |
| LAST_UPDATED_BY | CollectorsLastUpdatedBy | — |
| NAME | CollectorsName | ✅ |
| OBJECT_VERSION_NUMBER | CollectorsObjectVersionNumber | — |
| RESOURCE_ID | CollectorsResourceId | — |
| RESOURCE_TYPE | CollectorsResourceType | — |
| SET_ID | CollectorsSetId | — |
| STATUS | CollectorsStatus | — |
| TELEPHONE_NUMBER | CollectorsTelephoneNumber | — |

### [[customerprofile|CustomerProfile]] (AR · BICC: 6/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIAS | CollectorsAlias | — |
| ATTRIBUTE_CATEGORY | CollectorsAttributeCategory | — |
| COLLECTOR_ID | CollectorsCollectorId | — |
| CREATED_BY | CollectorsCreatedBy | ✅ |
| CREATION_DATE | CollectorsCreationDate | ✅ |
| DESCRIPTION | CollectorsDescription | — |
| EMPLOYEE_ID | CollectorsEmployeeId | — |
| INACTIVE_DATE | CollectorsInactiveDate | — |
| LAST_UPDATE_DATE | CollectorsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CollectorsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CollectorsLastUpdatedBy | ✅ |
| NAME | CollectorsName | ✅ |
| OBJECT_VERSION_NUMBER | CollectorsObjectVersionNumber | — |
| RESOURCE_ID | CollectorsResourceId | — |
| RESOURCE_TYPE | CollectorsResourceType | — |
| SET_ID | CollectorsSetId | — |
| STATUS | CollectorsStatus | — |
| TELEPHONE_NUMBER | CollectorsTelephoneNumber | — |

### [[customersiteprofile|CustomerSiteProfile]] (AR · BICC: 6/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIAS | CollectorsAlias | — |
| ATTRIBUTE_CATEGORY | CollectorsAttributeCategory | — |
| COLLECTOR_ID | CollectorsCollectorId | — |
| CREATED_BY | CollectorsCreatedBy | ✅ |
| CREATION_DATE | CollectorsCreationDate | ✅ |
| DESCRIPTION | CollectorsDescription | — |
| EMPLOYEE_ID | CollectorsEmployeeId | — |
| INACTIVE_DATE | CollectorsInactiveDate | — |
| LAST_UPDATE_DATE | CollectorsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CollectorsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CollectorsLastUpdatedBy | ✅ |
| NAME | CollectorsName | ✅ |
| OBJECT_VERSION_NUMBER | CollectorsObjectVersionNumber | — |
| RESOURCE_ID | CollectorsResourceId | — |
| RESOURCE_TYPE | CollectorsResourceType | — |
| SET_ID | CollectorsSetId | — |
| STATUS | CollectorsStatus | — |
| TELEPHONE_NUMBER | CollectorsTelephoneNumber | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIAS | CollectorsAlias | — |
| COLLECTOR_ID | CollectorsCollectorId | — |
| DESCRIPTION | CollectorsDescription | — |
| EMPLOYEE_ID | CollectorsEmployeeId | — |
| INACTIVE_DATE | CollectorsInactiveDate | — |
| NAME | CollectorsName | — |
| RESOURCE_ID | CollectorsResourceId | — |
| RESOURCE_TYPE | CollectorsResourceType | — |
| SET_ID | CollectorsSetId | — |
| STATUS | CollectorsStatus | — |
| TELEPHONE_NUMBER | CollectorsTelephoneNumber | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIAS | CollectorsAlias | — |
| COLLECTOR_ID | CollectorsCollectorId | — |
| DESCRIPTION | CollectorsDescription | — |
| EMPLOYEE_ID | CollectorsEmployeeId | — |
| INACTIVE_DATE | CollectorsInactiveDate | — |
| NAME | CollectorsName | — |
| RESOURCE_ID | CollectorsResourceId | — |
| RESOURCE_TYPE | CollectorsResourceType | — |
| SET_ID | CollectorsSetId | — |
| STATUS | CollectorsStatus | — |
| TELEPHONE_NUMBER | CollectorsTelephoneNumber | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIAS | CollectorsAlias | — |
| COLLECTOR_ID | CollectorsCollectorId | — |
| DESCRIPTION | CollectorsDescription | — |
| EMPLOYEE_ID | CollectorsEmployeeId | — |
| INACTIVE_DATE | CollectorsInactiveDate | — |
| NAME | CollectorsName | ✅ |
| RESOURCE_ID | CollectorsResourceId | — |
| RESOURCE_TYPE | CollectorsResourceType | — |
| SET_ID | CollectorsSetId | — |
| STATUS | CollectorsStatus | — |
| TELEPHONE_NUMBER | CollectorsTelephoneNumber | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIAS | CollectorsAlias | — |
| COLLECTOR_ID | CollectorsCollectorId | — |
| DESCRIPTION | CollectorsDescription | — |
| EMPLOYEE_ID | CollectorsEmployeeId | — |
| INACTIVE_DATE | CollectorsInactiveDate | — |
| NAME | CollectorsName | ✅ |
| RESOURCE_ID | CollectorsResourceId | — |
| RESOURCE_TYPE | CollectorsResourceType | — |
| SET_ID | CollectorsSetId | — |
| STATUS | CollectorsStatus | — |
| TELEPHONE_NUMBER | CollectorsTelephoneNumber | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIAS | CollectorsAlias | — |
| COLLECTOR_ID | CollectorsCollectorId | — |
| DESCRIPTION | CollectorsDescription | — |
| EMPLOYEE_ID | CollectorsEmployeeId | — |
| INACTIVE_DATE | CollectorsInactiveDate | — |
| NAME | CollectorsName | ✅ |
| OBJECT_VERSION_NUMBER | CollectorsObjectVersionNumber | — |
| RESOURCE_ID | CollectorsResourceId | — |
| RESOURCE_TYPE | CollectorsResourceType | — |
| SET_ID | CollectorsSetId | — |
| STATUS | CollectorsStatus | — |
| TELEPHONE_NUMBER | CollectorsTelephoneNumber | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Collections Management Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
