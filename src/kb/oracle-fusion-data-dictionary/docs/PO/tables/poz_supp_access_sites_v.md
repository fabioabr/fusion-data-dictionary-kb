---
id: DOC-PO-097
doc_type: system-doc
title: "POZ_SUPP_ACCESS_SITES_V — Acesso de Fornecedores por Site"
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
  - supplier-access
  - seguranca
  - data-security
aliases:
  - POZ_SUPP_ACCESS_SITES_V
  - poz_supp_access_sites_v
  - acesso-fornecedor-sites
  - supplier-access-sites
  - seguranca-sites-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPP_ACCESS_SITES_V

## Visão Geral

View que apresenta a **relação de acesso entre fornecedores/contatos e seus sites**, consolidando as regras de segurança de dados (data-level security) do Oracle Supplier Portal. Define quais sites cada contato de fornecedor pode acessar, combinando informações de atribuições de site, roles de contato e configurações de segurança.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** (visão), combinando dados de múltiplas tabelas de segurança e acesso.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Segurança do portal:** Controla quais sites cada contato pode visualizar e operar no Supplier Portal.
- **Data-level security:** Implementa restrições de acesso a nível de dados (DLS) para contatos de fornecedores.
- **Auditoria de acessos:** Permite verificar quais sites estão acessíveis para cada contato externo.
- **Provisioning:** Suporta o processo de concessão/revogação de acesso a sites.
- **Compliance:** Garante segregação de acesso conforme políticas corporativas de segurança.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟡 75% |
| 2 | VENDOR_SITE_ID | NUMBER(18) | NOT NULL | FK | Identificador do site acessível | [[poz_supplier_sites_all_m]] | 🟡 75% |
| 3 | VENDOR_CONTACT_ID | NUMBER(18) | NULL | FK | Identificador do contato com acesso | [[poz_supplier_contacts]] | 🟡 70% |
| 4 | VENDOR_SITE_CODE | VARCHAR2(15) | NULL | Identificação | Código do site | — | 🟡 70% |
| 5 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit do site | [[hr_all_organization_units_f]] | 🟡 70% |
| 6 | ACCESS_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de acesso concedido | — | 🟡 65% |
| 7 | PARTY_ID | NUMBER(18) | NULL | FK | Party ID (TCA) do contato | [[hz_parties]] | 🟡 65% |

---

## Relacionamentos

### Tabelas-base

### Tabelas relacionadas

---

## Uso Típico

### Sites acessíveis por um contato
```sql
SELECT asv.VENDOR_SITE_ID, asv.VENDOR_SITE_CODE,
       asv.ACCESS_TYPE, asv.ORG_ID
FROM   POZ_SUPP_ACCESS_SITES_V asv
WHERE  asv.VENDOR_CONTACT_ID = :p_contact_id;
```

### Contatos com acesso a um site específico
```sql
SELECT asv.VENDOR_CONTACT_ID, asv.ACCESS_TYPE
FROM   POZ_SUPP_ACCESS_SITES_V asv
WHERE  asv.VENDOR_SITE_ID = :p_vendor_site_id;
```

---

## Observações

- Por ser uma **view**, não suporta operações DML; a manutenção de acessos é feita via configuração de segurança e atribuição de roles.
- A view consolida múltiplas fontes de configuração de acesso (roles, site assignments, data access).
- No Supplier Portal, um contato só visualiza dados de sites que aparecem nesta view.
- A combinação de `POZ_SUPP_ACCESS_SITES_V` com `POZ_CONTACT_ACT_DATA_ACCESS_V` define o acesso completo do contato (site + atividade).

---

## Referências

- [Oracle Docs — Supplier Access Security](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[supplieraccessiblesitepvo|SupplierAccessibleSitePVO]] (PO · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENABLED_FLAG | AccessibleSiteSupplierEnabledFlag | ✅ |
| END_DATE_ACTIVE | AccessibleSiteSupplierEndDateActive | ✅ |
| INACTIVE_DATE | AccessibleSiteSiteInactiveDate | ✅ |
| PARTY_SITE_NAME | AccessibleSitePartySiteName | ✅ |
| PRC_BU_ID | AccessibleSitePrcBuId | ✅ |
| SEGMENT1 | AccessibleSiteSegment1 | ✅ |
| SUPPLIER_NAME | AccessibleSiteSupplierName | ✅ |
| VENDOR_ID | AccessibleSiteVendorId | ✅ |
| VENDOR_SITE_CODE | AccessibleSiteVendorSiteCode | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |
