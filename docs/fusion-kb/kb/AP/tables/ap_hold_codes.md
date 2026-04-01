---
id: DOC-AP-008
doc_type: system-doc
title: "AP_HOLD_CODES — Códigos de Retenção (Hold Codes) de Contas a Pagar"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, hold-codes, codigos-retencao, bloqueios, configuracao]
aliases: [AP_HOLD_CODES, ap_hold_codes, hold_codes_ap, codigos_hold_ap, tipos_retencao_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_HOLD_CODES

## Visão Geral

Tabela de definição dos códigos de retenção (hold codes) disponíveis no módulo de Contas a Pagar. Cada registro representa um tipo de hold que pode ser aplicado a faturas, definindo seu nome, descrição, tipo (manual ou automático) e se pode ser liberado por usuários específicos. É uma tabela de configuração/lookup que alimenta `AP_HOLDS_ALL`.

## Propósito de Negócio

Os hold codes padronizam os motivos de bloqueio de faturas, garantindo consistência na classificação de problemas. No Banco Patria, permitem que a equipe financeira identifique rapidamente a natureza do bloqueio (preço, quantidade, documento, aprovação) e direcione a resolução ao responsável correto. Também alimentam relatórios gerenciais de eficiência no processamento de faturas.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | HOLD_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | PK | Chave primária. Código do tipo de hold (ex.: PRICE, QTY_REC, AMOUNT). | — | 🟢 100% |
| 2 | HOLD_TYPE | VARCHAR2(25) | NOT NULL | Classificação | Tipo de hold: MATCHING, VARIANCE, MANUAL, INSUFFICIENT FUNDS, etc. | — | 🟢 95% |
| 3 | DESCRIPTION | VARCHAR2(80) | NULL | Negócio | Descrição do código de hold. | — | 🟢 95% |
| 4 | USER_RELEASEABLE_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o hold pode ser liberado manualmente (Y/N). | — | 🟢 90% |
| 5 | INITIATE_WORKFLOW_FLAG | VARCHAR2(1) | NULL | Controle | Indica se o hold dispara workflow de aprovação (Y/N). | — | 🟡 70% |
| 6 | WAIT_BEFORE_NOTIFY_DAYS | NUMBER(5) | NULL | Negócio | Dias de espera antes de notificar sobre o hold pendente. | — | 🟡 65% |
| 7 | INACTIVE_DATE | DATE | NULL | Controle | Data de inativação do código de hold. | — | 🟢 90% |
| 8 | POSTABLE_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se faturas com este hold podem ser contabilizadas (Y/N). | — | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 10 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- Nenhuma FK direta conhecida. Tabela raiz de configuração.

### Tabelas-filha

- **[[ap_holds_all]]** — Holds aplicados a faturas que referenciam este código (via `HOLD_LOOKUP_CODE`).

## Uso Típico

```sql
-- Listar hold codes ativos e liberáveis por usuário
SELECT hc.HOLD_LOOKUP_CODE,
       hc.HOLD_TYPE,
       hc.DESCRIPTION,
       hc.USER_RELEASEABLE_FLAG,
       hc.POSTABLE_FLAG
  FROM AP_HOLD_CODES hc
 WHERE (hc.INACTIVE_DATE IS NULL OR hc.INACTIVE_DATE > SYSDATE)
 ORDER BY hc.HOLD_TYPE, hc.HOLD_LOOKUP_CODE;
```

## Observações

- Hold codes com `USER_RELEASEABLE_FLAG = 'N'` só podem ser liberados pelo sistema (ex.: após correção da discrepância de matching).
- O campo `POSTABLE_FLAG` controla se a fatura pode ser contabilizada mesmo com o hold ativo — importante para provisões contábeis.
- Códigos seeded (pré-configurados pela Oracle) não devem ser modificados; criar códigos customizados para necessidades específicas.
- Holds do tipo MATCHING são geralmente automáticos; holds MANUAL são criados por usuários.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle BICC — AP Hold Codes Configuration Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[approvalcodeextractpvo|ApprovalCodeExtractPVO]] (OTHER · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ApHoldCodesCreatedBy | ✅ |
| CREATION_DATE | ApHoldCodesCreationDate | ✅ |
| EXTERNAL_DESCRIPTION | ApHoldCodesExternalDescription | ✅ |
| HOLD_INSTRUCTION | ApHoldCodesHoldInstruction | ✅ |
| HOLD_LOOKUP_CODE | ApHoldCodesHoldLookupCode | ✅ |
| HOLD_TYPE | ApHoldCodesHoldType | ✅ |
| INACTIVE_DATE | ApHoldCodesInactiveDate | ✅ |
| INITIATE_WORKFLOW_FLAG | ApHoldCodesInitiateWorkflowFlag | ✅ |
| LAST_UPDATE_DATE | ApHoldCodesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApHoldCodesLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ApHoldCodesLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ApHoldCodesObjectVersionNumber | ✅ |
| POSTABLE_FLAG | ApHoldCodesPostableFlag | ✅ |
| REMINDER_DAYS | ApHoldCodesReminderDays | ✅ |
| USER_RELEASEABLE_FLAG | ApHoldCodesUserReleaseableFlag | ✅ |
| USER_UPDATEABLE_FLAG | ApHoldCodesUserUpdateableFlag | ✅ |
| WAIT_BEFORE_NOTIFY_DAYS | ApHoldCodesWaitBeforeNotifyDays | ✅ |

### [[approvalcodepvo|ApprovalCodePVO]] (AP · BICC: 7/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ApHoldCodesCreatedBy | ✅ |
| CREATION_DATE | ApHoldCodesCreationDate | ✅ |
| EXTERNAL_DESCRIPTION | ApHoldCodesExternalDescription | — |
| HOLD_INSTRUCTION | ApHoldCodesHoldInstruction | — |
| HOLD_LOOKUP_CODE | HoldLookupCode | ✅ |
| HOLD_TYPE | ApHoldCodesHoldType | ✅ |
| INACTIVE_DATE | ApHoldCodesInactiveDate | ✅ |
| INITIATE_WORKFLOW_FLAG | ApHoldCodesInitiateWorkflowFlag | — |
| LAST_UPDATE_DATE | ApHoldCodesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApHoldCodesLastUpdateLogin | — |
| LAST_UPDATED_BY | ApHoldCodesLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ApHoldCodesObjectVersionNumber | — |
| POSTABLE_FLAG | ApHoldCodesPostableFlag | — |
| REMINDER_DAYS | ApHoldCodesReminderDays | — |
| USER_RELEASEABLE_FLAG | ApHoldCodesUserReleaseableFlag | — |
| USER_UPDATEABLE_FLAG | ApHoldCodesUserUpdateableFlag | — |
| WAIT_BEFORE_NOTIFY_DAYS | ApHoldCodesWaitBeforeNotifyDays | — |
