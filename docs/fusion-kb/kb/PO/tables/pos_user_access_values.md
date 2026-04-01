---
id: DOC-PO-068
doc_type: system-doc
title: "POS_USER_ACCESS_VALUES — Valores de Acesso de Usuários do Portal de Fornecedores"
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
  - supplier-portal
  - acesso
  - seguranca
aliases:
  - POS_USER_ACCESS_VALUES
  - pos_user_access_values
  - acesso-usuarios-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POS_USER_ACCESS_VALUES

## 📌 Visão Geral

Armazena os **valores de acesso** atribuídos a usuários do portal de fornecedores (Oracle Supplier Portal). Define quais fornecedores, sites e funcionalidades cada usuário externo (representante do fornecedor) pode acessar no portal self-service.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle de acesso:** Definição granular de quais fornecedores e sites um usuário do portal pode visualizar e gerenciar.
- **Self-service do fornecedor:** Autorização para que representantes do fornecedor consultem POs, faturas, pagamentos e informações cadastrais.
- **Segregação de dados:** Garantia de que cada contato do fornecedor veja apenas os dados de seus fornecedores/sites autorizados.
- **Auditoria de segurança:** Rastreamento de quem tem acesso a quais dados no portal de fornecedores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | USER_ACCESS_VALUE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de acesso | — | 🟡 80% |
| 2 | USER_ID | NUMBER(18) | NOT NULL | FK | Identificador do usuário do portal | [[fnd_user]] | 🟡 75% |
| 3 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor autorizado | [[poz_suppliers]] | 🟡 80% |
| 4 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor autorizado (se granular) | [[poz_supplier_sites_all_m]] | 🟡 75% |
| 5 | ACCESS_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de acesso concedido (FULL, VIEW_ONLY, etc.) | — | 🟡 65% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o acesso está ativo (Y/N) | — | 🟡 75% |
| 7 | START_DATE | DATE | NULL | Data | Data de início da vigência do acesso | — | 🟡 70% |
| 8 | END_DATE | DATE | NULL | Data | Data de término da vigência do acesso | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[fnd_user]] — via `USER_ID` (usuário do sistema)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor cujo acesso do usuário portal é controlado)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)

### Tabelas-filha (FK de saída)
- Nenhuma direta

---

## 📎 Uso Típico

### Acessos ativos de um usuário do portal
```sql
SELECT uav.VENDOR_ID, uav.VENDOR_SITE_ID,
       uav.ACCESS_TYPE, uav.START_DATE, uav.END_DATE
FROM   POS_USER_ACCESS_VALUES uav
WHERE  uav.USER_ID = :p_user_id
  AND  uav.ENABLED_FLAG = 'Y'
  AND  (uav.END_DATE IS NULL OR uav.END_DATE >= SYSDATE);
```

### Todos os usuários com acesso a um fornecedor
```sql
SELECT uav.USER_ID, uav.ACCESS_TYPE
FROM   POS_USER_ACCESS_VALUES uav
WHERE  uav.VENDOR_ID = :p_vendor_id
  AND  uav.ENABLED_FLAG = 'Y';
```

---

## 🔒 Observações

- O acesso pode ser a nível de fornecedor (todos os sites) ou a nível de site específico.
- Acessos com `END_DATE` no passado são considerados expirados, mesmo que `ENABLED_FLAG = 'Y'`.
- Esta tabela é gerenciada pelo Oracle Supplier Portal; alterações diretas não são recomendadas.
- Integra com o modelo de segurança Oracle Fusion para garantir data-level security no portal self-service.

---

## 🔗 PVOs Relacionados

### [[supplieruseraccessvaluespvo|SupplierUserAccessValuesPVO]] (PO · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_CODE | AccessCode | ✅ |
| ACCESS_VALUE | AccessValue | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PER_PARTY_ID | PerPartyId | ✅ |

### [[supplieruserdataaccessvalueextractpvo|SupplierUserDataAccessValueExtractPVO]] (PO · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_CODE | AccessCode | ✅ |
| ACCESS_VALUE | AccessValue | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PER_PARTY_ID | PerPartyId | ✅ |

---

## 📚 Referências

- [Oracle Docs — POS Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/postables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
