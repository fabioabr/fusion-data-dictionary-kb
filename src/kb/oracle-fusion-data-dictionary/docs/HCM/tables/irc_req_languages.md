---
id: DOC-HCM-524
doc_type: system-doc
title: "IRC_REQ_LANGUAGES — Idiomas de Requisicoes"
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
  - req-languages
  - irc-recruiting
aliases:
  - IRC_REQ_LANGUAGES
  - irc_req_languages
  - req-languages
  - req-languages-hcm
  - irc-req-languages
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_REQ_LANGUAGES

## Visao Geral

**Idiomas** associados a requisicoes de vaga. Proficiencia exigida.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Requisitos linguisticos:** Idiomas necessarios para a vaga.
- **Filtragem:** Vagas por idioma exigido.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQ_LANGUAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Requisicao | IRC_REQUISITIONS_B | 🟢 90% |
| 3 | LANGUAGE_CODE | VARCHAR2(4) | NOT NULL | Dados | Idioma | — | 🟢 90% |
| 4 | PROFICIENCY_LEVEL | VARCHAR2(30) | NULL | Classificacao | Nivel de proficiencia | — | 🟡 70% |
| 5 | REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificacao | Obrigatorio (Y/N) | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao do idioma exigido)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Idiomas de uma requisicao
```sql
SELECT rl.LANGUAGE_CODE, rl.PROFICIENCY_LEVEL, rl.REQUIRED_FLAG
FROM   IRC_REQ_LANGUAGES rl WHERE rl.REQUISITION_ID = :p_id;
```

### Filtros comuns
- `REQUIRED_FLAG = 'Y'` — Obrigatorios
---

## Observacoes

- Multiplos idiomas por requisicao.
- REQUIRED_FLAG diferencia obrigatorios de desejaveis.
---

## Referencias

- [Oracle Docs -- IRC_REQ_LANGUAGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircreqlanguages.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[requisitionlanguagepvo|RequisitionLanguagePVO]] (PO · BICC: 8/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| IS_BASE_FLAG | IsBaseFlag | ✅ |
| LANGUAGE_CODE | LanguageCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| REQ_LANGUAGE_ID | ReqLanguageId | ✅ |
| REQUISITION_ID | RequisitionId | ✅ |
