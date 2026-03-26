---
id: DOC-HCM-468
doc_type: system-doc
title: "IRC_CMT_LAUNCHES — Lancamentos de Comunicacoes"
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
  - communication-launches
  - irc-recruiting
aliases:
  - IRC_CMT_LAUNCHES
  - irc_cmt_launches
  - cmt-launches
  - cmt-launches-hcm
  - irc-cmt-launches
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CMT_LAUNCHES

## Visao Geral

Registra **lancamentos de comunicacoes** (e-mails, notificacoes) de recrutamento.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Rastreamento:** Historico de envios realizados.
- **Compliance:** Evidencia de comunicacoes obrigatorias.
- **Eficacia:** Correlacao entre envios e acoes de candidatos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CMT_LAUNCH_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | COMMUNICATION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de comunicacao | — | 🟡 70% |
| 3 | TEMPLATE_ID | NUMBER(18) | NULL | FK | Template utilizado | — | 🟡 70% |
| 4 | LAUNCH_DATE | TIMESTAMP | NULL | Dados | Data/hora do lancamento | — | 🟡 75% |
| 5 | LAUNCH_STATUS | VARCHAR2(30) | NULL | Classificacao | Status (sent, failed, pending) | — | 🟡 70% |
| 6 | LAUNCHED_BY | NUMBER(18) | NULL | FK | Pessoa que enviou | PER_ALL_PEOPLE_F | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `LAUNCHED_BY` (pessoa que disparou a comunicacao)

### Tabelas-filha (FK de saida)
- [[irc_cmt_recipients]] — via `CMT_LAUNCH_ID` (destinatarios da comunicacao de recrutamento)

---

## Uso Tipico

### Lancamentos recentes
```sql
SELECT cl.CMT_LAUNCH_ID, cl.COMMUNICATION_TYPE, cl.LAUNCH_STATUS
FROM   IRC_CMT_LAUNCHES cl
WHERE  cl.LAUNCH_DATE >= SYSDATE - 30
ORDER BY cl.LAUNCH_DATE DESC;
```

### Filtros comuns
- `LAUNCH_STATUS = 'SENT'` — Enviados
---

## Observacoes

- Cada lancamento pode ter multiplos destinatarios.
---

## Referencias

- [Oracle Docs -- IRC_CMT_LAUNCHES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccmtlaunches.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
