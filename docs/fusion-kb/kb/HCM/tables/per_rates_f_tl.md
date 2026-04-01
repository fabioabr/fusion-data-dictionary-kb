---
id: DOC-HCM-704
doc_type: system-doc
title: "PER_RATES_F_TL — Traduções de Taxas/Valores"
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
  - taxas
  - rates-tl
  - traducao
  - multilanguage
aliases:
  - PER_RATES_F_TL
  - per_rates_f_tl
  - traducao-taxas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_RATES_F_TL

## Visão Geral

Armazena as **traduções** das definições de taxas/valores em múltiplos idiomas. Cada registro contém o nome descritivo traduzido de uma taxa para um idioma específico.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **tradução** — cada registro da tabela base possui N registros nesta tabela, um por idioma configurado.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Exibição localizada de taxas** — nomes traduzidos em relatórios e interfaces
- **Relatórios multilíngues** — gerar nomes de taxas no idioma do usuário
- **Interfaces de compensação** — exibir tipos de taxa no idioma da sessão

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da taxa | PER_RATES_F | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 90% |
| 4 | RATE_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido da taxa | — | 🟢 85% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida da taxa | — | 🟡 75% |
| 6 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 90% |
| 7 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_rates_f]] — via `RATE_ID` (tabela base da taxa salarial)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Nome traduzido de uma taxa
```sql
SELECT tl.RATE_NAME, tl.DESCRIPTION
FROM   PER_RATES_F_TL tl
WHERE  tl.RATE_ID = :p_rate_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## Observações

- A chave primária é composta por `RATE_ID` + `LANGUAGE`.
- Sempre filtrar por `LANGUAGE` para obter a tradução desejada.
- `SOURCE_LANG` indica se a tradução é nativa ou herdada.

---

## Referências

- [Oracle Docs — PER_RATES_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perratesftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[ratepvo|RatePVO]] (GL · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | RateTranslationPEOCreatedBy | — |
| CREATION_DATE | RateTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | RateTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | RateTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | RateTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | RateTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RateTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RateTranslationPEOLastUpdatedBy | — |
| NAME | RateTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | RateTranslationPEOObjectVersionNumber | — |
| RATE_ID | RateTranslationPEORateId | — |
| SOURCE_LANG | RateTranslationPEOSourceLang | — |

### [[ratetranslationpvo|RateTranslationPVO]] (GL · BICC: 5/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | RateTranslationPEOCreatedBy | — |
| CREATION_DATE | RateTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | RateTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RateTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RateTranslationPEOLastUpdatedBy | — |
| NAME | RateTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | RateTranslationPEOObjectVersionNumber | — |
| RATE_ID | RateId | ✅ |
| SOURCE_LANG | RateTranslationPEOSourceLang | — |
