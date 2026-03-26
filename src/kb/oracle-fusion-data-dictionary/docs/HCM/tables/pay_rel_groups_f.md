---
id: DOC-HCM-595
doc_type: system-doc
title: "PAY_REL_GROUPS_F — Grupos de Relacionamento de Folha"
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
  - rel-groups
  - grupos
  - pay-rel-groups
aliases:
  - PAY_REL_GROUPS_F
  - pay_rel_groups_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_REL_GROUPS_F

## 📌 Visão Geral

Armazena os **grupos de relacionamento** (relationship groups) que permitem agrupar relacionamentos de pagamento para processamento seletivo. Utilizado para executar folha para subconjuntos de colaboradores.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Agrupamento de colaboradores para processamento seletivo
- Configuracao de filtros de execucao de folha
- Processamento parcial de payroll por grupo

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REL_GROUP_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do grupo | --- | 🟢 85% |
| 2 | REL_GROUP_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do grupo | --- | 🟢 80% |
| 3 | PAYROLL_ID | NUMBER(18) | NULL | FK | ID da folha de pagamento | PAY_ALL_PAYROLLS_F | 🟢 80% |
| 4 | GROUP_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do grupo | --- | 🟡 70% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_all_payrolls_f]] --- via `PAYROLL_ID` (folha de pagamento do grupo de relacionamento)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Grupos vigentes de uma folha
```sql
SELECT rg.REL_GROUP_ID, rg.REL_GROUP_NAME, rg.GROUP_TYPE
FROM   PAY_REL_GROUPS_F rg
WHERE  rg.PAYROLL_ID = :p_payroll_id
  AND  SYSDATE BETWEEN rg.EFFECTIVE_START_DATE AND rg.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_REL_GROUPS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payrelgroupsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
