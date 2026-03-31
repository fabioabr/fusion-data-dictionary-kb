---
id: DOC-HCM-546
doc_type: system-doc
title: "IRC_TP_PARTNER_PROVISNGS — Provisionamentos de Parceiros de Recrutamento"
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
  - tp-provisioning
  - provisionamento
  - irc-tp-provisngs
aliases:
  - IRC_TP_PARTNER_PROVISNGS
  - irc_tp_partner_provisngs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_TP_PARTNER_PROVISNGS

## 📌 Visão Geral

Registra os **provisionamentos** (habilitacoes de acesso) de parceiros terceirizados a requisicoes especificas. Controla quais vagas cada parceiro pode visualizar e submeter candidatos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Controle de acesso de parceiros a requisicoes especificas
- Provisionamento seletivo de vagas para agencias
- Auditoria de acesso de terceiros ao sistema

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROVISIONING_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do provisionamento | --- | 🟢 85% |
| 2 | PARTNER_ID | NUMBER(18) | NOT NULL | FK | ID do parceiro | IRC_TP_PARTNERS | 🟢 85% |
| 3 | REQUISITION_ID | NUMBER(18) | NULL | FK | ID da requisicao provisionada | IRC_REQUISITIONS_B | 🟢 85% |
| 4 | PROVISIONING_STATUS | VARCHAR2(30) | NULL | Classificacao | Status do provisionamento | --- | 🟡 70% |
| 5 | START_DATE | DATE | NULL | Vigencia | Data de inicio do acesso | --- | 🟡 70% |
| 6 | END_DATE | DATE | NULL | Vigencia | Data de fim do acesso | --- | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_tp_partners]] --- via `PARTNER_ID` (parceiro terceiro do provisionamento)
- [[irc_requisitions_b]] --- via `REQUISITION_ID` (requisição de vaga provisionada ao parceiro)

### Tabelas-filha (FK de saída)
- --- Tabela de associacao, sem filhas conhecidas

---

## 📎 Uso Típico

### Provisionamentos por requisicao
```sql
SELECT pp.PROVISIONING_ID, pp.PARTNER_ID, pp.REQUISITION_ID, pp.PROVISIONING_STATUS
FROM   IRC_TP_PARTNER_PROVISNGS pp
WHERE  pp.REQUISITION_ID = :p_requisition_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — IRC_TP_PARTNER_PROVISNGS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/irctppartnerprovisioning.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
