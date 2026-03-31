---
id: DOC-HCM-662
doc_type: system-doc
title: "PER_GRADE_LADDERS_F — Escadas Salariais"
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
  - escadas-salariais
  - grade-ladders
aliases:
  - PER_GRADE_LADDERS_F
  - per_grade_ladders_f
  - per-grade-ladders-f
  - escadas-salariais
  - per-grade-ladders-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_GRADE_LADDERS_F

## 📌 Visão Geral

Armazena as **escadas (ladders) salariais** da organização, com vigência temporal. Uma escada define uma sequência ordenada de grades que representam uma trilha de carreira.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Trilhas de carreira** — define os caminhos de progressão salarial.
- **Planejamento de carreira** — visualização das possibilidades de evolução.
- **Políticas de remuneração** — estruturação da política de grades e faixas.
- **Relatórios de compensação** — análise da estrutura salarial por escada.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRADE_LADDER_ID | NUMBER(18) | NOT NULL | PK | Identificador único da escada | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | BUSINESS_GROUP_ID | NUMBER(18) | NOT NULL | FK | Grupo de negócio | — | 🟢 90% |
| 5 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Status | Se está ativa (Y/N) | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de escadas salariais.

### Tabelas-filha (FK de saída)
- [[per_grade_ladders_f_tl]] — via `GRADE_LADDER_ID` (traduções da escala de grades salariais)
- [[per_grades_in_ladders_f]] — via `GRADE_LADDER_ID` (grades na escada)

---

## 📎 Uso Típico

### Escadas salariais ativas
```sql
SELECT pgl.GRADE_LADDER_ID, pgl.ACTIVE_FLAG
FROM   PER_GRADE_LADDERS_F pgl
WHERE  pgl.ACTIVE_FLAG = 'Y'
  AND  SYSDATE BETWEEN pgl.EFFECTIVE_START_DATE AND pgl.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ACTIVE_FLAG = 'Y'` — Escadas ativas
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Cada escada contém uma sequência ordenada de grades via PER_GRADES_IN_LADDERS_F.
- Escadas representam trilhas de carreira (ex.: Técnica, Gerencial, Especialista).
---

## 📚 Referências

- [Oracle Docs — PER_GRADE_LADDERS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pergradeladdersf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
