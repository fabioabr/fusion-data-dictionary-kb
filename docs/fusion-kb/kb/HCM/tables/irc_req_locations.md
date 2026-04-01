---
id: DOC-HCM-525
doc_type: system-doc
title: "IRC_REQ_LOCATIONS — Localizacoes de Requisicoes"
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
  - req-locations
  - irc-recruiting
aliases:
  - IRC_REQ_LOCATIONS
  - irc_req_locations
  - req-locations
  - req-locations-hcm
  - irc-req-locations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_REQ_LOCATIONS

## Visao Geral

**Localizacoes** de requisicoes de vaga. Suporte a vagas multi-localidade.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Multi-localidade:** Requisicoes com multiplas localizacoes.
- **Filtragem geografica:** Vagas por localizacao.
- **Relatorios regionais:** Distribuicao de vagas.
- **Career site:** Localizacoes nas publicacoes.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQ_LOCATION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Requisicao | IRC_REQUISITIONS_B | 🟢 90% |
| 3 | LOCATION_ID | NUMBER(18) | NULL | FK | Localizacao | — | 🟢 85% |
| 4 | LOCATION_NAME | VARCHAR2(240) | NULL | Dados | Nome da localizacao | — | 🟡 75% |
| 5 | COUNTRY_CODE | VARCHAR2(30) | NULL | Dados | Pais | — | 🟡 75% |
| 6 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Classificacao | Principal (Y/N) | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao da localidade da vaga)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Localizacoes de uma requisicao
```sql
SELECT rl.LOCATION_NAME, rl.COUNTRY_CODE, rl.PRIMARY_FLAG
FROM   IRC_REQ_LOCATIONS rl WHERE rl.REQUISITION_ID = :p_id;
```

### Filtros comuns
- `PRIMARY_FLAG = 'Y'` — Principal
- `COUNTRY_CODE = 'BR'` — Brasil
---

## Observacoes

- Multiplas localizacoes por requisicao.
- PRIMARY_FLAG indica localizacao principal.
- Suporta vagas remotas.
---

## Referencias

- [Oracle Docs -- IRC_REQ_LOCATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircreqlocations.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[requisitionlocationpvo|RequisitionLocationPVO]] (PO · BICC: 3/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| GEOGRAPHY_ID | GeographyId | ✅ |
| GEOGRAPHY_NODE_ID | GeographyNodeId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| REQUISITION_ID | RequisitionId | ✅ |
