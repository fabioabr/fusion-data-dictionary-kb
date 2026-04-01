---
id: DOC-HCM-321
doc_type: system-doc
title: "HWM_RULE_TMPLT_USAGES — Usos de Templates de Regras"
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
  - regras
  - templates
  - usos
aliases:
  - HWM_RULE_TMPLT_USAGES
  - hwm_rule_tmplt_usages
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RULE_TMPLT_USAGES

## 📌 Visão Geral

Registra os contextos e cenários de uso de cada template de regra, indicando onde e como os modelos podem ser aplicados.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Motor de regras:** Definição e execução de regras de cálculo para processamento de tempo e ausências.
- **Configuração flexível:** Permite criação de regras customizadas sem desenvolvimento.
- **Reutilização:** Templates e conjuntos de regras promovem padronização e reuso.
- **Auditoria de cálculos:** Rastreamento de quais regras foram aplicadas em cada processamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do uso do template | — | 🟡 80% |
| 2 | RULE_TMPLT_ID | NUMBER(18) | NOT NULL | FK | Referência ao template de regra | HWM_RULE_TMPLTS | 🟡 80% |
| 3 | USAGE_CONTEXT | VARCHAR2(30) | NULL | Classificação | Contexto de uso do template | — | 🟡 75% |
| 4 | USAGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de uso do template | — | 🟡 70% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição do uso | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_rule_tmplts]] — via `RULE_TMPLT_ID` (template de regra do uso)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.USAGE_CONTEXT, t.USAGE_TYPE, t.DESCRIPTION
FROM   HWM_RULE_TMPLT_USAGES t
WHERE  t.RULE_TMPLT_ID = :p_tmplt_id
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Rules Engine dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[ruletemplateusagepvo|RuleTemplateUsagePVO]] (GL · BICC: 17/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATRB_FLD_NAME | RuleTemplateUsageBPEOAtrbFldName | ✅ |
| ATRB_FLD_SET_ID | RuleTemplateUsageBPEOAtrbFldSetId | — |
| CREATED_BY | RuleTemplateUsageBPEOCreatedBy | ✅ |
| CREATION_DATE | RuleTemplateUsageBPEOCreationDate | ✅ |
| DISPLAY_SEQUENCE | RuleTemplateUsageBPEODisplaySequence | ✅ |
| ENTERPRISE_ID | RuleTemplateUsageBPEOEnterpriseId | — |
| HIDE_FLAG | RuleTemplateUsageBPEOHideFlag | ✅ |
| LAST_UPDATE_DATE | RuleTemplateUsageBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RuleTemplateUsageBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RuleTemplateUsageBPEOLastUpdatedBy | ✅ |
| MSG_SEVERITY | RuleTemplateUsageBPEOMsgSeverity | ✅ |
| OBJECT_VERSION_NUMBER | RuleTemplateUsageBPEOObjectVersionNumber | — |
| OUTPUT_NAME | RuleTemplateUsageBPEOOutputName | ✅ |
| OUTPUT_SOURCE | RuleTemplateUsageBPEOOutputSource | ✅ |
| OUTPUT_VALUE_TYPE | RuleTemplateUsageBPEOOutputValueType | ✅ |
| RECURSIVE | RuleTemplateUsageBPEORecursive | — |
| RELATED_INPUT_NAME | RuleTemplateUsageBPEORelatedInputName | — |
| RULE_TMPLT_USAGES_ID | RuleTemplateUsageBPEORuleTmpltUsagesId | ✅ |
| RULE_TMPLTS_ID | RuleTemplateUsageBPEORuleTmpltsId | ✅ |
| SEED_DATA_SOURCE | RuleTemplateUsageBPEOSeedDataSource | — |
| SGUID | RuleTemplateUsageBPEOSguid | — |
| TBB_GROUP_NUMBER | RuleTemplateUsageBPEOTbbGroupNumber | ✅ |
| TM_ATRB_FLD_ID | RuleTemplateUsageBPEOTmAtrbFldId | ✅ |
| VALUE_SET_ID | RuleTemplateUsageBPEOValueSetId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_RULE_TMPLT_USAGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rule_tmplt_usages.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
