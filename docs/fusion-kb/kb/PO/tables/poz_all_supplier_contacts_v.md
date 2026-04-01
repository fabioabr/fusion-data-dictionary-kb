---
id: DOC-PO-070
doc_type: system-doc
title: "POZ_ALL_SUPPLIER_CONTACTS_V — View de Todos os Contatos de Fornecedores"
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
  - contatos
  - view
aliases:
  - POZ_ALL_SUPPLIER_CONTACTS_V
  - poz_all_supplier_contacts_v
  - contatos-fornecedores-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_ALL_SUPPLIER_CONTACTS_V

## 📌 Visão Geral

View que consolida **todos os contatos** associados a fornecedores, combinando dados de contatos do TCA (Trading Community Architecture) com informações específicas de procurement. Retorna nome, telefone, e-mail, cargo e status de cada contato vinculado a um fornecedor ou site de fornecedor.

> [!note] Sufixo _V
> O sufixo `_V` indica uma view que consolida dados de múltiplas tabelas-base para simplificar consultas.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Gestão de contatos:** Visualização consolidada de todos os contatos de um fornecedor.
- **Comunicação:** Obtenção rápida de dados de contato (telefone, e-mail) para comunicação com fornecedores.
- **Portal de fornecedores:** Base para exibição de contatos no Supplier Portal.
- **Relatórios:** Análises de completude cadastral e dados de contato por fornecedor.
- **Integrações:** Camada simplificada para extração de contatos em processos de migração e sincronização.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_CONTACT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do contato do fornecedor | — | 🟡 80% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 90% |
| 3 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor (se contato a nível de site) | [[poz_supplier_sites_all_m]] | 🟡 80% |
| 4 | PERSON_FIRST_NAME | VARCHAR2(150) | NULL | Contato | Primeiro nome do contato | — | 🟢 85% |
| 5 | PERSON_LAST_NAME | VARCHAR2(150) | NULL | Contato | Sobrenome do contato | — | 🟢 85% |
| 6 | EMAIL_ADDRESS | VARCHAR2(320) | NULL | Contato | E-mail do contato | — | 🟢 90% |
| 7 | PHONE_NUMBER | VARCHAR2(40) | NULL | Contato | Número de telefone | — | 🟢 85% |
| 8 | PHONE_AREA_CODE | VARCHAR2(10) | NULL | Contato | Código de área do telefone | — | 🟡 75% |
| 9 | FAX_NUMBER | VARCHAR2(40) | NULL | Contato | Número de fax | — | 🟡 70% |
| 10 | JOB_TITLE | VARCHAR2(100) | NULL | Contato | Cargo/função do contato | — | 🟡 75% |
| 11 | INACTIVE_DATE | DATE | NULL | Controle | Data de inativação do contato | — | 🟡 80% |
| 12 | PARTY_ID | NUMBER(18) | NULL | FK | Party ID no TCA | [[hz_parties]] | 🟡 80% |
| 13 | RELATIONSHIP_ID | NUMBER(18) | NULL | FK | ID do relacionamento no TCA | [[hz_relationships]] | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor dos contatos listados na view)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[hz_parties]] — via `PARTY_ID` (entidade TCA do contato do fornecedor)
- [[hz_relationships]] — via `RELATIONSHIP_ID` (relacionamento TCA)

### Tabelas-filha (FK de saída)
- Nenhuma direta (view de consulta)

---

## 📎 Uso Típico

### Contatos ativos de um fornecedor
```sql
SELECT vc.PERSON_FIRST_NAME, vc.PERSON_LAST_NAME,
       vc.EMAIL_ADDRESS, vc.PHONE_NUMBER, vc.JOB_TITLE
FROM   POZ_ALL_SUPPLIER_CONTACTS_V vc
WHERE  vc.VENDOR_ID = :p_vendor_id
  AND  (vc.INACTIVE_DATE IS NULL OR vc.INACTIVE_DATE > SYSDATE);
```

