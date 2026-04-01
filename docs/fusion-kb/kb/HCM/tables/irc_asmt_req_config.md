---
id: DOC-HCM-441
doc_type: system-doc
title: "IRC_ASMT_REQ_CONFIG — Configuracao de Avaliacao por Requisicao"
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
  - irc
  - assessment
  - configuracao-requisicao
aliases:
  - IRC_ASMT_REQ_CONFIG
  - irc_asmt_req_config
  - irc-asmt-req-config
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_ASMT_REQ_CONFIG

## 📌 Visao Geral

Armazena a **configuracao de avaliacao por requisicao** de vaga do modulo Recruiting (IRC). Define quais avaliacoes sao aplicadas para cada requisicao especifica.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao por vaga:** define avaliacoes especificas para cada requisicao.
- **Personalizacao:** permite diferentes avaliacoes por tipo de vaga.
- **Automatizacao:** configura avaliacoes automaticas no fluxo de recrutamento.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQ_CONFIG_ID | NUMBER(18) | NOT NULL | PK | Identificador da configuracao | — | 🟡 70% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Requisicao de vaga | — | 🟡 70% |
| 3 | PARTNER_CONFIG_ID | NUMBER(18) | NULL | FK | Parceiro de avaliacao | IRC_ASMT_PARTNER_CONFIG | 🟡 65% |
| 4 | ASSESSMENT_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de avaliacao | — | 🟡 60% |
| 5 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Controle | Avaliacao obrigatoria | — | 🟡 55% |
| 6 | AUTO_INITIATE_FLAG | VARCHAR2(1) | NULL | Controle | Iniciar automaticamente | — | 🟡 55% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_asmt_partner_config]] — via `PARTNER_CONFIG_ID` (configuracao do parceiro de avaliacao)

### Tabelas-filha (FK de saida)
- [[irc_asmt_req_packages]] — via `REQ_CONFIG_ID` (pacotes por requisicao)

---

## 📎 Uso Tipico

### Configuracoes de avaliacao de uma requisicao
```sql
SELECT rc.ASSESSMENT_TYPE, rc.MANDATORY_FLAG,
       rc.AUTO_INITIATE_FLAG
FROM   IRC_ASMT_REQ_CONFIG rc
WHERE  rc.REQUISITION_ID = :p_req_id;
```

### Filtros comuns
- `REQUISITION_ID = :p_req_id — Por requisicao`
- `MANDATORY_FLAG = 'Y' — Avaliacoes obrigatorias`

---

## 🔒 Observacoes

- Define quais avaliacoes sao aplicadas por requisicao de vaga.
- Avaliacoes automaticas (AUTO_INITIATE_FLAG = 'Y') sao disparadas ao candidato avancar no fluxo.

---

## 📚 Referencias

- [Oracle Docs — IRC_ASMT_REQ_CONFIG](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircasmtreqconfig.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[asmtpackageresultviewallpvo|AsmtPackageResultViewAllPVO]] (HCM · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USERNAME | AsmtReqConfigPEOAccountUsername | ✅ |
| ASSESSMENT_CONFIG_ID | AsmtReqConfigPEOAssessmentConfigId | — |
| PROVISIONING_ID | AsmtReqConfigPEOProvisioningId | ✅ |
| REQUISITION_ID | AsmtReqConfigPEORequisitionId | ✅ |

### [[asmtreqpackageviewallpvo|AsmtReqPackageViewAllPVO]] (HCM · BICC: 5/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USERNAME | AsmtReqConfigPEOAccountUsername | ✅ |
| ASSESSMENT_CONFIG_ID | AsmtReqConfigPEOAssessmentConfigId | — |
| CREATED_BY | AsmtReqConfigPEOCreatedBy | — |
| CREATION_DATE | AsmtReqConfigPEOCreationDate | — |
| LAST_UPDATE_DATE | AsmtReqConfigPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AsmtReqConfigPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AsmtReqConfigPEOLastUpdatedBy | — |
| MULTI_PHASE_CSP_FLAG | AsmtReqConfigPEOMultiPhaseCspFlag | ✅ |
| OBJECT_VERSION_NUMBER | AsmtReqConfigPEOObjectVersionNumber | — |
| PROVISIONING_ID | AsmtReqConfigPEOProvisioningId | ✅ |
| REQUISITION_ID | AsmtReqConfigPEORequisitionId | ✅ |
