---
id: DOC-AR-024
doc_type: system-doc
title: "AR_TRANSMISSIONS_ALL — Transmissões de Remessa Bancária"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - transmissoes
  - remessa-bancaria
  - bank-remittance
aliases:
  - AR_TRANSMISSIONS_ALL
  - ar_transmissions_all
  - transmissoes-remessa-ar
  - bank-transmissions
  - remittance-transmissions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_TRANSMISSIONS_ALL

## 📌 Visão Geral

Armazena as **transmissões de remessa bancária** do módulo Accounts Receivable. Cada registro representa uma transmissão — o envio de um conjunto de recebimentos ao banco para processamento (depósito, compensação ou cobrança). Contém informações sobre a data, formato e status da transmissão, bem como a conta bancária de destino.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Remessa bancária:** Registro de cada envio de recebimentos ao banco para processamento.
- **Cobrança bancária:** Controle de transmissões de boletos e duplicatas para cobrança via banco.
- **Rastreamento de status:** Monitoramento do estado de cada transmissão (criada, enviada, processada).
- **Integração bancária:** Base para automação de envio de arquivos de remessa ao banco.
- **Auditoria:** Rastreabilidade completa de quando e para qual conta bancária os recebimentos foram transmitidos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TRANSMISSION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da transmissão | — | 🟢 100% |
| 2 | TRANSMISSION_NAME | VARCHAR2(60) | NOT NULL | Identificação | Nome da transmissão | — | 🟢 100% |
| 3 | TRANSMISSION_DATE | DATE | NOT NULL | Data | Data da transmissão | — | 🟢 100% |
| 4 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status da transmissão (CREATED/SUBMITTED/COMPLETED/ERROR) | — | 🟢 100% |
| 5 | REMIT_BANK_ACCT_USE_ID | NUMBER(18) | NULL | Bancário | Conta bancária de remessa | [[ce_bank_acct_uses_all]] | 🟢 100% |
| 6 | TRANSMISSION_FORMAT_ID | NUMBER(18) | NULL | Classificação | Formato de transmissão utilizado | — | 🟢 100% |
| 7 | REMIT_METHOD_CODE | VARCHAR2(30) | NULL | Classificação | Método de remessa (STANDARD/FACTORING) | — | 🟡 75% |
| 8 | RECEIPT_COUNT | NUMBER | NULL | Controle | Número de recebimentos na transmissão | — | 🟡 75% |
| 9 | RECEIPT_AMOUNT | NUMBER | NULL | Controle | Valor total dos recebimentos transmitidos | — | 🟡 75% |
| 10 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda da transmissão | — | 🟢 100% |
| 11 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre a transmissão | — | 🟡 75% |
| 12 | PROGRAM_APPLICATION_ID | NUMBER | NULL | Sistema | ID da aplicação do programa concorrente | — | 🟢 100% |
| 13 | PROGRAM_ID | NUMBER | NULL | Sistema | ID do programa concorrente que criou a transmissão | — | 🟢 100% |
| 14 | REQUEST_ID | NUMBER(18) | NULL | Sistema | ID do request concorrente | — | 🟢 100% |
| 15 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 20 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ce_bank_acct_uses_all]] — via `REMIT_BANK_ACCT_USE_ID` (conta bancária de remessa)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da transmissão bancária)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Transmissões por período
```sql
SELECT t.TRANSMISSION_NAME, t.TRANSMISSION_DATE, t.STATUS,
       t.RECEIPT_COUNT, t.RECEIPT_AMOUNT, t.CURRENCY_CODE
FROM   AR_TRANSMISSIONS_ALL t
WHERE  t.TRANSMISSION_DATE BETWEEN :start_date AND :end_date
  AND  t.ORG_ID = :p_org_id
ORDER BY t.TRANSMISSION_DATE DESC;
```

### Transmissões com erro
```sql
SELECT t.TRANSMISSION_NAME, t.TRANSMISSION_DATE, t.STATUS
FROM   AR_TRANSMISSIONS_ALL t
WHERE  t.STATUS = 'ERROR'
  AND  t.ORG_ID = :p_org_id;
```

