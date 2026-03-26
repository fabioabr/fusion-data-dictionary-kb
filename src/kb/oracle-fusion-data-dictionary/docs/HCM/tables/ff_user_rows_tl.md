---
id: DOC-HCM-096
doc_type: system-doc
title: "FF_USER_ROWS_TL — Linhas de Tabelas FF (Tradução)"
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
  - fast-formula
  - linhas
  - traducao
  - translation
aliases:
  - FF_USER_ROWS_TL
  - ff_user_rows_tl
  - ff-user-rows-tl
  - DOC-HCM-096
  - linhas-de-tabelas-ff-(tradução)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# FF_USER_ROWS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes de linhas das tabelas de usuário Fast Formula. Tabela _TL que complementa `FF_USER_ROWS_F` com conteúdo multilíngue.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Multilinguismo:** Nomes de linhas traduzidos por idioma.
- **Interface localizada:** Exibição de labels no idioma do usuário.
- **Relatórios:** Nomes traduzidos em relatórios de configuração.
- **Integração:** Base para views _VL combinadas.
- **Governança de dados:** Controle centralizado de traduções.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | USER_ROW_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da linha | [[ff_user_rows_f]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 95% |
| 4 | ROW_LOW_RANGE_OR_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome/range traduzido | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ff_user_rows_f]] — via `USER_ROW_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Tradução de linhas em português
```sql
SELECT tl.ROW_LOW_RANGE_OR_NAME
FROM   FF_USER_ROWS_TL tl
WHERE  tl.USER_ROW_ID = :p_row_id
  AND  tl.LANGUAGE = 'PTBR';
```

### Linhas com tradução
```sql
SELECT r.USER_ROW_ID, r.ROW_LOW_RANGE_OR_NAME AS nome_base,
       tl.ROW_LOW_RANGE_OR_NAME AS nome_traduzido
FROM   FF_USER_ROWS_F r
JOIN   FF_USER_ROWS_TL tl ON r.USER_ROW_ID = tl.USER_ROW_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `USER_ROW_ID` + `LANGUAGE`.
- Padrão Oracle _TL: um registro por idioma instalado por linha.
- O `SOURCE_LANG` indica o idioma original da tradução.
- Para tabelas com match numérico (range), a tradução pode ser irrelevante.

---

## 📚 Referências

- [Oracle Docs — FF_USER_ROWS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ffuserrowstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
