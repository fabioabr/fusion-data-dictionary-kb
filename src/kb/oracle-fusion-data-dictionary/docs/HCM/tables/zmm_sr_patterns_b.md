---
id: DOC-HCM-751
doc_type: system-doc
title: "ZMM_SR_PATTERNS_B — Padrões de Escala de Trabalho (Base)"
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
  - workforce-management
aliases:
  - ZMM_SR_PATTERNS_B
  - zmm_sr_patterns_b
  - padroes-escala-trabalho
  - schedule-patterns-base
  - zmm-sr-patterns
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ZMM_SR_PATTERNS_B

## 📌 Visão Geral

Tabela base customizada (prefixo `ZMM`) que armazena os **padrões de escala de trabalho** (Schedule/Roster Patterns) do módulo HCM. Define os modelos recorrentes de jornada utilizados para compor escalas de trabalho dos colaboradores. O sufixo `_B` indica tabela base sem tradução.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de escalas:** Define padrões reutilizáveis de jornada (ex.: 5x2, 6x1, 12x36) que são aplicados na montagem de escalas.
- **Planejamento de força de trabalho:** Permite configurar modelos de turnos e folgas que atendem a requisitos operacionais e legais.
- **Conformidade trabalhista:** Armazena padrões que respeitam limites de jornada, intervalos obrigatórios e legislação vigente.
- **Automação de escalas:** Base para a geração automática de escalas de trabalho a partir de padrões pré-definidos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PATTERN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do padrão de escala | — | 🟡 80% |
| 2 | PATTERN_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código alfanumérico do padrão (ex.: PAT_5X2) | — | 🟡 75% |
| 3 | PATTERN_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do padrão (rotativo, fixo, flexível) | — | 🟡 70% |
| 4 | CYCLE_DAYS | NUMBER(5) | NULL | Configuração | Número total de dias no ciclo do padrão | — | 🟡 65% |
| 5 | ACTIVE_FLAG | VARCHAR2(1) | NOT NULL | Status | Indica se o padrão está ativo (Y/N) | — | 🟡 70% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 11 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma identificada — tabela raiz do padrão de escala.

### Tabelas-filha
- [[zmm_sr_patterns_tl]] — via `PATTERN_ID` (traduções do padrão)
- [[zmm_sr_pattern_dtls]] — via `PATTERN_ID` (detalhes/dias do padrão)
- [[zmm_sr_schedules_b]] — via `PATTERN_ID` (escalas que utilizam este padrão)

---

## 📎 Uso Típico

### Padrões de escala ativos
```sql
SELECT p.PATTERN_ID, p.PATTERN_CODE,
       p.PATTERN_TYPE, p.CYCLE_DAYS
FROM   ZMM_SR_PATTERNS_B p
WHERE  p.ACTIVE_FLAG = 'Y'
ORDER BY p.PATTERN_CODE;
```

---

## 🔒 Observações

- Tabela customizada (prefixo `ZMM`) — não faz parte do modelo padrão Oracle Fusion. Estrutura inferida por naming convention.
- Tabela base (sufixo `_B`) — traduções armazenadas em [[zmm_sr_patterns_tl]].
- Padrão Oracle de versionamento via `OBJECT_VERSION_NUMBER` para controle de concorrência.
- Os detalhes de cada dia do padrão são armazenados em [[zmm_sr_pattern_dtls]].

---

## 🔗 PVOs Relacionados

