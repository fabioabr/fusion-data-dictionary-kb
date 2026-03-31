---
id: DOC-HCM-642
doc_type: system-doc
title: "PER_CHECKLIST_CONTENTS — Conteúdos de Template de Checklist"
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
  - conteudos-template
aliases:
  - PER_CHECKLIST_CONTENTS
  - per_checklist_contents
  - per-checklist-contents
  - conteúdos-de-template-de-checklist
  - per-checklist-conten
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CHECKLIST_CONTENTS

## 📌 Visão Geral

Armazena os **conteúdos padrão** associados ao template de checklist. Define materiais de referência que serão disponibilizados em todas as instâncias alocadas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Material padrão** — define conteúdos replicados em cada instância de checklist.
- **Padronização** — garante que todos os colaboradores recebam os mesmos materiais.
- **Base de conhecimento** — centralização de documentos de suporte.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECKLIST_CONTENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do conteúdo | — | 🟢 90% |
| 2 | CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Template de checklist | PER_CHECKLISTS_B | 🟢 90% |
| 3 | CONTENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de conteúdo | — | 🟡 75% |
| 4 | CONTENT_URL | VARCHAR2(2000) | NULL | Conteúdo | URL do recurso | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_checklists_b]] — via `CHECKLIST_ID` (template de checklist do conteúdo)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Conteúdos de um template
```sql
SELECT pcc.CONTENT_TYPE, pcc.CONTENT_URL
FROM   PER_CHECKLIST_CONTENTS pcc
WHERE  pcc.CHECKLIST_ID = :p_checklist_id;
```

### Filtros comuns
- `CONTENT_TYPE = 'URL'` — Links
---

## 🔒 Observações

- Conteúdos do template são copiados para PER_ALLOC_CHKLST_CONTENTS ao alocar.
- Permite definir links para portais, documentos e vídeos de treinamento.
---

## 📚 Referências

- [Oracle Docs — PER_CHECKLIST_CONTENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perchecklistcontents.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
