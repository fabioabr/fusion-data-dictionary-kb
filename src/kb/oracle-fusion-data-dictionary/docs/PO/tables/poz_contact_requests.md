---
id: DOC-PO-082
doc_type: system-doc
title: "POZ_CONTACT_REQUESTS — Solicitações de Contatos de Fornecedores"
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
  - supplier-contacts
  - registration
  - solicitacoes
aliases:
  - POZ_CONTACT_REQUESTS
  - poz_contact_requests
  - solicitacoes-contato-fornecedor
  - contact-requests
  - registro-contato-supplier
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_CONTACT_REQUESTS

## Visão Geral

Armazena as **solicitações de criação e atualização de contatos** de fornecedores no Oracle Procurement. Cada registro representa uma requisição pendente ou processada para adicionar ou modificar um contato associado a um fornecedor, incluindo dados pessoais, informações de comunicação e atribuições de site.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de novos contatos:** Captura solicitações para adicionar contatos a fornecedores existentes.
- **Atualização de contatos:** Registro de requisições de alteração de dados de contato (telefone, e-mail, endereço).
- **Workflow de aprovação:** Controla o fluxo de aprovação de inclusão/alteração de contatos.
- **Supplier Portal:** Suporta o autoatendimento onde fornecedores solicitam inclusão de contatos.
- **Auditoria de mudanças:** Mantém histórico de todas as solicitações de alteração de contatos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTACT_REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da solicitação de contato | — | 🟡 75% |
| 2 | SUPPLIER_REG_ID | NUMBER(18) | NULL | FK | Registro de fornecedor associado | [[poz_supplier_registrations]] | 🟡 70% |
| 3 | VENDOR_ID | NUMBER(18) | NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟡 75% |
| 4 | FIRST_NAME | VARCHAR2(150) | NULL | Dados pessoais | Primeiro nome do contato | — | 🟢 85% |
| 5 | LAST_NAME | VARCHAR2(150) | NOT NULL | Dados pessoais | Sobrenome do contato | — | 🟢 85% |
| 6 | EMAIL_ADDRESS | VARCHAR2(320) | NULL | Comunicação | Endereço de e-mail do contato | — | 🟢 85% |
| 7 | PHONE_NUMBER | VARCHAR2(60) | NULL | Comunicação | Número de telefone | — | 🟡 80% |
| 8 | REQUEST_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status da solicitação: PENDING, APPROVED, REJECTED | — | 🟡 75% |
| 9 | REQUEST_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da solicitação: NEW, UPDATE | — | 🟡 70% |
| 10 | ADMIN_EMAIL | VARCHAR2(320) | NULL | Comunicação | E-mail do administrador responsável | — | 🟡 65% |
| 11 | JOB_TITLE | VARCHAR2(100) | NULL | Dados pessoais | Cargo do contato | — | 🟡 70% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor solicitante)
- [[poz_supplier_registrations]] — via `SUPPLIER_REG_ID` (registro de fornecedor)

### Tabelas-filha (FK de saída)

### Tabelas relacionadas

---

## Uso Típico

### Solicitações pendentes de aprovação
```sql
SELECT cr.CONTACT_REQUEST_ID, cr.FIRST_NAME, cr.LAST_NAME,
       cr.EMAIL_ADDRESS, cr.REQUEST_TYPE, cr.CREATION_DATE
FROM   POZ_CONTACT_REQUESTS cr
WHERE  cr.REQUEST_STATUS = 'PENDING'
ORDER BY cr.CREATION_DATE DESC;
```

### Histórico de solicitações por fornecedor
```sql
SELECT cr.CONTACT_REQUEST_ID, cr.FIRST_NAME, cr.LAST_NAME,
       cr.REQUEST_STATUS, cr.REQUEST_TYPE
FROM   POZ_CONTACT_REQUESTS cr
WHERE  cr.VENDOR_ID = :p_vendor_id
ORDER BY cr.CREATION_DATE DESC;
```

---

## Observações

- As solicitações de contato podem ser originadas pelo **Supplier Portal** (autoatendimento) ou pelo módulo interno de Procurement.
- O campo `REQUEST_STATUS` controla o ciclo de vida da solicitação: PENDING → APPROVED/REJECTED.
- Contatos aprovados são efetivados na tabela `POZ_SUPPLIER_CONTACTS`.
- Campos de dados pessoais (nome, e-mail, telefone) podem conter informações sensíveis — aplicar controles de PII conforme política corporativa.

---

## Referências

- [Oracle Docs — Supplier Contact Requests](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
