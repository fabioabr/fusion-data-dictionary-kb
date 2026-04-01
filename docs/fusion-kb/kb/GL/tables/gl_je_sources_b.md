---
id: DOC-GL-025
doc_type: system-doc
title: "GL_JE_SOURCES_B — Fontes de Lançamentos Contábeis (Base)"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - journal-sources
  - fontes-lancamento
  - configuracao
aliases:
  - GL_JE_SOURCES_B
  - gl_je_sources_b
  - fontes-lancamento
  - journal-sources
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_JE_SOURCES_B

## 📌 Visão Geral

Armazena as definições das **fontes (sources) de lançamentos contábeis** no General Ledger. Cada fonte identifica o módulo ou processo de origem de um journal entry — por exemplo, Payables, Receivables, Assets, Manual, Spreadsheet. Esta é a tabela base (_B) do padrão multi-idioma Oracle; as traduções ficam em [[gl_je_sources_tl]].

> [!note] Tabela de configuração (baixa volumetria)
> Esta é uma tabela de setup com poucas dezenas de registros. Define as fontes válidas para criação de journals no GL.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação de journals:** Identifica a origem de cada lançamento (AP, AR, FA, Manual etc.).
- **Controle de acesso:** Permite restringir quais fontes podem postar em determinados ledgers.
- **Auditoria:** Rastreamento da origem dos lançamentos contábeis.
- **Configuração:** Setup obrigatório para integração de subledgers com o GL.
- **Relatórios:** Filtro e agrupamento de journals por fonte/origem.
- **Subledger Accounting (SLA):** Cada subledger registra sua fonte para transferência ao GL.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JE_SOURCE_NAME | VARCHAR2(25) | NOT NULL | PK | Nome único da fonte de lançamento (ex: Payables, Receivables, Manual) | — | 🟢 100% |
| 2 | OVERRIDE_EDITS_FLAG | VARCHAR2(1) | NOT NULL | Controle | Permite sobrescrever edições/validações de journal (Y/N) | — | 🟢 90% |
| 3 | JOURNAL_REFERENCE_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se referências de journal são obrigatórias para esta fonte (Y/N) | — | 🟢 90% |
| 4 | JOURNAL_APPROVAL_FLAG | VARCHAR2(1) | NULL | Controle | Indica se journals desta fonte requerem aprovação (Y/N) | — | 🟢 90% |
| 5 | IMPORT_USING_KEY_FLAG | VARCHAR2(1) | NULL | Controle | Importar usando chave (Y) ou ID (N) no journal import | — | 🟡 75% |
| 6 | EFFECTIVE_DATE_RULE_CODE | VARCHAR2(1) | NULL | Controle | Regra de data efetiva: A (Any), P (Period), null (N/A) | — | 🟡 75% |
| 7 | ATTRIBUTE_CATEGORY | VARCHAR2(150) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟡 80% |
| 8 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Campos de atributo descritivo (DFF) configuráveis | — | 🟡 80% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta — esta é uma tabela raiz de configuração.

### Tabelas-filha (FK de saída)
- [[gl_je_sources_tl]] — via `JE_SOURCE_NAME` (traduções do nome da fonte)
- [[gl_je_headers]] — via `JE_SOURCE` (journals que usam esta fonte)

---

## 📎 Uso Típico

### Listar todas as fontes de lançamento
```sql
SELECT sb.JE_SOURCE_NAME,
       stl.USER_JE_SOURCE_NAME,
       sb.JOURNAL_APPROVAL_FLAG,
       sb.OVERRIDE_EDITS_FLAG
FROM   GL_JE_SOURCES_B sb
JOIN   GL_JE_SOURCES_TL stl
       ON stl.JE_SOURCE_NAME = sb.JE_SOURCE_NAME
      AND stl.LANGUAGE = USERENV('LANG')
ORDER BY sb.JE_SOURCE_NAME;
```

### Journals agrupados por fonte
```sql
SELECT jh.JE_SOURCE,
       stl.USER_JE_SOURCE_NAME,
       COUNT(*) AS total_journals
FROM   GL_JE_HEADERS jh
JOIN   GL_JE_SOURCES_TL stl
       ON stl.JE_SOURCE_NAME = jh.JE_SOURCE
      AND stl.LANGUAGE = USERENV('LANG')
WHERE  jh.LEDGER_ID = :p_ledger_id
  AND  jh.PERIOD_NAME = 'MAR-26'
GROUP BY jh.JE_SOURCE, stl.USER_JE_SOURCE_NAME
ORDER BY total_journals DESC;
```

