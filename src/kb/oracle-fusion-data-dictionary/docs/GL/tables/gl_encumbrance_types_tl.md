---
id: DOC-GL-012
doc_type: system-doc
title: "GL_ENCUMBRANCE_TYPES_TL — Traduções dos Tipos de Reserva"
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
  - encumbrance
  - traducao
  - i18n
aliases:
  - GL_ENCUMBRANCE_TYPES_TL
  - gl_encumbrance_types_tl
  - traducoes-tipos-reserva
  - encumbrance-types-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_ENCUMBRANCE_TYPES_TL

## Visao Geral

Armazena as **traduções** (nomes e descrições em múltiplos idiomas) dos tipos de reserva/comprometimento definidos em [[gl_encumbrance_types_b]]. Cada registro contém o nome e a descrição de um tipo de encumbrance em um idioma específico. Segue o padrão Oracle `_TL` (Translation) com uma linha por combinação de `ENCUMBRANCE_TYPE_ID` + `LANGUAGE`.

> [!note] Padrão _TL
> A tabela `_TL` sempre tem uma linha para cada idioma instalado no ambiente Oracle. Em ambientes com apenas um idioma (ex: pt-BR), haverá uma linha por tipo de encumbrance. Em ambientes multi-idioma, haverá N linhas (uma por idioma).

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Exibição de nomes traduzidos:** Fornece o nome e descrição do tipo de encumbrance no idioma do usuário logado.
- **Relatórios multi-idioma:** Permite gerar relatórios financeiros com nomes de tipos de reserva no idioma apropriado.
- **Interface do usuário:** O Oracle Fusion consulta esta tabela para exibir labels em LOVs e formulários.
- **Integração:** Consumidores externos podem consultar nomes em idiomas específicos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ENCUMBRANCE_TYPE_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do tipo de reserva | [[gl_encumbrance_types_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex: US, PTB, ESA) | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução (idioma base) | — | 🟢 90% |
| 4 | NAME | VARCHAR2(30) | NOT NULL | Identificação | Nome do tipo de reserva no idioma indicado | — | 🟢 95% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do tipo de reserva no idioma indicado | — | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_encumbrance_types_b]] — via `ENCUMBRANCE_TYPE_ID` (tabela base do tipo de reserva)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de tradução (leaf table).

---

## Uso Tipico

### Tipos de encumbrance no idioma do usuário
```sql
SELECT tl.ENCUMBRANCE_TYPE_ID, tl.NAME, tl.DESCRIPTION
FROM   GL_ENCUMBRANCE_TYPES_TL tl
WHERE  tl.LANGUAGE = USERENV('LANG')
ORDER BY tl.NAME;
```

### Traduções disponíveis para um tipo
```sql
SELECT tl.LANGUAGE, tl.NAME, tl.DESCRIPTION, tl.SOURCE_LANG
FROM   GL_ENCUMBRANCE_TYPES_TL tl
WHERE  tl.ENCUMBRANCE_TYPE_ID = :p_encumbrance_type_id
ORDER BY tl.LANGUAGE;
```

### Join completo com tabela base
```sql
SELECT b.ENCUMBRANCE_TYPE_ID, b.ENCUMBRANCE_TYPE_KEY,
       tl.NAME, tl.DESCRIPTION, b.ENABLED_FLAG
FROM   GL_ENCUMBRANCE_TYPES_B b
JOIN   GL_ENCUMBRANCE_TYPES_TL tl ON tl.ENCUMBRANCE_TYPE_ID = b.ENCUMBRANCE_TYPE_ID
                                  AND tl.LANGUAGE = USERENV('LANG')
WHERE  b.ENABLED_FLAG = 'Y'
ORDER BY tl.NAME;
```

### Filtros comuns
- `LANGUAGE = USERENV('LANG')` — Idioma da sessão do usuário
- `LANGUAGE = 'US'` — Inglês americano (idioma base)
- `LANGUAGE = 'PTB'` — Português brasileiro
- `SOURCE_LANG = LANGUAGE` — Apenas traduções efetivas (não herdadas do idioma base)

---

## Observacoes

- A chave primária é composta por `ENCUMBRANCE_TYPE_ID` + `LANGUAGE`.
- Quando `SOURCE_LANG` = `LANGUAGE`, a tradução foi efetivamente feita naquele idioma. Quando `SOURCE_LANG` difere de `LANGUAGE`, o registro está usando o texto do idioma de origem (tradução pendente).
- O filtro `LANGUAGE = USERENV('LANG')` é o padrão para consultas que precisam exibir nomes no idioma do usuário logado.
- Esta tabela deve ser sempre consultada via join com [[gl_encumbrance_types_b]] para obter o `ENABLED_FLAG` e outros campos da tabela base.
- Em ambientes mono-idioma (apenas "US"), cada tipo terá exatamente uma linha nesta tabela.

---

## Referencias

- [Oracle Docs — GL_ENCUMBRANCE_TYPES_TL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glencumbrancetypestl-25088.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
