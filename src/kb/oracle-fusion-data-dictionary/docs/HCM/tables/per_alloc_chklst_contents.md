---
id: DOC-HCM-624
doc_type: system-doc
title: "PER_ALLOC_CHKLST_CONTENTS — Conteúdos de Checklists Alocados"
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
  - workforce-management
  - checklists
  - conteudos
aliases:
  - PER_ALLOC_CHKLST_CONTENTS
  - per_alloc_chklst_contents
  - per-alloc-chklst-contents
  - conteúdos-de-checklists-alocados
  - per-alloc-chklst-con
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALLOC_CHKLST_CONTENTS

## 📌 Visão Geral

Armazena os **conteúdos e materiais** associados a checklists alocados. Define links, documentos ou informações adicionais disponibilizados ao colaborador durante a execução do checklist.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Material de suporte** — links para documentos, vídeos e guias de referência.
- **Onboarding** — conteúdos informativos para novos colaboradores.
- **Personalização** — conteúdos específicos por instância de checklist.
- **Base de conhecimento** — centralização de materiais de apoio.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOC_CHKLST_CONTENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do conteúdo | — | 🟢 90% |
| 2 | ALLOCATED_CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Checklist associado | PER_ALLOCATED_CHECKLISTS | 🟢 90% |
| 3 | CONTENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de conteúdo (URL, DOCUMENT, TEXT) | — | 🟡 75% |
| 4 | CONTENT_URL | VARCHAR2(2000) | NULL | Conteúdo | URL do recurso | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_allocated_checklists]] — via `ALLOCATED_CHECKLIST_ID` (checklist ao qual pertence o conteúdo)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Conteúdos de um checklist
```sql
SELECT pcc.CONTENT_TYPE, pcc.CONTENT_URL
FROM   PER_ALLOC_CHKLST_CONTENTS pcc
WHERE  pcc.ALLOCATED_CHECKLIST_ID = :p_checklist_id;
```

### Filtros comuns
- `CONTENT_TYPE = 'URL'` — Conteúdos do tipo link
---

## 🔒 Observações

- Conteúdos são adicionados por instância de checklist — podem ser personalizados.
- Links para portais internos, vídeos de treinamento e documentos são usos comuns.
---

## 🔗 PVOs Relacionados

### [[allocatedchecklistspvo|AllocatedChecklistsPVO]] (HCM · BICC: 12/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE1AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE2AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE3AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE4AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE5AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPEAllocChklstContentId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE1AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE2AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE3AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE4AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE5AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPEOAllocatedChecklistId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE1ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE2ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE3ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE4ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE5ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPEChecklistContentId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE1ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE2ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE3ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE4ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE5ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPEOChkContentDefnId | — |
| CONTENT_TYPE | AllocatedChecklistContentsPE1ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPE2ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPE3ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPE4ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPE5ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPEOContentType | ✅ |
| CREATED_BY | AllocatedChecklistContentsPE1CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPE2CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPE3CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPE4CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPE5CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPEOCreatedBy | — |
| CREATION_DATE | AllocatedChecklistContentsPE1CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPE2CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPE3CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPE4CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPE5CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPEOCreationDate | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE1EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE2EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE3EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE4EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE5EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPEOEnterpriseId | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE1LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE2LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE3LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE4LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE5LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE2LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE3LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE4LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE5LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE1LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE2LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE3LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE4LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE5LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE2ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE3ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE4ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE5ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPEOObjectVersionNumber | — |
| SEQUENCE | AllocatedChecklistContentsPE1Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPE2Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPE3Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPE4Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPE5Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPEOSequence | ✅ |

### [[allocatedchecklisttaskspvo|AllocatedChecklistTasksPVO]] (HCM · BICC: 12/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE1AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE2AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE3AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE4AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPE5AllocChklstContentId | — |
| ALLOC_CHKLST_CONTENT_ID | AllocatedChecklistContentsPEAllocChklstContentId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE1AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE2AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE3AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE4AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPE5AllocatedChecklistId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistContentsPEAllocatedChecklistId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE1ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE2ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE3ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE4ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPE5ChecklistContentId | — |
| CHECKLIST_CONTENT_ID | AllocatedChecklistContentsPEChecklistContentId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE1ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE2ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE3ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE4ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPE5ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | AllocatedChecklistContentsPEChkContentDefnId | — |
| CONTENT_TYPE | AllocatedChecklistContentsPE1ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPE2ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPE3ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPE4ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPE5ContentType | ✅ |
| CONTENT_TYPE | AllocatedChecklistContentsPEContentType | ✅ |
| CREATED_BY | AllocatedChecklistContentsPE1CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPE2CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPE3CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPE4CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPE5CreatedBy | — |
| CREATED_BY | AllocatedChecklistContentsPECreatedBy | — |
| CREATION_DATE | AllocatedChecklistContentsPE1CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPE2CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPE3CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPE4CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPE5CreationDate | — |
| CREATION_DATE | AllocatedChecklistContentsPECreationDate | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE1EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE2EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE3EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE4EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPE5EnterpriseId | — |
| ENTERPRISE_ID | AllocatedChecklistContentsPEEnterpriseId | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE1LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE2LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE3LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE4LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPE5LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedChecklistContentsPELastUpdateDate | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE2LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE3LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE4LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPE5LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistContentsPELastUpdateLogin | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE1LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE2LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE3LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE4LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPE5LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedChecklistContentsPELastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE2ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE3ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE4ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPE5ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistContentsPEObjectVersionNumber | — |
| SEQUENCE | AllocatedChecklistContentsPE1Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPE2Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPE3Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPE4Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPE5Sequence | ✅ |
| SEQUENCE | AllocatedChecklistContentsPESequence | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_ALLOC_CHKLST_CONTENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallocchklstcontents.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
