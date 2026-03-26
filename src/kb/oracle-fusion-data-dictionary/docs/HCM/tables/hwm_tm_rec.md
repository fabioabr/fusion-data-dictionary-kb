---
id: DOC-HCM-381
doc_type: system-doc
title: "HWM_TM_REC — Registros de Time Management"
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
  - time-management
  - time-record
  - registro-tempo
aliases:
  - HWM_TM_REC
  - hwm_tm_rec
  - hwm-tm-rec
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REC

## 📌 Visão Geral

Armazena os **registros de tempo** (time records) do módulo Time Management. Cada registro representa uma entrada de ponto ou tempo registrada por um colaborador.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de ponto:** armazena entradas de tempo dos colaboradores.
- **Base para folha de pagamento:** dados de horas trabalhadas alimentam o payroll.
- **Controle de jornada:** gestão de horas normais, extras e banco de horas.
- **Auditoria trabalhista:** evidência de jornada para conformidade legal.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TM_REC_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de tempo | — | 🟡 70% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Identificador da atribuição | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 4 | REC_DATE | DATE | NOT NULL | Período | Data do registro de tempo | — | 🟡 65% |
| 5 | REC_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do registro (normal, extra, etc.) | — | 🟡 60% |
| 6 | MEASURE | NUMBER | NULL | Dados | Quantidade de tempo registrado | — | 🟡 60% |
| 7 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 65% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa do registro de tempo)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo do registro de tempo)

### Tabelas-filha (FK de saída)
- [[hwm_tm_rec_grp]] — via `TM_REC_ID` (agrupamento de registros)

---

## 📎 Uso Típico

### Registros de tempo por colaborador
```sql
SELECT r.TM_REC_ID, r.PERSON_ID, r.REC_DATE,
       r.MEASURE, r.STATUS
FROM   HWM_TM_REC r
WHERE  r.PERSON_ID = :p_person_id
  AND  r.REC_DATE BETWEEN :dt_ini AND :dt_fim;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Filtrar por colaborador`
- `REC_DATE BETWEEN :dt_ini AND :dt_fim — Período`
- `STATUS = 'APPROVED' — Registros aprovados`

---

## 🔒 Observações

- Tabela central do módulo Time Management.
- Registros devem ser aprovados antes de serem enviados ao payroll.
- Integração com HXT (Time & Labor) para configurações avançadas.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_REC](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrec.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
