---
id: DOC-HCM-564
doc_type: system-doc
title: "PAY_DIR_CARD_COMPONENTS_F — Componentes de Cartoes Diretos"
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
  - dir-card-components
  - componentes
  - pay-dir-comp
aliases:
  - PAY_DIR_CARD_COMPONENTS_F
  - pay_dir_card_components_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_DIR_CARD_COMPONENTS_F

## 📌 Visão Geral

Armazena os **componentes** de cada cartao de informacao direta. Um componente representa uma secao especifica do cartao (ex.: IRRF, INSS, dependentes fiscais) com vigencia temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Detalhamento de secoes de cartoes fiscais
- Configuracao de parametros de calculo por componente
- Historico temporal de alteracoes em informacoes fiscais

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DIR_CARD_COMP_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do componente | --- | 🟢 90% |
| 2 | DIR_CARD_ID | NUMBER(18) | NOT NULL | FK | ID do cartao pai | PAY_DIR_CARDS_F | 🟢 90% |
| 3 | DIR_CARD_COMP_DEF_ID | NUMBER(18) | NOT NULL | FK | ID da definicao do componente | PAY_DIR_CARD_COMP_DEFS_F | 🟢 85% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_dir_cards_f]] --- via `DIR_CARD_ID` (cartÃ£o de depÃ³sito direto do componente)
- [[pay_dir_card_comp_defs_f]] --- via `DIR_CARD_COMP_DEF_ID` (definiÃ§Ã£o do componente do cartÃ£o)

### Tabelas-filha (FK de saída)
- [[pay_dir_comp_details_f]] --- via `DIR_CARD_COMP_ID` (detalhes do componente do cartÃ£o)

---

## 📎 Uso Típico

### Componentes vigentes de um cartao
```sql
SELECT dcc.DIR_CARD_COMP_ID, dcc.DIR_CARD_COMP_DEF_ID
FROM   PAY_DIR_CARD_COMPONENTS_F dcc
WHERE  dcc.DIR_CARD_ID = :p_card_id
  AND  SYSDATE BETWEEN dcc.EFFECTIVE_START_DATE AND dcc.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Cada componente pode ter detalhes adicionais via `PAY_DIR_COMP_DETAILS_F`.

---

## 📚 Referências

- [Oracle Docs — PAY_DIR_CARD_COMPONENTS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paydircardcomponentsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
