---
id: DOC-HCM-576
doc_type: system-doc
title: "PAY_ELE_CLASSIFICATIONS_TL — Classificacoes de Elementos (Traducoes)"
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
  - classifications-tl
  - traducoes
  - pay-class-tl
aliases:
  - PAY_ELE_CLASSIFICATIONS_TL
  - pay_ele_classifications_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELE_CLASSIFICATIONS_TL

## 📌 Visão Geral

Armazena as **traducoes** dos nomes das classificacoes de elementos de folha para multiplos idiomas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Suporte multiidioma para classificacoes de elementos
- Exibicao localizada em interfaces de configuracao

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da classificacao (chave composta) | PAY_ELE_CLASSIFICATIONS | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | --- | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Dados | Idioma de origem | --- | 🟢 90% |
| 4 | CLASSIFICATION_NAME | VARCHAR2(80) | NULL | Identificacao | Nome traduzido da classificacao | --- | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Dados | Descricao traduzida | --- | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_ele_classifications]] --- via `CLASSIFICATION_ID` (tabela base da classificação de elemento)

### Tabelas-filha (FK de saída)
- --- Tabela de traducao, sem filhas

---

## 📎 Uso Típico

### Traducao de classificacao no idioma corrente
```sql
SELECT tl.CLASSIFICATION_NAME, tl.DESCRIPTION
FROM   PAY_ELE_CLASSIFICATIONS_TL tl
WHERE  tl.CLASSIFICATION_ID = :p_classification_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[elementclassificationstranslation|ElementClassificationsTranslation]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | ClassificationId | ✅ |
| CLASSIFICATION_NAME | ElementClassificationTLClassificationName | — |
| CREATED_BY | ElementClassificationTLCreatedBy | — |
| CREATION_DATE | ElementClassificationTLCreationDate | — |
| DESCRIPTION | ElementClassificationTLDescription | — |
| LANGUAGE | ElementClassificationTLLanguage | — |
| LAST_UPDATE_DATE | ElementClassificationTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ElementClassificationTLLastUpdateLogin | — |
| LAST_UPDATED_BY | ElementClassificationTLLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ElementClassificationTLObjectVersionNumber | — |
| SOURCE_LANG | ElementClassificationTLSourceLang | — |

---

## 📚 Referências

- [Oracle Docs — PAY_ELE_CLASSIFICATIONS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payeleclassificationstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
