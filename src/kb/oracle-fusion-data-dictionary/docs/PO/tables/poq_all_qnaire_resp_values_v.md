---
id: DOC-PO-036
doc_type: system-doc
title: "POQ_ALL_QNAIRE_RESP_VALUES_V — Valores de Respostas de Questionários de Qualificação (View)"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - supplier-qualification
  - questionario
  - qualificacao
  - view
aliases:
  - POQ_ALL_QNAIRE_RESP_VALUES_V
  - poq_all_qnaire_resp_values_v
  - valores-respostas-questionarios-qualificacao
  - qnaire-resp-values
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_ALL_QNAIRE_RESP_VALUES_V

## Visão Geral

**View** que consolida os **valores das respostas** de questionários de qualificação de fornecedores no módulo Oracle Supplier Qualification Management (SQM). Apresenta as respostas individuais dos fornecedores a cada pergunta de um questionário, incluindo valores textuais, numéricos e de seleção, com informações desnormalizadas para facilitar consultas e relatórios.

> [!note] Sufixo _V
> O sufixo `_V` indica que este é um **view** (visão), não uma tabela-base. Os dados são derivados de tabelas subjacentes do módulo POQ e expostos em formato consolidado para consumo analítico.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Análise de respostas de qualificação:** Consulta consolidada das respostas dos fornecedores a questionários de qualificação.
- **Relatórios de compliance:** Geração de relatórios sobre conformidade dos fornecedores com critérios de qualificação.
- **Comparação de fornecedores:** Análise lado a lado das respostas de múltiplos fornecedores ao mesmo questionário.
- **Extração de dados (BICC/BI):** Fonte de dados desnormalizados para pipelines de BI e analytics.
- **Auditoria de qualificação:** Evidência das respostas fornecidas em processos de qualificação.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESPONSE_VALUE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do valor da resposta | — | 🟡 65% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Identificador do questionário | [[poq_questionnaires]] | 🟡 65% |
| 3 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Identificador da pergunta | [[poq_questions]] | 🟡 65% |
| 4 | RESPONSE_ID | NUMBER(18) | NOT NULL | FK | Identificador da resposta do fornecedor | [[poq_responses]] | 🟡 65% |
| 5 | SUPPLIER_ID | NUMBER(18) | NULL | FK | Fornecedor respondente | [[poz_suppliers]] | 🟡 70% |
| 6 | QUESTION_TEXT | VARCHAR2(4000) | NULL | Texto | Texto da pergunta (desnormalizado) | — | 🟡 60% |
| 7 | RESPONSE_VALUE | VARCHAR2(4000) | NULL | Texto | Valor da resposta (texto livre ou seleção) | — | 🟡 70% |
| 8 | RESPONSE_NUMBER_VALUE | NUMBER | NULL | Numérico | Valor numérico da resposta (quando aplicável) | — | 🟡 60% |
| 9 | RESPONSE_DATE_VALUE | DATE | NULL | Data | Valor de data da resposta (quando aplicável) | — | 🟡 60% |
| 10 | QUESTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da pergunta (TEXT, NUMBER, DATE, SINGLE_SELECT, MULTI_SELECT) | — | 🟡 60% |
| 11 | SECTION_NAME | VARCHAR2(240) | NULL | Identificação | Nome da seção do questionário (desnormalizado) | — | 🟡 55% |
| 12 | QUESTIONNAIRE_NAME | VARCHAR2(240) | NULL | Identificação | Nome do questionário (desnormalizado) | — | 🟡 60% |
| 13 | SUPPLIER_NAME | VARCHAR2(360) | NULL | Identificação | Nome do fornecedor (desnormalizado) | — | 🟡 60% |
| 14 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data/hora de criação da resposta | — | 🟢 90% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NULL | Auditoria | Data/hora da última alteração | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-base (fontes do view)

### Views relacionadas

---

## Uso Típico

### Respostas de um fornecedor a um questionário
```sql
SELECT v.QUESTION_TEXT, v.RESPONSE_VALUE,
       v.RESPONSE_NUMBER_VALUE, v.QUESTION_TYPE,
       v.SECTION_NAME
FROM   POQ_ALL_QNAIRE_RESP_VALUES_V v
WHERE  v.QUESTIONNAIRE_ID = :p_questionnaire_id
  AND  v.SUPPLIER_ID = :p_supplier_id
ORDER BY v.SECTION_NAME, v.QUESTION_ID;
```

### Comparação de respostas entre fornecedores
```sql
SELECT v.SUPPLIER_NAME, v.QUESTION_TEXT,
       v.RESPONSE_VALUE
FROM   POQ_ALL_QNAIRE_RESP_VALUES_V v
WHERE  v.QUESTIONNAIRE_ID = :p_questionnaire_id
ORDER BY v.QUESTION_ID, v.SUPPLIER_NAME;
```

---

## Observações

- Por ser uma **view**, não possui índices próprios — o desempenho depende dos índices das tabelas-base subjacentes.
- Os campos desnormalizados (`QUESTION_TEXT`, `QUESTIONNAIRE_NAME`, `SUPPLIER_NAME`, `SECTION_NAME`) evitam joins adicionais em consultas analíticas.
- O tipo de resposta (`QUESTION_TYPE`) determina qual coluna de valor está preenchida: `RESPONSE_VALUE` (texto/seleção), `RESPONSE_NUMBER_VALUE` (numérico), ou `RESPONSE_DATE_VALUE` (data).
- Esta view é frequentemente utilizada por ferramentas de BI (OTBI/BICC) para extração de dados de qualificação de fornecedores.
- As colunas e estrutura exatas podem variar conforme o release do Oracle Fusion; recomenda-se validação no ambiente.

---

## Referências

- [Oracle Docs — POQ_ALL_QNAIRE_RESP_VALUES_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poqallqnairerespvaluesv.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
