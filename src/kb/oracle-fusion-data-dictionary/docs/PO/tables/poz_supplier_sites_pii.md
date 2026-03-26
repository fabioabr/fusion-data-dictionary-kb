---
id: DOC-PO-096
doc_type: system-doc
title: "POZ_SUPPLIER_SITES_PII — Dados Sensíveis (PII) de Sites de Fornecedores"
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
  - supplier-sites-pii
  - dados-sensiveis
  - lgpd
  - compliance
aliases:
  - POZ_SUPPLIER_SITES_PII
  - poz_supplier_sites_pii
  - pii-sites-fornecedor
  - supplier-sites-pii
  - dados-sensiveis-sites
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIER_SITES_PII

## Visão Geral

Armazena os **dados pessoais sensíveis (PII) associados a sites de fornecedores** no Oracle Fusion. Contém informações fiscais e tributárias específicas por site/filial, segregadas da tabela principal `POZ_SUPPLIER_SITES_ALL_M` por razões de segurança e compliance (LGPD, GDPR).

> [!warning] Dados Sensíveis
> Esta tabela contém **informações de identificação pessoal/fiscal** (PII). O acesso deve ser controlado conforme a política de segurança da informação e legislação de proteção de dados (LGPD/GDPR).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Identificação fiscal por site:** CNPJ da filial, inscrição estadual, inscrição municipal por site.
- **Obrigações acessórias:** Dados fiscais por filial para SPED, EFD, NFe e outras obrigações.
- **Retenções tributárias:** Informações para cálculo de retenções na fonte (IR, PIS, COFINS, CSLL, ISS).
- **LGPD/GDPR:** Segregação de dados sensíveis com controle de acesso granular.
- **Compliance fiscal:** Validação de dados fiscais por site antes do processamento de pagamentos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_SITE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do site (1:1 com POZ_SUPPLIER_SITES_ALL_M) | [[poz_supplier_sites_all_m]] | 🟢 85% |
| 2 | TAX_PAYER_ID | VARCHAR2(80) | NULL | Fiscal | CNPJ da filial / CPF (no Brasil) | — | 🟡 75% |
| 3 | TAX_REGISTRATION_NUM | VARCHAR2(80) | NULL | Fiscal | Número de registro tributário por site | — | 🟡 70% |
| 4 | STATE_REPORTABLE_FLAG | VARCHAR2(1) | NULL | Fiscal | Sujeito a reporte estadual (Y/N) | — | 🟡 60% |
| 5 | FEDERAL_REPORTABLE_FLAG | VARCHAR2(1) | NULL | Fiscal | Sujeito a reporte federal (Y/N) | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (relacionamento 1:1 com o site)

### Tabelas relacionadas

---

## Uso Típico

### Dados fiscais de um site específico
```sql
SELECT ss.VENDOR_SITE_CODE, pii.TAX_PAYER_ID,
       pii.TAX_REGISTRATION_NUM
FROM   POZ_SUPPLIER_SITES_ALL_M ss
JOIN   POZ_SUPPLIER_SITES_PII pii ON ss.VENDOR_SITE_ID = pii.VENDOR_SITE_ID
WHERE  ss.VENDOR_ID = :p_vendor_id;
```

### Sites sem identificação fiscal
```sql
SELECT ss.VENDOR_ID, ss.VENDOR_SITE_ID, ss.VENDOR_SITE_CODE
FROM   POZ_SUPPLIER_SITES_ALL_M ss
LEFT JOIN POZ_SUPPLIER_SITES_PII pii ON ss.VENDOR_SITE_ID = pii.VENDOR_SITE_ID
WHERE  (pii.TAX_PAYER_ID IS NULL OR pii.TAX_PAYER_ID = '')
  AND  (ss.INACTIVE_DATE IS NULL OR ss.INACTIVE_DATE > SYSDATE);
```

---

## Observações

- A tabela mantém relacionamento **1:1** com `POZ_SUPPLIER_SITES_ALL_M` — cada site tem no máximo um registro PII.
- No contexto brasileiro, o `TAX_PAYER_ID` do site pode conter um **CNPJ diferente** do CNPJ da empresa-mãe (`POZ_SUPPLIERS_PII`), representando a filial.
- O campo `confidentiality` do front matter está definido como `restricted` devido à natureza sensível dos dados.
- Em extrações ETL/BICC, os campos PII devem ser **mascarados ou excluídos** dependendo do destino e das políticas de dados.
- A combinação de `POZ_SUPPLIERS_PII` (empresa) + `POZ_SUPPLIER_SITES_PII` (filial) fornece a visão completa de dados fiscais do fornecedor.

---

## Referências

- [Oracle Docs — Supplier Sites PII](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
