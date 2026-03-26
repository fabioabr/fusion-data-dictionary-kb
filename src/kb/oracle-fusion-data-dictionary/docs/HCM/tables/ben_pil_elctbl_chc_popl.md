---
id: DOC-HCM-053
doc_type: system-doc
title: "BEN_PIL_ELCTBL_CHC_POPL — População de Escolhas Elegíveis"
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
  - escolhas-elegiveis
  - electable-choices
aliases:
  - BEN_PIL_ELCTBL_CHC_POPL
  - ben_pil_elctbl_chc_popl
  - escolhas-elegiveis-beneficios
  - electable-choices-population
  - ben-pil-elctbl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PIL_ELCTBL_CHC_POPL

## 📌 Visão Geral

Armazena a **população de escolhas elegíveis** durante um evento de inscrição. Lista todas as opções de benefício disponíveis para cada participante elegível.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Apresentação de opções:** Lista de planos/opções disponíveis para o participante.
- **Self-service:** Alimenta a tela de inscrição com opções válidas.
- **Histórico:** Registra quais opções foram apresentadas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de população de escolhas elegíveis
```sql
SELECT * FROM BEN_PIL_ELCTBL_CHC_POPL
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (População de Escolhas Elegíveis).

---

## 📚 Referências

- [Oracle Docs — BEN_PIL_ELCTBL_CHC_POPL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benpil-elctblchcpopl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
