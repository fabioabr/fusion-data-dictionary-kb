---
id: DOC-HCM-498
doc_type: system-doc
title: "IRC_JA_SECONDARY_FLOWS — Fluxos Secundarios de Candidatura"
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
  - secondary-flows
  - irc-recruiting
aliases:
  - IRC_JA_SECONDARY_FLOWS
  - irc_ja_secondary_flows
  - ja-secondary-flows
  - ja-secondary-hcm
  - irc-ja-secondary-flows
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_JA_SECONDARY_FLOWS

## Visao Geral

**Fluxos secundarios** de candidaturas. Caminhos alternativos ao fluxo principal.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Flexibilidade:** Fluxos paralelos no processo.
- **Avaliacoes adicionais:** Etapas complementares.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JA_SECONDARY_FLOW_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | JOB_APPLICATION_ID | NUMBER(18) | NOT NULL | FK | Candidatura | — | 🟢 85% |
| 3 | FLOW_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de fluxo | — | 🟡 70% |
| 4 | FLOW_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Fluxos secundarios ativos
```sql
SELECT sf.FLOW_TYPE, sf.FLOW_STATUS
FROM   IRC_JA_SECONDARY_FLOWS sf
WHERE  sf.JOB_APPLICATION_ID = :p_id AND sf.FLOW_STATUS = 'ACTIVE';
```

### Filtros comuns
- `FLOW_STATUS = 'ACTIVE'` — Ativos
---

## Observacoes

- Fluxos paralelos ao principal.
---

## Referencias

- [Oracle Docs -- IRC_JA_SECONDARY_FLOWS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircjasecondaryflows.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[esignaturepvo|ESignaturePVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AF_VERSION_ID | JASecondaryFlowsPEOAfVersionId | ✅ |
| SECONDARY_FLOW_ID | JASecondaryFlowsPEOSecondaryFlowId | — |
