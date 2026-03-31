---
id: DOC-PO-023
doc_type: system-doc
title: "PON_NEGOTIATION_STYLES_TL — Traduções de Estilos de Negociação"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - negotiation-styles
  - sourcing
  - translation
aliases:
  - PON_NEGOTIATION_STYLES_TL
  - pon_negotiation_styles_tl
  - traducao-estilos-negociacao
  - negotiation-styles-translation
  - pon-neg-styles-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_NEGOTIATION_STYLES_TL

## 📌 Visão Geral

Tabela de traduções que armazena os **nomes e descrições** dos estilos de negociação em múltiplos idiomas. Cada registro da tabela base [[pon_negotiation_styles_b]] possui N registros correspondentes nesta tabela — um por idioma instalado na instância Oracle Fusion.

> [!note] Sufixo _TL
> O sufixo `_TL` indica uma **tabela de tradução** (Translation). Contém uma linha por combinação de `STYLE_ID` + `LANGUAGE`, com os textos traduzidos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização (i18n):** Fornece nomes e descrições de estilos no idioma do usuário.
- **Interface de usuário:** As telas de criação de negociação exibem nomes traduzidos a partir desta tabela.
- **Relatórios multilíngue:** Permite geração de relatórios no idioma preferido de cada usuário/região.
- **View consolidada:** Alimenta a view [[pon_doctype_styles_vl]] que combina dados base + tradução automaticamente.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STYLE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do estilo de negociação | [[pon_negotiation_styles_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex: US, PTBR, ES) | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Sistema | Idioma de origem da tradução | — | 🟢 90% |
| 4 | STYLE_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome do estilo de negociação traduzido | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição do estilo traduzida | — | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_negotiation_styles_b]] — via `STYLE_ID` (tabela base com definição do estilo)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Obter nome traduzido de um estilo
```sql
SELECT tl.STYLE_NAME, tl.DESCRIPTION
FROM   PON_NEGOTIATION_STYLES_TL tl
WHERE  tl.STYLE_ID = :p_style_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

### Listar todos os estilos com tradução em português
```sql
SELECT b.STYLE_ID, b.STYLE_CODE, tl.STYLE_NAME, tl.DESCRIPTION,
       b.NEGOTIATION_TYPE
FROM   PON_NEGOTIATION_STYLES_B b
JOIN   PON_NEGOTIATION_STYLES_TL tl ON tl.STYLE_ID = b.STYLE_ID
WHERE  tl.LANGUAGE = 'PTB'
  AND  b.ENABLED_FLAG = 'Y';
```

---

## 🔒 Observações

- A chave primária é composta: `STYLE_ID` + `LANGUAGE`.
- Se `SOURCE_LANG <> LANGUAGE`, o texto exibido é uma cópia do idioma-fonte (ainda não traduzido de fato). Isso é o padrão Oracle MLS (Multi-Language Support).
- Novas instalações de idioma geram automaticamente registros nesta tabela copiando os textos do idioma-fonte (`SOURCE_LANG`).
- Para consultas em produção, prefira a view [[pon_doctype_styles_vl]] que faz o JOIN automaticamente com o idioma da sessão.

---

## 🔗 PVOs Relacionados

### [[negotiationstylebpvo|NegotiationStyleBPVO]] (PO · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | NegotiationStyleTranslatedCreatedBy | — |
| CREATION_DATE | NegotiationStyleTranslatedCreationDate | — |
| DESCRIPTION | NegotiationStyleTranslatedDescription | ✅ |
| LANGUAGE | NegotiationStyleTranslatedLanguage | — |
| LAST_UPDATE_DATE | NegotiationStyleTranslatedLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationStyleTranslatedLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationStyleTranslatedLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | NegotiationStyleTranslatedObjectVersionNumber | — |
| SOURCE_LANG | NegotiationStyleTranslatedSourceLang | — |
| STYLE_ID | NegotiationStyleTranslatedStyleId | — |
| STYLE_NAME | NegotiationStyleTranslatedStyleName | ✅ |

### [[negstyletranslationextractpvo|NegStyleTranslationExtractPVO]] (PO · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
| STYLE_ID | StyleId | ✅ |
| STYLE_NAME | StyleName | ✅ |

### [[sourcingnegotiationstyletranslationpvo|SourcingNegotiationStyleTranslationPVO]] (PO · BICC: 10/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SOURCE_LANG | SourceLang | ✅ |
| STYLE_ID | StyleId | ✅ |
| STYLE_NAME | StyleName | ✅ |

---

## 📚 Referências

- [Oracle Docs — Sourcing Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
