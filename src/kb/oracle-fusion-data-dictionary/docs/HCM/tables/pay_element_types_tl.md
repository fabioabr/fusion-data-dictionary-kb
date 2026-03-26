---
id: DOC-HCM-574
doc_type: system-doc
title: "PAY_ELEMENT_TYPES_TL — Tipos de Elementos (Traducoes)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - element-types-tl
  - traducoes
  - pay-elem-types-tl
aliases:
  - PAY_ELEMENT_TYPES_TL
  - pay_element_types_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELEMENT_TYPES_TL

## 📌 Visão Geral

Armazena as **traducoes** dos nomes e descricoes dos tipos de elementos de folha para multiplos idiomas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Suporte multiidioma para tipos de elementos de folha
- Exibicao localizada em contracheques e relatorios

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ELEMENT_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do tipo (chave composta) | PAY_ELEMENT_TYPES_F | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | --- | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Dados | Idioma de origem | --- | 🟢 90% |
| 4 | ELEMENT_NAME | VARCHAR2(80) | NULL | Identificacao | Nome traduzido do elemento | --- | 🟢 90% |
| 5 | REPORTING_NAME | VARCHAR2(80) | NULL | Identificacao | Nome para relatorios | --- | 🟡 80% |
| 6 | DESCRIPTION | VARCHAR2(240) | NULL | Dados | Descricao traduzida | --- | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_element_types_f]] --- via `ELEMENT_TYPE_ID` (tabela base do tipo de elemento de folha)

### Tabelas-filha (FK de saída)
- --- Tabela de traducao, sem filhas

---

## 📎 Uso Típico

### Traducao de um tipo de elemento
```sql
SELECT tl.ELEMENT_NAME, tl.REPORTING_NAME, tl.DESCRIPTION
FROM   PAY_ELEMENT_TYPES_TL tl
WHERE  tl.ELEMENT_TYPE_ID = :p_element_type_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_ELEMENT_TYPES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payelementtypestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