### [[patternextractpvo|PatternExtractPVO]] (OTHER · BICC: 40/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | PatternPEOAttribute1 | ✅ |
| ATTRIBUTE10 | PatternPEOAttribute10 | ✅ |
| ATTRIBUTE11 | PatternPEOAttribute11 | ✅ |
| ATTRIBUTE12 | PatternPEOAttribute12 | ✅ |
| ATTRIBUTE13 | PatternPEOAttribute13 | ✅ |
| ATTRIBUTE14 | PatternPEOAttribute14 | ✅ |
| ATTRIBUTE15 | PatternPEOAttribute15 | ✅ |
| ATTRIBUTE16 | PatternPEOAttribute16 | ✅ |
| ATTRIBUTE17 | PatternPEOAttribute17 | ✅ |
| ATTRIBUTE18 | PatternPEOAttribute18 | ✅ |
| ATTRIBUTE19 | PatternPEOAttribute19 | ✅ |
| ATTRIBUTE2 | PatternPEOAttribute2 | ✅ |
| ATTRIBUTE20 | PatternPEOAttribute20 | ✅ |
| ATTRIBUTE21 | PatternPEOAttribute21 | ✅ |
| ATTRIBUTE22 | PatternPEOAttribute22 | ✅ |
| ATTRIBUTE23 | PatternPEOAttribute23 | ✅ |
| ATTRIBUTE24 | PatternPEOAttribute24 | ✅ |
| ATTRIBUTE25 | PatternPEOAttribute25 | ✅ |
| ATTRIBUTE26 | PatternPEOAttribute26 | ✅ |
| ATTRIBUTE27 | PatternPEOAttribute27 | ✅ |
| ATTRIBUTE28 | PatternPEOAttribute28 | ✅ |
| ATTRIBUTE29 | PatternPEOAttribute29 | ✅ |
| ATTRIBUTE3 | PatternPEOAttribute3 | ✅ |
| ATTRIBUTE30 | PatternPEOAttribute30 | ✅ |
| ATTRIBUTE4 | PatternPEOAttribute4 | ✅ |
| ATTRIBUTE5 | PatternPEOAttribute5 | ✅ |
| ATTRIBUTE6 | PatternPEOAttribute6 | ✅ |
| ATTRIBUTE7 | PatternPEOAttribute7 | ✅ |
| ATTRIBUTE8 | PatternPEOAttribute8 | ✅ |
| ATTRIBUTE9 | PatternPEOAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | PatternPEOAttributeCategory | ✅ |
| CREATED_BY | PatternPEOCreatedBy | ✅ |
| CREATION_DATE | PatternPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | PatternPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PatternPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PatternPEOLastUpdatedBy | ✅ |
| LENGTH_DAYS_NUM | PatternPEOLengthDaysNum | ✅ |
| OBJECT_VERSION_NUMBER | PatternPEOObjectVersionNumber | ✅ |
| PATTERN_ID | PatternId | ✅ |
| PATTERN_TYPE_CODE | PatternPEOPatternTypeCode | ✅ |

### [[scheduleassignmentpvo|ScheduleAssignmentPVO]] (GL · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | PatternsPEOAttribute1 | — |
| ATTRIBUTE10 | PatternsPEOAttribute10 | — |
| ATTRIBUTE11 | PatternsPEOAttribute11 | — |
| ATTRIBUTE12 | PatternsPEOAttribute12 | — |
| ATTRIBUTE13 | PatternsPEOAttribute13 | — |
| ATTRIBUTE14 | PatternsPEOAttribute14 | — |
| ATTRIBUTE15 | PatternsPEOAttribute15 | — |
| ATTRIBUTE16 | PatternsPEOAttribute16 | — |
| ATTRIBUTE17 | PatternsPEOAttribute17 | — |
| ATTRIBUTE18 | PatternsPEOAttribute18 | — |
| ATTRIBUTE19 | PatternsPEOAttribute19 | — |
| ATTRIBUTE2 | PatternsPEOAttribute2 | — |
| ATTRIBUTE20 | PatternsPEOAttribute20 | — |
| ATTRIBUTE21 | PatternsPEOAttribute21 | — |
| ATTRIBUTE22 | PatternsPEOAttribute22 | — |
| ATTRIBUTE23 | PatternsPEOAttribute23 | — |
| ATTRIBUTE24 | PatternsPEOAttribute24 | — |
| ATTRIBUTE25 | PatternsPEOAttribute25 | — |
| ATTRIBUTE26 | PatternsPEOAttribute26 | — |
| ATTRIBUTE27 | PatternsPEOAttribute27 | — |
| ATTRIBUTE28 | PatternsPEOAttribute28 | — |
| ATTRIBUTE29 | PatternsPEOAttribute29 | — |
| ATTRIBUTE3 | PatternsPEOAttribute3 | — |
| ATTRIBUTE30 | PatternsPEOAttribute30 | — |
| ATTRIBUTE4 | PatternsPEOAttribute4 | — |
| ATTRIBUTE5 | PatternsPEOAttribute5 | — |
| ATTRIBUTE6 | PatternsPEOAttribute6 | — |
| ATTRIBUTE7 | PatternsPEOAttribute7 | — |
| ATTRIBUTE8 | PatternsPEOAttribute8 | — |
| ATTRIBUTE9 | PatternsPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PatternsPEOAttributeCategory | — |
| CREATED_BY | PatternsPEOCreatedBy | — |
| CREATION_DATE | PatternsPEOCreationDate | — |
| DELETED_FLAG | PatternsPEODeletedFlag | — |
| LAST_UPDATE_DATE | PatternsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PatternsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PatternsPEOLastUpdatedBy | — |
| LENGTH_DAYS_NUM | PatternsPEOLengthDaysNum | — |
| NUMERIC_DAY_FLAG | PatternsPEONumericDayFlag | — |
| OBJECT_VERSION_NUMBER | PatternsPEOObjectVersionNumber | — |
| PATTERN_ID | PatternsPEOPatternId | — |
| PATTERN_TYPE_CODE | PatternsPEOPatternTypeCode | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
