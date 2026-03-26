---
id: DOC-HCM-469
doc_type: system-doc
title: "IRC_CMT_RECIPIENTS — Destinatarios de Comunicacoes"
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
  - communication-recipients
  - irc-recruiting
aliases:
  - IRC_CMT_RECIPIENTS
  - irc_cmt_recipients
  - cmt-recipients
  - cmt-recipients-hcm
  - irc-cmt-recipients
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CMT_RECIPIENTS

## Visao Geral

Armazena **destinatarios** de cada comunicacao lancada no recrutamento.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Rastreamento individual:** Quem recebeu cada comunicacao.
- **Entrega:** Status de recebimento por destinatario.
- **Compliance:** Comprovar envio a candidatos especificos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CMT_RECIPIENT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | CMT_LAUNCH_ID | NUMBER(18) | NOT NULL | FK | Lancamento | IRC_CMT_LAUNCHES | 🟢 85% |
| 3 | RECIPIENT_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de destinatario | — | 🟡 70% |
| 4 | RECIPIENT_ID | NUMBER(18) | NULL | FK | ID do destinatario | — | 🟡 75% |
| 5 | EMAIL_ADDRESS | VARCHAR2(240) | NULL | Contato | E-mail | — | 🟡 75% |
| 6 | DELIVERY_STATUS | VARCHAR2(30) | NULL | Classificacao | Status de entrega | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_cmt_launches]] — via `CMT_LAUNCH_ID` (comunicacao enviada ao destinatario)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Destinatarios de um lancamento
```sql
SELECT cr.RECIPIENT_TYPE, cr.EMAIL_ADDRESS, cr.DELIVERY_STATUS
FROM   IRC_CMT_RECIPIENTS cr
WHERE  cr.CMT_LAUNCH_ID = :p_launch_id;
```

### Filtros comuns
- `CMT_LAUNCH_ID = :id` — Por lancamento
---

## Observacoes

- EMAIL_ADDRESS — dados sensiveis.
- DELIVERY_STATUS monitora problemas de entrega.
---

## Referencias

- [Oracle Docs -- IRC_CMT_RECIPIENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccmtrecipients.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
