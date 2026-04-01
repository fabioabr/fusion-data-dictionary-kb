---
id: DOC-PO-092
doc_type: system-doc
title: "POZ_SUPPLIER_CONTACTS — Contatos de Fornecedores"
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
  - contatos
  - comunicacao
aliases:
  - POZ_SUPPLIER_CONTACTS
  - poz_supplier_contacts
  - contatos-fornecedor
  - supplier-contacts
  - comunicacao-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIER_CONTACTS

## Visão Geral

Armazena os **contatos associados a fornecedores** no Oracle Fusion Procurement. Cada registro representa uma pessoa de contato vinculada a um fornecedor e/ou site específico, incluindo dados de comunicação (e-mail, telefone), cargo e informações de acesso ao Supplier Portal. É a tabela central para gestão de relacionamento com contatos de fornecedores.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de contatos:** Cadastro e manutenção de pessoas de contato por fornecedor/site.
- **Comunicação:** E-mails automáticos de POs, notificações de negociação e avisos de pagamento.
- **Supplier Portal:** Vinculação de contatos a usuários do portal de autoatendimento.
- **Sourcing:** Identificação do contato responsável para convites de negociação (RFQ/Auction).
- **Pedidos de compra:** Contato padrão impresso no PO para comunicação com o fornecedor.
- **Compliance:** Registro do responsável pela empresa para fins contratuais e legais.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_CONTACT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do contato do fornecedor | — | 🟢 90% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 90% |
| 3 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor associado ao contato | [[poz_supplier_sites_all_m]] | 🟢 85% |
| 4 | PER_PARTY_ID | NUMBER(18) | NULL | FK | Party ID da pessoa (TCA) | [[hz_parties]] | 🟡 75% |
| 5 | REL_PARTY_ID | NUMBER(18) | NULL | FK | Party ID do relacionamento (TCA) | [[hz_parties]] | 🟡 70% |
| 6 | ORG_CONTACT_ID | NUMBER(18) | NULL | FK | Contato organizacional (TCA) | [[hz_org_contacts]] | 🟡 70% |
| 7 | FIRST_NAME | VARCHAR2(150) | NULL | Dados pessoais | Primeiro nome do contato | — | 🟢 85% |
| 8 | LAST_NAME | VARCHAR2(150) | NOT NULL | Dados pessoais | Sobrenome do contato | — | 🟢 85% |
| 9 | EMAIL_ADDRESS | VARCHAR2(320) | NULL | Comunicação | Endereço de e-mail | — | 🟢 85% |
| 10 | PHONE | VARCHAR2(60) | NULL | Comunicação | Número de telefone | — | 🟢 85% |
| 11 | FAX | VARCHAR2(60) | NULL | Comunicação | Número de fax | — | 🟡 75% |
| 12 | INACTIVE_DATE | DATE | NULL | Vigência | Data de inativação do contato | — | 🟢 85% |
| 13 | ADMIN_USER_FLAG | VARCHAR2(1) | NULL | Configuração | Contato é administrador do portal (Y/N) | — | 🟡 70% |
| 14 | PRIMARY_CONTACT_FLAG | VARCHAR2(1) | NULL | Configuração | Contato principal do fornecedor (Y/N) | — | 🟡 70% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor ao qual o contato pertence)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[hz_parties]] — via `PER_PARTY_ID` (party da pessoa no TCA)
- [[hz_org_contacts]] — via `ORG_CONTACT_ID` (contato organizacional TCA)

### Tabelas-filha (FK de saída)

### Tabelas relacionadas

---

## Uso Típico

### Contatos ativos de um fornecedor
```sql
SELECT sc.VENDOR_CONTACT_ID, sc.FIRST_NAME, sc.LAST_NAME,
       sc.EMAIL_ADDRESS, sc.PHONE, sc.PRIMARY_CONTACT_FLAG
FROM   POZ_SUPPLIER_CONTACTS sc
WHERE  sc.VENDOR_ID = :p_vendor_id
  AND  (sc.INACTIVE_DATE IS NULL OR sc.INACTIVE_DATE > SYSDATE)
ORDER BY sc.PRIMARY_CONTACT_FLAG DESC, sc.LAST_NAME;
```

