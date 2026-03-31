---
id: DOC-HCM-137
doc_type: system-doc
title: "HRA_DOC_TYPES_B — Tipos de Documento de Performance (Base)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - performance-management
  - doc-type
  - avaliacao
  - hra
aliases:
  - HRA_DOC_TYPES_B
  - hra_doc_types_b
  - hra-doc-types-b
  - DOC-HCM-137
  - tipos-de-documento-de-performance-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_DOC_TYPES_B

## 📌 Visão Geral

Armazena as **definições base** de tipos de documento de performance. Tabela _B (base language) contendo atributos não-traduzíveis como códigos, status e configurações estruturais.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de tipos de documento de performance:** Cadastro central de configurações.
- **Configuração estrutural:** Parâmetros base do registro.
- **Controle de versão:** Versionamento via `OBJECT_VERSION_NUMBER`.
- **Base para tradução:** Complementada por `HRA_DOC_TYPES_TL`.
- **Governança:** Configurações auditáveis e rastreáveis.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOC_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | CODE | VARCHAR2(30) | NULL | Identificação | Código do registro | — | 🟡 80% |
| 3 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 4 | EFFECTIVE_START_DATE | DATE | NULL | Data | Início de vigência | — | 🟡 80% |
| 5 | EFFECTIVE_END_DATE | DATE | NULL | Data | Fim de vigência | — | 🟡 80% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Número de versão do objeto | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhum relacionamento de entrada identificado até o momento.

### Tabelas-filha (FK de saída)
- [[hra_doc_types_tl]] — via `DOC_TYPE_ID` (traducoes multilingue do registro)

---

## 📎 Uso Típico

### Registros ativos
```sql
SELECT b.DOC_TYPE_ID, b.CODE, b.STATUS_CODE
FROM   HRA_DOC_TYPES_B b
WHERE  b.STATUS_CODE = 'ACTIVE';
```

### Com tradução
```sql
SELECT b.DOC_TYPE_ID, b.CODE, tl.NAME
FROM   HRA_DOC_TYPES_B b
JOIN   HRA_DOC_TYPES_TL tl ON b.DOC_TYPE_ID = tl.DOC_TYPE_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela _B (base) contém dados independentes de idioma.
- Para nomes traduzidos, juntar com `HRA_DOC_TYPES_TL` via `DOC_TYPE_ID`.
- O `OBJECT_VERSION_NUMBER` é usado para controle de concorrência otimista.
- Views _VL unem _B + _TL automaticamente para o idioma da sessão.

---

## 🔗 PVOs Relacionados

### [[documenttypepvo|DocumentTypePVO]] (HCM · BICC: 11/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | DocumentTypeBPEODateFrom | ✅ |
| DATE_TO | DocumentTypeBPEODateTo | ✅ |
| DOC_TYPE_ID | DocTypeId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SELECT_MGR_ALLOWED_FLAG | DocumentTypeBPEOSelectMgrAllowedFlag | ✅ |
| STATUS_CODE | DocumentTypeBPEOStatusCode | ✅ |

---

## 📚 Referências

- [Oracle Docs — HRA_DOC_TYPES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hradoctypesb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
