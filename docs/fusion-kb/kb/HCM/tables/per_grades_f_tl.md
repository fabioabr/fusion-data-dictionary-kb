---
id: DOC-HCM-660
doc_type: system-doc
title: "PER_GRADES_F_TL — Grades Salariais (Traduções)"
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
  - compensation
  - traducoes
  - grades-tl
aliases:
  - PER_GRADES_F_TL
  - per_grades_f_tl
  - per-grades-f-tl
  - grades-salariais-(traduções)
  - per-grades-f-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_GRADES_F_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes das grades salariais em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe grades no idioma do usuário.
- **Relatórios localizados** — suporte multilíngue para relatórios de compensação.
- **Self-service** — interface traduzida.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRADE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da grade | PER_GRADES_F | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | GRADE_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido da grade | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_grades_f]] — via `GRADE_ID` (tabela base da grade salarial)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Grades em português
```sql
SELECT tl.GRADE_ID, tl.GRADE_NAME
FROM   PER_GRADES_F_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `GRADE_ID` + `LANGUAGE`.
---

## 🔗 PVOs Relacionados

### [[gradepvo|GradePVO]] (GL · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GradeTranslationPEOCreatedBy | — |
| CREATION_DATE | GradeTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | GradeTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GradeTranslationPEOEffectiveStartDate | ✅ |
| GRADE_ID | GradeTranslationPEOGradeId | — |
| LANGUAGE | GradeTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | GradeTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GradeTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GradeTranslationPEOLastUpdatedBy | — |
| NAME | GradeTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | GradeTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | GradeTranslationPEOSourceLang | — |

### [[graderefpvo|GradeRefPVO]] (GL · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GradeTranslationPEOCreatedBy | — |
| CREATION_DATE | GradeTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | GradeTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GradeTranslationPEOEffectiveStartDate | ✅ |
| GRADE_ID | GradeTranslationPEOGradeId | — |
| LANGUAGE | GradeTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | GradeTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GradeTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GradeTranslationPEOLastUpdatedBy | — |
| NAME | GradeTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | GradeTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | GradeTranslationPEOSourceLang | — |

### [[gradetranslationextractpvo|GradeTranslationExtractPVO]] (HCM · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GRADE_ID | GradeId | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[gradetranslationpvo|GradeTranslationPVO]] (GL · BICC: 10/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GradeTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | GradeTranslationPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GRADE_ID | GradeId | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | GradeTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GradeTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GradeTranslationPEOLastUpdatedBy | ✅ |
| NAME | GradeTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | GradeTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | GradeTranslationPEOSourceLang | ✅ |

### [[validgradespvo|ValidGradesPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GradeTranslationPEOCreatedBy | — |
| CREATION_DATE | GradeTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | GradeTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GradeTranslationPEOEffectiveStartDate | — |
| GRADE_ID | GradeTranslationPEOGradeId | — |
| LANGUAGE | GradeTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | GradeTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | GradeTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GradeTranslationPEOLastUpdatedBy | — |
| NAME | GradeTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | GradeTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | GradeTranslationPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Docs — PER_GRADES_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pergradesftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
