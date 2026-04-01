---
id: DOC-HCM-539
doc_type: system-doc
title: "IRC_STATES_TL — Estados de Candidatura (Traducoes)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - states-tl
  - traducoes
  - irc-states-tl
aliases:
  - IRC_STATES_TL
  - irc_states_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_STATES_TL

## 📌 Visão Geral

Armazena as **traducoes** dos nomes e descricoes dos estados de candidatura para multiplos idiomas. Tabela de traducao com sufixo `_TL`, vinculada a `IRC_STATES_B`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Suporte multiidioma para estados de candidatura
- Exibicao localizada de estados no portal de carreiras
- Relatorios em idioma local do usuario

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STATE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do estado (chave composta) | IRC_STATES_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma (ex.: PT, EN, ES) | --- | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Dados | Idioma de origem da traducao | --- | 🟢 85% |
| 4 | STATE_NAME | VARCHAR2(240) | NULL | Identificacao | Nome traduzido do estado | --- | 🟢 85% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida do estado | --- | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_states_b]] --- via `STATE_ID` (tabela base do estado do processo seletivo)

### Tabelas-filha (FK de saída)
- --- Tabela de traducao, sem filhas

---

## 📎 Uso Típico

### Traducao de um estado no idioma corrente
```sql
SELECT tl.STATE_NAME, tl.DESCRIPTION
FROM   IRC_STATES_TL tl
WHERE  tl.STATE_ID = :p_state_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[asmtreqpackageviewallpvo|AsmtReqPackageViewAllPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | StateTranslationPEOLanguage | — |
| NAME | StateTranslationPEOName | ✅ |
| STATE_ID | StateTranslationPEOStateId | — |

### [[candidatepoolmemberpvo|CandidatePoolMemberPVO]] (PO · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | Language1 | ✅ |
| NAME | Name1 | ✅ |
| STATE_ID | StateId1 | ✅ |

### [[routingstepstatepvo|RoutingStepStatePVO]] (HCM · BICC: 3/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | PublicStateTranslationPEOActionDescription | — |
| DESCRIPTION | StateTranslationPEODescription | ✅ |
| LANGUAGE | PublicStateTranslationPEOLanguage | — |
| LANGUAGE | StateTranslationPEOLanguage | — |
| NAME | PublicStateTranslationPEOName | ✅ |
| NAME | StateTranslationPEOName | ✅ |
| SOURCE_LANG | PublicStateTranslationPEOSourceLang | — |
| SOURCE_LANG | StateTranslationPEOSourceLang | — |
| STATE_ID | PublicStateTranslationPEOStateId | — |
| STATE_ID | StateTranslationPEOStateId | — |

### [[statepvo|StatePVO]] (HCM · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy1 | ✅ |
| CREATION_DATE | CreationDate1 | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LANGUAGE | Language1 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy1 | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
| STATE_ID | StateId1 | ✅ |

### [[wfmodelrequisitionpvo|WfModelRequisitionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | StateTranslationLanguage | — |
| NAME | StateTranslationPEOName | — |
| STATE_ID | StateTranslationStateId | — |

---

## 📚 Referências

- [Oracle Docs — IRC_STATES_TL](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircstatestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
