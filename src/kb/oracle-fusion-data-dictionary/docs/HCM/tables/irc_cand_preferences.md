---
id: DOC-HCM-464
doc_type: system-doc
title: "IRC_CAND_PREFERENCES — Preferencias de Candidatos"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - candidate-preferences
  - irc-recruiting
aliases:
  - IRC_CAND_PREFERENCES
  - irc_cand_preferences
  - cand-preferences
  - cand-preferences-hcm
  - irc-cand-preferences
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAND_PREFERENCES

## Visao Geral

Armazena **preferencias de emprego** dos candidatos: tipo de contrato, disponibilidade, pretensao salarial.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Matching candidato-vaga:** Comparar preferencias com requisitos.
- **Filtragem inteligente:** Shortlists por compatibilidade.
- **Experiencia do candidato:** Captura expectativas.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAND_PREFERENCE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato | IRC_CANDIDATES | 🟢 90% |
| 3 | PREFERENCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de preferencia | — | 🟡 70% |
| 4 | PREFERENCE_VALUE | VARCHAR2(240) | NULL | Dados | Valor da preferencia | — | 🟡 70% |
| 5 | WORK_TYPE | VARCHAR2(30) | NULL | Dados | Tipo de trabalho desejado | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato titular das preferencias)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Preferencias de um candidato
```sql
SELECT cp.PREFERENCE_TYPE, cp.PREFERENCE_VALUE, cp.WORK_TYPE
FROM   IRC_CAND_PREFERENCES cp
WHERE  cp.CANDIDATE_ID = :p_candidate_id;
```

### Filtros comuns
- `CANDIDATE_ID = :id` — Por candidato
---

## Observacoes

- Multiplas preferencias por candidato.
- Dados declarados pelo candidato.
---

## Referencias

- [Oracle Docs -- IRC_CAND_PREFERENCES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccandpreferences.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
