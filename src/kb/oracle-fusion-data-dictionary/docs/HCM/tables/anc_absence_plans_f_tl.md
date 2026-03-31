---
id: DOC-HCM-004
doc_type: system-doc
title: "ANC_ABSENCE_PLANS_F_TL — Traduções de Planos de Ausência"
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
  - absence-management
  - traducoes
  - translations
  - planos-ausencia-tl
aliases:
  - ANC_ABSENCE_PLANS_F_TL
  - anc_absence_plans_f_tl
  - planos-ausencia-tl
  - absence-plans-tl
  - anc-abs-plans-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_PLANS_F_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições dos planos de ausência em múltiplos idiomas.

> [!note] Sufixos _F_TL
> Combina **date-effective** (`_F`) e **traduções** (`_TL`). Cada registro possui vigência temporal e idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Exibição de nomes de planos no idioma do usuário.
- **Self-service multilíngue:** Suporte a colaboradores globais na solicitação de ausências.
- **Relatórios localizados:** Geração de relatórios de ausência no idioma local.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_PLAN_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do plano de ausência | [[anc_absence_plans_f]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 90% |
| 4 | PLAN_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do plano | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida do plano | — | 🟡 75% |
| 6 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 7 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_absence_plans_f]] — via `ABSENCE_PLAN_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Nome do plano em português
```sql
SELECT pl.ABSENCE_PLAN_ID, tl.PLAN_NAME, tl.DESCRIPTION
FROM   ANC_ABSENCE_PLANS_F pl
JOIN   ANC_ABSENCE_PLANS_F_TL tl ON pl.ABSENCE_PLAN_ID = tl.ABSENCE_PLAN_ID
WHERE  tl.LANGUAGE = 'PT'
  AND  SYSDATE BETWEEN pl.EFFECTIVE_START_DATE AND pl.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Traduções em português
- `LANGUAGE = USERENV('LANG')` — Idioma da sessão do usuário

---

## 🔒 Observações

- Sempre fazer JOIN com a tabela base `_F` para obter registros vigentes.
- O campo `SOURCE_LANG` indica o idioma de origem da tradução.
- Registros com `LANGUAGE = SOURCE_LANG` são as traduções originais.

---

## 🔗 PVOs Relacionados

### [[absenceplanpvo|AbsencePlanPVO]] (GL · BICC: 11/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_PLAN_ID | AbsencePlanId1 | ✅ |
| CREATED_BY | CreatedBy1 | ✅ |
| CREATION_DATE | CreationDate1 | ✅ |
| DESCRIPTION | Description | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| ENTERPRISE_ID | EnterpriseId1 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | ✅ |
| MODULE_ID | ModuleId1 | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| SOURCE_LANG | SourceLang | ✅ |

### [[accrualplanpvo|AccrualPlanPVO]] (GL · BICC: 3/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_PLAN_ID | AbsencePlanId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DESCRIPTION | Description | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| ENTERPRISE_ID | EnterpriseId1 | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| MODULE_ID | ModuleId1 | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| SOURCE_LANG | SourceLang | — |

### [[personabscertificationspvo|PersonAbsCertificationsPVO]] (GL · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_PLAN_ID | AbsencePlanId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| LANGUAGE | Language1 | — |
| NAME | AbsenceTargetPlanName | ✅ |

---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_PLANS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsenceplansftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
