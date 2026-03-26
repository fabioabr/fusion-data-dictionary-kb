---
id: DOC-AR-010
doc_type: system-doc
title: "RA_REMIT_TOS_ALL — Endereços de Remessa para Pagamento"
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
  - remit-to
  - endereco-remessa
  - cobranca
aliases:
  - RA_REMIT_TOS_ALL
  - ra_remit_tos_all
  - enderecos-remessa-ar
  - remit-to-addresses
  - remit-tos-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_REMIT_TOS_ALL

## 📌 Visão Geral

Armazena os **endereços de remessa (remit-to addresses)** associados a transações do Accounts Receivable. Cada registro define um endereço para onde os clientes devem enviar seus pagamentos, sendo impresso em faturas e documentos de cobrança.

É uma tabela de **configuração de endereços de cobrança** — usada para controlar o destino de pagamento exibido nas faturas emitidas pela organização.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Impressão de faturas:** O endereço remit-to é impresso na fatura para orientar o cliente sobre onde enviar o pagamento.
- **Gestão de múltiplos endereços:** Organizações com várias filiais ou caixas postais podem manter endereços distintos por tipo de transação ou região.
- **Configuração de transações AR:** Cada transação em [[ra_customer_trx_all]] pode referenciar um endereço remit-to específico.
- **Compliance regulatório:** Endereços de remessa corretos são exigidos para conformidade fiscal e bancária.
- **Localização:** Suporte a endereços em múltiplos países para operações internacionais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REMIT_TO_ADDRESS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do endereço de remessa | — | 🟢 100% |
| 2 | ADDRESS1 | VARCHAR2(240) | NOT NULL | Endereço | Linha 1 do endereço (logradouro principal) | — | 🟢 100% |
| 3 | ADDRESS2 | VARCHAR2(240) | NULL | Endereço | Linha 2 do endereço (complemento) | — | 🟢 100% |
| 4 | ADDRESS3 | VARCHAR2(240) | NULL | Endereço | Linha 3 do endereço (informações adicionais) | — | 🟢 100% |
| 5 | ADDRESS4 | VARCHAR2(240) | NULL | Endereço | Linha 4 do endereço (informações adicionais) | — | 🟢 100% |
| 6 | CITY | VARCHAR2(60) | NULL | Endereço | Cidade | — | 🟢 100% |
| 7 | STATE | VARCHAR2(60) | NULL | Endereço | Estado/UF (usado em países com estados) | — | 🟢 100% |
| 8 | PROVINCE | VARCHAR2(60) | NULL | Endereço | Província (usado em países com províncias) | — | 🟢 100% |
| 9 | POSTAL_CODE | VARCHAR2(60) | NULL | Endereço | CEP/Código postal | — | 🟢 100% |
| 10 | COUNTRY | VARCHAR2(60) | NOT NULL | Endereço | Código do país (ISO 3166) | [[fnd_territories]] | 🟢 100% |
| 11 | STATUS | VARCHAR2(1) | NOT NULL | Classificação | Status ativo/inativo (A=Active, I=Inactive) | — | 🟢 100% |
| 12 | COUNTY | VARCHAR2(60) | NULL | Endereço | Condado/Município (localização granular) | — | 🟢 100% |
| 13 | ADDRESS_STYLE | VARCHAR2(30) | NULL | Configuração | Estilo de formatação do endereço (por país) | — | 🟢 100% |
| 14 | SITE_USE_ID | NUMBER(18) | NULL | Referência | Site de uso associado (se aplicável) | [[hz_cust_site_uses_all]] | 🟢 100% |
| 15 | LOCATION_ID | NUMBER(18) | NULL | Referência | ID de localização no HR/HCM | [[hr_locations_all]] | 🟢 100% |
| 16 | ADDRESS_KEY | VARCHAR2(500) | NULL | Identificação | Chave de endereço para deduplicação | — | 🟢 100% |
| 17 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 18 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 19 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 20 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 21 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 22 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 23 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 24 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[fnd_territories]] — via `COUNTRY` (país do endereço de remessa)
- [[hr_locations_all]] — via `LOCATION_ID` (localização do HR)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do endereço de remessa)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_all]] — via `REMIT_TO_ADDRESS_ID` (transações que usam este endereço)

---

## 📎 Uso Típico

### Consultar endereços de remessa ativos
```sql
SELECT rt.REMIT_TO_ADDRESS_ID, rt.ADDRESS1, rt.ADDRESS2,
       rt.CITY, rt.STATE, rt.POSTAL_CODE, rt.COUNTRY
FROM   RA_REMIT_TOS_ALL rt
WHERE  rt.STATUS = 'A'
  AND  rt.ORG_ID = :p_org_id
ORDER BY rt.CITY, rt.ADDRESS1;
```

### Identificar transações por endereço de remessa
```sql
SELECT ct.TRX_NUMBER, ct.TRX_DATE, ct.INVOICE_CURRENCY_CODE,
       rt.ADDRESS1, rt.CITY, rt.STATE
FROM   RA_CUSTOMER_TRX_ALL ct
JOIN   RA_REMIT_TOS_ALL rt ON rt.REMIT_TO_ADDRESS_ID = ct.REMIT_TO_ADDRESS_ID
WHERE  ct.ORG_ID = :p_org_id
  AND  ct.TRX_DATE BETWEEN :start_date AND :end_date;
```

### Filtros comuns
- `STATUS = 'A'` — Apenas endereços ativos
- `COUNTRY = 'BR'` — Endereços no Brasil
- `ORG_ID = :p_org_id` — Filtro por business unit

---

## 🔒 Observações

- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.
- O endereço remit-to é **impresso na fatura** — alterações afetam apenas faturas futuras, não as já emitidas.
- Em implementações brasileiras, os campos `ADDRESS1`–`ADDRESS4` são tipicamente mapeados para logradouro, número, complemento e bairro.
- O campo `COUNTRY` normalmente referencia o código ISO do território em `FND_TERRITORIES`.
- Organizações com operações internacionais podem ter múltiplos endereços remit-to, um por país ou região de operação.
- Desativar um endereço (`STATUS = 'I'`) não afeta transações já emitidas — apenas impede novas atribuições.

---

## 📚 Referências

- [Oracle Docs — RA_REMIT_TOS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/raremittosall-25268.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
