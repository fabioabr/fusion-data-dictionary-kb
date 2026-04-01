---
id: DOC-PO-080
doc_type: system-doc
title: "POZ_CERTIFYING_AGENCIES — Agências Certificadoras de Fornecedores"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - fornecedores
  - certificacao
  - agencias
aliases:
  - POZ_CERTIFYING_AGENCIES
  - poz_certifying_agencies
  - agencias-certificadoras
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_CERTIFYING_AGENCIES

## 📌 Visão Geral

Armazena o cadastro de **agências certificadoras** que emitem e validam classificações de diversidade e certificações de fornecedores. Cada registro representa uma agência (governamental, privada ou setorial) que pode atestar classificações como Small Business, Minority-Owned, ISO, entre outras.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de certificações:** Cadastro de agências reconhecidas para validação de classificações de fornecedores.
- **Compliance de diversidade:** Identificação de quais agências são aceitas para certificar classificações de diversidade.
- **Qualificação de fornecedores:** Validação de que a certificação foi emitida por uma agência reconhecida.
- **Relatórios:** Análise de fornecedores por agência certificadora.
- **Setup de Procurement:** Configuração das agências aceitas pela organização.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CERTIFYING_AGENCY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da agência certificadora | — | 🟢 90% |
| 2 | AGENCY_NAME | VARCHAR2(240) | NOT NULL | Descrição | Nome da agência certificadora | — | 🟢 90% |
| 3 | AGENCY_CODE | VARCHAR2(30) | NULL | Identificação | Código da agência (abreviação) | — | 🟡 75% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Descrição | Descrição da agência e tipos de certificação que emite | — | 🟡 75% |
| 5 | COUNTRY_CODE | VARCHAR2(2) | NULL | Endereço | País da agência (código ISO) | — | 🟡 70% |
| 6 | AGENCY_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo: GOVERNMENT, PRIVATE, INDUSTRY | — | 🟡 65% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se a agência está ativa (Y/N) | — | 🟡 80% |
| 8 | START_DATE_ACTIVE | DATE | NULL | Data | Data de início da vigência | — | 🟡 70% |
| 9 | END_DATE_ACTIVE | DATE | NULL | Data | Data de término da vigência | — | 🟡 70% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 14 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma direta — tabela de referência independente

### Tabelas-filha (FK de saída)
- [[poz_bus_classifications]] — via `CERTIFYING_AGENCY_ID` (classificações certificadas por esta agência)
- [[poz_bus_class_reqs]] — via `CERTIFYING_AGENCY_ID` (requisitos de classificação em registro)

---

## 📎 Uso Típico

### Listar agências ativas
```sql
SELECT ca.CERTIFYING_AGENCY_ID, ca.AGENCY_NAME,
       ca.AGENCY_CODE, ca.COUNTRY_CODE
FROM   POZ_CERTIFYING_AGENCIES ca
WHERE  ca.ENABLED_FLAG = 'Y'
  AND  (ca.END_DATE_ACTIVE IS NULL OR ca.END_DATE_ACTIVE > SYSDATE)
ORDER BY ca.AGENCY_NAME;
```

### Fornecedores certificados por uma agência
```sql
SELECT s.VENDOR_NAME, bc.LOOKUP_CODE, bc.CERTIFICATION_NUM
FROM   POZ_BUS_CLASSIFICATIONS bc
JOIN   POZ_SUPPLIERS s ON s.VENDOR_ID = bc.VENDOR_ID
WHERE  bc.CERTIFYING_AGENCY_ID = :p_agency_id
  AND  (bc.EXPIRATION_DATE IS NULL OR bc.EXPIRATION_DATE > SYSDATE);
```

---

## 🔒 Observações

- Esta é uma tabela de **referência/setup** — geralmente populada durante a configuração inicial do módulo Procurement.
- Agências desabilitadas (`ENABLED_FLAG = 'N'`) não aparecem como opção na entrada de classificações, mas permanecem para histórico.
- Exemplos comuns de agências certificadoras: SBA (Small Business Administration), NMSDC (National Minority Supplier Development Council), WBENC (Women's Business Enterprise National Council).
- No contexto brasileiro, podem ser cadastradas agências como SEBRAE, BNDES ou certificadoras ISO.
- A tabela é compartilhada por todas as business units (não é multi-org).

---

## 🔗 PVOs Relacionados

### [[supplierbusinessclassificationextractpvo|SupplierBusinessClassificationExtractPVO]] (PO · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGENCY_ID | CertifyingAgencyAgencyId | ✅ |
| DESCRIPTION | CertifyingAgencyDescription | ✅ |
| END_DATE | CertifyingAgencyEndDate | ✅ |
| NAME | CertifyingAgencyName | ✅ |

### [[supplierregistrationbusclassreqpvo|SupplierRegistrationBusClassReqPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGENCY_ID | SupplierCertifyingAgenciesAgencyId | — |
| NAME | SupplierCertifyingAgenciesName | ✅ |

---

## 📚 Referências

- [Oracle Docs — POZ_CERTIFYING_AGENCIES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pozcertifyingagencies.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
