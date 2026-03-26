---
id: DOC-HCM-700
doc_type: system-doc
title: "PER_POS_FUNDING_POSITIONS_F — Financiamento de Posições"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - financiamento-posicoes
  - position-funding
  - orcamento
  - headcount
aliases:
  - PER_POS_FUNDING_POSITIONS_F
  - per_pos_funding_positions_f
  - financiamento-posicoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_POS_FUNDING_POSITIONS_F

## Visão Geral

Armazena os dados de **financiamento de posições** — como cada cargo/posição é custeado orçamentariamente. Define as fontes de financiamento (centros de custo, projetos, grants) e suas respectivas proporções. Tabela date-effective.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle orçamentário de headcount** — vincular posições a fontes de financiamento
- **Rateio de custos** — distribuir custos de pessoal entre centros de custo
- **Aprovação de vagas** — validar disponibilidade orçamentária
- **Relatórios financeiros de RH** — custo por posição e fonte de financiamento
- **Planejamento de workforce** — orçamento para novas posições

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POS_FUNDING_ID | NUMBER(18) | NOT NULL | PK | Identificador único do financiamento | — | 🟡 80% |
| 2 | POSITION_ID | NUMBER(18) | NOT NULL | FK | Referência à posição | HR_ALL_POSITIONS_F | 🟢 90% |
| 3 | FUNDING_SOURCE_ID | NUMBER(18) | NULL | FK | Fonte de financiamento | — | 🟡 70% |
| 4 | PROPORTION | NUMBER | NULL | Financeiro | Proporção/percentual do financiamento | — | 🟡 70% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `POSITION_ID` (posiÃ§Ã£o com financiamento orÃ§amentÃ¡rio)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Fontes de financiamento de uma posição
```sql
SELECT pf.FUNDING_SOURCE_ID, pf.PROPORTION
FROM   PER_POS_FUNDING_POSITIONS_F pf
WHERE  pf.POSITION_ID = :p_position_id
  AND  SYSDATE BETWEEN pf.EFFECTIVE_START_DATE AND pf.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência.
- Uma posição pode ter múltiplas fontes de financiamento (rateio).
- A soma das proporções deve totalizar 100%.
- Utilizada em conjunto com módulos financeiros para controle orçamentário.

---

## Referências

- [Oracle Docs — PER_POS_FUNDING_POSITIONS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perposfundingpositionsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
