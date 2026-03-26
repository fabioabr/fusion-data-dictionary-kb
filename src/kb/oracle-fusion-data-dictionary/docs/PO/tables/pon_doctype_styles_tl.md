---
id: DOC-PO-020
doc_type: system-doc
title: "PON_DOCTYPE_STYLES_TL — Traduções de Estilos de Tipo de Documento"
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
  - sourcing
  - doctype-styles
  - traducao
  - mls
aliases:
  - PON_DOCTYPE_STYLES_TL
  - pon_doctype_styles_tl
  - traducoes-doctype-styles
  - doctype-styles-traducao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_DOCTYPE_STYLES_TL

## 📌 Visão Geral

Armazena as **traduções dos nomes e descrições** dos estilos de tipo de documento de negociação de Sourcing. Cada registro contém a tradução para um idioma específico do estilo definido em [[pon_doctype_styles_b]]. Segue o padrão Oracle de Multi-Language Support (MLS) com sufixo `_TL`.

> [!note] Sufixo _TL
> O sufixo `_TL` indica a tabela de **traduções** do padrão Oracle MLS. Contém um registro por idioma instalado para cada estilo de tipo de documento. A chave primária é composta pelo ID do estilo + código do idioma (`LANGUAGE`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização (i18n):** Exibição do nome do estilo no idioma do usuário logado.
- **Interface multilíngue:** Suporte a organizações globais com usuários em diferentes idiomas.
- **Relatórios localizados:** Nomes de estilos traduzidos em reports e dashboards.
- **Setup administrativo:** Manutenção de traduções dos estilos configurados no Sourcing.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCTYPE_STYLE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do estilo de tipo de documento | [[pon_doctype_styles_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução (e.g., US, PTBR, ES) | [[fnd_languages_vl]] | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Classificação | Idioma de origem da tradução | — | 🟢 100% |
| 4 | DOCTYPE_STYLE_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome traduzido do estilo de tipo de documento | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição traduzida do estilo | — | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_doctype_styles_b]] — via `DOCTYPE_STYLE_ID` (tabela base com dados não traduzíveis)
- [[fnd_languages_vl]] — via `LANGUAGE` (idiomas instalados)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Nome do estilo no idioma do usuário
```sql
SELECT dstl.DOCTYPE_STYLE_NAME, dstl.DESCRIPTION
FROM   PON_DOCTYPE_STYLES_TL dstl
WHERE  dstl.DOCTYPE_STYLE_ID = :p_doctype_style_id
  AND  dstl.LANGUAGE = USERENV('LANG');
```

### Join completo: estilo base + tradução + tipo de documento
```sql
SELECT ds.DOCTYPE_STYLE_ID, dstl.DOCTYPE_STYLE_NAME,
       dt.DOCTYPE_NAME, ds.ENABLED_FLAG, ds.OUTCOME_CODE
FROM   PON_DOCTYPE_STYLES_B ds
JOIN   PON_DOCTYPE_STYLES_TL dstl
       ON dstl.DOCTYPE_STYLE_ID = ds.DOCTYPE_STYLE_ID
      AND dstl.LANGUAGE = USERENV('LANG')
JOIN   PON_AUC_DOCTYPES_TL dt
       ON dt.DOCTYPE_ID = ds.DOCTYPE_ID
      AND dt.LANGUAGE = USERENV('LANG')
WHERE  ds.ENABLED_FLAG = 'Y'
ORDER BY dt.DOCTYPE_NAME, dstl.DOCTYPE_STYLE_NAME;
```

### Verificar traduções faltantes
```sql
SELECT fl.LANGUAGE_CODE, fl.NLS_LANGUAGE
FROM   FND_LANGUAGES_VL fl
WHERE  fl.INSTALLED_FLAG IN ('I', 'B')
  AND  NOT EXISTS (
    SELECT 1 FROM PON_DOCTYPE_STYLES_TL dstl
    WHERE  dstl.DOCTYPE_STYLE_ID = :p_doctype_style_id
      AND  dstl.LANGUAGE = fl.LANGUAGE_CODE
  );
```

---

## 🔒 Observações

- A chave primária é composta por `DOCTYPE_STYLE_ID` + `LANGUAGE`.
- Existe um registro para cada idioma instalado (`FND_LANGUAGES.INSTALLED_FLAG IN ('I','B')`).
- O campo `SOURCE_LANG` indica de qual idioma a tradução foi copiada; quando `SOURCE_LANG <> LANGUAGE`, a tradução ainda não foi feita (fallback para o idioma de origem).
- Em queries de interface, sempre filtrar por `LANGUAGE = USERENV('LANG')` para obter o texto no idioma da sessão.
- Para ambientes com apenas um idioma, a tabela terá um registro por estilo; para ambientes multilíngues, N registros por estilo (onde N = número de idiomas instalados).

---

## 📚 Referências

- [Oracle Docs — PON_DOCTYPE_STYLES_TL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pondoctypestylestl.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
