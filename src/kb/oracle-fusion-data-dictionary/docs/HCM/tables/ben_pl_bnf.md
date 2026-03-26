---
id: DOC-HCM-054
doc_type: system-doc
title: "BEN_PL_BNF — Beneficiários por Plano"
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
  - beneficiarios-plano
  - plan-beneficiary
aliases:
  - BEN_PL_BNF
  - ben_pl_bnf
  - beneficiarios-plano-beneficios
  - plan-beneficiary
  - ben-pl-bnf
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PL_BNF

## 📌 Visão Geral

Armazena os **beneficiários designados** a nível de plano de benefício, com percentuais de distribuição.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Designação por plano:** Beneficiários específicos para cada plano.
- **Distribuição:** Percentuais e prioridades entre beneficiários.
- **Seguro de vida:** Primário vs. contingente.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de beneficiários por plano
```sql
SELECT * FROM BEN_PL_BNF
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Beneficiários por Plano).

---

## 📚 Referências

- [Oracle Docs — BEN_PL_BNF](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benplbnf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
