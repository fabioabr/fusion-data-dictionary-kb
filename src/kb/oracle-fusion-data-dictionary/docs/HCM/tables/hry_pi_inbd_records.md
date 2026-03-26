---
id: DOC-HCM-272
doc_type: system-doc
title: "HRY_PI_INBD_RECORDS — Registros de Inbound de Informacoes Pessoais"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - inbound
  - integracao
  - hdl
aliases:
  - HRY_PI_INBD_RECORDS
  - hry_pi_inbd_records
  - hry-pi-inbd-records
  - pi-inbd-records
  - registros-inbound-pessoal
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRY_PI_INBD_RECORDS

## 📌 Visao Geral

Armazena os **registros de carga inbound** (entrada) de informacoes pessoais via HDL (HCM Data Loader) ou outras interfaces de integracao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Integracao:** Registrar dados importados via HDL.
- **Rastreabilidade:** Auditar cargas de dados pessoais.
- **Troubleshooting:** Identificar erros em cargas de dados.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PI_INBD_RECORD_ID | NUMBER(18) | NOT NULL | PK | Identificador do registro inbound | — | 🟢 90% |
| 2 | BATCH_ID | NUMBER(18) | NULL | FK | Lote de importacao | — | 🟡 80% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa associada | [[per_all_people_f]] | 🟡 80% |
| 4 | RECORD_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de registro importado | — | 🟡 75% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do registro (SUCCESS, ERROR) | — | 🟡 80% |
| 6 | ERROR_MESSAGE | VARCHAR2(4000) | NULL | Dados | Mensagem de erro (se houver) | — | 🟡 75% |
| 7 | SOURCE_SYSTEM | VARCHAR2(30) | NULL | Classificacao | Sistema de origem | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa do registro de integracao inbound)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Registros com erro
```sql
SELECT pi.PI_INBD_RECORD_ID, pi.RECORD_TYPE,
       pi.ERROR_MESSAGE
FROM   HRY_PI_INBD_RECORDS pi
WHERE  pi.BATCH_ID = :p_batch_id
  AND  pi.STATUS = 'ERROR';
```

---

## 🔒 Observacoes

- Tabela de staging para cargas inbound.
- Registros com STATUS = 'ERROR' devem ser investigados e reprocessados.

---

## 📚 Referencias

- [Oracle Docs — HRY_PI_INBD_RECORDS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrypiinbdrecords.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
