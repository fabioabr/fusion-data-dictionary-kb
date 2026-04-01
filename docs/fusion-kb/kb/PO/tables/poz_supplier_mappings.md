---
id: DOC-PO-093
doc_type: system-doc
title: "POZ_SUPPLIER_MAPPINGS — Mapeamentos de Fornecedores"
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
  - supplier-mappings
  - mapeamento
  - integracao
aliases:
  - POZ_SUPPLIER_MAPPINGS
  - poz_supplier_mappings
  - mapeamento-fornecedores
  - supplier-mappings
  - mapeamento-supplier
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIER_MAPPINGS

## Visão Geral

Armazena os **mapeamentos entre fornecedores** de diferentes contextos ou sistemas no Oracle Fusion. Permite vincular um fornecedor a registros equivalentes em outras entidades, sistemas legados ou referências cruzadas, facilitando a consolidação e rastreabilidade durante migrações, integrações e processos de merge de fornecedores.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Migração de dados:** Mapeamento entre IDs de fornecedores do sistema legado e Oracle Fusion.
- **Merge de fornecedores:** Rastreamento de fornecedores consolidados (merged) e seus registros originais.
- **Integrações:** Referência cruzada entre IDs de fornecedores em diferentes sistemas (ERP, CRM, portais).
- **Reconciliação:** Identificação de correspondências entre registros de fornecedores duplicados.
- **Auditoria de conversão:** Histórico de mapeamentos realizados durante a implementação.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SUPPLIER_MAPPING_ID | NUMBER(18) | NOT NULL | PK | Identificador único do mapeamento | — | 🟡 70% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor no Fusion | [[poz_suppliers]] | 🟡 75% |
| 3 | SOURCE_SYSTEM | VARCHAR2(100) | NULL | Referência cruzada | Sistema de origem do mapeamento | — | 🟡 65% |
| 4 | SOURCE_VENDOR_ID | VARCHAR2(100) | NULL | Referência cruzada | ID do fornecedor no sistema de origem | — | 🟡 65% |
| 5 | MAPPING_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do mapeamento: MIGRATION, MERGE, CROSS_REF | — | 🟡 60% |
| 6 | THIRD_PARTY_REG_NUM | VARCHAR2(100) | NULL | Referência cruzada | Número de registro em sistema de terceiros | — | 🟡 60% |
| 7 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor mapeado | [[poz_supplier_sites_all_m]] | 🟡 65% |
| 8 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do mapeamento: ACTIVE, INACTIVE | — | 🟡 60% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor no Fusion)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site mapeado no relacionamento entre fornecedores)

### Tabelas relacionadas

---

## Uso Típico

### Buscar mapeamento por fornecedor legado
```sql
SELECT sm.VENDOR_ID, sm.SOURCE_SYSTEM,
       sm.SOURCE_VENDOR_ID, sm.MAPPING_TYPE
FROM   POZ_SUPPLIER_MAPPINGS sm
WHERE  sm.SOURCE_SYSTEM = :p_source_system
  AND  sm.SOURCE_VENDOR_ID = :p_legacy_vendor_id;
```

### Mapeamentos ativos de um fornecedor Fusion
```sql
SELECT sm.SUPPLIER_MAPPING_ID, sm.SOURCE_SYSTEM,
       sm.SOURCE_VENDOR_ID, sm.MAPPING_TYPE
FROM   POZ_SUPPLIER_MAPPINGS sm
WHERE  sm.VENDOR_ID = :p_vendor_id
  AND  sm.STATUS = 'ACTIVE';
```

---

## Observações

- Esta tabela é essencial durante **migrações de ERP** (legado → Fusion) para manter a rastreabilidade de IDs.
- O campo `SOURCE_SYSTEM` identifica a origem dos dados (ex.: `SAP`, `LEGACY_ERP`, `PORTAL_EXTERNO`).
- Em processos de **merge de fornecedores**, o mapeamento preserva o histórico dos registros originais.
- A combinação `SOURCE_SYSTEM + SOURCE_VENDOR_ID` deve ser única por `VENDOR_ID` para evitar ambiguidade.
- Mapeamentos com `STATUS = 'INACTIVE'` representam referências históricas que não são mais utilizadas ativamente.

---

## Referências

- [Oracle Docs — Supplier Mappings](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[supplierregistrationmappingpvo|SupplierRegistrationMappingPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| MAPPING_ID | SuppMapMappingId | ✅ |
| SUPPLIER_REG_ID | SuppMapSupplierRegId | — |
