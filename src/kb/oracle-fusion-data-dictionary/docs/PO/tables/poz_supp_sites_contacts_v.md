---
id: DOC-PO-102
doc_type: system-doc
title: "POZ_SUPP_SITES_CONTACTS_V — Contatos de Sites de Fornecedores"
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
  - POZ_SUPP_SITES_CONTACTS_V
  - poz_supp_sites_contacts_v
  - poz-supp-sites-contacts-v
  - poz-supp
  - contatos-de-sites-de-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPP_SITES_CONTACTS_V

## 📌 Visão Geral

View que consolida os **contatos associados a sites de fornecedores**. Apresenta nome, e-mail, telefone vinculados a cada site, facilitando comunicacao e integracao.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view**, projetada para simplificar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Comunicacao:** Recuperacao de contatos por site para envio de POs e notificacoes.
- **Validacao cadastral:** Completude de dados de contato antes de ativar um site.
- **Integracao B2B:** Alimentacao de plataformas de e-procurement.
- **Relatorios:** Analise de cobertura de contatos por fornecedor/site.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Fornecedor | [[poz_suppliers]] | 🟢 95% |
| 2 | VENDOR_SITE_ID | NUMBER(18) | NOT NULL | FK | Site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 95% |
| 3 | VENDOR_CONTACT_ID | NUMBER(18) | NOT NULL | PK | ID unico do contato | — | 🟢 90% |
| 4 | FIRST_NAME | VARCHAR2(150) | NULL | Dados pessoais | Primeiro nome | — | 🟢 90% |
| 5 | LAST_NAME | VARCHAR2(150) | NULL | Dados pessoais | Sobrenome | — | 🟢 90% |
| 6 | EMAIL_ADDRESS | VARCHAR2(320) | NULL | Comunicacao | E-mail | — | 🟢 90% |
| 7 | PHONE | VARCHAR2(60) | NULL | Comunicacao | Telefone | — | 🟡 80% |
| 8 | FAX | VARCHAR2(60) | NULL | Comunicacao | Fax | — | 🟡 70% |
| 9 | INACTIVE_DATE | DATE | NULL | Status | Data de inativacao | — | 🟡 75% |
| 10 | PARTY_SITE_ID | NUMBER(18) | NULL | FK | Site TCA | [[hz_party_sites]] | 🟢 85% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario alterador | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor dos contatos de site na view)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor com contatos na view)
- [[hz_party_sites]] — via `PARTY_SITE_ID` (endereço TCA do contato do site do fornecedor)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Contatos ativos de um site
```sql
SELECT FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, PHONE
FROM   POZ_SUPP_SITES_CONTACTS_V
WHERE  VENDOR_SITE_ID = :p_site_id
  AND  (INACTIVE_DATE IS NULL OR INACTIVE_DATE > SYSDATE);
```

---

## 🔒 Observações

- Dados de contato podem conter PII; aplicar filtros de confidencialidade (LGPD).
- Campo `INACTIVE_DATE` controla validade do contato.
- View sem indices proprios.

---

## 🔗 PVOs Relacionados

### [[supplierfactlessfactpvo|SupplierFactLessFactPVO]] (PO · BICC: 7/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CARRIER_ID | CarrierId | ✅ |
| PARTY_SITE_ID | PartySiteId | ✅ |
| PERSON_PARTY_ID | PersonPartyId | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| SUPP_PARTY_ID | SuppPartyId | ✅ |
| VENDOR_ID | VendorId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |

---

## 📚 Referências

- [Oracle Docs — POZ_SUPP_SITES_CONTACTS_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
