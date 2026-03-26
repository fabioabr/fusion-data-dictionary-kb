---
id: DOC-HCM-753
doc_type: system-doc
title: "ZMM_SR_PATTERN_DTLS — Detalhes dos Padrões de Escala de Trabalho"
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
  - schedule-patterns
  - pattern-details
aliases:
  - ZMM_SR_PATTERN_DTLS
  - zmm_sr_pattern_dtls
  - detalhes-padroes-escala
  - schedule-pattern-details
  - zmm-sr-pattern-dtls
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ZMM_SR_PATTERN_DTLS

## 📌 Visão Geral

Tabela customizada (prefixo `ZMM`) que armazena os **detalhes granulares de cada dia** dentro de um padrão de escala de trabalho. Cada registro representa um dia específico do ciclo do padrão, indicando se é dia de trabalho ou folga, horários de início/fim e tipo de turno.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de turnos:** Especifica, para cada dia do ciclo do padrão, os horários de trabalho e tipo de jornada.
- **Gestão de folgas:** Identifica quais dias do padrão são folgas, descansos semanais ou feriados programados.
- **Cálculo de horas:** Fornece a base granular para cálculos de horas trabalhadas, extras e noturnas.
- **Montagem de escalas:** Cada dia do padrão é replicado ciclicamente ao gerar a escala efetiva do colaborador.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PATTERN_DTL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe do padrão | — | 🟡 75% |
| 2 | PATTERN_ID | NUMBER(18) | NOT NULL | FK | Referência ao padrão de escala | [[zmm_sr_patterns_b]].PATTERN_ID | 🟡 80% |
| 3 | DAY_SEQUENCE | NUMBER(5) | NOT NULL | Ordenação | Número sequencial do dia dentro do ciclo (1, 2, 3...) | — | 🟡 70% |
| 4 | DAY_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do dia (WORK, OFF, HOLIDAY, REST) | — | 🟡 65% |
| 5 | START_TIME | VARCHAR2(5) | NULL | Horário | Hora de início do turno (formato HH:MI) | — | 🟡 60% |
| 6 | END_TIME | VARCHAR2(5) | NULL | Horário | Hora de fim do turno (formato HH:MI) | — | 🟡 60% |
| 7 | SHIFT_CODE | VARCHAR2(30) | NULL | Classificação | Código do turno aplicável (manhã, tarde, noite) | — | 🔴 50% |
| 8 | HOURS | NUMBER(5,2) | NULL | Cálculo | Total de horas previstas para o dia | — | 🟡 60% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 14 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[zmm_sr_patterns_b]] — via `PATTERN_ID` (padrão ao qual o detalhe pertence)

### Tabelas-filha
- Nenhuma identificada — tabela de detalhe granular (nível folha).

---

## 📎 Uso Típico

### Dias de trabalho de um padrão de escala
```sql
SELECT d.DAY_SEQUENCE, d.DAY_TYPE,
       d.START_TIME, d.END_TIME, d.HOURS
FROM   ZMM_SR_PATTERN_DTLS d
WHERE  d.PATTERN_ID = :p_pattern_id
  AND  d.DAY_TYPE = 'WORK'
ORDER BY d.DAY_SEQUENCE;
```

### Total de horas previstas por padrão
```sql
SELECT p.PATTERN_CODE,
       SUM(d.HOURS) AS total_horas_ciclo
FROM   ZMM_SR_PATTERNS_B p
JOIN   ZMM_SR_PATTERN_DTLS d ON d.PATTERN_ID = p.PATTERN_ID
WHERE  p.ACTIVE_FLAG = 'Y'
GROUP BY p.PATTERN_CODE;
```

---

## 🔒 Observações

- Tabela customizada (prefixo `ZMM`) — não faz parte do modelo padrão Oracle Fusion. Estrutura inferida por naming convention.
- A quantidade de registros por `PATTERN_ID` deve corresponder ao `CYCLE_DAYS` da tabela [[zmm_sr_patterns_b]].
- `DAY_SEQUENCE` deve ser contíguo e iniciar em 1.
- Dias do tipo `OFF` ou `REST` tipicamente possuem `START_TIME`, `END_TIME` e `HOURS` nulos.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
