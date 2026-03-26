---
id: DOC-HCM-025
doc_type: system-doc
title: "BEN_BENEFIT_RELATIONS_F — Relações de Benefício"
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
  - relacoes-beneficio
  - benefit-relations
aliases:
  - BEN_BENEFIT_RELATIONS_F
  - ben_benefit_relations_f
  - relacoes-beneficio-hcm
  - benefit-relations
  - ben-benefit-relations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BENEFIT_RELATIONS_F

## 📌 Visão Geral

Armazena as **relações de benefício** que vinculam colaboradores ao sistema de benefícios. Cada registro representa a relação de um participante com o programa de benefícios, com datas de vigência.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Elegibilidade base:** Estabelece a relação do colaborador com o sistema de benefícios.
- **Histórico de participação:** Controle de vigência da participação.
- **Base para inscrições:** Pré-requisito para inscrição em planos específicos.
- **Integração com folha:** Vinculação com deduções de benefícios na folha.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BENEFIT_RELATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da relação | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 95% |
| 3 | PGM_ID | NUMBER(18) | NULL | FK | Programa de benefícios | [[ben_pgm_f]] | 🟡 80% |
| 4 | RELATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de relação (EMPLOYEE, DEPENDENT, etc.) | — | 🟡 75% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do vinculo de beneficio)
- [[ben_pgm_f]] — via `PGM_ID` (programa de beneficios do vinculo)

### Tabelas-filha (FK de saída)
- [[ben_per_in_ler]] — via `BENEFIT_RELATION_ID` (eventos de vida)
- [[ben_prtt_enrt_rslt]] — via `BENEFIT_RELATION_ID` (inscricoes em planos do beneficio)

---

## 📎 Uso Típico

### Relações ativas de benefício
```sql
SELECT br.BENEFIT_RELATION_ID, br.PERSON_ID, br.RELATION_TYPE
FROM   BEN_BENEFIT_RELATIONS_F br
WHERE  SYSDATE BETWEEN br.EFFECTIVE_START_DATE AND br.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Vigentes

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigência.
- A relação de benefício é o vínculo base; inscrições específicas estão em `BEN_PRTT_ENRT_RSLT`.
- Pode incluir tanto funcionários quanto dependentes.

---

## 📚 Referências

- [Oracle Docs — BEN_BENEFIT_RELATIONS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbenefitrelationsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
