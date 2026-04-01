---
id: DOC-AR-015
doc_type: system-doc
title: "RA_TERMS_TL — Traduções das Condições de Pagamento"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - payment-terms
  - traducoes
  - multi-language
aliases:
  - RA_TERMS_TL
  - ra_terms_tl
  - traducoes-condicoes-pagamento
  - payment-terms-translation
  - termos-pagamento-idiomas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_TERMS_TL

## 📌 Visão Geral

Armazena as **traduções dos nomes e descrições** das condições de pagamento definidas em [[ra_terms_b]]. Para cada termo de pagamento, existe um registro por idioma instalado no ambiente Oracle Fusion, contendo o nome e a descrição traduzidos.

Faz parte do padrão Oracle **MLS (Multi-Language Support)**: a tabela `_B` (base) contém dados não-traduzíveis, a `_TL` (translation) contém textos traduzidos, e a view [[ra_terms_vl]] combina ambas filtrando pelo idioma da sessão do usuário.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Suporte multi-idioma:** Permite que usuários em diferentes localidades vejam os nomes das condições de pagamento em seu idioma nativo.
- **Exibição em interfaces (UI):** As telas do Oracle Fusion consultam [[ra_terms_vl]] que, internamente, filtra esta tabela pelo idioma da sessão (`USERENV('LANG')`).
- **Relatórios localizados:** Relatórios e extrações podem exibir nomes de termos no idioma apropriado para o destinatário.
- **Manutenção de traduções:** Administradores podem atualizar traduções sem afetar os dados base da condição de pagamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TERM_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da condição de pagamento (parte da PK composta) | [[ra_terms_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução (ex.: US, PTB, ESA) — parte da PK composta | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Tradução | Idioma de origem da tradução; se igual a `LANGUAGE`, a tradução foi feita diretamente; se diferente, é um fallback | — | 🟢 100% |
| 4 | NAME | VARCHAR2(15) | NOT NULL | Identificação | Nome da condição de pagamento no idioma especificado | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição detalhada da condição de pagamento no idioma especificado | — | 🟢 100% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_terms_b]] — via `TERM_ID` (condição de pagamento base à qual a tradução pertence)

### Tabelas-filha (FK de saída)
- Nenhuma — tabela terminal de traduções.

### Views relacionadas

---

## 📎 Uso Típico

### Consultar traduções disponíveis para um termo
```sql
SELECT tl.TERM_ID, b.NAME AS nome_base, tl.LANGUAGE, tl.NAME AS nome_traduzido,
       tl.DESCRIPTION, tl.SOURCE_LANG
FROM   RA_TERMS_TL tl
JOIN   RA_TERMS_B b ON b.TERM_ID = tl.TERM_ID
WHERE  b.NAME = 'NET 30'
ORDER BY tl.LANGUAGE;
```

### Obter nome do termo no idioma da sessão
```sql
SELECT b.TERM_ID, tl.NAME, tl.DESCRIPTION
FROM   RA_TERMS_B b
JOIN   RA_TERMS_TL tl ON tl.TERM_ID = b.TERM_ID
                       AND tl.LANGUAGE = USERENV('LANG')
WHERE  NVL(b.END_DATE_ACTIVE, SYSDATE + 1) > SYSDATE;
```

### Identificar traduções pendentes (fallback para outro idioma)
```sql
SELECT tl.TERM_ID, tl.LANGUAGE, tl.SOURCE_LANG, tl.NAME
FROM   RA_TERMS_TL tl
WHERE  tl.LANGUAGE <> tl.SOURCE_LANG;
```

### Filtros comuns
- `LANGUAGE = 'US'` — Traduções em inglês americano
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
- `SOURCE_LANG = LANGUAGE` — Apenas traduções nativas (não herdadas)

---

## 🔒 Observações

- A chave primária é composta: (`TERM_ID`, `LANGUAGE`). Existe exatamente um registro por combinação de termo + idioma instalado.
- Quando `SOURCE_LANG <> LANGUAGE`, significa que a tradução **não foi fornecida** para aquele idioma e está usando o texto do idioma de origem como fallback.
- Ao inserir um novo termo via API ou interface, o Oracle automaticamente cria registros em RA_TERMS_TL para **todos os idiomas instalados**, copiando o nome do idioma base.
- Para consultas em aplicações, **sempre preferir** [[ra_terms_vl]] em vez de fazer o join manualmente entre `_B` e `_TL`.
- Os códigos de idioma seguem o padrão Oracle NLS: US (English), PTB (Brazilian Portuguese), ESA (Latin American Spanish), etc.

---

## 🔗 PVOs Relacionados

