---
id: DOC-HCM-121
doc_type: system-doc
title: "HNS_PERSONS — Pessoas em Saúde e Segurança"
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
  - health-safety
  - pessoas
  - testemunhas
  - hns
aliases:
  - HNS_PERSONS
  - hns_persons
  - hns-persons
  - DOC-HCM-121
  - pessoas-em-saúde-e-segurança
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_PERSONS

## 📌 Visão Geral

Armazena os **dados de pessoas** envolvidas em eventos de saúde e segurança — testemunhas, reportantes, responsáveis, etc. Complementa as informações de `PER_ALL_PEOPLE_F` com dados específicos de H&S.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de envolvidos:** Pessoas relacionadas a eventos de segurança.
- **Testemunhas:** Identificação de testemunhas de incidentes.
- **Responsáveis:** Designação de responsáveis por ações/investigações.
- **Compliance:** Documentação de todas as partes envolvidas.
- **Relatórios:** Análise de envolvimento por pessoa.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | HNS_PERSON_ID | NUMBER(18) | NOT NULL | PK | Identificador único no contexto H&S | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa no HR | [[per_all_people_f]] | 🟢 90% |
| 3 | INCIDENT_ID | NUMBER(18) | NULL | FK | Incidente associado | [[hns_incidents_detail]] | 🟡 80% |
| 4 | ROLE_TYPE | VARCHAR2(30) | NULL | Classificação | Papel da pessoa (WITNESS, REPORTER, RESPONSIBLE) | — | 🟡 75% |
| 5 | STATEMENT | VARCHAR2(4000) | NULL | Texto | Depoimento/declaração | — | 🟡 70% |
| 6 | CONTACT_INFO | VARCHAR2(240) | NULL | Contato | Informação de contato | — | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador envolvido no incidente)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente da pessoa envolvida)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Testemunhas de um incidente
```sql
SELECT p.PERSON_ID, p.ROLE_TYPE, p.STATEMENT
FROM   HNS_PERSONS p
WHERE  p.INCIDENT_ID = :p_incident_id
  AND  p.ROLE_TYPE = 'WITNESS';
```

### Pessoas envolvidas em incidentes
```sql
SELECT p.PERSON_ID, p.ROLE_TYPE, p.INCIDENT_ID
FROM   HNS_PERSONS p
WHERE  p.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- O `ROLE_TYPE` classifica o envolvimento: WITNESS, REPORTER, RESPONSIBLE, SUPERVISOR.
- O campo `STATEMENT` armazena depoimentos e declarações.
- Uma mesma pessoa pode aparecer em múltiplos incidentes com papéis diferentes.
- Para pessoas externas à organização, `PERSON_ID` pode ser nulo.

---

## 📚 Referências

- [Oracle Docs — HNS_PERSONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnspersons.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
