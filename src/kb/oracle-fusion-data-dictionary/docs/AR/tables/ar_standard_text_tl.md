---
id: DOC-AR-059
doc_type: system-doc
title: "AR_STANDARD_TEXT_TL — Traduções dos Textos Padrão"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, standard-text, traducoes, multilinguagem]
aliases: [AR_STANDARD_TEXT_TL, ar_standard_text_tl, standard_text_tl, traducoes_textos_padrao, ar_std_text_tl]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_STANDARD_TEXT_TL

## 📌 Visão Geral

Tabela de **traduções** (sufixo `_TL`) dos textos padrão do AR. Armazena nome e conteúdo de texto traduzidos para cada idioma instalado. Segue o padrão MLS (Multi-Language Support) do Oracle Fusion.

## 🧠 Propósito de Negócio

Permite que textos padrão (dunning letters, notas em faturas, statements) sejam emitidos no **idioma do cliente**. Essencial para operações internacionais onde comunicações de cobrança devem respeitar o idioma do destinatário.

Casos de uso principais:
- Dunning letters no idioma do cliente
- Faturas com termos e condições localizados
- Statements multilíngues
- Comunicações de cobrança internacionais

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | STANDARD_TEXT_ID | NUMBER | PK/FK composta. Referencia [[ar_standard_text_b]]. | Chave | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2 | PK composta. Código do idioma da tradução (ex: `PTB`, `US`, `ESA`). | Chave | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2 | Idioma de origem da tradução. Quando igual a `LANGUAGE`, é tradução direta. | Controle | 🟢 100% |
| 4 | NAME | VARCHAR2 | Nome traduzido do texto padrão. | Identificação | 🟢 100% |
| 5 | TEXT | CLOB/VARCHAR2 | Conteúdo do texto traduzido. | Conteúdo | 🟢 100% |
| 6 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 7 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_standard_text_b]] | STANDARD_TEXT_ID | FK | Tabela base do texto padrão |
| [[fnd_languages]] | LANGUAGE | FK | Idioma da tradução |

## 📎 Uso Típico

```sql
-- Texto padrão em português
SELECT b.standard_text_id,
       tl.name,
       tl.text
  FROM ar_standard_text_b b
  JOIN ar_standard_text_tl tl ON tl.standard_text_id = b.standard_text_id
 WHERE tl.language = 'PTB'
   AND (b.end_date IS NULL OR b.end_date > SYSDATE);
```

```sql
-- Textos com tradução pendente
SELECT tl.standard_text_id,
       tl.language,
       tl.source_lang,
       tl.name
  FROM ar_standard_text_tl tl
 WHERE tl.language <> tl.source_lang;
```

## 🔒 Observações

- A PK composta é `STANDARD_TEXT_ID` + `LANGUAGE` — um registro por idioma instalado para cada texto padrão.
- Quando `SOURCE_LANG <> LANGUAGE`, a tradução é **herdada** do idioma base e ainda não foi traduzida diretamente.
- O campo `TEXT` pode conter **variáveis de substituição** — as mesmas variáveis da tabela base [[ar_standard_text_b]] devem ser mantidas nas traduções.
- Em migrações, carregar **ambas as tabelas** (`_B` e `_TL`) para garantir integridade multilíngue.

## 🔗 PVOs Relacionados

### [[customerprofile|CustomerProfile]] (AR · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | StdTextTransTLCreatedBy | — |
| CREATION_DATE | StdTextTransTLCreationDate | — |
| LANGUAGE | StdTextTransTLLanguage | — |
| LAST_UPDATE_DATE | StdTextTransTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | StdTextTransTLLastUpdateLogin | — |
| LAST_UPDATED_BY | StdTextTransTLLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | StdTextTransTLObjectVersionNumber | — |
| SOURCE_LANG | StdTextTransTLSourceLang | — |
| STANDARD_TEXT_ID | StdTextTransTLStandardTextId | — |
| TEXT | StdTextTransTLText | ✅ |

### [[customersiteprofile|CustomerSiteProfile]] (AR · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | StdTextTransTLCreatedBy | — |
| CREATION_DATE | StdTextTransTLCreationDate | — |
| LANGUAGE | StdTextTransTLLanguage | — |
| LAST_UPDATE_DATE | StdTextTransTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | StdTextTransTLLastUpdateLogin | — |
| LAST_UPDATED_BY | StdTextTransTLLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | StdTextTransTLObjectVersionNumber | — |
| SOURCE_LANG | StdTextTransTLSourceLang | — |
| STANDARD_TEXT_ID | StdTextTransTLStandardTextId | — |
| TEXT | StdTextTransTLText | ✅ |

### [[standardtexttranslationextractpvo|StandardTextTranslationExtractPVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ArStandardTextTLCreatedBy | ✅ |
| CREATION_DATE | ArStandardTextTLCreationDate | ✅ |
| LANGUAGE | ArStandardTextTLLanguage | ✅ |
| LAST_UPDATE_DATE | ArStandardTextTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArStandardTextTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArStandardTextTLLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ArStandardTextTLObjectVersionNumber | ✅ |
| SOURCE_LANG | ArStandardTextTLSourceLang | ✅ |
| STANDARD_TEXT_ID | ArStandardTextTLStandardTextId | ✅ |
| TEXT | ArStandardTextTLText | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Standard Text Translation View Object
- Oracle Fusion Cloud — Multi-Language Support (MLS) Technical Guide
