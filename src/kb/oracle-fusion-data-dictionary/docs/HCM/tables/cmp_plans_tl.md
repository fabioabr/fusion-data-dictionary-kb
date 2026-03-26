---
id: DOC-HCM-082
doc_type: system-doc
title: "CMP_PLANS_TL — Planos de Compensação (Tradução)"
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
  - planos
  - traducao
  - translation
aliases:
  - CMP_PLANS_TL
  - cmp_plans_tl
  - cmp-plans-tl
  - DOC-HCM-082
  - planos-de-compensação-(tradução)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_PLANS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições dos planos de compensação. Tabela _TL (translation) que complementa `CMP_PLANS_B` com conteúdo multilíngue.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Multilinguismo:** Suporte a nomes de planos em múltiplos idiomas.
- **Interface do usuário:** Exibição de nomes traduzidos conforme idioma do login.
- **Relatórios localizados:** Nomes de planos no idioma do destinatário.
- **Integração:** Base para views _VL que unificam base + tradução.
- **Governança:** Controle centralizado de traduções dos planos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do plano (join com CMP_PLANS_B) | [[cmp_plans_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex: US, PTBR) | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | PLAN_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome do plano no idioma | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição do plano no idioma | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[cmp_plans_b]] — via `PLAN_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Nome do plano em português
```sql
SELECT tl.PLAN_NAME, tl.DESCRIPTION
FROM   CMP_PLANS_TL tl
WHERE  tl.PLAN_ID = :p_plan_id
  AND  tl.LANGUAGE = 'PTBR';
```

### Todos os planos com tradução
```sql
SELECT b.PLAN_ID, b.PLAN_CODE, tl.PLAN_NAME, tl.LANGUAGE
FROM   CMP_PLANS_B b
JOIN   CMP_PLANS_TL tl ON b.PLAN_ID = tl.PLAN_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `PLAN_ID` + `LANGUAGE`.
- O campo `SOURCE_LANG` indica o idioma original; se igual a `LANGUAGE`, é a tradução primária.
- Padrão Oracle _TL: um registro por idioma instalado por plano.
- Views _VL (como `CMP_PLANS_VL`) unem _B + _TL automaticamente para o idioma da sessão.

---

## 📚 Referências

- [Oracle Docs — CMP_PLANS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpplanstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
