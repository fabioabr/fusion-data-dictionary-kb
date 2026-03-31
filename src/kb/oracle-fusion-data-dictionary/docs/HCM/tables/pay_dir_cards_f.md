---
id: DOC-HCM-563
doc_type: system-doc
title: "PAY_DIR_CARDS_F — Cartoes de Informacao Direta (Direct Cards)"
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
  - dir-cards
  - calculation-cards
  - pay-dir-cards
aliases:
  - PAY_DIR_CARDS_F
  - pay_dir_cards_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_DIR_CARDS_F

## 📌 Visão Geral

Armazena os **cartoes de informacao direta** (calculation cards) de colaboradores. Cada cartao contem informacoes fiscais, legais ou de beneficios que impactam o calculo de folha (`_F` = date-effective).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Armazenamento de informacoes fiscais de colaboradores
- Configuracao de parametros de calculo individuais
- Controle de vigencia de informacoes de imposto de renda, previdencia, etc.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DIR_CARD_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do cartao | --- | 🟢 90% |
| 2 | DIR_CARD_DEFINITION_ID | NUMBER(18) | NOT NULL | FK | ID da definicao do cartao | PAY_DIR_CARD_DEFINITIONS_VL | 🟢 85% |
| 3 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | FK | ID do relacionamento de folha | PAY_PAY_RELATIONSHIPS_F | 🟢 90% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de fonte do cartao | --- | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_dir_card_definitions_vl]] --- via `DIR_CARD_DEFINITION_ID` (definição do cartão de depósito direto)
- [[pay_pay_relationships_f]] --- via `PAYROLL_RELATIONSHIP_ID` (relacionamento de folha do cartão de depósito)

### Tabelas-filha (FK de saída)
- [[pay_dir_card_components_f]] --- via `DIR_CARD_ID` (componentes do cartão de depósito direto)

---

## 📎 Uso Típico

### Cartoes vigentes por relacionamento de folha
```sql
SELECT dc.DIR_CARD_ID, dc.DIR_CARD_DEFINITION_ID
FROM   PAY_DIR_CARDS_F dc
WHERE  dc.PAYROLL_RELATIONSHIP_ID = :p_rel_id
  AND  SYSDATE BETWEEN dc.EFFECTIVE_START_DATE AND dc.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Calculation cards sao o mecanismo principal para informacoes fiscais no Oracle Fusion Payroll.
- Cada cartao pode ter multiplos componentes via `PAY_DIR_CARD_COMPONENTS_F`.

---

## 📚 Referências

- [Oracle Docs — PAY_DIR_CARDS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paydircardsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
