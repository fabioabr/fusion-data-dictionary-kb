---
id: DOC-HCM-061
doc_type: system-doc
title: "BEN_PRTT_ENRT_RSLT — Resultados de Inscrição de Participante"
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
  - resultados-inscricao
  - enrollment-results
  - inscricao
aliases:
  - BEN_PRTT_ENRT_RSLT
  - ben_prtt_enrt_rslt
  - resultados-inscricao-beneficios
  - enrollment-results
  - ben-prtt-enrt-rslt
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PRTT_ENRT_RSLT

## 📌 Visão Geral

Armazena os **resultados de inscrição** em planos de benefício. Cada registro representa a inscrição efetiva de um participante em um plano/opção específica. É a **tabela transacional principal** do módulo Benefits.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Inscrições ativas:** Tabela central de inscrições em benefícios.
- **Histórico de cobertura:** Registra início/fim de cada inscrição.
- **Integração com folha:** Base para deduções de benefícios.
- **Self-service:** Alimenta a visão de benefícios do colaborador.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PRTT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de resultados de inscrição de participante
```sql
SELECT * FROM BEN_PRTT_ENRT_RSLT
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Resultados de Inscrição de Participante).

---

## 📚 Referências

- [Oracle Docs — BEN_PRTT_ENRT_RSLT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benprttenrtrslt.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
