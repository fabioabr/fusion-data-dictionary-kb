---
id: DOC-HCM-612
doc_type: system-doc
title: "PER_ACTION_OCCURRENCES — Ocorrências de Ações de RH"
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
  - workforce-management
  - ocorrencias
  - action-occurrences
aliases:
  - PER_ACTION_OCCURRENCES
  - per_action_occurrences
  - per-action-occurrences
  - ocorrências-de-ações-de-rh
  - per-action-occurrenc
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACTION_OCCURRENCES

## 📌 Visão Geral

Armazena os **registros de ocorrências** de ações de RH realizadas sobre colaboradores. Cada registro representa uma instância concreta de uma ação (ex.: uma admissão específica, uma promoção realizada).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Histórico de movimentações** — registra cada ação executada no ciclo de vida.
- **Auditoria** — rastreabilidade completa com datas e responsáveis.
- **Relatórios de movimentação** — base para dashboards de RH.
- **Integração com workflow** — registra o resultado dos fluxos de aprovação.
- **Análise de tendências** — histórico de ações para planejamento de workforce.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_OCCURRENCE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da ocorrência | — | 🟢 95% |
| 2 | ACTION_ID | NUMBER(18) | NOT NULL | FK | Ação realizada | PER_ACTIONS_B | 🟢 90% |
| 3 | ACTION_REASON_ID | NUMBER(18) | NULL | FK | Motivo da ação | PER_ACTION_REASONS_B | 🟢 85% |
| 4 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador afetado | PER_ALL_PEOPLE_F | 🟢 90% |
| 5 | EFFECTIVE_DATE | DATE | NOT NULL | Vigência | Data efetiva da ação | — | 🟢 90% |
| 6 | ACTION_STATUS | VARCHAR2(30) | NULL | Status | Status da ocorrência (COMPLETED, PENDING) | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_actions_b]] — via `ACTION_ID` (aÃ§Ã£o de RH realizada na ocorrÃªncia)
- [[per_action_reasons_b]] — via `ACTION_REASON_ID` (motivo da aÃ§Ã£o de RH)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador afetado pela aÃ§Ã£o de RH)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Ocorrências de ações de um colaborador
```sql
SELECT pao.ACTION_OCCURRENCE_ID, pa.ACTION_CODE, pao.EFFECTIVE_DATE
FROM   PER_ACTION_OCCURRENCES pao
JOIN   PER_ACTIONS_B pa ON pao.ACTION_ID = pa.ACTION_ID
WHERE  pao.PERSON_ID = :p_person_id
ORDER BY pao.EFFECTIVE_DATE DESC;
```

### Filtros comuns
- `ACTION_STATUS = 'COMPLETED'` — Ações concluídas
- `EFFECTIVE_DATE >= TRUNC(SYSDATE, 'YEAR')` — Ações do ano corrente
---

## 🔒 Observações

- Cada registro representa uma instância concreta de uma ação sobre um colaborador.
- O `EFFECTIVE_DATE` marca quando a ação entra em vigor — pode ser retroativa ou futura.
- Utilizada em conjunto com PER_ALL_ASSIGNMENTS_M para rastrear mudanças no assignment.
---

## 📚 Referências

- [Oracle Docs — PER_ACTION_OCCURRENCES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peractionoccurrences.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
