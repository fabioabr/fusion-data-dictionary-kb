---
id: DOC-HCM-568
doc_type: system-doc
title: "PAY_DIR_COMP_DETAILS_F — Detalhes de Componentes de Cartao"
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
  - comp-details
  - detalhes-cartao
  - pay-comp-details
aliases:
  - PAY_DIR_COMP_DETAILS_F
  - pay_dir_comp_details_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_DIR_COMP_DETAILS_F

## 📌 Visão Geral

Armazena os **detalhes** (valores de parametros) de cada componente de cartao de informacao direta. Contem os valores efetivos que alimentam o calculo de folha (ex.: aliquota IRRF, faixa salarial, numero de dependentes).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Armazenamento de valores de parametros fiscais
- Configuracao detalhada de componentes de calculo
- Historico temporal de parametros individuais

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COMP_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do detalhe | --- | 🟢 90% |
| 2 | DIR_CARD_COMP_ID | NUMBER(18) | NOT NULL | FK | ID do componente pai | PAY_DIR_CARD_COMPONENTS_F | 🟢 90% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 5 | DETAIL_VALUE | VARCHAR2(240) | NULL | Dados | Valor do parametro | --- | 🟡 75% |
| 6 | DETAIL_LOOKUP_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de lookup do detalhe | --- | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_dir_card_components_f]] --- via `DIR_CARD_COMP_ID` (componente do cartão ao qual pertence o detalhe)

### Tabelas-filha (FK de saída)
- --- Tabela de detalhe, nivel mais granular

---

## 📎 Uso Típico

### Detalhes vigentes de um componente
```sql
SELECT cd.COMP_DETAIL_ID, cd.DETAIL_VALUE, cd.DETAIL_LOOKUP_TYPE
FROM   PAY_DIR_COMP_DETAILS_F cd
WHERE  cd.DIR_CARD_COMP_ID = :p_comp_id
  AND  SYSDATE BETWEEN cd.EFFECTIVE_START_DATE AND cd.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Nivel mais granular da hierarquia: Cartao > Componente > Detalhe.

---

## 📚 Referências

- [Oracle Docs — PAY_DIR_COMP_DETAILS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paydircompdetailsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
