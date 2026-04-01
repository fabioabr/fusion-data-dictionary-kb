---
id: DOC-HCM-112
doc_type: system-doc
title: "HRA_ROLE_DEFNS_TL — Definições de Papéis de Avaliação (Tradução)"
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
  - papéis
  - tradução
  - hra
aliases:
  - HRA_ROLE_DEFNS_TL
  - hra_role_defns_tl
  - hra-role-defns-tl
  - DOC-HCM-112
  - definições-de-papéis-de-avaliação-(tradução)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_ROLE_DEFNS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições dos papéis de avaliação. Tabela _TL que complementa `HRA_ROLE_DEFNS_B` com conteúdo multilíngue.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Multilinguismo:** Nomes de papéis em múltiplos idiomas.
- **Interface localizada:** Exibição traduzida na UI.
- **Relatórios:** Labels no idioma do destinatário.
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
| 1 | ROLE_DEFN_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do papel | [[hra_role_defns_b]] | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 95% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome do papel traduzido | — | 🟡 80% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descricao traduzida | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hra_role_defns_b]] — via `ROLE_DEFN_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Tradução em portugues
```sql
SELECT tl.NAME, tl.DESCRIPTION
FROM   HRA_ROLE_DEFNS_TL tl
WHERE  tl.ROLE_DEFN_ID = :p_id
  AND  tl.LANGUAGE = 'PTBR';
```

### Com tradução
```sql
SELECT b.ROLE_CODE, tl.NAME
FROM   HRA_ROLE_DEFNS_B b
JOIN   HRA_ROLE_DEFNS_TL tl ON b.ROLE_DEFN_ID = tl.ROLE_DEFN_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `ROLE_DEFN_ID` + `LANGUAGE`.
- Padrão Oracle _TL: um registro por idioma instalado.
- O `SOURCE_LANG` indica o idioma original da tradução.
- Para consultas na UI, utilizar views _VL.

---

## 🔗 PVOs Relacionados

### [[templateroledefnpvo|TemplateRoleDefnPVO]] (HCM · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | RoleDefinitionTranslationPEOBusinessGroupId | ✅ |
| DESCRIPTION | RoleDefinitionTranslationPEODescription | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | RoleDefinitionTranslationPEOLastUpdateDate | ✅ |
| NAME | RoleDefinitionTranslationPEOName | ✅ |
| ROLE_ID | RoleDefinitionTranslationPEORoleId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HRA_ROLE_DEFNS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hraroledefnstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
