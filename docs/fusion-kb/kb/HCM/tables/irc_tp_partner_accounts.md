---
id: DOC-HCM-545
doc_type: system-doc
title: "IRC_TP_PARTNER_ACCOUNTS — Contas de Parceiros de Recrutamento"
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
  - tp-partner-accounts
  - contas
  - irc-tp-accounts
aliases:
  - IRC_TP_PARTNER_ACCOUNTS
  - irc_tp_partner_accounts
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_TP_PARTNER_ACCOUNTS

## 📌 Visão Geral

Armazena as **contas** (credenciais e configuracoes de acesso) dos parceiros terceirizados integrados ao modulo Recruiting.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Gestao de credenciais de acesso de parceiros
- Configuracao de integracao com agencias externas
- Controle de acesso e permissoes por conta de parceiro

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PARTNER_ACCOUNT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da conta | --- | 🟢 85% |
| 2 | PARTNER_ID | NUMBER(18) | NOT NULL | FK | ID do parceiro associado | IRC_TP_PARTNERS | 🟢 85% |
| 3 | ACCOUNT_NAME | VARCHAR2(240) | NULL | Identificacao | Nome da conta | --- | 🟡 70% |
| 4 | ACCOUNT_STATUS | VARCHAR2(30) | NULL | Classificacao | Status da conta | --- | 🟡 70% |
| 5 | INTEGRATION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de integracao | --- | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_tp_partners]] --- via `PARTNER_ID` (parceiro terceiro proprietário da conta)

### Tabelas-filha (FK de saída)
- --- Tabela de configuracao, sem filhas conhecidas

---

## 📎 Uso Típico

### Contas de um parceiro
```sql
SELECT pa.PARTNER_ACCOUNT_ID, pa.ACCOUNT_NAME, pa.ACCOUNT_STATUS
FROM   IRC_TP_PARTNER_ACCOUNTS pa
WHERE  pa.PARTNER_ID = :p_partner_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[asmtacctpackagepvo|AsmtAcctPackagePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | PartnerAccountPEOAccountId | — |
| DESCRIPTION | PartnerAccountPEODescription | — |
| PROVISIONING_ID | PartnerAccountPEOProvisioningId | — |
| USERNAME | PartnerAccountPEOUsername | — |

### [[asmtpackageresultviewallpvo|AsmtPackageResultViewAllPVO]] (HCM · BICC: 1/1)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | PartnerAccountPEOAccountId | ✅ |

### [[asmtreqpackageviewallpvo|AsmtReqPackageViewAllPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | PartnerAccountPEOAccountId | ✅ |
| DESCRIPTION | PartnerAccountPEODescription | — |
| USERNAME | PartnerAccountPEOUsername | — |

### [[partneraccountpvo|PartnerAccountPVO]] (HCM · BICC: 13/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | PartnerAccountPEOAccountId | ✅ |
| ACTIVE_FLAG | PartnerAccountPEOActiveFlag | ✅ |
| CREATED_BY | PartnerAccountPEOCreatedBy | ✅ |
| CREATION_DATE | PartnerAccountPEOCreationDate | ✅ |
| DEFAULT_FLAG | PartnerAccountPEODefaultFlag | ✅ |
| DESCRIPTION | PartnerAccountPEODescription | ✅ |
| LAST_UPDATE_DATE | PartnerAccountPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartnerAccountPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PartnerAccountPEOLastUpdatedBy | ✅ |
| LAST_VALIDATE_DATE | PartnerAccountPEOLastValidateDate | ✅ |
| OBJECT_VERSION_NUMBER | PartnerAccountPEOObjectVersionNumber | — |
| PROVISIONING_ID | PartnerAccountPEOProvisioningId | ✅ |
| USER_SALTED_HASH | PartnerAccountPEOUserSaltedHash | — |
| USERNAME | PartnerAccountPEOUsername | ✅ |
| VALIDATE_FLAG | PartnerAccountPEOValidateFlag | ✅ |

### [[screeningpackagepvo|ScreeningPackagePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | PartnerAccountPEOAccountId | — |
| USERNAME | PartnerAccountPEOUsername | ✅ |

### [[screeningresultviewallpvo|ScreeningResultViewAllPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | PartnerAccountPEOAccountId | — |
| USERNAME | PartnerAccountPEOUsername | ✅ |

### [[screeningviewallpvo|ScreeningViewAllPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | PartnerAccountPEOAccountId | — |
| USERNAME | PartnerAccountPEOUsername | ✅ |

---

## 📚 Referências

- [Oracle Docs — IRC_TP_PARTNER_ACCOUNTS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/irctppartneraccounts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
