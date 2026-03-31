---
id: DOC-PO-085
doc_type: system-doc
title: "POZ_PROVISIONABLE_ROLES — Roles Provisionáveis para Contatos de Fornecedores"
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
  - supplier-roles
  - seguranca
  - provisioning
aliases:
  - POZ_PROVISIONABLE_ROLES
  - poz_provisionable_roles
  - roles-provisionaveis
  - supplier-provisionable-roles
  - provisioning-roles
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_PROVISIONABLE_ROLES

## Visão Geral

Armazena as **roles (papéis) que podem ser provisionadas** para contatos de fornecedores no Oracle Supplier Portal. Define quais perfis de acesso estão disponíveis para atribuição a usuários externos (contatos de fornecedores), controlando o que cada contato pode fazer no portal de autoatendimento.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Provisioning de acesso:** Define o catálogo de roles disponíveis para contatos de fornecedores no Supplier Portal.
- **Gestão de segurança:** Controla quais funcionalidades do portal cada contato pode acessar.
- **Onboarding de fornecedores:** Determina quais roles são atribuídas automaticamente durante o registro.
- **Compliance de acesso:** Permite auditar e controlar os perfis de acesso de usuários externos.
- **Self-service:** Suporta a configuração de roles para autoatendimento no portal do fornecedor.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROVISIONABLE_ROLE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da role provisionável | — | 🟡 70% |
| 2 | ROLE_NAME | VARCHAR2(320) | NOT NULL | Identificação | Nome da role (ex.: Supplier Bidding, Supplier ViewPO) | — | 🟡 75% |
| 3 | ROLE_CODE | VARCHAR2(100) | NOT NULL | Identificação | Código interno da role | — | 🟡 70% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição da role e suas permissões | — | 🟡 70% |
| 5 | ROLE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da role: SUPPLIER_PORTAL, SOURCING, etc. | — | 🟡 65% |
| 6 | AUTO_PROVISION_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se a role é provisionada automaticamente (Y/N) | — | 🟡 65% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Status | Indica se a role está ativa (Y/N) | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas relacionadas

---

## Uso Típico

### Listar roles provisionáveis ativas
```sql
SELECT pr.PROVISIONABLE_ROLE_ID, pr.ROLE_NAME,
       pr.ROLE_CODE, pr.AUTO_PROVISION_FLAG
FROM   POZ_PROVISIONABLE_ROLES pr
WHERE  pr.ENABLED_FLAG = 'Y'
ORDER BY pr.ROLE_NAME;
```

### Roles com auto-provisioning
```sql
SELECT pr.ROLE_NAME, pr.ROLE_CODE, pr.DESCRIPTION
FROM   POZ_PROVISIONABLE_ROLES pr
WHERE  pr.AUTO_PROVISION_FLAG = 'Y'
  AND  pr.ENABLED_FLAG = 'Y';
```

---

## Observações

- As roles provisionáveis controlam o acesso ao **Supplier Portal** e funcionalidades como: visualização de POs, participação em negociações, envio de faturas, etc.
- Roles com `AUTO_PROVISION_FLAG = 'Y'` são atribuídas automaticamente a novos contatos durante o registro.
- A tabela define o **catálogo de roles**; a atribuição efetiva é feita no relacionamento entre contato e role.
- Alterações nesta tabela afetam a segurança de todos os contatos de fornecedores — mudanças devem ser controladas.

---

## Referências

- [Oracle Docs — Supplier Roles](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[supplierupreqpvo|SupplierUpReqPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ROLE_GUID | SupplierProvRolesRoleGuid | — |
