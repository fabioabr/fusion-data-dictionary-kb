---
id: DOC-HCM-558
doc_type: system-doc
title: "PAY_CONSOLIDATION_SETS — Conjuntos de Consolidacao de Folha"
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
  - consolidation-sets
  - consolidacao
  - pay-consol-sets
aliases:
  - PAY_CONSOLIDATION_SETS
  - pay_consolidation_sets
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_CONSOLIDATION_SETS

## 📌 Visão Geral

Armazena os **conjuntos de consolidacao** (consolidation sets) que agrupam resultados de folha para fins de processamento de pagamento e contabilizacao. Um consolidation set eh o nivel no qual pagamentos sao gerados.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Agrupamento de resultados de folha para pagamento
- Configuracao de conjuntos para contabilizacao separada
- Controle de processamento de pagamentos por grupo

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONSOLIDATION_SET_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do conjunto | --- | 🟢 90% |
| 2 | CONSOLIDATION_SET_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do conjunto de consolidacao | --- | 🟢 85% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Dados | Descricao do conjunto | --- | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | --- | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela de configuracao raiz

### Tabelas-filha (FK de saída)
- [[pay_costs]] --- via `CONSOLIDATION_SET_ID` (custos agrupados no conjunto de consolidação)
- [[pay_pre_payments]] --- via `CONSOLIDATION_SET_ID` (pré-pagamentos do conjunto de consolidação)

---

## 📎 Uso Típico

### Conjuntos de consolidacao por grupo legislativo
```sql
SELECT cs.CONSOLIDATION_SET_ID, cs.CONSOLIDATION_SET_NAME
FROM   PAY_CONSOLIDATION_SETS cs
WHERE  cs.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_CONSOLIDATION_SETS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payconsolidationsets.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
