---
id: DOC-HCM-598
doc_type: system-doc
title: "PAY_RUN_TYPES_F — Tipos de Execucao de Folha"
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
  - payroll
  - run-types
  - tipos-execucao
  - pay-run-types
aliases:
  - PAY_RUN_TYPES_F
  - pay_run_types_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_RUN_TYPES_F

## 📌 Visão Geral

Armazena os **tipos de execucao** (run types) de folha de pagamento. Define as diferentes modalidades de processamento (regular, suplementar, reversa, etc.) com vigencia temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de modalidades de processamento de folha
- Configuracao de comportamento por tipo de execucao
- Controle de elementos incluidos por tipo de run

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RUN_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de execucao | --- | 🟢 90% |
| 2 | RUN_TYPE_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do tipo de execucao | --- | 🟢 85% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | SHORTNAME | VARCHAR2(30) | NULL | Identificacao | Nome curto | --- | 🟡 75% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | RUN_METHOD | VARCHAR2(30) | NULL | Classificacao | Metodo de execucao | --- | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela de configuracao raiz

### Tabelas-filha (FK de saída)
- [[pay_run_types_tl]] --- via `RUN_TYPE_ID` (traduções do tipo de execução de folha)

---

## 📎 Uso Típico

### Tipos de execucao vigentes por grupo legislativo
```sql
SELECT rt.RUN_TYPE_ID, rt.RUN_TYPE_NAME, rt.RUN_METHOD
FROM   PAY_RUN_TYPES_F rt
WHERE  rt.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id
  AND  SYSDATE BETWEEN rt.EFFECTIVE_START_DATE AND rt.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_RUN_TYPES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payruntypesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
