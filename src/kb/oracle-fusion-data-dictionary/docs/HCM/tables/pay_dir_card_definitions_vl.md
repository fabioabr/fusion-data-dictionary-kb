---
id: DOC-HCM-567
doc_type: system-doc
title: "PAY_DIR_CARD_DEFINITIONS_VL — Definicoes de Cartao (View Localizada)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - dir-card-definitions
  - definicoes-cartao
  - pay-card-defs
aliases:
  - PAY_DIR_CARD_DEFINITIONS_VL
  - pay_dir_card_definitions_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_DIR_CARD_DEFINITIONS_VL

## 📌 Visão Geral

**View localizada** que combina as definicoes de cartoes de informacao direta com suas traducoes. Define os tipos de calculation cards disponiveis (ex.: Tax Card, Social Insurance Card).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consulta de tipos de cartao disponiveis com traducao
- Uso em LOVs de criacao de cartoes fiscais
- Configuracao de cartoes por legislacao

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DIR_CARD_DEFINITION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da definicao | --- | 🟢 95% |
| 2 | CARD_DEFINITION_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do tipo de cartao traduzido | --- | 🟢 85% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | CARD_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do cartao | --- | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela base de definicoes de cartao + traducoes

### Tabelas-filha (FK de saída)
- [[pay_dir_cards_f]] --- via `DIR_CARD_DEFINITION_ID` (cartões criados a partir desta definição)
- [[pay_dir_card_comp_defs_f]] --- via `DIR_CARD_DEFINITION_ID` (definições de componentes do cartão)

---

## 📎 Uso Típico

### Tipos de cartao disponiveis por legislacao
```sql
SELECT vl.DIR_CARD_DEFINITION_ID, vl.CARD_DEFINITION_NAME, vl.CARD_TYPE
FROM   PAY_DIR_CARD_DEFINITIONS_VL vl
WHERE  vl.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id;
```

---

## 🔒 Observações

- Esta eh uma view (VL = View Localizada), nao uma tabela fisica.

---

## 📚 Referências

- [Oracle Docs — PAY_DIR_CARD_DEFINITIONS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paydircarddefinitionsvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