### Contatos por site de fornecedor
```sql
SELECT vc.PERSON_FIRST_NAME || ' ' || vc.PERSON_LAST_NAME AS nome_completo,
       vc.EMAIL_ADDRESS, vc.JOB_TITLE
FROM   POZ_ALL_SUPPLIER_CONTACTS_V vc
WHERE  vc.VENDOR_SITE_ID = :p_vendor_site_id
  AND  (vc.INACTIVE_DATE IS NULL OR vc.INACTIVE_DATE > SYSDATE);
```

---

## 🔒 Observações

- Esta é uma **view**, não uma tabela física — não aceita DML direto.
- Contatos podem estar associados ao fornecedor (nível empresa) ou a um site específico.
- O `INACTIVE_DATE` controla a vigência do contato; contatos com data no passado são considerados inativos.
- Os dados de contato são armazenados no TCA (`HZ_PARTIES`, `HZ_CONTACT_POINTS`); esta view desnormaliza para facilitar consultas de procurement.
- Informações sensíveis (e-mail, telefone) devem respeitar a política de confidencialidade da organização.

---

## 🔗 PVOs Relacionados

### [[allsuppliercontactspvo|AllSupplierContactsPVO]] (PO · BICC: 79/89)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | AllSupplierContactsAttribute1 | ✅ |
| ATTRIBUTE10 | AllSupplierContactsAttribute10 | ✅ |
| ATTRIBUTE11 | AllSupplierContactsAttribute11 | ✅ |
| ATTRIBUTE12 | AllSupplierContactsAttribute12 | ✅ |
| ATTRIBUTE13 | AllSupplierContactsAttribute13 | ✅ |
| ATTRIBUTE14 | AllSupplierContactsAttribute14 | ✅ |
| ATTRIBUTE15 | AllSupplierContactsAttribute15 | ✅ |
| ATTRIBUTE16 | AllSupplierContactsAttribute16 | ✅ |
| ATTRIBUTE17 | AllSupplierContactsAttribute17 | ✅ |
| ATTRIBUTE18 | AllSupplierContactsAttribute18 | ✅ |
| ATTRIBUTE19 | AllSupplierContactsAttribute19 | ✅ |
| ATTRIBUTE2 | AllSupplierContactsAttribute2 | ✅ |
| ATTRIBUTE20 | AllSupplierContactsAttribute20 | ✅ |
| ATTRIBUTE21 | AllSupplierContactsAttribute21 | ✅ |
| ATTRIBUTE22 | AllSupplierContactsAttribute22 | ✅ |
| ATTRIBUTE23 | AllSupplierContactsAttribute23 | ✅ |
| ATTRIBUTE24 | AllSupplierContactsAttribute24 | ✅ |
| ATTRIBUTE25 | AllSupplierContactsAttribute25 | ✅ |
| ATTRIBUTE26 | AllSupplierContactsAttribute26 | ✅ |
| ATTRIBUTE27 | AllSupplierContactsAttribute27 | ✅ |
| ATTRIBUTE28 | AllSupplierContactsAttribute28 | ✅ |
| ATTRIBUTE29 | AllSupplierContactsAttribute29 | ✅ |
| ATTRIBUTE3 | AllSupplierContactsAttribute3 | ✅ |
| ATTRIBUTE30 | AllSupplierContactsAttribute30 | ✅ |
| ATTRIBUTE4 | AllSupplierContactsAttribute4 | ✅ |
| ATTRIBUTE5 | AllSupplierContactsAttribute5 | ✅ |
| ATTRIBUTE6 | AllSupplierContactsAttribute6 | ✅ |
| ATTRIBUTE7 | AllSupplierContactsAttribute7 | ✅ |
| ATTRIBUTE8 | AllSupplierContactsAttribute8 | ✅ |
| ATTRIBUTE9 | AllSupplierContactsAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | AllSupplierContactsAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AllSupplierContactsAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | AllSupplierContactsAttributeDate10 | ✅ |
| ATTRIBUTE_DATE11 | AllSupplierContactsAttributeDate11 | ✅ |
| ATTRIBUTE_DATE12 | AllSupplierContactsAttributeDate12 | ✅ |
| ATTRIBUTE_DATE2 | AllSupplierContactsAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | AllSupplierContactsAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | AllSupplierContactsAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | AllSupplierContactsAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | AllSupplierContactsAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | AllSupplierContactsAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | AllSupplierContactsAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | AllSupplierContactsAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | AllSupplierContactsAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | AllSupplierContactsAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER11 | AllSupplierContactsAttributeNumber11 | ✅ |
| ATTRIBUTE_NUMBER12 | AllSupplierContactsAttributeNumber12 | ✅ |
| ATTRIBUTE_NUMBER2 | AllSupplierContactsAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER3 | AllSupplierContactsAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | AllSupplierContactsAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | AllSupplierContactsAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | AllSupplierContactsAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | AllSupplierContactsAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | AllSupplierContactsAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | AllSupplierContactsAttributeNumber9 | ✅ |
| CREATED_BY | AllSupplierContactsCreatedBy | ✅ |
| CREATION_DATE | AllSupplierContactsCreationDate | ✅ |
| EMAIL_ADDRESS | AllSupplierContactsEmailAddress | ✅ |
| EMAIL_CONTACT_POINT_ID | AllSupplierContactsEmailContactPointId | — |
| FAX_AREA_CODE | AllSupplierContactsFaxAreaCode | ✅ |
| FAX_CONTACT_POINT_ID | AllSupplierContactsFaxContactPointId | — |
| FAX_COUNTRY_CODE | AllSupplierContactsFaxCountryCode | ✅ |
| FAX_NUMBER | AllSupplierContactsFaxNumber | ✅ |
| INACTIVE_DATE | AllSupplierContactsInactiveDate | ✅ |
| LAST_UPDATE_DATE | AllSupplierContactsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AllSupplierContactsLastUpdateLogin | — |
| LAST_UPDATED_BY | AllSupplierContactsLastUpdatedBy | ✅ |
| MOBILE_AREA_CODE | AllSupplierContactsMobileAreaCode | ✅ |
| MOBILE_CONTACT_POINT_ID | AllSupplierContactsMobileContactPointId | — |
| MOBILE_COUNTRY_CODE | AllSupplierContactsMobileCountryCode | ✅ |
| MOBILE_NUMBER | AllSupplierContactsMobileNumber | ✅ |
| NAME | AllSupplierContactsName | — |
| OBJECT_VERSION_NUMBER | AllSupplierContactsObjectVersionNumber | — |
| PER_PARTY_ID | PerPartyId | ✅ |
| PERSON_FIRST_NAME | AllSupplierContactsPersonFirstName | ✅ |
| PERSON_LAST_NAME | AllSupplierContactsPersonLastName | ✅ |
| PERSON_MIDDLE_NAME | AllSupplierContactsPersonMiddleName | ✅ |
| PERSON_TITLE | AllSupplierContactsPersonTitle | — |
| PHONE_AREA_CODE | AllSupplierContactsPhoneAreaCode | ✅ |
| PHONE_CONTACT_POINT_ID | AllSupplierContactsPhoneContactPointId | — |
| PHONE_COUNTRY_CODE | AllSupplierContactsPhoneCountryCode | ✅ |
| PHONE_EXTENSION | AllSupplierContactsPhoneExtension | ✅ |
| PHONE_NUMBER | AllSupplierContactsPhoneNumber | ✅ |
| RELATIONSHIP_ID | AllSupplierContactsRelationshipId | — |
| SALUTATION | AllSupplierContactsSalutation | ✅ |
| STATUS | AllSupplierContactsStatus | ✅ |
| SUBJECT_ID | AllSupplierContactsSubjectId | — |
| SUP_PARTY_ID | SupPartyId | ✅ |
| SUPPLIER_NAME | AllSupplierContactsSupplierName | ✅ |

---

## 📚 Referências

- [Oracle Docs — POZ Views](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
