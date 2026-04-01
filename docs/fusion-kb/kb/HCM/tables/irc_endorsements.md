---
id: DOC-HCM-484
doc_type: system-doc
title: "IRC_ENDORSEMENTS — Endossos de Candidatos"
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
  - endorsements
  - irc-recruiting
aliases:
  - IRC_ENDORSEMENTS
  - irc_endorsements
  - irc-endorsements
  - irc_endorsements-oracle
  - irc_endorsements-oracle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_ENDORSEMENTS

## Visao Geral

**Endossos e recomendacoes** de referencias para candidatos.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Referencias:** Centraliza recomendacoes.
- **Avaliacao qualitativa:** Feedback de referencias.
- **Compliance:** Rastreabilidade.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ENDORSEMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato | IRC_CANDIDATES | 🟢 85% |
| 3 | ENDORSER_NAME | VARCHAR2(240) | NULL | Dados | Nome do endossante | — | 🟡 70% |
| 4 | ENDORSER_EMAIL | VARCHAR2(240) | NULL | Contato | E-mail do endossante | — | 🟡 70% |
| 5 | ENDORSEMENT_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 70% |
| 6 | ENDORSEMENT_DATE | DATE | NULL | Dados | Data do endosso | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato que recebeu a indicacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Endossos recebidos
```sql
SELECT e.ENDORSER_NAME, e.ENDORSEMENT_STATUS, e.ENDORSEMENT_DATE
FROM   IRC_ENDORSEMENTS e
WHERE  e.CANDIDATE_ID = :p_candidate_id AND e.ENDORSEMENT_STATUS = 'RECEIVED';
```

### Filtros comuns
- `ENDORSEMENT_STATUS = 'RECEIVED'` — Recebidos
---

## Observacoes

- ENDORSER_EMAIL — dados sensiveis.
---

## Referencias

- [Oracle Docs -- IRC_ENDORSEMENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircendorsements.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[endorsementspvo|EndorsementsPVO]] (PO · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CANDIDATE_PERSON_ID | CandidatePersonId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ENDORSEMENT_ID | EndorsementId | ✅ |
| ENDORSER_PERSON_ID | EndorserPersonId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NOTES | Notes | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RATING | Rating | ✅ |
| REQUISITION_ID | RequisitionId | ✅ |
