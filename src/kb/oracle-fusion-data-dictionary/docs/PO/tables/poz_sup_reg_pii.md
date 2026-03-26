---
id: DOC-PO-104
doc_type: system-doc
title: "POZ_SUP_REG_PII — Dados PII de Registro de Fornecedores"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: restricted
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - fornecedores
  - supplier-management
  - poz
aliases:
  - POZ_SUP_REG_PII
  - poz_sup_reg_pii
  - poz-sup-reg-pii
  - poz-sup
  - dados-pii-de-registro-de-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUP_REG_PII

## 📌 Visão Geral

Armazena **informacoes de identificacao pessoal (PII)** coletadas durante o registro de fornecedores. Contem dados sensiveis como CPF/CNPJ e documentos de identificacao.

> [!warning] Dados Sensiveis
> Esta tabela contem **PII**. Acesso deve ser restrito conforme LGPD.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro:** Captura de dados de identificacao no self-service registration.
- **Compliance KYC/AML:** Verificacao de identidade e due diligence.
- **Validacao fiscal:** Verificacao de CNPJ/CPF.
- **Auditoria regulatoria:** Rastreamento de PII (LGPD/GDPR).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REG_PII_ID | NUMBER(18) | NOT NULL | PK | ID unico do registro PII | — | 🟡 75% |
| 2 | SUPPLIER_REG_ID | NUMBER(18) | NOT NULL | FK | ID do registro de fornecedor | [[poz_up_requests]] | 🟡 70% |
| 3 | TAX_PAYER_ID | VARCHAR2(80) | NULL | PII | CNPJ/CPF | — | 🟡 75% |
| 4 | TAX_REGISTRATION_NUMBER | VARCHAR2(80) | NULL | PII | Registro fiscal | — | 🟡 75% |
| 5 | COUNTRY_CODE | VARCHAR2(10) | NULL | Classificacao | Pais do registro | — | 🟡 70% |
| 6 | PII_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de PII | — | 🟡 65% |
| 7 | PII_VALUE | VARCHAR2(240) | NULL | PII | Valor do dado pessoal | — | 🟡 65% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_up_requests]] — via `SUPPLIER_REG_ID` (registro de fornecedor com dados pessoais sensíveis)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Dados fiscais por registro
```sql
SELECT SUPPLIER_REG_ID, TAX_PAYER_ID, COUNTRY_CODE
FROM   POZ_SUP_REG_PII
WHERE  SUPPLIER_REG_ID = :p_reg_id;
```


---

## 🔒 Observações

- **LGPD/GDPR:** Requer politicas de retencao e anonimizacao.
- Acesso controlado por Oracle Data Masking ou roles especificas.
- Em nao-producao, dados devem ser obrigatoriamente mascarados.

---

## 📚 Referências

- [Oracle Docs — POZ_SUP_REG_PII](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
