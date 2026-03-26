---
id: DOC-HCM-275
doc_type: system-doc
title: "HR_ALL_POSITIONS_F_TL — Posicoes — Traducoes"
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
  - traducoes
  - nls
  - positions
aliases:
  - HR_ALL_POSITIONS_F_TL
  - hr_all_positions_f_tl
  - hr-all-positions-f-tl
  - positions-translations
  - posicoes-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ALL_POSITIONS_F_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hr_all_positions_f]].

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Multi-idioma:** Nomes e descricoes traduzidos para multiplos idiomas.
- **Exibicao:** Textos traduzidos para interfaces de usuario e relatorios.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POSITION_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hr_all_positions_f]] | 🟢 100% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 100% |
| 3 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 4 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 5 | NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `POSITION_ID` (registro base do cadastro)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.NAME
FROM   HR_ALL_POSITIONS_F_TL tl
WHERE  tl.POSITION_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (POSITION_ID, EFFECTIVE_START_DATE, LANGUAGE).
- JOIN com [[hr_all_positions_f]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HR_ALL_POSITIONS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrallpositionsftl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
