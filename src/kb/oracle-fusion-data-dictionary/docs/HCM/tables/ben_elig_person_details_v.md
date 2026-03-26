---
id: DOC-HCM-042
doc_type: system-doc
title: "BEN_ELIG_PERSON_DETAILS_V — Detalhes de Pessoa Elegível (View)"
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
  - benefits
  - detalhes-pessoa-elegivel
  - person-details-view
aliases:
  - BEN_ELIG_PERSON_DETAILS_V
  - ben_elig_person_details_v
  - detalhes-pessoa-elegivel
  - elig-person-details
  - ben-elig-person-details
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_ELIG_PERSON_DETAILS_V

## 📌 Visão Geral

View que consolida os **detalhes de elegibilidade** por pessoa, apresentando informações combinadas de múltiplas tabelas para facilitar a análise de elegibilidade.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta simplificada:** View pré-montada com dados de elegibilidade.
- **Relatórios:** Base para relatórios de elegibilidade por pessoa.
- **Self-service:** Alimenta telas de elegibilidade no portal.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_ELIG_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador | [[per_all_people_f]] | 🟡 80% |
| 3 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 4 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 5 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 6 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (quando aplicável)

### Tabelas-filha (FK de saída)
- Consultar documentação Oracle para tabelas-filha específicas.

---

## 📎 Uso Típico

### Consulta de detalhes de pessoa elegível (view)
```sql
SELECT * FROM BEN_ELIG_PERSON_DETAILS_V
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Detalhes de Pessoa Elegível (View)).

---

## 📚 Referências

- [Oracle Docs — BEN_ELIG_PERSON_DETAILS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/beneligpersondetailsv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
