---
id: DOC-PO-081
doc_type: system-doc
title: "POZ_CONTACT_ACT_DATA_ACCESS_V — Acesso de Contatos a Dados por Atividade"
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
  - data-access
  - seguranca
aliases:
  - POZ_CONTACT_ACT_DATA_ACCESS_V
  - poz_contact_act_data_access_v
  - acesso-contato-atividade
  - contact-activity-data-access
  - seguranca-contato-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_CONTACT_ACT_DATA_ACCESS_V

## Visão Geral

View que expõe o **controle de acesso dos contatos de fornecedores** a dados específicos por tipo de atividade no Oracle Supplier Portal. Consolida informações de permissões e restrições de acesso que determinam quais dados cada contato de fornecedor pode visualizar e manipular no portal de autoatendimento.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** (visão), não uma tabela física. Combina dados de múltiplas tabelas base para simplificar consultas de segurança e acesso.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Controle de acesso ao portal:** Define quais dados cada contato de fornecedor pode acessar no Supplier Portal.
- **Segregação por atividade:** Permite restringir acesso com base no tipo de atividade (pedidos, faturas, negociações, etc.).
- **Auditoria de acessos:** Facilita a verificação de permissões concedidas a contatos externos.
- **Gestão de segurança:** Suporta a configuração de data-level security para usuários do portal do fornecedor.
- **Compliance:** Garante que contatos acessem apenas os dados permitidos pela política corporativa.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_CONTACT_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do contato do fornecedor | [[poz_supplier_contacts]] | 🟡 75% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟡 75% |
| 3 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Identificador do site do fornecedor | [[poz_supplier_sites_all_m]] | 🟡 75% |
| 4 | ACTIVITY_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de atividade (ORDERING, INVOICING, SOURCING, etc.) | — | 🟡 70% |
| 5 | ACCESS_LEVEL | VARCHAR2(30) | NULL | Classificação | Nível de acesso concedido (VIEW, EDIT, FULL) | — | 🟡 65% |
| 6 | DATA_ACCESS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de acesso | — | 🟡 70% |
| 7 | PARTY_ID | NUMBER(18) | NULL | FK | Identificador do party (TCA) associado ao contato | [[hz_parties]] | 🟡 70% |
| 8 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor cujo acesso de contato é controlado)
- [[poz_supplier_contacts]] — via `VENDOR_CONTACT_ID` (contato do fornecedor)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[hz_parties]] — via `PARTY_ID` (entidade TCA do contato com acesso controlado)

### Views/Tabelas relacionadas

---

## Uso Típico

### Verificar acessos de um contato específico
```sql
SELECT cda.VENDOR_CONTACT_ID, cda.ACTIVITY_TYPE,
       cda.ACCESS_LEVEL, cda.VENDOR_SITE_ID
FROM   POZ_CONTACT_ACT_DATA_ACCESS_V cda
WHERE  cda.VENDOR_ID = :p_vendor_id
  AND  cda.VENDOR_CONTACT_ID = :p_contact_id;
```

### Listar contatos com acesso a determinada atividade
```sql
SELECT cda.VENDOR_CONTACT_ID, cda.VENDOR_ID,
       cda.ACCESS_LEVEL
FROM   POZ_CONTACT_ACT_DATA_ACCESS_V cda
WHERE  cda.ACTIVITY_TYPE = 'ORDERING'
  AND  cda.ORG_ID = :p_org_id;
```

---

## Observações

- Por ser uma **view**, não suporta operações de INSERT/UPDATE/DELETE diretamente; a manutenção dos dados é feita nas tabelas base.
- O controle de acesso por atividade é fundamental para o **Supplier Portal**, onde contatos externos visualizam informações restritas.
- A coluna `ACTIVITY_TYPE` segue os lookup values padrão do Oracle Procurement.
- A segurança de dados do contato pode ser combinada com roles provisionáveis (`POZ_PROVISIONABLE_ROLES`) para controle granular.

---

## Referências

- [Oracle Docs — Supplier Data Access](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
