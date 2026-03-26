---
id: DOC-HCM-385
doc_type: system-doc
title: "HWM_TM_REP_ATRBS — Atributos de Entradas Reportadas de Tempo"
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
  - reported-attributes
  - atributos-reportados
aliases:
  - HWM_TM_REP_ATRBS
  - hwm_tm_rep_atrbs
  - hwm-tm-rep-atrbs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REP_ATRBS

## 📌 Visão Geral

Armazena os **atributos associados a entradas reportadas** (reported entries) de tempo. Extende as informações das entradas reportadas com pares de atributo-valor adicionais.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Extensibilidade:** atributos adicionais para entradas reportadas ao payroll.
- **Mapeamento de custos:** atributos como centro de custo, projeto, tarefa.
- **Integração com GL/Projects:** dados complementares para contabilização.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REP_ATRB_ID | NUMBER(18) | NOT NULL | PK | Identificador único do atributo | — | 🟡 70% |
| 2 | REP_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada reportada associada | — | 🟡 70% |
| 3 | ATTRIBUTE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do atributo | — | 🟡 65% |
| 4 | ATTRIBUTE_VALUE | VARCHAR2(240) | NULL | Dados | Valor do atributo | — | 🟡 65% |
| 5 | ATTRIBUTE_CATEGORY | VARCHAR2(80) | NULL | Classificação | Categoria do atributo | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Típico

### Atributos de uma entrada reportada
```sql
SELECT a.REP_ATRB_ID, a.ATTRIBUTE_NAME, a.ATTRIBUTE_VALUE
FROM   HWM_TM_REP_ATRBS a
WHERE  a.REP_ENTRY_ID = :p_rep_entry_id;
```

### Filtros comuns
- `REP_ENTRY_ID = :p_rep_entry_id — Filtrar por entrada reportada`

---

## 🔒 Observações

- Estrutura EAV para extensão de entradas reportadas.
- Atributos típicos incluem centro de custo, projeto e código de elemento de pagamento.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_REP_ATRBS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrepatrbs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
