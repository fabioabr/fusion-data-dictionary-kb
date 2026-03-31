---
id: DOC-HCM-631
doc_type: system-doc
title: "PER_ASSIGNMENT_EXTRA_INFO_M — Informações Extras do Assignment (Materializada)"
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
  - flexfields
  - assignment-extra-info
aliases:
  - PER_ASSIGNMENT_EXTRA_INFO_M
  - per_assignment_extra_info_m
  - per-assignment-extra-info-m
  - informações-extras-do-assignment-(materializada)
  - per-assignment-extra
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASSIGNMENT_EXTRA_INFO_M

## 📌 Visão Geral

Armazena **informações adicionais** (flexfields) associadas aos assignments dos colaboradores. Permite armazenar dados customizados que não cabem na estrutura padrão do assignment.

> [!note] Sufixo _M
> O sufixo `_M` indica tabela **materializada** — combina dados de múltiplas fontes para otimização de consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Dados customizados** — armazena informações específicas da organização por assignment.
- **Flexfields** — suporte a campos descritivos flexíveis (DFF) do Oracle.
- **Extensibilidade** — permite adicionar dados sem alterar a estrutura da tabela principal.
- **Relatórios customizados** — base para relatórios com dados específicos da organização.
- **Integração** — dados extras para interfaces com sistemas externos.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_EXTRA_INFO_ID | NUMBER(18) | NOT NULL | PK | Identificador único da informação extra | — | 🟢 95% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Assignment associado | PER_ALL_ASSIGNMENTS_M | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | INFORMATION_TYPE | VARCHAR2(40) | NOT NULL | Classificação | Tipo/categoria da informação extra | — | 🟢 90% |
| 6 | AEI_ATTRIBUTE1 | VARCHAR2(150) | NULL | Dados | Atributo flexível 1 | — | 🟢 85% |
| 7 | AEI_ATTRIBUTE2 | VARCHAR2(150) | NULL | Dados | Atributo flexível 2 | — | 🟢 85% |
| 8 | AEI_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Classificação | Categoria dos atributos | — | 🟢 85% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vínculo das informações extras)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Informações extras de um assignment
```sql
SELECT paei.INFORMATION_TYPE, paei.AEI_ATTRIBUTE1, paei.AEI_ATTRIBUTE2
FROM   PER_ASSIGNMENT_EXTRA_INFO_M paei
WHERE  paei.ASSIGNMENT_ID = :p_assignment_id
  AND  SYSDATE BETWEEN paei.EFFECTIVE_START_DATE AND paei.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `INFORMATION_TYPE = :p_info_type` — Informações de um tipo específico
---

## 🔒 Observações

- Tabela materializada (_M) com date-effectiveness.
- Os campos AEI_ATTRIBUTE1..N são genéricos — o significado depende do `INFORMATION_TYPE`.
- Extensamente usada para armazenar dados específicos do país (dados trabalhistas brasileiros, por exemplo).
- A estrutura flexfield permite até 30 atributos (AEI_ATTRIBUTE1 a AEI_ATTRIBUTE30).
---

## 📚 Referências

- [Oracle Docs — PER_ASSIGNMENT_EXTRA_INFO_M](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perassignmentextrainfom.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
