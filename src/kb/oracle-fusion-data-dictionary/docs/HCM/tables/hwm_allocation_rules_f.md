---
id: DOC-HCM-296
doc_type: system-doc
title: "HWM_ALLOCATION_RULES_F — Regras de Alocacao de Workforce"
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
  - allocation-rules
  - workforce-management
  - automacao
aliases:
  - HWM_ALLOCATION_RULES_F
  - hwm_allocation_rules_f
  - hwm-allocation-rules-f
  - allocation-rules
  - regras-alocacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_ALLOCATION_RULES_F

## 📌 Visao Geral

Armazena as **regras de alocacao** de workforce com versionamento date-effective.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Automacao:** Definir regras para alocacao automatica de recursos.
- **Governanca:** Controlar criterios de alocacao.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATION_RULE_ID | NUMBER(18) | NOT NULL | PK | Identificador da regra | — | 🟢 85% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 85% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 85% |
| 4 | RULE_NAME | VARCHAR2(240) | NULL | Dados | Nome da regra | — | 🟡 80% |
| 5 | RULE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de regra | — | 🟡 75% |
| 6 | PRIORITY | NUMBER | NULL | Dados | Prioridade de execucao | — | 🟡 70% |
| 7 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status da regra | — | 🟡 75% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Regras ativas por prioridade
```sql
SELECT ar.RULE_NAME, ar.RULE_TYPE, ar.PRIORITY
FROM   HWM_ALLOCATION_RULES_F ar
WHERE  ar.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN ar.EFFECTIVE_START_DATE AND ar.EFFECTIVE_END_DATE
ORDER BY ar.PRIORITY;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica date-effective.
- Regras sao avaliadas por ordem de prioridade.

---

## 📚 Referencias

- [Oracle Docs — HWM_ALLOCATION_RULES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmallocationrulesf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
