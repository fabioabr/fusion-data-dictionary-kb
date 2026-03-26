---
id: DOC-HCM-092
doc_type: system-doc
title: "FF_FORMULAS_VL — Fórmulas Fast Formula (View Localized)"
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
  - fast-formula
  - formulas
  - calculo
  - payroll-engine
aliases:
  - FF_FORMULAS_VL
  - ff_formulas_vl
  - ff-formulas-vl
  - DOC-HCM-092
  - fórmulas-fast-formula-(view-localized)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# FF_FORMULAS_VL

## 📌 Visão Geral

**View localizada** que apresenta as **fórmulas Fast Formula** do Oracle Fusion — motor de cálculo usado em payroll, compensation, benefits e outros módulos. Combina dados base com traduções no idioma da sessão.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Motor de cálculo:** Consulta de fórmulas usadas em processamento de folha.
- **Configuração de regras:** Visualização de regras de cálculo por módulo.
- **Auditoria de cálculos:** Identificação de qual fórmula processa cada cenário.
- **Troubleshooting:** Diagnóstico de problemas em cálculos de payroll/benefits.
- **Documentação:** Inventário de todas as fórmulas disponíveis.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | FORMULA_ID | NUMBER(18) | NOT NULL | PK | Identificador único da fórmula | — | 🟢 95% |
| 2 | FORMULA_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome da fórmula | — | 🟢 95% |
| 3 | FORMULA_TYPE_ID | NUMBER(18) | NULL | FK | Tipo da fórmula | — | 🟢 90% |
| 4 | FORMULA_TYPE_NAME | VARCHAR2(80) | NULL | Classificação | Nome do tipo da fórmula | — | 🟡 80% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição | Descrição da fórmula | — | 🟢 90% |
| 6 | FORMULA_TEXT | CLOB | NULL | Conteúdo | Texto/código da fórmula | — | 🟢 90% |
| 7 | EFFECTIVE_START_DATE | DATE | NOT NULL | Data | Início de vigência | — | 🟢 95% |
| 8 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Fim de vigência | — | 🟢 95% |
| 9 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código de legislação (BR, US, etc.) | — | 🟢 90% |
| 10 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócios | [[per_business_groups]] | 🟡 80% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_business_groups]] — via `BUSINESS_GROUP_ID` (grupo de negócios)

### Tabelas-filha (FK de saída)
- Por ser uma view, não possui tabelas-filha diretas.

---

## 📎 Uso Típico

### Fórmulas ativas por tipo
```sql
SELECT f.FORMULA_ID, f.FORMULA_NAME, f.FORMULA_TYPE_NAME,
       f.LEGISLATION_CODE
FROM   FF_FORMULAS_VL f
WHERE  SYSDATE BETWEEN f.EFFECTIVE_START_DATE AND f.EFFECTIVE_END_DATE
  AND  f.FORMULA_TYPE_NAME = :p_type;
```

### Buscar fórmula por nome
```sql
SELECT f.FORMULA_NAME, f.DESCRIPTION, f.FORMULA_TEXT
FROM   FF_FORMULAS_VL f
WHERE  f.FORMULA_NAME LIKE '%SALARY%'
  AND  SYSDATE BETWEEN f.EFFECTIVE_START_DATE AND f.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Esta é uma **view localizada** (_VL) — combina tabelas _B + _TL no idioma da sessão.
- Fast Formula é o motor de cálculo central do Oracle Fusion HCM.
- O `FORMULA_TEXT` contém o código fonte da fórmula em linguagem proprietária Oracle.
- Fórmulas podem ser globais (`LEGISLATION_CODE` nulo) ou específicas por país.

---

## 📚 Referências

- [Oracle Docs — FF_FORMULAS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ffformulasvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
