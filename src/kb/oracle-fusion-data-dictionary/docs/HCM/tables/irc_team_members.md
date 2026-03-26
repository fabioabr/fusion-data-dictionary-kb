---
id: DOC-HCM-541
doc_type: system-doc
title: "IRC_TEAM_MEMBERS — Membros da Equipe de Recrutamento"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - team-members
  - equipe
  - irc-team-members
aliases:
  - IRC_TEAM_MEMBERS
  - irc_team_members
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_TEAM_MEMBERS

## 📌 Visão Geral

Armazena os **membros da equipe** de recrutamento associados a requisicoes. Define quais colaboradores (hiring manager, recrutador, entrevistadores) participam do processo seletivo de cada vaga.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao da equipe de selecao por requisicao
- Controle de acesso baseado em papel no processo seletivo
- Distribuicao de carga de trabalho entre recrutadores

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TEAM_MEMBER_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do membro | --- | 🟢 90% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | ID da requisicao associada | IRC_REQUISITIONS_B | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | ID do colaborador membro | PER_ALL_PEOPLE_F | 🟢 90% |
| 4 | MEMBER_ROLE | VARCHAR2(30) | NULL | Classificacao | Papel do membro (recruiter, hiring_manager, interviewer) | --- | 🟡 75% |
| 5 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Classificacao | Indica se eh o membro principal (Y/N) | --- | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_requisitions_b]] --- via `REQUISITION_ID` (requisiÃ§Ã£o de vaga do membro da equipe)
- [[per_all_people_f]] --- via `PERSON_ID` (pessoa membro da equipe de recrutamento)

### Tabelas-filha (FK de saída)
- --- Tabela de associacao, sem filhas diretas

---

## 📎 Uso Típico

### Equipe de recrutamento por requisicao
```sql
SELECT tm.PERSON_ID, tm.MEMBER_ROLE, tm.PRIMARY_FLAG
FROM   IRC_TEAM_MEMBERS tm
WHERE  tm.REQUISITION_ID = :p_requisition_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — IRC_TEAM_MEMBERS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircteammembers.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
