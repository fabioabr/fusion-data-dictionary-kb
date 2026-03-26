---
id: DOC-PO-078
doc_type: system-doc
title: "POZ_BUS_CLASSIFICATIONS — Classificações de Negócio de Fornecedores"
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
  - diversidade
aliases:
  - POZ_BUS_CLASSIFICATIONS
  - poz_bus_classifications
  - classificacoes-negocio
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_BUS_CLASSIFICATIONS

## 📌 Visão Geral

Armazena as **classificações de negócio** atribuídas a fornecedores — incluindo classificações de diversidade (Small Business, Minority-Owned, Woman-Owned, etc.), classificações setoriais e certificações. Cada registro representa uma classificação específica vinculada a um fornecedor, com dados de certificação, agência certificadora e validade.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de diversidade:** Registro e controle de classificações de diversidade de fornecedores.
- **Compliance regulatório:** Evidência de aderência a políticas de gastos com fornecedores diversificados.
- **Qualificação de fornecedores:** Armazenamento de certificações obrigatórias para participação em processos de compra.
- **Sourcing:** Filtro de fornecedores elegíveis por classificação em processos de licitação.
- **Relatórios de diversidade:** Base de dados para métricas de diversidade de fornecedores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da classificação | — | 🟢 90% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 90% |
| 3 | LOOKUP_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da classificação (ex: BUSINESS_CLASSIFICATION) | — | 🟢 85% |
| 4 | LOOKUP_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da classificação (ex: SMALL_BUSINESS, MINORITY_OWNED) | — | 🟢 85% |
| 5 | CERTIFYING_AGENCY_ID | NUMBER(18) | NULL | FK | Agência que emitiu a certificação | [[poz_certifying_agencies]] | 🟢 85% |
| 6 | CERTIFICATION_NUM | VARCHAR2(30) | NULL | Identificação | Número do certificado emitido | — | 🟡 80% |
| 7 | EXPIRATION_DATE | DATE | NULL | Data | Data de expiração da classificação/certificação | — | 🟢 85% |
| 8 | CLASS_STATUS | VARCHAR2(30) | NULL | Status | Status: APPROVED, PENDING, EXPIRED, REJECTED | — | 🟡 75% |
| 9 | PARTY_ID | NUMBER(18) | NULL | FK | Party ID no TCA | [[hz_parties]] | 🟡 80% |
| 10 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis | — | 🟢 90% |
| 11 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 90% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 16 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor classificado pela classificação empresarial)
- [[poz_certifying_agencies]] — via `CERTIFYING_AGENCY_ID` (agência certificadora)
- [[hz_parties]] — via `PARTY_ID` (entidade TCA da classificação empresarial)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Classificações ativas por fornecedor
```sql
SELECT bc.CLASSIFICATION_ID, bc.LOOKUP_CODE,
       bc.CERTIFICATION_NUM, bc.EXPIRATION_DATE,
       bc.CLASS_STATUS
FROM   POZ_BUS_CLASSIFICATIONS bc
WHERE  bc.VENDOR_ID = :p_vendor_id
  AND  (bc.EXPIRATION_DATE IS NULL OR bc.EXPIRATION_DATE > SYSDATE)
  AND  bc.CLASS_STATUS = 'APPROVED';
```

### Classificações expiradas (renovação necessária)
```sql
SELECT bc.VENDOR_ID, bc.LOOKUP_CODE,
       bc.CERTIFICATION_NUM, bc.EXPIRATION_DATE
FROM   POZ_BUS_CLASSIFICATIONS bc
WHERE  bc.EXPIRATION_DATE < SYSDATE
  AND  bc.CLASS_STATUS = 'APPROVED';
```

---

## 🔒 Observações

- Um fornecedor pode ter múltiplas classificações simultâneas (ex: Small Business + Minority-Owned).
- A `EXPIRATION_DATE` deve ser monitorada; classificações expiradas devem ser renovadas ou desativadas.
- Os códigos de classificação padrão Oracle incluem: `SMALL_BUSINESS`, `MINORITY_OWNED`, `WOMAN_OWNED`, `VETERAN_OWNED`, `HUB_ZONE`, `DISABLED_VETERAN`.
- A agência certificadora valida a autenticidade da classificação; referencia [[poz_certifying_agencies]].
- Classificações podem ser auto-declaradas ou certificadas por terceiros, conforme política da organização.

---

## 📚 Referências

- [Oracle Docs — POZ_BUS_CLASSIFICATIONS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pozbusclassifications.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
