---
id: DOC-HCM-754
doc_type: system-doc
title: "ZMM_SR_SCHEDULES_B — Escalas de Trabalho (Base)"
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
  - work-schedules
  - workforce-management
aliases:
  - ZMM_SR_SCHEDULES_B
  - zmm_sr_schedules_b
  - escalas-trabalho-base
  - work-schedules-base
  - zmm-sr-schedules
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ZMM_SR_SCHEDULES_B

## 📌 Visão Geral

Tabela base customizada (prefixo `ZMM`) que armazena as **escalas de trabalho** (Schedules) do módulo HCM. Define as escalas efetivas atribuídas a colaboradores ou grupos, vinculando padrões de escala a períodos de vigência. O sufixo `_B` indica tabela base sem tradução.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Atribuição de escalas:** Vincula colaboradores ou unidades organizacionais a escalas de trabalho específicas.
- **Controle de jornada:** Base para o registro de presença, cálculo de horas trabalhadas e gestão de ponto.
- **Planejamento operacional:** Permite planejar cobertura de turnos e alocação de recursos humanos.
- **Integração com folha:** Fornece dados de escala para cálculos de remuneração variável, adicional noturno e horas extras.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCHEDULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da escala de trabalho | — | 🟡 80% |
| 2 | SCHEDULE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código alfanumérico da escala | — | 🟡 75% |
| 3 | PATTERN_ID | NUMBER(18) | NULL | FK | Referência ao padrão de escala utilizado | [[zmm_sr_patterns_b]].PATTERN_ID | 🟡 70% |
| 4 | START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência da escala | — | 🟡 75% |
| 5 | END_DATE | DATE | NULL | Vigência | Data de término da vigência da escala | — | 🟡 75% |
| 6 | SCHEDULE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da escala (fixa, rotativa, flexível) | — | 🟡 65% |
| 7 | ACTIVE_FLAG | VARCHAR2(1) | NOT NULL | Status | Indica se a escala está ativa (Y/N) | — | 🟡 70% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[zmm_sr_patterns_b]] — via `PATTERN_ID` (padrão de escala utilizado)

### Tabelas-filha
- [[zmm_sr_schedules_tl]] — via `SCHEDULE_ID` (traduções da escala)

---

## 📎 Uso Típico

### Escalas ativas com seus padrões
```sql
SELECT s.SCHEDULE_ID, s.SCHEDULE_CODE,
       s.SCHEDULE_TYPE, s.START_DATE, s.END_DATE,
       p.PATTERN_CODE
FROM   ZMM_SR_SCHEDULES_B s
LEFT JOIN ZMM_SR_PATTERNS_B p ON p.PATTERN_ID = s.PATTERN_ID
WHERE  s.ACTIVE_FLAG = 'Y'
  AND  SYSDATE BETWEEN s.START_DATE AND NVL(s.END_DATE, SYSDATE + 1);
```

### Escalas por tipo
```sql
SELECT s.SCHEDULE_TYPE, COUNT(*) AS qtd
FROM   ZMM_SR_SCHEDULES_B s
WHERE  s.ACTIVE_FLAG = 'Y'
GROUP BY s.SCHEDULE_TYPE;
```

---

## 🔒 Observações

- Tabela customizada (prefixo `ZMM`) — não faz parte do modelo padrão Oracle Fusion. Estrutura inferida por naming convention.
- Tabela base (sufixo `_B`) — traduções armazenadas em [[zmm_sr_schedules_tl]].
- Padrão Oracle de versionamento via `OBJECT_VERSION_NUMBER` para controle de concorrência.
- Escalas sem `END_DATE` indicam vigência indefinida.
- Uma escala pode existir sem `PATTERN_ID` quando a definição de dias é feita diretamente em tabelas de detalhe.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
