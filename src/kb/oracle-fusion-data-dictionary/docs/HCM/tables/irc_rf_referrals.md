---
id: DOC-HCM-528
doc_type: system-doc
title: "IRC_RF_REFERRALS — Indicacoes de Candidatos (Referrals)"
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
  - referrals
  - indicacoes
  - irc-referrals
aliases:
  - IRC_RF_REFERRALS
  - irc_rf_referrals
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_RF_REFERRALS

## 📌 Visão Geral

Armazena as **indicacoes (referrals)** realizadas por colaboradores para vagas em aberto. Cada registro conecta um colaborador referenciador a um candidato indicado.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Programa de indicacao de candidatos por colaboradores
- Rastreamento de origem de candidatos por indicacao
- Calculo de bonificacoes por indicacao bem-sucedida

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REFERRAL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da indicacao | --- | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | ID do colaborador que indicou | PER_ALL_PEOPLE_F | 🟢 85% |
| 3 | CANDIDATE_ID | NUMBER(18) | NULL | FK | ID do candidato indicado | IRC_CANDIDATES | 🟢 85% |
| 4 | REQUISITION_ID | NUMBER(18) | NULL | FK | ID da requisicao associada | IRC_REQUISITIONS_B | 🟢 85% |
| 5 | REFERRAL_DATE | DATE | NULL | Dados | Data da indicacao | --- | 🟡 75% |
| 6 | REFERRAL_STATUS | VARCHAR2(30) | NULL | Classificacao | Status da indicacao | --- | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] --- via `PERSON_ID` (pessoa que fez a indicacao)
- [[irc_candidates]] --- via `CANDIDATE_ID` (candidato indicado na referencia)
- [[irc_requisitions_b]] --- via `REQUISITION_ID` (requisicao da indicacao)

### Tabelas-filha (FK de saída)
- --- Tabelas de submissao e candidatura do Recruiting

---

## 📎 Uso Típico

### Indicacoes por requisicao
```sql
SELECT rf.REFERRAL_ID, rf.PERSON_ID, rf.CANDIDATE_ID, rf.REFERRAL_DATE
FROM   IRC_RF_REFERRALS rf
WHERE  rf.REQUISITION_ID = :p_requisition_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — IRC_RF_REFERRALS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircrfreferrals.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
