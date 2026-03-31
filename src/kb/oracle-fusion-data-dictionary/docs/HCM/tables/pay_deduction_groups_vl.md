---
id: DOC-HCM-560
doc_type: system-doc
title: "PAY_DEDUCTION_GROUPS_VL — Grupos de Desconto (View Localizada)"
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
  - deduction-groups
  - grupos-desconto
  - pay-ded-groups
aliases:
  - PAY_DEDUCTION_GROUPS_VL
  - pay_deduction_groups_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_DEDUCTION_GROUPS_VL

## 📌 Visão Geral

**View localizada** que combina os grupos de desconto com suas traducoes. Grupos de desconto organizam tipos de desconto para processamento e relatorio.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consulta simplificada de grupos de desconto com traducao
- Organizacao de descontos por agrupamento logico
- Relatorios de descontos por grupo

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DEDUCTION_GROUP_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do grupo | --- | 🟢 85% |
| 2 | GROUP_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do grupo no idioma da sessao | --- | 🟢 85% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | PROCESSING_PRIORITY | NUMBER | NULL | Dados | Prioridade de processamento | --- | 🟡 70% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Dados | Descricao do grupo | --- | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela base de grupos de desconto + traducoes

### Tabelas-filha (FK de saída)
- [[pay_deduction_types]] --- via `DEDUCTION_GROUP_ID` (tipos de dedução do grupo)

---

## 📎 Uso Típico

### Grupos de desconto com nome traduzido
```sql
SELECT vl.DEDUCTION_GROUP_ID, vl.GROUP_NAME, vl.PROCESSING_PRIORITY
FROM   PAY_DEDUCTION_GROUPS_VL vl
WHERE  vl.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id;
```

---

## 🔒 Observações

- Esta eh uma view (VL = View Localizada), nao uma tabela fisica.
- Retorna automaticamente o nome no idioma da sessao do usuario.

---

## 📚 Referências

- [Oracle Docs — PAY_DEDUCTION_GROUPS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paydeductiongroupsvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
