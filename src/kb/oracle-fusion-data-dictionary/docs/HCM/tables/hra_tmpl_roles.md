---
id: DOC-HCM-153
doc_type: system-doc
title: "HRA_TMPL_ROLES — Papéis de Templates de Aprovação"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - approval-template
  - roles
aliases:
  - HRA_TMPL_ROLES
  - hra_tmpl_roles
  - papéis-de-templates-de-aprovação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_TMPL_ROLES

## 📌 Visão Geral

Armazena os **papéis (roles) associados a templates de aprovação** no HCM. Define quais funções organizacionais participam do fluxo de aprovação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de workflow:** Papéis em cada etapa de aprovação.
- **Delegação:** Quem pode aprovar baseado em papéis.
- **Hierarquia:** Sequência e nível de aprovação por papel.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TMPL_ROLE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do papel | — | 🟢 95% |
| 2 | TEMPLATE_ID | NUMBER(18) | NOT NULL | FK | Template de aprovação | — | 🟢 90% |
| 3 | ROLE_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do papel | — | 🟡 75% |
| 4 | ROLE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (APPROVER, REVIEWER, NOTIFIER) | — | 🟡 70% |
| 5 | SEQUENCE_NUMBER | NUMBER | NULL | Ordenação | Ordem no fluxo | — | 🟡 75% |
| 6 | APPROVAL_LEVEL | NUMBER | NULL | Configuração | Nível de aprovação hierárquica | — | 🟡 65% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Template de aprovação — via `TEMPLATE_ID`

### Tabelas relacionadas

---

## 📎 Uso Típico

### Papéis de um template
```sql
SELECT r.TMPL_ROLE_ID, r.ROLE_NAME, r.ROLE_TYPE, r.SEQUENCE_NUMBER
FROM   HRA_TMPL_ROLES r
WHERE  r.TEMPLATE_ID = :p_template_id
ORDER BY r.SEQUENCE_NUMBER;
```

---

## 🔒 Observações

- Cada template pode ter múltiplos papéis em sequência.
- `ROLE_TYPE` diferencia aprovadores, revisores e notificados.

---

## 🔗 PVOs Relacionados

### [[templateroledefnpvo|TemplateRoleDefnPVO]] (HCM · BICC: 4/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MINIMUM_NUM_PCPNS | TemplateRolePEOMinimumNumPcpns | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ROLE_TYPE_CODE | TemplateRolePEORoleTypeCode | — |
| TEMPLATE_DEFN_ID | TemplateRolePEOTemplateDefnId | — |
| TMPL_ROLE_ID | TmplRoleId | ✅ |

### [[templateroleextractpvo|TemplateRoleExtractPVO]] (HCM · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MINIMUM_NUM_PCPNS | MinimumNumPcpns | ✅ |
| MODULE_ID | ModuleId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ROLE_ID | RoleId | ✅ |
| ROLE_TYPE_CODE | RoleTypeCode | ✅ |
| TEMPLATE_DEFN_ID | TemplateDefnId | ✅ |
| TMPL_ROLE_ID | TmplRoleId | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