### Filtros comuns
- `JE_SOURCE_NAME = 'Manual'` — Lançamentos manuais
- `JE_SOURCE_NAME = 'Payables'` — Lançamentos originados de AP
- `JE_SOURCE_NAME = 'Receivables'` — Lançamentos originados de AR
- `JOURNAL_APPROVAL_FLAG = 'Y'` — Fontes que requerem aprovação

---

## 🔒 Observações

- A PK é `JE_SOURCE_NAME` (varchar, não numérica). É referenciada como texto nos headers de journal.
- Fontes padrão Oracle incluem: Manual, Spreadsheet, Payables, Receivables, Assets, Cash Management, Intercompany, Consolidation, Revaluation.
- O campo `OVERRIDE_EDITS_FLAG` permite que journals de determinadas fontes ignorem validações de conta — usar com cautela.
- `JOURNAL_APPROVAL_FLAG` controla se journals desta fonte entram em workflow de aprovação.
- Esta é uma tabela _B (Base) — para obter o nome traduzido/amigável, fazer JOIN com [[gl_je_sources_tl]].

---

## 🔗 PVOs Relacionados

### [[journalsourcebpvo|JournalSourceBPVO]] (GL · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JrnlSrcCreatedBy | — |
| CREATION_DATE | JrnlSrcCreationDate | — |
| EFFECTIVE_DATE_RULE_CODE | JrnlSrcEffectiveDateRuleCode | — |
| IMPORT_USING_KEY_FLAG | JrnlSrcImportUsingKeyFlag | — |
| JE_SOURCE_KEY | JrnlSrcJeSourceKey | ✅ |
| JE_SOURCE_NAME | JeSourceName | ✅ |
| JOURNAL_APPROVAL_FLAG | JrnlSrcJournalApprovalFlag | — |
| JOURNAL_REFERENCE_FLAG | JrnlSrcJournalReferenceFlag | — |
| LAST_UPDATE_DATE | JrnlSrcLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JrnlSrcLastUpdateLogin | — |
| LAST_UPDATED_BY | JrnlSrcLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | JrnlSrcObjectVersionNumber | — |
| OVERRIDE_EDITS_FLAG | JrnlSrcOverrideEditsFlag | — |

### [[journalsourceextractpvo|JournalSourceExtractPVO]] (OTHER · BICC: 13/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | JournalSourceAttribute1 | — |
| ATTRIBUTE2 | JournalSourceAttribute2 | — |
| ATTRIBUTE3 | JournalSourceAttribute3 | — |
| ATTRIBUTE4 | JournalSourceAttribute4 | — |
| ATTRIBUTE5 | JournalSourceAttribute5 | — |
| ATTRIBUTE_CATEGORY | JournalSourceAttributeCategory | — |
| CREATED_BY | JournalSourceCreatedBy | ✅ |
| CREATION_DATE | JournalSourceCreationDate | ✅ |
| EFFECTIVE_DATE_RULE_CODE | JournalSourceEffDateRuleCode | ✅ |
| IMPORT_USING_KEY_FLAG | JournalSourceImpUsingKeyFlag | ✅ |
| JE_SOURCE_KEY | JournalSourceJeSourceKey | ✅ |
| JE_SOURCE_NAME | JournalSourceJeSourceName | ✅ |
| JOURNAL_APPROVAL_FLAG | JournalSourceJournalApprvlFlag | ✅ |
| JOURNAL_REFERENCE_FLAG | JournalSourceJournalRefFlag | ✅ |
| LAST_UPDATE_DATE | JournalSourceLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JournalSourceLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | JournalSourceLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | JournalSourceObjectVersionNum | ✅ |
| OVERRIDE_EDITS_FLAG | JournalSourceOverrideEditsFlag | ✅ |
| XLA_APPROVAL_FLAG | JournalSourceXlaApprovalFlag | — |

---

## 📚 Referências

- [Oracle Docs — GL_JE_SOURCES_B](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gljesourcesb.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
