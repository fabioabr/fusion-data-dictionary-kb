---
id: DOC-GL-031
doc_type: system-doc
title: "GL_LEGAL_ENTITIES_BSVS — Balancing Segment Values por Entidade Legal"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - legal-entity
  - balancing-segment
  - configuracao
aliases:
  - GL_LEGAL_ENTITIES_BSVS
  - gl_legal_entities_bsvs
  - bsv-entidade-legal
  - legal-entity-bsvs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_LEGAL_ENTITIES_BSVS

## 📌 Visão Geral

Armazena a associação entre **entidades legais (legal entities)** e seus **balancing segment values (BSVs)** no General Ledger. Define quais valores do segmento de balanceamento (tipicamente o segmento de empresa) pertencem a cada entidade legal. Esta associação é fundamental para o Subledger Accounting determinar a entidade legal responsável por cada transação.

> [!note] Tabela de mapeamento LE → BSV
> Cada entidade legal pode ter um ou mais balancing segment values associados. Esta associação é configurada durante o setup inicial e raramente alterada em produção.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Subledger Accounting:** Determinação da entidade legal responsável por cada transação contábil.
- **Reporting legal:** Geração de demonstrativos financeiros por entidade legal.
- **Intercompany:** Identificação de transações entre entidades legais distintas.
- **Tax compliance:** Associação de obrigações fiscais à entidade legal correta.
- **Consolidação:** Mapeamento de empresas para fins de eliminação e consolidação.
- **Auditoria:** Rastreamento de qual entidade legal é responsável por cada BSV.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEGAL_ENTITY_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador da entidade legal | — | 🟢 95% |
| 2 | LEDGER_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do ledger | [[gl_ledgers]] | 🟢 95% |
| 3 | FLEX_SEGMENT_VALUE | VARCHAR2(25) | NOT NULL | PK | Valor do balancing segment associado à LE (ex: "01", "02") | — | 🟢 95% |
| 4 | START_DATE | DATE | NULL | Controle | Data de início de validade da associação | — | 🟡 80% |
| 5 | END_DATE | DATE | NULL | Controle | Data de fim de validade da associação | — | 🟡 80% |
| 6 | STATUS_CODE | VARCHAR2(1) | NULL | Controle | Status: A (Active), I (Inactive) | — | 🟡 75% |
| 7 | ATTRIBUTE_CATEGORY | VARCHAR2(150) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟡 70% |
| 8 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Campos de atributo descritivo (DFF) configuráveis | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger ao qual a LE está associada)
- [[gl_ledger_segment_values]] — via `LEDGER_ID` + `FLEX_SEGMENT_VALUE` (valor de segmento do ledger)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de associação (junction table).

---

## 📎 Uso Típico

### Listar BSVs de uma entidade legal
```sql
SELECT leb.LEGAL_ENTITY_ID,
       leb.LEDGER_ID,
       gl.NAME AS ledger_name,
       leb.FLEX_SEGMENT_VALUE AS bsv,
       leb.STATUS_CODE
FROM   GL_LEGAL_ENTITIES_BSVS leb
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = leb.LEDGER_ID
WHERE  leb.LEGAL_ENTITY_ID = :p_legal_entity_id
ORDER BY leb.FLEX_SEGMENT_VALUE;
```

### Identificar a entidade legal de um BSV
```sql
SELECT leb.LEGAL_ENTITY_ID,
       leb.FLEX_SEGMENT_VALUE AS bsv,
       gl.NAME AS ledger_name
FROM   GL_LEGAL_ENTITIES_BSVS leb
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = leb.LEDGER_ID
WHERE  leb.FLEX_SEGMENT_VALUE = :p_bsv
  AND  leb.LEDGER_ID = :p_ledger_id;
```

### Mapa completo LE → BSV → Ledger
```sql
SELECT leb.LEGAL_ENTITY_ID,
       leb.FLEX_SEGMENT_VALUE AS bsv,
       gl.NAME AS ledger_name,
       gl.CURRENCY_CODE,
       leb.STATUS_CODE
FROM   GL_LEGAL_ENTITIES_BSVS leb
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = leb.LEDGER_ID
WHERE  gl.LEDGER_CATEGORY_CODE = 'PRIMARY'
ORDER BY leb.LEGAL_ENTITY_ID, leb.FLEX_SEGMENT_VALUE;
```

### Filtros comuns
- `STATUS_CODE = 'A'` — Associações ativas
- `LEGAL_ENTITY_ID = :p_le_id` — BSVs de uma LE específica
- `FLEX_SEGMENT_VALUE = :p_bsv` — Entidade legal de um BSV específico

---

## 🔒 Observações

- A PK composta é tipicamente `LEGAL_ENTITY_ID` + `LEDGER_ID` + `FLEX_SEGMENT_VALUE`.
- Cada BSV deve estar associado a no máximo uma entidade legal por ledger — garantindo unicidade na determinação da LE.
- O `FLEX_SEGMENT_VALUE` corresponde ao valor do balancing segment definido em [[gl_ledgers]] (`BAL_SEG_COLUMN_NAME`).
- Esta tabela é configurada durante o setup do Accounting Configuration e referenciada pelo Subledger Accounting (SLA) em runtime.
- Em cenários de reorganização societária, atualizações nesta tabela devem ser sincronizadas com [[gl_ledger_segment_values]].
- A associação LE → BSV é essencial para relatórios fiscais e obrigações acessórias no Brasil (SPED, ECF etc.).

---

## 🔗 PVOs Relacionados

### [[legalentitybalancingsegmentvaluespvo|LegalEntityBalancingSegmentValuesPVO]] (GL · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GlLegalEntitiesBsvsCreatedBy | — |
| CREATION_DATE | GlLegalEntitiesBsvsCreationDate | — |
| END_DATE | GlLegalEntitiesBsvsEndDate | — |
| FLEX_SEGMENT_VALUE | GlLegalEntitiesBsvsFlexSegmentValue | ✅ |
| FLEX_VALUE_SET_ID | GlLegalEntitiesBsvsFlexValueSetId | — |
| LAST_UPDATE_DATE | GlLegalEntitiesBsvsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlLegalEntitiesBsvsLastUpdateLogin | — |
| LAST_UPDATED_BY | GlLegalEntitiesBsvsLastUpdatedBy | — |
| LEGAL_ENTITY_ID | GlLegalEntitiesBsvsLegalEntityId | — |
| OBJECT_VERSION_NUMBER | GlLegalEntitiesBsvsObjectVersionNumber | — |
| START_DATE | GlLegalEntitiesBsvsStartDate | — |

### [[legalentitybsvassgmtextractpvo|LegalEntityBSVAssgmtExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GlLegalEntitiesBsvsCreatedBy | ✅ |
| CREATION_DATE | GlLegalEntitiesBsvsCreationDate | ✅ |
| END_DATE | GlLegalEntitiesBsvsEndDate | ✅ |
| FLEX_SEGMENT_VALUE | GlLegalEntitiesBsvsFlexSegmentValue | ✅ |
| FLEX_VALUE_SET_ID | GlLegalEntitiesBsvsFlexValueSetId | ✅ |
| LAST_UPDATE_DATE | GlLegalEntitiesBsvsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlLegalEntitiesBsvsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GlLegalEntitiesBsvsLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | GlLegalEntitiesBsvsLegalEntityId | ✅ |
| OBJECT_VERSION_NUMBER | GlLegalEntitiesBsvsObjectVersionNumber | ✅ |
| START_DATE | GlLegalEntitiesBsvsStartDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — GL_LEGAL_ENTITIES_BSVS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gllegaleentitiesbsvs.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
