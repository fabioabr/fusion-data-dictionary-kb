---
id: DOC-PO-077
doc_type: system-doc
title: "POZ_BUSINESS_CLASSIFICATIONS_V — View de Classificações de Negócio de Fornecedores"
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
  - classificacao
  - diversidade
  - view
aliases:
  - POZ_BUSINESS_CLASSIFICATIONS_V
  - poz_business_classifications_v
  - classificacoes-negocio-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_BUSINESS_CLASSIFICATIONS_V

## 📌 Visão Geral

View que consolida as **classificações de negócio** atribuídas a fornecedores — incluindo classificações de diversidade (Small Business, Minority-Owned, Woman-Owned, etc.), classificações industriais e certificações. Combina dados de `POZ_BUS_CLASSIFICATIONS` com informações do fornecedor e da agência certificadora.

> [!note] Sufixo _V
> O sufixo `_V` indica uma view que consolida dados de múltiplas tabelas-base.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Programa de diversidade:** Identificação de fornecedores classificados em categorias de diversidade.
- **Compliance regulatório:** Atendimento a requisitos governamentais de gastos com fornecedores diversificados.
- **Relatórios de diversidade:** Dashboards de percentual de spend com small/minority/woman-owned businesses.
- **Qualificação de fornecedores:** Verificação de certificações e classificações válidas.
- **Licitações:** Filtro de fornecedores elegíveis por classificação em processos de sourcing.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da classificação | [[poz_bus_classifications]] | 🟡 80% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 90% |
| 3 | VENDOR_NAME | VARCHAR2(360) | NULL | Descrição | Nome do fornecedor | — | 🟡 80% |
| 4 | LOOKUP_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da classificação (ex: BUSINESS_CLASSIFICATION) | — | 🟡 80% |
| 5 | LOOKUP_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da classificação (ex: SMALL_BUSINESS, MINORITY_OWNED) | — | 🟡 80% |
| 6 | CLASSIFICATION_NAME | VARCHAR2(240) | NULL | Descrição | Nome legível da classificação | — | 🟡 75% |
| 7 | CERTIFYING_AGENCY_ID | NUMBER(18) | NULL | FK | Agência que emitiu a certificação | [[poz_certifying_agencies]] | 🟡 75% |
| 8 | CERTIFYING_AGENCY_NAME | VARCHAR2(240) | NULL | Descrição | Nome da agência certificadora | — | 🟡 70% |
| 9 | CERTIFICATION_NUM | VARCHAR2(30) | NULL | Identificação | Número do certificado | — | 🟡 70% |
| 10 | EXPIRATION_DATE | DATE | NULL | Data | Data de expiração da classificação | — | 🟡 80% |
| 11 | STATUS | VARCHAR2(30) | NULL | Status | Status da classificação: APPROVED, PENDING, EXPIRED | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_bus_classifications]] — via `CLASSIFICATION_ID` (classificação base)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor da view de classificações empresariais)
- [[poz_certifying_agencies]] — via `CERTIFYING_AGENCY_ID` (agência certificadora)

### Tabelas-filha (FK de saída)
- Nenhuma direta (view de consulta)

---

## 📎 Uso Típico

### Classificações ativas de um fornecedor
```sql
SELECT bcv.LOOKUP_CODE, bcv.CLASSIFICATION_NAME,
       bcv.CERTIFYING_AGENCY_NAME, bcv.CERTIFICATION_NUM,
       bcv.EXPIRATION_DATE
FROM   POZ_BUSINESS_CLASSIFICATIONS_V bcv
WHERE  bcv.VENDOR_ID = :p_vendor_id
  AND  (bcv.EXPIRATION_DATE IS NULL OR bcv.EXPIRATION_DATE > SYSDATE);
```

### Fornecedores small business
```sql
SELECT bcv.VENDOR_NAME, bcv.CERTIFICATION_NUM,
       bcv.EXPIRATION_DATE
FROM   POZ_BUSINESS_CLASSIFICATIONS_V bcv
WHERE  bcv.LOOKUP_CODE = 'SMALL_BUSINESS'
  AND  (bcv.EXPIRATION_DATE IS NULL OR bcv.EXPIRATION_DATE > SYSDATE);
```

---

## 🔒 Observações

- Esta é uma **view**, não uma tabela física — não aceita DML direto.
- Classificações com `EXPIRATION_DATE` no passado devem ser consideradas expiradas em relatórios de compliance.
- Os códigos de classificação seguem lookups padrão Oracle (ex: `SMALL_BUSINESS`, `MINORITY_OWNED`, `WOMAN_OWNED`, `VETERAN_OWNED`).
- A agência certificadora (`CERTIFYING_AGENCY_ID`) referencia [[poz_certifying_agencies]] e pode ser governamental ou privada.
- Para dados transacionais, use diretamente [[poz_bus_classifications]].

---

## 📚 Referências

- [Oracle Docs — POZ Views](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
