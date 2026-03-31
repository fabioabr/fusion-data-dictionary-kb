---
id: DOC-HCM-752
doc_type: system-doc
title: "ZMM_SR_PATTERNS_TL — Padrões de Escala de Trabalho (Traduções)"
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
  - schedule-patterns
  - translations
aliases:
  - ZMM_SR_PATTERNS_TL
  - zmm_sr_patterns_tl
  - padroes-escala-traducao
  - schedule-patterns-translation
  - zmm-sr-patterns-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ZMM_SR_PATTERNS_TL

## 📌 Visão Geral

Tabela de traduções customizada (prefixo `ZMM`) que armazena os **textos traduzidos dos padrões de escala de trabalho** em múltiplos idiomas. O sufixo `_TL` indica tabela de tradução, seguindo o padrão MLS (Multi-Language Support) do Oracle Fusion.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Permite que nomes e descrições dos padrões de escala sejam exibidos no idioma do usuário logado.
- **Interface multilíngue:** Suporta operações em múltiplos países com idiomas distintos.
- **Relatórios localizados:** Garante que relatórios de escalas sejam gerados no idioma adequado à localidade.
- **Conformidade regional:** Atende requisitos de exibição de informações em idioma local conforme legislação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PATTERN_ID | NUMBER(18) | NOT NULL | PK/FK | Referência ao padrão de escala base | [[zmm_sr_patterns_b]].PATTERN_ID | 🟡 80% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex.: PT, EN, ES) | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 90% |
| 4 | PATTERN_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do padrão de escala | — | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida do padrão | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[zmm_sr_patterns_b]] — via `PATTERN_ID` (tabela base do padrão)

### Tabelas-filha
- Nenhuma — tabela terminal de tradução.

---

## 📎 Uso Típico

### Obter nome do padrão no idioma do usuário
```sql
SELECT b.PATTERN_ID, b.PATTERN_CODE,
       tl.PATTERN_NAME, tl.DESCRIPTION
FROM   ZMM_SR_PATTERNS_B b
JOIN   ZMM_SR_PATTERNS_TL tl
       ON tl.PATTERN_ID = b.PATTERN_ID
       AND tl.LANGUAGE = USERENV('LANG')
WHERE  b.ACTIVE_FLAG = 'Y';
```

---

## 🔒 Observações

- Tabela customizada (prefixo `ZMM`) — não faz parte do modelo padrão Oracle Fusion. Estrutura inferida por naming convention.
- Chave primária composta: `PATTERN_ID` + `LANGUAGE`.
- Padrão MLS Oracle: `SOURCE_LANG` indica o idioma em que o texto foi originalmente cadastrado.
- Sempre realizar JOIN com [[zmm_sr_patterns_b]] para obter dados completos do padrão.

---

## 🔗 PVOs Relacionados

### [[patternextractpvo|PatternExtractPVO]] (OTHER · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | PatternTranslationPEOLanguage | — |
| PATTERN_DESC | PatternTranslationPEOPatternDesc | ✅ |
| PATTERN_NAME | PatternTranslationPEOPatternName | ✅ |

### [[patterntranslationextractpvo|PatternTranslationExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PATTERN_DESC | PatternDesc | ✅ |
| PATTERN_ID | PatternId | ✅ |
| PATTERN_NAME | PatternName | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[scheduleassignmentpvo|ScheduleAssignmentPVO]] (GL · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PatternsTranslationPEOCreatedBy | — |
| CREATION_DATE | PatternsTranslationPEOCreationDate | — |
| LANGUAGE | PatternsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | PatternsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PatternsTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PatternsTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PatternsTranslationPEOObjectVersionNumber | — |
| PATTERN_DESC | PatternsTranslationPEOPatternDesc | — |
| PATTERN_ID | PatternsTranslationPEOPatternId | — |
| PATTERN_NAME | PatternsTranslationPEOPatternName | ✅ |
| SOURCE_LANG | PatternsTranslationPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
