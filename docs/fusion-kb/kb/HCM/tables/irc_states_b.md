---
id: DOC-HCM-538
doc_type: system-doc
title: "IRC_STATES_B — Estados de Candidatura (Base)"
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
  - states
  - estados-candidatura
  - irc-states
aliases:
  - IRC_STATES_B
  - irc_states_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_STATES_B

## 📌 Visão Geral

Armazena os **estados** possiveis de uma candidatura no processo seletivo (ex.: nova, em analise, entrevista agendada, oferta, contratado, rejeitado). Tabela base com sufixo `_B`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao dos estados do fluxo de candidatura
- Configuracao de transicoes de estado validas
- Base para relatorios de funil de recrutamento

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STATE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do estado | --- | 🟢 90% |
| 2 | STATE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do estado | --- | 🟢 85% |
| 3 | STATE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do estado (phase, status) | --- | 🟡 70% |
| 4 | DISPLAY_ORDER | NUMBER | NULL | Dados | Ordem de exibicao | --- | 🟡 65% |
| 5 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Classificacao | Indica se o estado esta ativo (Y/N) | --- | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela de configuracao raiz

### Tabelas-filha (FK de saída)
- [[irc_states_tl]] --- via `STATE_ID` (traduções do estado do processo seletivo)

---

## 📎 Uso Típico

### Estados ativos ordenados por exibicao
```sql
SELECT sb.STATE_ID, sb.STATE_CODE, sb.STATE_TYPE, sb.DISPLAY_ORDER
FROM   IRC_STATES_B sb
WHERE  sb.ACTIVE_FLAG = 'Y'
ORDER BY sb.DISPLAY_ORDER;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[candidatepoolmemberpvo|CandidatePoolMemberPVO]] (PO · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE | Code1 | ✅ |
| STATE_ID | StateId | ✅ |
| TYPE_CODE | TypeCode1 | ✅ |

### [[jobapphisteventpvo|JobAppHistEventPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE | StateBPEOCode | ✅ |
| STATE_ID | StateBPEOStateId | — |

### [[jobreqhisteventpvo|JobReqHistEventPVO]] (PO · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE | StateBPEOCode | ✅ |
| STATE_ID | StateId | ✅ |

### [[poolcandhisteventpvo|PoolCandHistEventPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE | StateBPEOCode | ✅ |
| STATE_ID | StateId | — |

### [[statepvo|StatePVO]] (HCM · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE | Code | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODULE_ID | ModuleId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| STATE_ID | StateId | ✅ |
| TYPE_CODE | TypeCode | ✅ |

### [[wfmodelrequisitionpvo|WfModelRequisitionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE | StateBPEOCode | — |
| STATE_ID | StateBPEOStateId | — |
| TYPE_CODE | StateBPEOTypeCode | — |

---

## 📚 Referências

- [Oracle Docs — IRC_STATES_B](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircstatesb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
