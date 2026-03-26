---
id: DOC-PO-079
doc_type: system-doc
title: "POZ_BUS_CLASS_REQS — Requisitos de Classificação de Negócio de Fornecedores"
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
  - fornecedores
  - classificacao
  - requisitos
  - registro
aliases:
  - POZ_BUS_CLASS_REQS
  - poz_bus_class_reqs
  - requisitos-classificacao-negocio
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_BUS_CLASS_REQS

## 📌 Visão Geral

Armazena os **requisitos de classificação de negócio** solicitados durante o processo de registro de fornecedores. Esta tabela de staging captura as classificações informadas pelo fornecedor (ou pelo comprador) durante o onboarding, antes que sejam efetivadas na tabela principal `POZ_BUS_CLASSIFICATIONS` após aprovação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de fornecedores:** Captura de classificações de diversidade e certificações durante o supplier registration.
- **Workflow de aprovação:** Classificações informadas aguardam validação antes de serem promovidas ao cadastro oficial.
- **Auditoria de onboarding:** Histórico de classificações declaradas durante o processo de registro.
- **Compliance:** Rastreamento de quais classificações foram solicitadas e seu status de aprovação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BUS_CLASS_REQ_ID | NUMBER(18) | NOT NULL | PK | Identificador único do requisito de classificação | — | 🟡 75% |
| 2 | SUPPLIER_REG_ID | NUMBER(18) | NULL | FK | Registro de fornecedor associado | — | 🟡 75% |
| 3 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor (se alteração de cadastro existente) | [[poz_suppliers]] | 🟡 70% |
| 4 | LOOKUP_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da classificação | — | 🟡 80% |
| 5 | LOOKUP_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da classificação (ex: SMALL_BUSINESS) | — | 🟡 80% |
| 6 | CERTIFYING_AGENCY_ID | NUMBER(18) | NULL | FK | Agência certificadora informada | [[poz_certifying_agencies]] | 🟡 70% |
| 7 | CERTIFICATION_NUM | VARCHAR2(30) | NULL | Identificação | Número do certificado informado | — | 🟡 70% |
| 8 | EXPIRATION_DATE | DATE | NULL | Data | Data de expiração informada | — | 🟡 75% |
| 9 | REQUEST_STATUS | VARCHAR2(30) | NULL | Status | Status da solicitação: PENDING, APPROVED, REJECTED | — | 🟡 70% |
| 10 | CLASSIFICATION_ID | NUMBER(18) | NULL | FK | Classificação efetivada (após aprovação) | [[poz_bus_classifications]] | 🟡 65% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor existente)
- [[poz_certifying_agencies]] — via `CERTIFYING_AGENCY_ID` (agência certificadora)

### Tabelas-filha (FK de saída)
- [[poz_bus_classifications]] — via `CLASSIFICATION_ID` (classificação efetivada após aprovação)

---

## 📎 Uso Típico

### Classificações pendentes de aprovação
```sql
SELECT bcr.BUS_CLASS_REQ_ID, bcr.SUPPLIER_REG_ID,
       bcr.LOOKUP_CODE, bcr.CERTIFICATION_NUM,
       bcr.EXPIRATION_DATE, bcr.REQUEST_STATUS
FROM   POZ_BUS_CLASS_REQS bcr
WHERE  bcr.REQUEST_STATUS = 'PENDING';
```

### Classificações solicitadas por fornecedor
```sql
SELECT bcr.LOOKUP_CODE, bcr.CERTIFICATION_NUM,
       bcr.EXPIRATION_DATE, bcr.REQUEST_STATUS
FROM   POZ_BUS_CLASS_REQS bcr
WHERE  bcr.VENDOR_ID = :p_vendor_id
ORDER BY bcr.CREATION_DATE DESC;
```

---

## 🔒 Observações

- Esta tabela funciona como **staging** — após aprovação, os dados são transferidos para [[poz_bus_classifications]] e o `CLASSIFICATION_ID` é populado.
- Solicitações rejeitadas permanecem para auditoria com `REQUEST_STATUS = 'REJECTED'`.
- Durante o supplier registration (novo cadastro), o `VENDOR_ID` pode ser nulo; o `SUPPLIER_REG_ID` conecta ao registro em andamento.
- A validação da certificação (número, agência, validade) é responsabilidade do aprovador interno.

---

## 📚 Referências

- [Oracle Docs — POZ Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
