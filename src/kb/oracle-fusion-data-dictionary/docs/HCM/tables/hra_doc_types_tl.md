---
id: DOC-HCM-138
doc_type: system-doc
title: "HRA_DOC_TYPES_TL — Tipos de Documento de Performance (Tradução)"
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
  - performance-management
  - doc-type-tl
  - avaliacao
  - hra
aliases:
  - HRA_DOC_TYPES_TL
  - hra_doc_types_tl
  - hra-doc-types-tl
  - DOC-HCM-138
  - tipos-de-documento-de-performance-(tradução)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_DOC_TYPES_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições de traduções de tipos de documento. Tabela _TL (translation) que complementa `HRA_DOC_TYPES_B` com conteúdo multilíngue.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Multilinguismo:** Nomes e descrições em múltiplos idiomas.
- **Interface localizada:** Exibição traduzida na UI.
- **Relatórios localizados:** Labels no idioma do destinatário.
- **Integração:** Base para views _VL.
- **Governança:** Controle centralizado de traduções.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOC_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador (join com HRA_DOC_TYPES_B) | [[hra_doc_types_b]] | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 95% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido | — | 🟡 80% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hra_doc_types_b]] — via `DOC_TYPE_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Tradução em português
```sql
SELECT tl.NAME, tl.DESCRIPTION
FROM   HRA_DOC_TYPES_TL tl
WHERE  tl.DOC_TYPE_ID = :p_id
  AND  tl.LANGUAGE = 'PTBR';
```

### Todas as traduções
```sql
SELECT b.DOC_TYPE_ID, tl.NAME, tl.LANGUAGE
FROM   HRA_DOC_TYPES_B b
JOIN   HRA_DOC_TYPES_TL tl ON b.DOC_TYPE_ID = tl.DOC_TYPE_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `DOC_TYPE_ID` + `LANGUAGE`.
- Padrão Oracle _TL: um registro por idioma instalado.
- O `SOURCE_LANG` indica o idioma original da tradução.
- Para consultas na UI, utilizar views _VL que resolvem o idioma automaticamente.

---

## 📚 Referências

- [Oracle Docs — HRA_DOC_TYPES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hradoctypestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
