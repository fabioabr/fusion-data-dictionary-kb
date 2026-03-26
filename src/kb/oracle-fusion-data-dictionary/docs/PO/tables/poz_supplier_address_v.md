---
id: DOC-PO-091
doc_type: system-doc
title: "POZ_SUPPLIER_ADDRESS_V — Endereços de Fornecedores"
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
  - supplier-address
  - enderecos
  - localizacao
aliases:
  - POZ_SUPPLIER_ADDRESS_V
  - poz_supplier_address_v
  - enderecos-fornecedor
  - supplier-address-view
  - localizacao-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIER_ADDRESS_V

## Visão Geral

View que consolida os **endereços de fornecedores** combinando dados de sites de fornecedor (`POZ_SUPPLIER_SITES_ALL_M`) com informações de localização do TCA (`HZ_LOCATIONS`, `HZ_PARTY_SITES`). Apresenta endereço completo (logradouro, cidade, estado, CEP, país) de cada site de fornecedor de forma denormalizada e pronta para consumo.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** (visão), combinando dados de tabelas de Procurement e TCA.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Cadastro de fornecedores:** Consulta de endereços completos associados a cada site de fornecedor.
- **Logística e entrega:** Identificação de endereços de remessa (Ship-From) e faturamento (Bill-From).
- **Relatórios fiscais:** Endereço do fornecedor para notas fiscais e obrigações acessórias.
- **Análise geográfica:** Distribuição geográfica de fornecedores para análise de supply chain.
- **Correspondência:** Base para geração de etiquetas, cartas e comunicados.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 85% |
| 2 | VENDOR_SITE_ID | NUMBER(18) | NOT NULL | FK | Identificador do site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 85% |
| 3 | PARTY_SITE_ID | NUMBER(18) | NULL | FK | Identificador do party site (TCA) | [[hz_party_sites]] | 🟡 75% |
| 4 | LOCATION_ID | NUMBER(18) | NULL | FK | Identificador da localização (TCA) | [[hz_locations]] | 🟡 75% |
| 5 | ADDRESS_LINE1 | VARCHAR2(240) | NULL | Endereço | Linha 1 do endereço (logradouro + número) | — | 🟢 85% |
| 6 | ADDRESS_LINE2 | VARCHAR2(240) | NULL | Endereço | Linha 2 do endereço (complemento) | — | 🟢 85% |
| 7 | ADDRESS_LINE3 | VARCHAR2(240) | NULL | Endereço | Linha 3 do endereço | — | 🟡 80% |
| 8 | CITY | VARCHAR2(60) | NULL | Endereço | Cidade | — | 🟢 85% |
| 9 | STATE | VARCHAR2(60) | NULL | Endereço | Estado / UF | — | 🟢 85% |
| 10 | POSTAL_CODE | VARCHAR2(60) | NULL | Endereço | CEP / código postal | — | 🟢 85% |
| 11 | COUNTRY | VARCHAR2(60) | NULL | Endereço | País (código ISO) | — | 🟢 85% |
| 12 | PROVINCE | VARCHAR2(60) | NULL | Endereço | Província (contexto internacional) | — | 🟡 70% |
| 13 | COUNTY | VARCHAR2(60) | NULL | Endereço | Condado (contexto US/UK) | — | 🟡 70% |
| 14 | ADDRESS_NAME | VARCHAR2(240) | NULL | Identificação | Nome/descrição do endereço do site | — | 🟡 70% |
| 15 | VENDOR_SITE_CODE | VARCHAR2(15) | NULL | Identificação | Código do site do fornecedor | — | 🟡 75% |

---

## Relacionamentos

### Tabelas-base

### Tabelas relacionadas

---

## Uso Típico

### Endereço completo de um fornecedor
```sql
SELECT sa.VENDOR_SITE_CODE, sa.ADDRESS_LINE1,
       sa.ADDRESS_LINE2, sa.CITY, sa.STATE,
       sa.POSTAL_CODE, sa.COUNTRY
FROM   POZ_SUPPLIER_ADDRESS_V sa
WHERE  sa.VENDOR_ID = :p_vendor_id;
```

### Fornecedores por cidade/estado
```sql
SELECT sa.VENDOR_ID, sa.VENDOR_SITE_CODE,
       sa.CITY, sa.STATE, sa.COUNTRY
FROM   POZ_SUPPLIER_ADDRESS_V sa
WHERE  sa.STATE = :p_state
  AND  sa.COUNTRY = 'BR'
ORDER BY sa.CITY;
```

---

## Observações

- Por ser uma **view**, não suporta operações DML; alterações de endereço devem ser feitas via TCA (`HZ_LOCATIONS`) ou pelo cadastro de sites do fornecedor.
- No contexto brasileiro, `STATE` contém a **UF** (2 letras) e `POSTAL_CODE` contém o **CEP** (8 dígitos).
- Cada site de fornecedor tem **um endereço**; um fornecedor pode ter múltiplos sites (e portanto múltiplos endereços).
- O `PARTY_SITE_ID` vincula ao TCA, permitindo que o mesmo endereço seja compartilhado entre diferentes entidades (supplier, customer, etc.).

---

## Referências

- [Oracle Docs — Supplier Address](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
