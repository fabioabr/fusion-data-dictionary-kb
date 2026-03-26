---
id: DOC-PO-049
doc_type: system-doc
title: "POQ_QUAL_MODEL_AREAS — Áreas Associadas a Modelos de Qualificação"
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
  - qualificacao
  - supplier-qualification
  - model-areas
aliases:
  - POQ_QUAL_MODEL_AREAS
  - poq_qual_model_areas
  - areas-modelo-qualificacao
  - qualification-model-areas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_MODEL_AREAS

## 📌 Visão Geral

Armazena a **associação entre modelos de qualificação e áreas de qualificação**, definindo quais áreas compõem cada modelo e com que peso. Funciona como tabela de interseção entre [[poq_qual_models]] e [[poq_qual_areas_vl]], adicionando o peso relativo de cada área no cálculo da nota final.

> [!note] Tabela de interseção
> Esta tabela materializa o relacionamento N:N entre modelos e áreas, sendo fundamental para o cálculo ponderado da pontuação final do fornecedor.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Composição de modelos:** Definição de quais áreas de qualificação compõem cada modelo.
- **Ponderação:** Configuração do peso de cada área no cálculo da nota consolidada.
- **Flexibilidade:** Permite que a mesma área seja reutilizada em múltiplos modelos com pesos diferentes.
- **Cálculo de score:** Base para o algoritmo de pontuação ponderada do Supplier Qualification Management.
- **Relatórios detalhados:** Drill-down de resultados por área dentro de um modelo específico.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUAL_MODEL_AREA_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de associação | — | 🟢 90% |
| 2 | QUAL_MODEL_ID | NUMBER(18) | NOT NULL | FK | Modelo de qualificação | [[poq_qual_models]] | 🟢 95% |
| 3 | QUAL_AREA_ID | NUMBER(18) | NOT NULL | FK | Área de qualificação | [[poq_qual_areas_vl]] | 🟢 95% |
| 4 | WEIGHT_PERCENT | NUMBER | NULL | Pontuação | Peso percentual da área no modelo (0–100) | — | 🟡 80% |
| 5 | SEQUENCE_NUMBER | NUMBER | NULL | Identificação | Ordem de exibição da área no modelo | — | 🟡 75% |
| 6 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Classificação | Se a área é obrigatória no modelo: Y/N | — | 🟡 70% |
| 7 | PASS_FAIL_FLAG | VARCHAR2(1) | NULL | Classificação | Se a área usa critério pass/fail independente: Y/N | — | 🟡 65% |
| 8 | MIN_PASSING_SCORE | NUMBER | NULL | Pontuação | Score mínimo na área para aprovação (quando pass/fail) | — | 🟡 65% |
| 9 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Se a associação está ativa: Y/N | — | 🟡 80% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 14 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_qual_models]] — via `QUAL_MODEL_ID` (modelo de qualificação)
- [[poq_qual_areas_vl]] — via `QUAL_AREA_ID` (área de qualificação)

### Tabelas-filha (FK de saída)
- Nenhuma direta — esta é uma tabela de interseção.

### Tabelas relacionadas

---

## 📎 Uso Típico

### Áreas e pesos de um modelo
```sql
SELECT qa.QUAL_AREA_NAME, qma.WEIGHT_PERCENT,
       qma.MANDATORY_FLAG, qma.PASS_FAIL_FLAG,
       qma.MIN_PASSING_SCORE
FROM   POQ_QUAL_MODEL_AREAS qma
JOIN   POQ_QUAL_AREAS_VL qa ON qa.QUAL_AREA_ID = qma.QUAL_AREA_ID
WHERE  qma.QUAL_MODEL_ID = :p_model_id
  AND  qma.ENABLED_FLAG = 'Y'
ORDER  BY qma.SEQUENCE_NUMBER;
```

### Verificar se pesos somam 100%
```sql
SELECT qma.QUAL_MODEL_ID,
       SUM(qma.WEIGHT_PERCENT) AS total_peso
FROM   POQ_QUAL_MODEL_AREAS qma
WHERE  qma.ENABLED_FLAG = 'Y'
GROUP  BY qma.QUAL_MODEL_ID
HAVING SUM(qma.WEIGHT_PERCENT) <> 100;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Associações ativas
- `MANDATORY_FLAG = 'Y'` — Áreas obrigatórias
- `PASS_FAIL_FLAG = 'Y'` — Áreas com critério eliminatório

---

## 🔒 Observações

- A soma de `WEIGHT_PERCENT` de todas as áreas ativas de um modelo deve totalizar 100%.
- Quando `PASS_FAIL_FLAG = 'Y'`, o fornecedor precisa atingir o `MIN_PASSING_SCORE` nesta área **independentemente** da nota final ponderada — funciona como critério eliminatório.
- Cada par `QUAL_MODEL_ID` + `QUAL_AREA_ID` deve ser único (constraint esperada).
- A mesma área pode aparecer em múltiplos modelos com pesos diferentes, proporcionando flexibilidade na configuração.

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
