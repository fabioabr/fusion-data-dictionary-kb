---
id: DOC-HCM-020
doc_type: system-doc
title: "ANC_PER_ABS_TYPE_ENTRIES — Entradas de Tipo de Ausência por Pessoa"
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
  - absence-management
  - entradas-tipo
  - type-entries
  - absenteismo
aliases:
  - ANC_PER_ABS_TYPE_ENTRIES
  - anc_per_abs_type_entries
  - entradas-tipo-ausencia
  - absence-type-entries
  - anc-per-abs-type-entries
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ABS_TYPE_ENTRIES

## 📌 Visão Geral

Armazena as **entradas de ausência agregadas por tipo** para cada colaborador. Consolida dados de utilização por tipo de ausência.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consolidação por tipo:** Visão agregada de ausências por tipo para cada colaborador.
- **Relatórios de absenteísmo:** Análise de freqüência e duração por tipo.
- **Thresholds e alertas:** Base para regras de alerta por tipo (ex.: mais de X dias de falta injustificada).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_ABS_TYPE_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 85% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | ABSENCE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de ausência | [[anc_absence_types_f]] | 🟢 90% |
| 4 | TOTAL_DURATION | NUMBER | NULL | Duração | Duração total acumulada | — | 🟡 75% |
| 5 | TOTAL_OCCURRENCES | NUMBER | NULL | Contagem | Número total de ocorrências | — | 🟡 75% |
| 6 | PERIOD_START_DATE | DATE | NULL | Período | Início do período | — | 🟡 70% |
| 7 | PERIOD_END_DATE | DATE | NULL | Período | Fim do período | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do saldo por tipo de ausencia)
- [[anc_absence_types_f]] — via `ABSENCE_TYPE_ID` (tipo de ausencia do saldo)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Total de ausências por tipo e colaborador
```sql
SELECT te.PERSON_ID, t.ABSENCE_TYPE_NAME,
       te.TOTAL_DURATION, te.TOTAL_OCCURRENCES
FROM   ANC_PER_ABS_TYPE_ENTRIES te
JOIN   ANC_ABSENCE_TYPES_F t ON te.ABSENCE_TYPE_ID = t.ABSENCE_TYPE_ID
WHERE  te.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN t.EFFECTIVE_START_DATE AND t.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `TOTAL_OCCURRENCES > :threshold` — Colaboradores acima do limite de ocorrências

---

## 🔒 Observações

- Tabela de consolidação por tipo de ausência.
- Pode conter múltiplos registros por colaborador (um por tipo e período).
- Útil para dashboards de absenteísmo e análises de tendência.

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ABS_TYPE_ENTRIES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperabstypeentries.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
