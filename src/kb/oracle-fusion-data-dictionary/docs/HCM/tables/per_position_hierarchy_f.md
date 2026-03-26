---
id: DOC-HCM-697
doc_type: system-doc
title: "PER_POSITION_HIERARCHY_F — Hierarquia de Posições"
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
  - hierarquia-posicoes
  - position-hierarchy
  - organograma
  - cargo
aliases:
  - PER_POSITION_HIERARCHY_F
  - per_position_hierarchy_f
  - hierarquia-posicoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_POSITION_HIERARCHY_F

## Visão Geral

Armazena a **hierarquia de posições** (cargos) com vigência temporal. Define as relações pai-filho entre posições, formando o organograma baseado em cargos (diferente da hierarquia de gestores que é baseada em pessoas).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Organograma institucional** — estrutura hierárquica baseada em posições/cargos
- **Planejamento de workforce** — identificar posições vagas e suas relações
- **Fluxo de aprovações** — aprovar requisições com base na hierarquia de cargos
- **Sucessão e carreira** — mapear caminhos de progressão de carreira
- **Controle orçamentário** — aprovar headcount por posição

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POS_HIERARCHY_NODE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do nó de hierarquia | — | 🟡 80% |
| 2 | POSITION_ID | NUMBER(18) | NOT NULL | FK | Posição/cargo do nó | HR_ALL_POSITIONS_F | 🟢 90% |
| 3 | PARENT_POSITION_ID | NUMBER(18) | NULL | FK | Posição/cargo pai | HR_ALL_POSITIONS_F | 🟢 85% |
| 4 | POSITION_HIERARCHY_ID | NUMBER(18) | NOT NULL | FK | Identificador da hierarquia | — | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócio | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `POSITION_ID` e `PARENT_POSITION_ID`

### Tabelas-filha (FK de saída)
- [[per_position_hrchy_rf]] — via `POS_HIERARCHY_NODE_ID` (nÃ³s de referÃªncia da hierarquia de posiÃ§Ãµes)

---

## Uso Típico

### Posições subordinadas a uma posição específica
```sql
SELECT ph.POSITION_ID, ph.PARENT_POSITION_ID
FROM   PER_POSITION_HIERARCHY_F ph
WHERE  ph.PARENT_POSITION_ID = :p_position_id
  AND  SYSDATE BETWEEN ph.EFFECTIVE_START_DATE AND ph.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência.
- Diferente da hierarquia de gestores — esta é baseada em posições/cargos, não em pessoas.
- Uma posição sem `PARENT_POSITION_ID` indica o topo da hierarquia.
- Suporta múltiplas hierarquias via `POSITION_HIERARCHY_ID`.

---

## Referências

- [Oracle Docs — PER_POSITION_HIERARCHY_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpositionhierarchyf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
