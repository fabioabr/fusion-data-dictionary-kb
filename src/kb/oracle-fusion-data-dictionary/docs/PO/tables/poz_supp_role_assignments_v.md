---
id: DOC-PO-101
doc_type: system-doc
title: "POZ_SUPP_ROLE_ASSIGNMENTS_V — Atribuicoes de Papeis de Fornecedores"
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
  - supplier-management
  - poz
aliases:
  - POZ_SUPP_ROLE_ASSIGNMENTS_V
  - poz_supp_role_assignments_v
  - poz-supp-role-assignments-v
  - poz-supp
  - atribuicoes-de-papeis-de-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPP_ROLE_ASSIGNMENTS_V

## 📌 Visão Geral

View que expoe as **atribuicoes de papeis (roles) de fornecedores** no modulo Procurement. Consolida a relacao entre fornecedores, sites e os papeis atribuidos (ex.: Spend Authorized, Sourcing) para facilitar consultas de seguranca e acesso.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view**, projetada para simplificar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle de acesso por papel:** Determina quais fornecedores estao autorizados para cada funcao.
- **Validacao de cadastro:** Verifica papeis necessarios antes de incluir em processos de compras.
- **Relatorios de compliance:** Auditoria de papeis atribuidos versus requeridos.
- **Integracao:** Alimenta sistemas downstream com papeis de fornecedores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 95% |
| 2 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 95% |
| 3 | ROLE_ID | NUMBER(18) | NOT NULL | FK | Papel atribuido | — | 🟡 75% |
| 4 | ROLE_NAME | VARCHAR2(240) | NULL | Classificacao | Nome do papel (Spend Authorized, Sourcing) | — | 🟡 70% |
| 5 | ASSIGNMENT_STATUS | VARCHAR2(30) | NULL | Status | Status (ACTIVE, INACTIVE) | — | 🟡 70% |
| 6 | START_DATE | DATE | NULL | Data | Inicio da atribuicao | — | 🟡 75% |
| 7 | END_DATE | DATE | NULL | Data | Termino da atribuicao | — | 🟡 75% |
| 8 | PARTY_ID | NUMBER(18) | NULL | FK | Party TCA | [[hz_parties]] | 🟢 85% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario alterador | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor com papel atribuído)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site com papel atribuído na view de roles)
- [[hz_parties]] — via `PARTY_ID` (entidade TCA na atribuição de papel do fornecedor)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Papeis ativos de um fornecedor
```sql
SELECT VENDOR_ID, ROLE_NAME, ASSIGNMENT_STATUS
FROM   POZ_SUPP_ROLE_ASSIGNMENTS_V
WHERE  VENDOR_ID = :p_vendor_id
  AND  ASSIGNMENT_STATUS = 'ACTIVE';
```

---

## 🔒 Observações

- View sem indices proprios; performance depende das tabelas base.
- Papeis disponiveis sao configuraveis por implementacao.
- Papeis inativos/expirados devem ser filtrados em consultas operacionais.

---

## 🔗 PVOs Relacionados

### [[suppliercontactuseracctdetailspvo|SupplierContactUserAcctDetailsPVO]] (PO · BICC: 6/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserRolesActiveFlag | — |
| ALLOW_SUPP_PROV_FLAG | SupplierContactUserAccountAllowSupplierProvisionFlag | — |
| BUSINESS_GROUP_ID | UserRolesBusinessGroupId | — |
| CREATED_BY | SupplierContactUserAccountCreatedBy | ✅ |
| CREATED_BY | UserRolesCreatedBy | — |
| CREATION_DATE | SupplierContactUserAccountCreationDate | ✅ |
| CREATION_DATE | UserRolesCreationDate | — |
| DEFAULT_FOR_PON_FLAG | SupplierContactUserAccountDefaultForPonFlag | — |
| DEFAULT_FOR_POS_FLAG | SupplierContactUserAccountDefaultForPosFlag | — |
| END_DATE | UserRolesEndDate | — |
| LAST_UPDATE_DATE | SupplierContactUserAccountLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | UserRolesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierContactUserAccountLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | UserRolesLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierContactUserAccountLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | UserRolesLastUpdatedBy | — |
| METHOD_CODE | UserRolesMethodCode | — |
| OBJECT_VERSION_NUMBER | SupplierContactUserAccountObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserRolesObjectVersionNumber | — |
| PROVISIONAL_ROLE_GUID | RoleGuid | ✅ |
| ROLE_GUID | UserRolesRoleGuid | — |
| ROLE_ID | UserRolesRoleId | — |
| START_DATE | UserRolesStartDate | — |
| TERMINATED_FLAG | UserRolesTerminatedFlag | — |
| USER_ID | UserRolesUserId | — |
| USER_ROLE_ID | UserRolesUserRoleId | — |

---

## 📚 Referências

- [Oracle Docs — POZ_SUPP_ROLE_ASSIGNMENTS_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
