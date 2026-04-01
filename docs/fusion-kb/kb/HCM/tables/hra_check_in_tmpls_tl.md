---
id: DOC-HCM-135
doc_type: system-doc
title: "HRA_CHECK_IN_TMPLS_TL — Templates de Check-In (Tradução)"
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
  - template-tl
  - avaliacao
  - hra
aliases:
  - HRA_CHECK_IN_TMPLS_TL
  - hra_check_in_tmpls_tl
  - hra-check-in-tmpls-tl
  - DOC-HCM-135
  - templates-de-check-in-(tradução)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_CHECK_IN_TMPLS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições de traduções de templates de check-in. Tabela _TL (translation) que complementa `HRA_CHECK_IN_TMPLS_B` com conteúdo multilíngue.

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
| 1 | CHECK_IN_TMPL_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador (join com HRA_CHECK_IN_TMPLS_B) | [[hra_check_in_tmpls_b]] | 🟢 90% |
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
- [[hra_check_in_tmpls_b]] — via `CHECK_IN_TMPL_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Tradução em português
```sql
SELECT tl.NAME, tl.DESCRIPTION
FROM   HRA_CHECK_IN_TMPLS_TL tl
WHERE  tl.CHECK_IN_TMPL_ID = :p_id
  AND  tl.LANGUAGE = 'PTBR';
```

### Todas as traduções
```sql
SELECT b.CHECK_IN_TMPL_ID, tl.NAME, tl.LANGUAGE
FROM   HRA_CHECK_IN_TMPLS_B b
JOIN   HRA_CHECK_IN_TMPLS_TL tl ON b.CHECK_IN_TMPL_ID = tl.CHECK_IN_TMPL_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `CHECK_IN_TMPL_ID` + `LANGUAGE`.
- Padrão Oracle _TL: um registro por idioma instalado.
- O `SOURCE_LANG` indica o idioma original da tradução.
- Para consultas na UI, utilizar views _VL que resolvem o idioma automaticamente.

---

## 🔗 PVOs Relacionados

### [[checkintemplatepvo|CheckInTemplatePVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CheckInTemplateTranslationPEOBusinessGroupId | — |
| CHECK_IN_TEMPLATE_ID | CheckInTemplateTranslationPEOCheckInTemplateId | — |
| COMMENTS | CheckInTemplateTranslationPEOComments | ✅ |
| LANGUAGE | CheckInTemplateTranslationPEOLanguage | — |
| NAME | CheckInTemplateTranslationPEOName | ✅ |
| SOURCE_LANG | CheckInTemplateTranslationPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Docs — HRA_CHECK_IN_TMPLS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hracheckintmplstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
