---
id: DOC-GL-026
doc_type: system-doc
title: "GL_JE_SOURCES_TL — Traduções das Fontes de Lançamentos"
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
  - traducao
  - i18n
aliases:
  - GL_JE_SOURCES_TL
  - gl_je_sources_tl
  - traducao-fontes
  - journal-sources-translation
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_JE_SOURCES_TL

## 📌 Visão Geral

Armazena as **traduções dos nomes das fontes de lançamentos contábeis** para múltiplos idiomas. Segue o padrão Oracle _TL (Translation) — para cada registro em [[gl_je_sources_b]], existem N registros nesta tabela (um por idioma instalado). Contém o nome amigável da fonte (`USER_JE_SOURCE_NAME`) e a descrição traduzida.

> [!note] Tabela de tradução (padrão _TL)
> Tabela de baixa volumetria. O número de registros é o produto de fontes cadastradas × idiomas instalados. Essencial para exibição de nomes amigáveis em relatórios multi-idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Exibição multi-idioma:** Nomes de fontes traduzidos conforme o idioma do usuário.
- **Relatórios financeiros:** Exibição do nome amigável da fonte nos reports do GL.
- **Consultas e dashboards:** JOIN obrigatório para obter `USER_JE_SOURCE_NAME` traduzido.
- **Localização:** Suporte a operações multi-idioma no ERP.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JE_SOURCE_NAME | VARCHAR2(25) | NOT NULL | FK/PK | Nome da fonte de lançamento (chave para a tabela base) | [[gl_je_sources_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex: US, PTB, ESA) | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 100% |
| 4 | USER_JE_SOURCE_NAME | VARCHAR2(25) | NOT NULL | Identificação | Nome amigável/traduzido da fonte de lançamento | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição textual da fonte no idioma especificado | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_je_sources_b]] — via `JE_SOURCE_NAME` (tabela base com definição da fonte)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de tradução (leaf table).

---

## 📎 Uso Típico

### Obter nome amigável das fontes no idioma do usuário
```sql
SELECT stl.JE_SOURCE_NAME,
       stl.USER_JE_SOURCE_NAME,
       stl.DESCRIPTION,
       stl.LANGUAGE
FROM   GL_JE_SOURCES_TL stl
WHERE  stl.LANGUAGE = USERENV('LANG')
ORDER BY stl.USER_JE_SOURCE_NAME;
```

### JOIN com headers de journal para exibição
```sql
SELECT jh.NAME AS journal_name,
       stl.USER_JE_SOURCE_NAME AS fonte,
       jh.PERIOD_NAME,
       jh.STATUS
FROM   GL_JE_HEADERS jh
JOIN   GL_JE_SOURCES_TL stl
       ON stl.JE_SOURCE_NAME = jh.JE_SOURCE
      AND stl.LANGUAGE = USERENV('LANG')
WHERE  jh.LEDGER_ID = :p_ledger_id
  AND  jh.PERIOD_NAME = 'MAR-26'
ORDER BY jh.NAME;
```

### Filtros comuns
- `LANGUAGE = USERENV('LANG')` — Idioma da sessão do usuário
- `LANGUAGE = 'US'` — Inglês americano (padrão Oracle)
- `LANGUAGE = 'PTB'` — Português brasileiro
- `SOURCE_LANG = LANGUAGE` — Registro traduzido (não herdado do idioma base)

---

## 🔒 Observações

- A PK composta é `JE_SOURCE_NAME` + `LANGUAGE`. Cada fonte tem um registro por idioma instalado.
- Quando `SOURCE_LANG != LANGUAGE`, significa que a tradução foi herdada do idioma base (ainda não traduzida para o idioma específico).
- O campo `USER_JE_SOURCE_NAME` é o que aparece nas telas e relatórios do Oracle Fusion — sempre usar este campo em vez do `JE_SOURCE_NAME` para exibição.
- Padrão Oracle _TL: para consultas, sempre filtrar `LANGUAGE = USERENV('LANG')` para obter a tradução no idioma corrente.
- Alterações nesta tabela são feitas via UI do Oracle Fusion (Setup > General Ledger > Journal Sources), não diretamente.

---

## 📚 Referências

- [Oracle Docs — GL_JE_SOURCES_TL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gljesourcestl.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
