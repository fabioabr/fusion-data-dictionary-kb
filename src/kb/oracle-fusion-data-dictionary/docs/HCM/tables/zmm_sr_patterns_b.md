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

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
