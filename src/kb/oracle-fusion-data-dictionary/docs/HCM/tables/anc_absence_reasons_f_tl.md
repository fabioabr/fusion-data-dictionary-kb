---
id: DOC-HCM-006
doc_type: system-doc
title: "ANC_ABSENCE_REASONS_F_TL — Traduções de Motivos de Ausência"
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
  - motivos-ausencia-tl
aliases:
  - ANC_ABSENCE_REASONS_F_TL
  - anc_absence_reasons_f_tl
  - motivos-ausencia-tl
  - absence-reasons-tl
  - anc-abs-reasons-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_REASONS_F_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes dos motivos de ausência em múltiplos idiomas.

> [!note] Sufixos _F_TL
> Combina **date-effective** (`_F`) e **traduções** (`_TL`). Cada registro possui vigência temporal e idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Exibição de motivos no idioma do colaborador.
- **Self-service multilíngue:** Seleção de motivos em interfaces localizadas.
- **Relatórios localizados:** Nomes de motivos no idioma do relatório.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_REASON_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do motivo de ausência | [[anc_absence_reasons_f]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 90% |
| 4 | REASON_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do motivo | — | 🟢 90% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_absence_reasons_f]] — via `ABSENCE_REASON_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Nome do motivo em português
```sql
SELECT ar.ABSENCE_REASON_ID, tl.REASON_NAME
FROM   ANC_ABSENCE_REASONS_F ar
JOIN   ANC_ABSENCE_REASONS_F_TL tl ON ar.ABSENCE_REASON_ID = tl.ABSENCE_REASON_ID
WHERE  tl.LANGUAGE = 'PT'
  AND  SYSDATE BETWEEN ar.EFFECTIVE_START_DATE AND ar.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Traduções em português

---

## 🔒 Observações

- Sempre fazer JOIN com a tabela base `_F` para filtrar por vigência.
- O campo `SOURCE_LANG` indica o idioma de origem da tradução.

---

## 🔗 PVOs Relacionados

### [[absencereasonpvo|AbsenceReasonPVO]] (GL · BICC: 11/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_REASON_ID | AbsenceReasonId1 | ✅ |
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

---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_REASONS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsencereasonsftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
