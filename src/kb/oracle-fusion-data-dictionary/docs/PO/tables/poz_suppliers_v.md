---
id: DOC-PO-090
doc_type: system-doc
title: "POZ_SUPPLIERS_V — View Consolidada de Fornecedores"
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
  - suppliers
  - fornecedores
  - view-consolidada
aliases:
  - POZ_SUPPLIERS_V
  - poz_suppliers_v
  - view-fornecedores
  - suppliers-view
  - fornecedores-consolidado
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIERS_V

## Visão Geral

View consolidada que combina dados do **cadastro principal de fornecedores** (`POZ_SUPPLIERS`) com informações do Trading Community Architecture (`HZ_PARTIES`). Apresenta uma visão unificada do fornecedor incluindo nome, número, status, tipo, classificação e dados de party — simplificando consultas que normalmente exigiriam joins manuais.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** (visão), combinando dados de múltiplas tabelas base para simplificar consultas.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Consulta simplificada:** Acesso rápido a dados de fornecedores sem necessidade de joins com HZ_PARTIES.
- **Relatórios:** Base para reports e analytics que necessitam de dados consolidados de fornecedores.
- **LOVs (List of Values):** Utilizada em telas de seleção de fornecedor para exibir nome e número.
- **Integrações:** Fonte de dados para interfaces e APIs que consomem dados de fornecedores.
- **BI/Analytics:** Dimensão de fornecedor em modelos analíticos e OTBI.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | PK | Identificador único do fornecedor | [[poz_suppliers]] | 🟢 90% |
| 2 | VENDOR_NAME | VARCHAR2(360) | NOT NULL | Identificação | Razão social / nome do fornecedor | — | 🟢 90% |
| 3 | SEGMENT1 | VARCHAR2(30) | NOT NULL | Identificação | Número do fornecedor (código visível) | — | 🟢 90% |
| 4 | VENDOR_TYPE_LOOKUP_CODE | VARCHAR2(30) | NULL | Classificação | Tipo: VENDOR, EMPLOYEE, TAX_AUTHORITY | — | 🟢 85% |
| 5 | PARTY_ID | NUMBER(18) | NOT NULL | FK | Identificador do party no TCA | [[hz_parties]] | 🟢 85% |
| 6 | PARTY_NAME | VARCHAR2(360) | NULL | Identificação | Nome do party no TCA (pode diferir de VENDOR_NAME) | — | 🟡 75% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Status | Fornecedor ativo (Y/N) | — | 🟢 85% |
| 8 | BUSINESS_RELATIONSHIP | VARCHAR2(30) | NULL | Classificação | Tipo de relacionamento: SPEND_AUTHORIZED, NOT_AUTHORIZED | — | 🟡 75% |
| 9 | START_DATE_ACTIVE | DATE | NULL | Vigência | Data de início de atividade | — | 🟢 85% |
| 10 | END_DATE_ACTIVE | DATE | NULL | Vigência | Data de encerramento de atividade | — | 🟢 85% |
| 11 | DUNS_NUMBER | VARCHAR2(30) | NULL | Identificação | Número DUNS (Dun & Bradstreet) | — | 🟡 70% |
| 12 | ONE_TIME_FLAG | VARCHAR2(1) | NULL | Classificação | Fornecedor de uso único (Y/N) | — | 🟡 75% |
| 13 | PARENT_VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor-pai (hierarquia) | [[poz_suppliers]] | 🟡 70% |
| 14 | TAX_ORGANIZATION_TYPE_CODE | VARCHAR2(30) | NULL | Fiscal | Tipo de organização fiscal | — | 🟡 65% |

---

## Relacionamentos

### Tabelas-base

### Tabelas relacionadas

---

## Uso Típico

### Pesquisa de fornecedores ativos
```sql
SELECT sv.VENDOR_ID, sv.SEGMENT1, sv.VENDOR_NAME,
       sv.VENDOR_TYPE_LOOKUP_CODE, sv.BUSINESS_RELATIONSHIP
FROM   POZ_SUPPLIERS_V sv
WHERE  sv.ENABLED_FLAG = 'Y'
  AND  (sv.END_DATE_ACTIVE IS NULL OR sv.END_DATE_ACTIVE > SYSDATE)
  AND  UPPER(sv.VENDOR_NAME) LIKE UPPER(:p_search || '%');
```

### LOV de fornecedores para seleção
```sql
SELECT sv.VENDOR_ID, sv.SEGMENT1 || ' - ' || sv.VENDOR_NAME AS display
FROM   POZ_SUPPLIERS_V sv
WHERE  sv.ENABLED_FLAG = 'Y'
  AND  sv.VENDOR_TYPE_LOOKUP_CODE = 'VENDOR'
ORDER BY sv.SEGMENT1;
```

---

## Observações

- Por ser uma **view**, não suporta operações DML; alterações devem ser feitas nas tabelas base (`POZ_SUPPLIERS`, `HZ_PARTIES`).
- A view combina dados de **POZ_SUPPLIERS** e **HZ_PARTIES**, eliminando a necessidade de join explícito.
- O campo `PARTY_NAME` pode diferir de `VENDOR_NAME` quando o registro TCA foi atualizado independentemente.
- Esta view é frequentemente utilizada como base para **OTBI (Oracle Transactional BI)** e relatórios customizados.
- Não contém dados PII — para informações fiscais, consultar `POZ_SUPPLIERS_PII` separadamente.

---

## Referências

- [Oracle Docs — POZ_SUPPLIERS_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