---

## 🔒 Observações

- O campo `TRANSMISSION_FORMAT_ID` referencia o formato do arquivo de remessa bancária (e.g., CNAB 240/400 no Brasil, SEPA na Europa).
- Transmissões são tipicamente geradas por processos concorrentes (scheduled processes) — os campos `PROGRAM_ID` e `REQUEST_ID` permitem rastrear a origem.
- O status segue a progressão: **CREATED → SUBMITTED → COMPLETED**. O status **ERROR** indica falha no processamento.
- Cada transmissão está vinculada a uma única conta bancária de remessa.

---

## 🔗 PVOs Relacionados

### [[transmissionextractpvo|TransmissionExtractPVO]] (OTHER · BICC: 27/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | ArTransmissionAmount | ✅ |
| ATTRIBUTE1 | ArTransmissionAttribute1 | — |
| ATTRIBUTE10 | ArTransmissionAttribute10 | — |
| ATTRIBUTE11 | ArTransmissionAttribute11 | — |
| ATTRIBUTE12 | ArTransmissionAttribute12 | — |
| ATTRIBUTE13 | ArTransmissionAttribute13 | — |
| ATTRIBUTE14 | ArTransmissionAttribute14 | — |
| ATTRIBUTE15 | ArTransmissionAttribute15 | — |
| ATTRIBUTE2 | ArTransmissionAttribute2 | — |
| ATTRIBUTE3 | ArTransmissionAttribute3 | — |
| ATTRIBUTE4 | ArTransmissionAttribute4 | — |
| ATTRIBUTE5 | ArTransmissionAttribute5 | — |
| ATTRIBUTE6 | ArTransmissionAttribute6 | — |
| ATTRIBUTE7 | ArTransmissionAttribute7 | — |
| ATTRIBUTE8 | ArTransmissionAttribute8 | — |
| ATTRIBUTE9 | ArTransmissionAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArTransmissionAttributeCategory | — |
| COMMENTS | ArTransmissionComments | ✅ |
| COUNT | ArTransmissionCount1 | ✅ |
| CREATED_BY | ArTransmissionCreatedBy | ✅ |
| CREATION_DATE | ArTransmissionCreationDate | ✅ |
| DESTINATION | ArTransmissionDestination | ✅ |
| ERROR_COUNT | ArTransmissionErrorCount | ✅ |
| LAST_UPDATE_DATE | ArTransmissionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArTransmissionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArTransmissionLastUpdatedBy | ✅ |
| LATEST_REQUEST_ID | ArTransmissionLatestRequestId | ✅ |
| OBJECT_VERSION_NUMBER | ArTransmissionObjectVersionNumber | ✅ |
| ORG_ID | ArTransmissionOrgId | ✅ |
| ORIGIN | ArTransmissionOrigin | ✅ |
| REQUESTED_GL_DATE | ArTransmissionRequestedGlDate | ✅ |
| REQUESTED_LOCKBOX_ID | ArTransmissionRequestedLockboxId | ✅ |
| REQUESTED_TRANS_FORMAT_ID | ArTransmissionRequestedTransFormatId | ✅ |
| SCORING_MODEL_ID | ArTransmissionScoringModelId | ✅ |
| SOURCE_TYPE_FLAG | ArTransmissionSourceTypeFlag | ✅ |
| STATUS | ArTransmissionStatus | ✅ |
| TIME | ArTransmissionTime | ✅ |
| TRANS_DATE | ArTransmissionTransDate | ✅ |
| TRANSMISSION_ID | ArTransmissionTransmissionId | ✅ |
| TRANSMISSION_NAME | ArTransmissionTransmissionName | ✅ |
| TRANSMISSION_REQUEST_ID | ArTransmissionTransmissionRequestId | ✅ |
| VALIDATED_AMOUNT | ArTransmissionValidatedAmount | ✅ |
| VALIDATED_COUNT | ArTransmissionValidatedCount | ✅ |

---

## 📚 Referências

- [Oracle Docs — AR_TRANSMISSIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/artransmissionsall-25186.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
