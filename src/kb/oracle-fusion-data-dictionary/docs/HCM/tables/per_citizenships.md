---
id: DOC-HCM-645
doc_type: system-doc
title: "PER_CITIZENSHIPS — Cidadanias"
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
  - cidadanias
  - citizenships
aliases:
  - PER_CITIZENSHIPS
  - per_citizenships
  - per-citizenships
  - cidadanias
  - per-citizenships
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CITIZENSHIPS

## 📌 Visão Geral

Armazena as **cidadanias/nacionalidades** dos colaboradores. Permite registrar múltiplas cidadanias por pessoa, incluindo status e documentação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de nacionalidade** — armazena cidadanias de cada colaborador.
- **Compliance migratório** — controle de autorizações de trabalho por nacionalidade.
- **Relatórios demográficos** — análise da diversidade de nacionalidades.
- **Elegibilidade** — cidadania pode impactar elegibilidade a benefícios e posições.
- **Mobilidade internacional** — suporte a transferências entre países.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CITIZENSHIP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de cidadania | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa associada | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | LEGISLATION_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código do país da cidadania | — | 🟢 90% |
| 4 | CITIZENSHIP_STATUS | VARCHAR2(30) | NULL | Status | Status da cidadania (CITIZEN, PERMANENT_RESIDENT, etc.) | — | 🟢 85% |
| 5 | DATE_FROM | DATE | NULL | Período | Data de obtenção da cidadania | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular da cidadania)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Cidadanias de um colaborador
```sql
SELECT pc.LEGISLATION_CODE, pc.CITIZENSHIP_STATUS, pc.DATE_FROM
FROM   PER_CITIZENSHIPS pc
WHERE  pc.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `LEGISLATION_CODE = 'BR'` — Cidadania brasileira
---

## 🔒 Observações

- Um colaborador pode ter múltiplas cidadanias registradas.
- O `CITIZENSHIP_STATUS` diferencia entre cidadão, residente permanente e outros status.
- Dados sensíveis sujeitos a LGPD — acesso deve ser controlado.
---

## 📚 Referências

- [Oracle Docs — PER_CITIZENSHIPS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/percitizenships.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
