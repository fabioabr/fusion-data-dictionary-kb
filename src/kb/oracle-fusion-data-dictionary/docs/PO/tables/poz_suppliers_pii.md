---
id: DOC-PO-089
doc_type: system-doc
title: "POZ_SUPPLIERS_PII — Dados Sensíveis (PII) de Fornecedores"
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
  - suppliers-pii
  - dados-sensiveis
  - lgpd
  - compliance
aliases:
  - POZ_SUPPLIERS_PII
  - poz_suppliers_pii
  - dados-sensiveis-fornecedor
  - supplier-pii
  - pii-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIERS_PII

## Visão Geral

Armazena os **dados pessoais sensíveis (PII — Personally Identifiable Information)** de fornecedores no Oracle Fusion. Contém informações fiscais, documentos de identidade e dados tributários que são segregados da tabela principal `POZ_SUPPLIERS` por razões de segurança e compliance (LGPD, GDPR). O acesso a esta tabela deve ser restrito a usuários autorizados.

> [!warning] Dados Sensíveis
> Esta tabela contém **informações de identificação pessoal** (PII). O acesso deve ser controlado conforme a política de segurança da informação e legislação de proteção de dados (LGPD/GDPR).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Identificação fiscal:** Armazenamento de CNPJ/CPF, inscrição estadual e dados tributários do fornecedor.
- **Compliance fiscal:** Suporte a obrigações acessórias (SPED, EFD, DIRF) que requerem dados fiscais.
- **Due diligence:** Verificação de identidade e documentação do fornecedor durante o onboarding.
- **LGPD/GDPR:** Segregação de dados sensíveis para controle de acesso e gestão do ciclo de vida de dados pessoais.
- **Reporte regulatório:** Geração de relatórios fiscais que exigem número de identificação tributária.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do fornecedor (1:1 com POZ_SUPPLIERS) | [[poz_suppliers]] | 🟢 90% |
| 2 | TAX_PAYER_ID | VARCHAR2(80) | NULL | Fiscal | Número de identificação fiscal (CNPJ/CPF no Brasil, TIN nos EUA) | — | 🟡 80% |
| 3 | TAX_REGISTRATION_NUM | VARCHAR2(80) | NULL | Fiscal | Número de registro tributário | — | 🟡 75% |
| 4 | INDIVIDUAL_1099 | VARCHAR2(30) | NULL | Fiscal | Tipo de reporte 1099 (contexto US) | — | 🟡 65% |
| 5 | STATE_REPORTABLE_FLAG | VARCHAR2(1) | NULL | Fiscal | Sujeito a reporte estadual (Y/N) | — | 🟡 60% |
| 6 | FEDERAL_REPORTABLE_FLAG | VARCHAR2(1) | NULL | Fiscal | Sujeito a reporte federal (Y/N) | — | 🟡 60% |
| 7 | TAX_VERIFICATION_DATE | DATE | NULL | Fiscal | Data da última verificação fiscal | — | 🟡 60% |
| 8 | NAME_CONTROL | VARCHAR2(4) | NULL | Fiscal | Código de controle de nome (contexto US-IRS) | — | 🟡 55% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (relacionamento 1:1 com o cadastro principal)

### Tabelas relacionadas

---

## Uso Típico

### Consultar dados fiscais de um fornecedor (acesso restrito)
```sql
SELECT s.VENDOR_NAME, s.SEGMENT1,
       pii.TAX_PAYER_ID, pii.TAX_REGISTRATION_NUM
FROM   POZ_SUPPLIERS s
JOIN   POZ_SUPPLIERS_PII pii ON s.VENDOR_ID = pii.VENDOR_ID
WHERE  s.VENDOR_ID = :p_vendor_id;
```

### Fornecedores sem identificação fiscal
```sql
SELECT s.VENDOR_ID, s.SEGMENT1, s.VENDOR_NAME
FROM   POZ_SUPPLIERS s
LEFT JOIN POZ_SUPPLIERS_PII pii ON s.VENDOR_ID = pii.VENDOR_ID
WHERE  s.ENABLED_FLAG = 'Y'
  AND  (pii.TAX_PAYER_ID IS NULL OR pii.TAX_PAYER_ID = '');
```

---

## Observações

- A tabela mantém um relacionamento **1:1** com `POZ_SUPPLIERS` — cada fornecedor tem no máximo um registro PII.
- O campo `TAX_PAYER_ID` armazena o **CNPJ** (14 dígitos) para pessoas jurídicas ou **CPF** (11 dígitos) para pessoas físicas no contexto brasileiro.
- Esta tabela deve ter **acesso restrito** (data-level security) conforme políticas de LGPD/GDPR.
- Em extrações de dados (ETL/BICC), os campos PII devem ser **mascarados ou excluídos** dependendo do destino.
- O campo `confidentiality` do front matter está definido como `restricted` devido à natureza sensível dos dados.
- Valores como `INDIVIDUAL_1099` e `NAME_CONTROL` são específicos do contexto **US (IRS)** e podem não ser preenchidos em implementações brasileiras.

---

## Referências

- [Oracle Docs — POZ_SUPPLIERS_PII](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
