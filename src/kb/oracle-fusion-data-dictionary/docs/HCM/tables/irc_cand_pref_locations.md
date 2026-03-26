---
id: DOC-HCM-466
doc_type: system-doc
title: "IRC_CAND_PREF_LOCATIONS — Localizacoes Preferidas"
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
  - candidate-pref-location
  - irc-recruiting
aliases:
  - IRC_CAND_PREF_LOCATIONS
  - irc_cand_pref_locations
  - cand-pref-locations
  - cand-pref-hcm
  - irc-cand-pref-locations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAND_PREF_LOCATIONS

## Visao Geral

Armazena **localizacoes** preferidas por candidatos para trabalho.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Matching geografico:** Filtrar por localizacao desejada.
- **Planejamento:** Vagas em multiplas localidades.
- **Mobilidade:** Candidatos dispostos a realocacao.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAND_PREF_LOCATION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | CAND_PREFERENCE_ID | NUMBER(18) | NOT NULL | FK | Preferencia | IRC_CAND_PREFERENCES | 🟢 85% |
| 3 | LOCATION_ID | NUMBER(18) | NULL | FK | Localizacao | — | 🟡 75% |
| 4 | GEOGRAPHY_ID | NUMBER(18) | NULL | FK | Hierarquia geografica | IRC_GEO_HIERARCHIES | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_cand_preferences]] — via `CAND_PREFERENCE_ID` (preferencia do candidato por localidade)
- [[irc_geo_hierarchies]] — via `GEOGRAPHY_ID` (localidade geografica da preferencia)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Localizacoes preferidas
```sql
SELECT pl.LOCATION_ID, pl.GEOGRAPHY_ID
FROM   IRC_CAND_PREF_LOCATIONS pl
JOIN   IRC_CAND_PREFERENCES cp ON cp.CAND_PREFERENCE_ID = pl.CAND_PREFERENCE_ID
WHERE  cp.CANDIDATE_ID = :p_candidate_id;
```

### Filtros comuns
- `LOCATION_ID = :id` — Por localizacao
---

## Observacoes

- Tabela associativa entre preferencias e localizacoes.
- Multiplas localizacoes por candidato.
---

## Referencias

- [Oracle Docs -- IRC_CAND_PREF_LOCATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccandpreflocations.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
