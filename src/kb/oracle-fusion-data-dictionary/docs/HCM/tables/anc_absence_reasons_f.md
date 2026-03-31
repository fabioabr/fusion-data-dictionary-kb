---
id: DOC-HCM-005
doc_type: system-doc
title: "ANC_ABSENCE_REASONS_F — Motivos de Ausência"
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
  - motivos-ausencia
  - absence-reasons
aliases:
  - ANC_ABSENCE_REASONS_F
  - anc_absence_reasons_f
  - motivos-ausencia-hcm
  - absence-reasons
  - anc-abs-reasons
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_REASONS_F

## 📌 Visão Geral

Armazena os **motivos de ausência** configuráveis no Absence Management. Cada motivo detalha a razão específica de uma ausência (ex.: consulta médica, cirurgia, falecimento familiar), vinculado a tipos de ausência.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento de ausências:** Permite especificar a razão exata de cada ausência além do tipo geral.
- **Relatórios analíticos:** Base para análise de causas de absenteísmo.
- **Compliance:** Atende requisitos de registro detalhado de motivos para auditorias trabalhistas.
- **Regras condicionais:** Motivos podem disparar regras específicas (ex.: motivos médicos exigem atestado).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_REASON_ID | NUMBER(18) | NOT NULL | PK | Identificador único do motivo de ausência | — | 🟢 95% |
| 2 | REASON_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do motivo de ausência | — | 🟢 90% |
| 3 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 90% |
| 4 | REASON_STATUS | VARCHAR2(30) | NULL | Classificação | Status do motivo (A — ativo, I — inativo) | — | 🟡 75% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta identificada (tabela de configuração raiz).

### Tabelas-filha (FK de saída)
- [[anc_absence_reasons_f_tl]] — via `ABSENCE_REASON_ID` (traducoes multilingue do registro)
- [[anc_absence_type_reasons_f]] — via `ABSENCE_REASON_ID` (associação tipo-motivo)

---

## 📎 Uso Típico

### Motivos ativos por legislação
```sql
SELECT ar.ABSENCE_REASON_ID, ar.REASON_NAME, ar.LEGISLATION_CODE
FROM   ANC_ABSENCE_REASONS_F ar
WHERE  SYSDATE BETWEEN ar.EFFECTIVE_START_DATE AND ar.EFFECTIVE_END_DATE
  AND  ar.LEGISLATION_CODE = :p_legislation_code;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
- `LEGISLATION_CODE = 'BR'` — Motivos para legislação brasileira

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigência.
- Motivos são associados a tipos de ausência via `ANC_ABSENCE_TYPE_REASONS_F`.
- A tabela de traduções (`_TL`) armazena o nome em múltiplos idiomas.

---

## 🔗 PVOs Relacionados

### [[absencereasonpvo|AbsenceReasonPVO]] (GL · BICC: 11/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_REASON_ID | AbsenceReasonId | ✅ |
| ANC_ABS_REASONS_F_ALTCD | AncAbsReasonsFAltcd | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| MODULE_ID | ModuleId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| STATUS | Status | ✅ |

---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_REASONS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsencereasonsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
