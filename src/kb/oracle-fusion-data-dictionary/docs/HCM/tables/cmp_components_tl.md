---
id: DOC-HCM-069
doc_type: system-doc
title: "CMP_COMPONENTS_TL — Traduções de Componentes de Compensação"
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
  - compensation
  - traducoes
  - translations
  - componentes-tl
aliases:
  - CMP_COMPONENTS_TL
  - cmp_components_tl
  - componentes-compensacao-tl
  - components-tl
  - cmp-components-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_COMPONENTS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições dos componentes de compensação em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Nomes de componentes no idioma do gestor/colaborador.
- **Total Comp Statements:** Nomes traduzidos em demonstrativos de compensação.
- **Relatórios localizados:** Componentes no idioma local.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COMPONENT_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do componente | [[cmp_components_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[cmp_components_b]] — via `COMPONENT_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Nomes de componentes em português
```sql
SELECT c.COMPONENT_ID, tl.NAME, tl.DESCRIPTION
FROM   CMP_COMPONENTS_B c
JOIN   CMP_COMPONENTS_TL tl ON c.COMPONENT_ID = tl.COMPONENT_ID
WHERE  tl.LANGUAGE = 'PT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Traduções em português

---

## 🔒 Observações

- Tabela de traduções vinculada à tabela base `CMP_COMPONENTS_B`.
- Sempre fazer JOIN com a tabela base para obter dados técnicos.

---

## 🔗 PVOs Relacionados

### [[componentspvo|ComponentsPVO]] (HCM · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMPONENT_ID | ComponentsTLPEOComponentId1 | ✅ |
| COMPONENT_NAME | ComponentsTLPEOComponentName | ✅ |
| CREATED_BY | ComponentsTLPEOCreatedBy | ✅ |
| CREATION_DATE | ComponentsTLPEOCreationDate | ✅ |
| LANGUAGE | ComponentsTLPEOLanguage | ✅ |
| LAST_UPDATE_DATE | ComponentsTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ComponentsTLPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ComponentsTLPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ComponentsTLPEOObjectVersionNumber | ✅ |
| PLAN_ID | ComponentsTLPEOPlanId1 | ✅ |
| SOURCE_LANG | ComponentsTLPEOSourceLang | ✅ |

---

## 📚 Referências

- [Oracle Docs — CMP_COMPONENTS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcomponentstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