### Contatos administradores do portal
```sql
SELECT sc.VENDOR_CONTACT_ID, sc.FIRST_NAME, sc.LAST_NAME,
       sc.EMAIL_ADDRESS, s.VENDOR_NAME
FROM   POZ_SUPPLIER_CONTACTS sc
JOIN   POZ_SUPPLIERS s ON sc.VENDOR_ID = s.VENDOR_ID
WHERE  sc.ADMIN_USER_FLAG = 'Y'
  AND  (sc.INACTIVE_DATE IS NULL OR sc.INACTIVE_DATE > SYSDATE);
```

---

## Observações

- Um contato pode estar vinculado ao **fornecedor** (nível global) ou a um **site específico** (`VENDOR_SITE_ID` preenchido).
- O campo `PRIMARY_CONTACT_FLAG = 'Y'` identifica o **contato principal** do fornecedor/site.
- Contatos com `ADMIN_USER_FLAG = 'Y'` têm permissões administrativas no **Supplier Portal** e podem gerenciar outros contatos.
- Os campos `PER_PARTY_ID` e `REL_PARTY_ID` vinculam ao **TCA**, permitindo compartilhamento de dados de pessoa entre módulos.
- Dados de contato (nome, e-mail, telefone) são **informações pessoais** — aplicar controles de PII conforme política corporativa.
- A inativação é feita via `INACTIVE_DATE`; contatos inativos não são elegíveis para novas transações.

---

## Referências

- [Oracle Docs — POZ_SUPPLIER_CONTACTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[allsuppliercontactspvo|AllSupplierContactsPVO]] (PO · BICC: 1/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SuppAddrContactsCreatedBy | — |
| CREATION_DATE | SuppAddrContactsCreationDate | — |
| INACTIVE_DATE | SuppAddrContactsInactiveDate | — |
| LAST_UPDATE_DATE | SuppAddrContactsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SuppAddrContactsLastUpdateLogin | — |
| LAST_UPDATED_BY | SuppAddrContactsLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SuppAddrContactsObjectVersionNumber | — |
| ORG_CONTACT_ID | SuppAddrContactsOrgContactId | — |
| ORG_PARTY_SITE_ID | SuppAddrContactsOrgPartySiteId | — |
| PARTY_SITE_ID | SuppAddrContactsPartySiteId | — |
| PER_PARTY_ID | SuppAddrContactsPerPartyId | — |
| PROGRAM_APPLICATION_ID | SuppAddrContactsProgramApplicationId | — |
| PROGRAM_ID | SuppAddrContactsProgramId | — |
| PROGRAM_UPDATE_DATE | SuppAddrContactsProgramUpdateDate | — |
| RELATIONSHIP_ID | SuppAddrContactsRelationshipId | — |
| REQUEST_ID | SuppAddrContactsRequestId | — |
| VENDOR_CONTACT_ID | SuppAddrContactsVendorContactId | — |

### [[suppliercontactspvo|SupplierContactsPVO]] (PO · BICC: 5/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SupplierContactCreatedBy | ✅ |
| CREATION_DATE | SupplierContactCreationDate | ✅ |
| INACTIVE_DATE | SupplierContactInactiveDate | — |
| LAST_UPDATE_DATE | SupplierContactLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierContactLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierContactLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | SupplierContactObjectVersionNumber | — |
| ORG_CONTACT_ID | SupplierContactOrgContactId | — |
| ORG_PARTY_SITE_ID | SupplierContactOrgPartySiteId | — |
| PARTY_SITE_ID | SupplierContactPartySiteId | — |
| PER_PARTY_ID | SupplierContactPerPartyId | — |
| PROGRAM_APPLICATION_ID | SupplierContactProgramApplicationId | — |
| PROGRAM_ID | SupplierContactProgramId | — |
| PROGRAM_UPDATE_DATE | SupplierContactProgramUpdateDate | — |
| RELATIONSHIP_ID | SupplierContactRelationshipId | — |
| REQUEST_ID | SupplierContactRequestId | — |
| VENDOR_CONTACT_ID | VendorContactId | ✅ |
