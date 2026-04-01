---
id: DOC-HCM-527
doc_type: system-doc
title: "IRC_REQ_WORK_LOCATIONS — Localizacoes de Trabalho de Requisicoes"
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
  - work-locations
  - requisicao
  - irc-req-locations
aliases:
  - IRC_REQ_WORK_LOCATIONS
  - irc_req_work_locations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_REQ_WORK_LOCATIONS

## 📌 Visão Geral

Armazena as **localizacoes de trabalho** associadas a cada requisicao de recrutamento. Permite que uma vaga seja publicada para multiplas localidades.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de locais de trabalho elegiveis por vaga
- Filtro geografico para candidatos
- Relatorios de vagas por localidade

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQ_WORK_LOCATION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da localizacao | --- | 🟢 90% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | ID da requisicao associada | IRC_REQUISITIONS_B | 🟢 90% |
| 3 | LOCATION_ID | NUMBER(18) | NULL | FK | ID da localizacao de trabalho | HR_LOCATIONS_ALL | 🟢 85% |
| 4 | GEOGRAPHY_ID | NUMBER(18) | NULL | FK | ID da geografia associada | --- | 🟡 70% |
| 5 | PRIMARY_LOCATION_FLAG | VARCHAR2(1) | NULL | Classificacao | Indica se eh a localizacao principal (Y/N) | --- | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_requisitions_b]] --- via `REQUISITION_ID` (requisicao do local de trabalho)
- [[hr_locations_all]] --- via `LOCATION_ID` (localidade do local de trabalho da vaga)

### Tabelas-filha (FK de saída)
- --- Tabelas de candidatura e posting do Recruiting

---

## 📎 Uso Típico

### Localizacoes de trabalho por requisicao
```sql
SELECT rwl.LOCATION_ID, rwl.PRIMARY_LOCATION_FLAG
FROM   IRC_REQ_WORK_LOCATIONS rwl
WHERE  rwl.REQUISITION_ID = :p_requisition_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[requisitionworklocationpvo|RequisitionWorkLocationPVO]] (PO · BICC: 3/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOCATION_ID | LocationId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| REQUISITION_ID | RequisitionId | ✅ |

---

## 📚 Referências

- [Oracle Docs — IRC_REQ_WORK_LOCATIONS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircreqworklocations.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
