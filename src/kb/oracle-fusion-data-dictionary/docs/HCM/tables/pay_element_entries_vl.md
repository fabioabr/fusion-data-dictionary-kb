---
id: DOC-HCM-571
doc_type: system-doc
title: "PAY_ELEMENT_ENTRIES_VL — Entradas de Elementos (View Localizada)"
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
  - element-entries-vl
  - view-localizada
  - pay-entries-vl
aliases:
  - PAY_ELEMENT_ENTRIES_VL
  - pay_element_entries_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELEMENT_ENTRIES_VL

## 📌 Visão Geral

**View localizada** que combina entradas de elementos com informacoes traduzidas dos tipos de elementos. Facilita consultas que necessitem nome do elemento no idioma do usuario.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas simplificadas de entradas com nome traduzido
- Relatorios de folha no idioma do usuario

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ELEMENT_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da entrada | --- | 🟢 95% |
| 2 | ELEMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | ID do tipo de elemento | PAY_ELEMENT_TYPES_F | 🟢 95% |
| 3 | ELEMENT_NAME | VARCHAR2(80) | NULL | Identificacao | Nome do elemento traduzido | --- | 🟢 85% |
| 4 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | FK | ID do relacionamento de folha | --- | 🟢 90% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- --- View, sem filhas diretas

---

## 📎 Uso Típico

### Entradas vigentes com nome traduzido
```sql
SELECT vl.ELEMENT_ENTRY_ID, vl.ELEMENT_NAME, vl.EFFECTIVE_START_DATE
FROM   PAY_ELEMENT_ENTRIES_VL vl
WHERE  vl.PAYROLL_RELATIONSHIP_ID = :p_rel_id
  AND  SYSDATE BETWEEN vl.EFFECTIVE_START_DATE AND vl.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Esta eh uma view (VL = View Localizada), nao uma tabela fisica.

---

## 📚 Referências

- [Oracle Docs — PAY_ELEMENT_ENTRIES_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payelemententriesvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
