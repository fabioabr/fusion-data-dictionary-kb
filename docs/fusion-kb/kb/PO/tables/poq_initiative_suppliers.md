---
id: DOC-PO-042
doc_type: system-doc
title: "POQ_INITIATIVE_SUPPLIERS — Fornecedores em Iniciativas de Qualificação"
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
  - qualificacao
  - supplier-qualification
  - initiative-suppliers
aliases:
  - POQ_INITIATIVE_SUPPLIERS
  - poq_initiative_suppliers
  - fornecedores-iniciativa-qualificacao
  - initiative-suppliers
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_INITIATIVE_SUPPLIERS

## 📌 Visão Geral

Armazena a **associação entre fornecedores e iniciativas de qualificação**. Cada registro representa um fornecedor incluído em uma iniciativa específica, com seu respectivo status de avaliação. Funciona como tabela de interseção entre iniciativas e fornecedores no fluxo de Supplier Qualification Management.

> [!note] Tabela de interseção
> Esta tabela materializa o relacionamento N:N entre iniciativas de qualificação e fornecedores, adicionando atributos como status da avaliação e datas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de participantes:** Controle de quais fornecedores foram incluídos em cada iniciativa.
- **Acompanhamento de avaliação:** Status individual de cada fornecedor na iniciativa (pendente, em andamento, concluído).
- **Notificações:** Base para envio de questionários e convites de qualificação aos fornecedores.
- **Relatórios de cobertura:** Análise de quais fornecedores já foram avaliados e em quais iniciativas.
- **Auditoria de qualificação:** Registro histórico de participação de fornecedores em processos de qualificação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INITIATIVE_SUPPLIER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de associação | — | 🟢 90% |
| 2 | INITIATIVE_ID | NUMBER(18) | NOT NULL | FK | Iniciativa de qualificação | [[poq_initiatives]] | 🟢 95% |
| 3 | SUPPLIER_ID | NUMBER(18) | NOT NULL | FK | Fornecedor participante | [[poz_suppliers]] | 🟢 90% |
| 4 | SUPPLIER_SITE_ID | NUMBER(18) | NULL | FK | Site específico do fornecedor (quando aplicável) | [[poz_supplier_sites_all_m]] | 🟡 75% |
| 5 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status do fornecedor na iniciativa: PENDING, IN_PROGRESS, COMPLETED, DISQUALIFIED | — | 🟢 90% |
| 6 | QUALIFICATION_RESULT | VARCHAR2(30) | NULL | Classificação | Resultado da qualificação: QUALIFIED, NOT_QUALIFIED, CONDITIONAL | — | 🟡 75% |
| 7 | RESPONSE_DATE | DATE | NULL | Data | Data em que o fornecedor respondeu ao questionário | — | 🟡 70% |
| 8 | EVALUATION_DATE | DATE | NULL | Data | Data da avaliação/conclusão | — | 🟡 70% |
| 9 | EVALUATOR_ID | NUMBER(18) | NULL | Referência | Usuário que realizou a avaliação | — | 🟡 65% |
| 10 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre a qualificação do fornecedor | — | 🟡 75% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 16 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 17 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 18 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_initiatives]] — via `INITIATIVE_ID` (iniciativa de qualificação)
- [[poz_suppliers]] — via `SUPPLIER_ID` (fornecedor participante da iniciativa de qualificação)
- [[poz_supplier_sites_all_m]] — via `SUPPLIER_SITE_ID` (site do fornecedor)

### Tabelas-filha (FK de saída)
- Nenhuma identificada — esta é uma tabela de interseção folha.

---

## 📎 Uso Típico

### Fornecedores qualificados em uma iniciativa
```sql
SELECT isup.SUPPLIER_ID, sup.VENDOR_NAME,
       isup.STATUS_CODE, isup.QUALIFICATION_RESULT,
       isup.EVALUATION_DATE
FROM   POQ_INITIATIVE_SUPPLIERS isup
JOIN   POZ_SUPPLIERS sup ON sup.VENDOR_ID = isup.SUPPLIER_ID
WHERE  isup.INITIATIVE_ID = :p_initiative_id
  AND  isup.QUALIFICATION_RESULT = 'QUALIFIED';
```

### Fornecedores pendentes de avaliação
```sql
SELECT isup.SUPPLIER_ID, isup.STATUS_CODE
FROM   POQ_INITIATIVE_SUPPLIERS isup
WHERE  isup.INITIATIVE_ID = :p_initiative_id
  AND  isup.STATUS_CODE IN ('PENDING', 'IN_PROGRESS');
```

### Filtros comuns
- `STATUS_CODE = 'COMPLETED'` — Fornecedores com avaliação concluída
- `QUALIFICATION_RESULT = 'QUALIFIED'` — Fornecedores aprovados
- `QUALIFICATION_RESULT = 'NOT_QUALIFIED'` — Fornecedores reprovados

---

## 🔒 Observações

- Cada fornecedor pode aparecer apenas uma vez por iniciativa (constraint de unicidade esperada em `INITIATIVE_ID` + `SUPPLIER_ID`).
- O `STATUS_CODE` reflete o progresso da avaliação; o `QUALIFICATION_RESULT` é o resultado final.
- Quando `SUPPLIER_SITE_ID` está preenchido, a qualificação é a nível de site; quando nulo, é a nível de fornecedor.
- Esta tabela é consultada pelo Supplier Qualification dashboard para exibir progresso de cada iniciativa.

---

## 🔗 PVOs Relacionados

### [[initiativesupplierextractpvo|InitiativeSupplierExtractPVO]] (PO · BICC: 14/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| INIT_SUPPLIER_ID | InitSupplierId | ✅ |
| INITIATIVE_ID | InitiativeId | ✅ |
| INTERNAL_RESPONDER_ID | InternalResponderId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SEND_INT_QNNAIRE_FLAG | SendIntQnnaireFlag | ✅ |
| SEND_SUPP_QNNAIRE_FLAG | SendSuppQnnaireFlag | ✅ |
| SUPP_CONTACT_PARTY_ID | SuppContactPartyId | ✅ |
| SUPPLIER_ID | SupplierId | ✅ |
| SUPPLIER_SITE_ID | SupplierSiteId | ✅ |

### [[initiativesupplierpvo|InitiativeSupplierPVO]] (PO · BICC: 15/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InitiativeSupplierCreatedBy | ✅ |
| CREATION_DATE | InitiativeSupplierCreationDate | ✅ |
| INIT_SUPPLIER_ID | InitSupplierId | ✅ |
| INITIATIVE_ID | InitiativeSupplierInitiativeId | ✅ |
| INTERNAL_RESPONDER_ID | InitiativeSupplierInternalResponderId | ✅ |
| LAST_UPDATE_DATE | InitiativeSupplierLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InitiativeSupplierLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | InitiativeSupplierLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | InitiativeSupplierObjectVersionNumber | ✅ |
| RESPONSE_PULLED_FLAG | InitiativeSupplierResponsePulledFlag | ✅ |
| SEND_INT_QNNAIRE_FLAG | InitiativeSupplierSendIntQnnaireFlag | ✅ |
| SEND_SUPP_QNNAIRE_FLAG | InitiativeSupplierSendSuppQnnaireFlag | ✅ |
| SUPP_CONTACT_PARTY_ID | InitiativeSupplierSuppContactPartyId | ✅ |
| SUPPLIER_ID | InitiativeSupplierSupplierId | ✅ |
| SUPPLIER_SITE_ID | InitiativeSupplierSupplierSiteId | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
