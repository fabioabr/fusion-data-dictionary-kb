---
id: DOC-HCM-544
doc_type: system-doc
title: "IRC_TP_PARTNERS — Parceiros Terceirizados de Recrutamento"
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
  - tp-partners
  - parceiros
  - irc-tp-partners
aliases:
  - IRC_TP_PARTNERS
  - irc_tp_partners
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_TP_PARTNERS

## 📌 Visão Geral

Armazena os **parceiros terceirizados** (agencias de recrutamento, job boards, provedores de background check, etc.) cadastrados no modulo Recruiting.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Cadastro de agencias de recrutamento e parceiros
- Gestao de contratos e acesso de parceiros externos
- Rastreamento de candidatos por agencia de origem

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PARTNER_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do parceiro | --- | 🟢 90% |
| 2 | PARTNER_NAME | VARCHAR2(240) | NOT NULL | Identificacao | Nome do parceiro | --- | 🟢 85% |
| 3 | CATEGORY_ID | NUMBER(18) | NULL | FK | ID da categoria do parceiro | IRC_TP_CATEGORIES_B | 🟢 85% |
| 4 | PARTNER_STATUS | VARCHAR2(30) | NULL | Classificacao | Status do parceiro (ativo, inativo) | --- | 🟡 75% |
| 5 | CONTACT_EMAIL | VARCHAR2(240) | NULL | Dados | Email de contato do parceiro | --- | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_tp_categories_b]] --- via `CATEGORY_ID` (categoria do parceiro terceiro de recrutamento)

### Tabelas-filha (FK de saída)
- [[irc_tp_partner_accounts]] --- via `PARTNER_ID` (contas do parceiro terceiro de recrutamento)
- [[irc_tp_partner_provisngs]] --- via `PARTNER_ID` (provisionamentos do parceiro terceiro)

---

## 📎 Uso Típico

### Parceiros ativos
```sql
SELECT p.PARTNER_ID, p.PARTNER_NAME, p.PARTNER_STATUS
FROM   IRC_TP_PARTNERS p
WHERE  p.PARTNER_STATUS = 'ACTIVE';
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[asmtpackageresultviewallpvo|AsmtPackageResultViewAllPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[asmtreqpackageviewallpvo|AsmtReqPackageViewAllPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[jobposthistorypvo|JobPostHistoryPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[jobposthistoryviewallpvo|JobPostHistoryViewAllPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[jobpostingpvo|JobPostingPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[jobpostingviewallpvo|JobPostingViewAllPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[jobpostresultpvo|JobPostResultPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PatnerPEOPartnerId | ✅ |

### [[jobpostresultviewallpvo|JobPostResultViewAllPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PatnerPEOPartnerId | ✅ |

### [[partneraccountpvo|PartnerAccountPVO]] (HCM · BICC: 8/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PartnerPEOCreatedBy | ✅ |
| CREATION_DATE | PartnerPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | PartnerPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartnerPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PartnerPEOLastUpdatedBy | ✅ |
| LOGO | PartnerPEOLogo | — |
| NAME | PartnerPEOName | ✅ |
| OBJECT_VERSION_NUMBER | PartnerPEOObjectVersionNumber | — |
| PARTNER_GUID | PartnerPEOPartnerGuid | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[partnerprovisionpvo|PartnerProvisionPVO]] (HCM · BICC: 8/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PartnerPEOCreatedBy | ✅ |
| CREATION_DATE | PartnerPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | PartnerPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartnerPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PartnerPEOLastUpdatedBy | ✅ |
| LOGO | PartnerPEOLogo | — |
| NAME | PartnerPEOName | ✅ |
| OBJECT_VERSION_NUMBER | PartnerPEOObjectVersionNumber | — |
| PARTNER_GUID | PartnerPEOPartnerGuid | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[partnerpvo|PartnerPVO]] (HCM · BICC: 8/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PartnerPEOCreatedBy | ✅ |
| CREATION_DATE | PartnerPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | PartnerPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartnerPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PartnerPEOLastUpdatedBy | ✅ |
| LOGO | PartnerPEOLogo | — |
| NAME | PartnerPEOName | ✅ |
| OBJECT_VERSION_NUMBER | PartnerPEOObjectVersionNumber | — |
| PARTNER_GUID | PartnerPEOPartnerGuid | ✅ |
| PARTNER_ID | PartnerId | ✅ |

### [[screeningpackagepvo|ScreeningPackagePVO]] (AP · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[screeningresultviewallpvo|ScreeningResultViewAllPVO]] (AP · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

### [[screeningviewallpvo|ScreeningViewAllPVO]] (AP · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | PartnerPEOName | ✅ |
| PARTNER_ID | PartnerPEOPartnerId | ✅ |

---

## 📚 Referências

- [Oracle Docs — IRC_TP_PARTNERS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/irctppartners.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