### [[customerprofile|CustomerProfile]] (AR · BICC: 2/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | LatePaymentTermTranslCreatedBy | — |
| CREATED_BY | PaymentTermTranslationCreatedBy | — |
| CREATION_DATE | LatePaymentTermTranslCreationDate | — |
| CREATION_DATE | PaymentTermTranslationCreationDate | — |
| DESCRIPTION | LatePaymentTermTranslDescription | — |
| DESCRIPTION | PaymentTermTranslationDescription | — |
| LANGUAGE | LatePaymentTermTranslLanguage | — |
| LANGUAGE | PaymentTermTranslationLanguage | — |
| LAST_UPDATE_DATE | LatePaymentTermTranslLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentTermTranslationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LatePaymentTermTranslLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PaymentTermTranslationLastUpdateLogin | — |
| LAST_UPDATED_BY | LatePaymentTermTranslLastUpdatedBy | — |
| LAST_UPDATED_BY | PaymentTermTranslationLastUpdatedBy | — |
| NAME | LatePaymentTermTranslName | — |
| NAME | PaymentTermTranslationName | — |
| OBJECT_VERSION_NUMBER | LatePaymentTermTranslObjVerNumber | — |
| OBJECT_VERSION_NUMBER | PayTermTransObjectVersionNumber | — |
| SET_ID | LatePaymentTermTranslSetId | — |
| SET_ID | PaymentTermTranslationSetId | — |
| SOURCE_LANG | LatePaymentTermTranslSourceLang | — |
| SOURCE_LANG | PaymentTermTranslationSourceLang | — |
| TERM_ID | LatePaymentTermTranslTermId | — |
| TERM_ID | PaymentTermTranslationTermId | — |

### [[customersiteprofile|CustomerSiteProfile]] (AR · BICC: 2/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | LatePaymentTermTranslCreatedBy | — |
| CREATED_BY | PaymentTermTranslationCreatedBy | — |
| CREATION_DATE | LatePaymentTermTranslCreationDate | — |
| CREATION_DATE | PaymentTermTranslationCreationDate | — |
| DESCRIPTION | LatePaymentTermTranslDescription | — |
| DESCRIPTION | PaymentTermTranslationDescription | — |
| LANGUAGE | LatePaymentTermTranslLanguage | — |
| LANGUAGE | PaymentTermTranslationLanguage | — |
| LAST_UPDATE_DATE | LatePaymentTermTranslLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentTermTranslationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LatePaymentTermTranslLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PaymentTermTranslationLastUpdateLogin | — |
| LAST_UPDATED_BY | LatePaymentTermTranslLastUpdatedBy | — |
| LAST_UPDATED_BY | PaymentTermTranslationLastUpdatedBy | — |
| NAME | LatePaymentTermTranslName | — |
| NAME | PaymentTermTranslationName | — |
| OBJECT_VERSION_NUMBER | LatePaymentTermTranslObjVerNumber | — |
| OBJECT_VERSION_NUMBER | PayTermTransObjectVersionNumber | — |
| SET_ID | LatePaymentTermTranslSetId | — |
| SET_ID | PaymentTermTranslationSetId | — |
| SOURCE_LANG | LatePaymentTermTranslSourceLang | — |
| SOURCE_LANG | PaymentTermTranslationSourceLang | — |
| TERM_ID | LatePaymentTermTranslTermId | — |
| TERM_ID | PaymentTermTranslationTermId | — |

### [[paymenttermextractpvo|PaymentTermExtractPVO]] (OTHER · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | RaTermTLCreatedBy | ✅ |
| CREATION_DATE | RaTermTLCreationDate | ✅ |
| DESCRIPTION | RaTermTLDescription | ✅ |
| LANGUAGE | RaTermTLLanguage | ✅ |
| LAST_UPDATE_DATE | RaTermTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaTermTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RaTermTLLastUpdatedBy | ✅ |
| NAME | RaTermTLName | ✅ |
| OBJECT_VERSION_NUMBER | RaTermTLObjectVersionNumber | ✅ |
| SEED_DATA_SOURCE | RaTermTLSeedDataSource | ✅ |
| SET_ID | RaTermTLSetId | ✅ |
| SOURCE_LANG | RaTermTLSourceLang | ✅ |
| TERM_ID | RaTermTLTermId | ✅ |

### [[paymenttermtlextractpvo|PaymentTermTLExtractPVO]] (OTHER · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | RaTermTLCreatedBy | ✅ |
| CREATION_DATE | RaTermTLCreationDate | ✅ |
| DESCRIPTION | RaTermTLDescription | ✅ |
| LANGUAGE | RaTermTLLanguage | ✅ |
| LAST_UPDATE_DATE | RaTermTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaTermTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RaTermTLLastUpdatedBy | ✅ |
| NAME | RaTermTLName | ✅ |
| OBJECT_VERSION_NUMBER | RaTermTLObjectVersionNumber | ✅ |
| SEED_DATA_SOURCE | RaTermTLSeedDataSource | ✅ |
| SET_ID | RaTermTLSetId | ✅ |
| SOURCE_LANG | RaTermTLSourceLang | ✅ |
| TERM_ID | RaTermTLTermId | ✅ |

### [[paymenttermtranslationpvo|PaymentTermTranslationPVO]] (AR · BICC: 11/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SET_ID | SetId | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
| TERM_ID | TermId | ✅ |

---

## 📚 Referências

- [Oracle Docs — RA_TERMS_TL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/ratermstl-10077.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
