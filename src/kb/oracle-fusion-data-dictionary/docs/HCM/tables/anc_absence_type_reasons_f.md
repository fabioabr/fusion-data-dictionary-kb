---
id: DOC-HCM-010
doc_type: system-doc
title: "ANC_ABSENCE_TYPE_REASONS_F — Associação Tipo-Motivo de Ausência"
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
  - absence-management
  - tipo-motivo
  - type-reasons
  - associacao
aliases:
  - ANC_ABSENCE_TYPE_REASONS_F
  - anc_absence_type_reasons_f
  - tipo-motivo-ausencia
  - absence-type-reasons
  - anc-abs-type-reasons
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_TYPE_REASONS_F

## 📌 Visão Geral

Armazena a **associação entre tipos e motivos de ausência**. Tabela de relação que vincula quais motivos são válidos para cada tipo de ausência.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Validação de motivos:** Restringe quais motivos podem ser selecionados para cada tipo de ausência.
- **Self-service:** Filtra a lista de motivos disponíveis na interface do colaborador conforme o tipo selecionado.
- **Consistência de dados:** Garante que apenas motivos válidos sejam associados a cada tipo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_TYPE_REASON_ID | NUMBER(18) | NOT NULL | PK | Identificador único da associação | — | 🟢 90% |
| 2 | ABSENCE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de ausência | [[anc_absence_types_f]] | 🟢 95% |
| 3 | ABSENCE_REASON_ID | NUMBER(18) | NOT NULL | FK | Motivo de ausência | [[anc_absence_reasons_f]] | 🟢 95% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_absence_types_f]] — via `ABSENCE_TYPE_ID` (tipo de ausencia do motivo)
- [[anc_absence_reasons_f]] — via `ABSENCE_REASON_ID` (motivo de ausencia associado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Motivos válidos por tipo de ausência
```sql
SELECT typ.ABSENCE_TYPE_NAME, rsn.REASON_NAME
FROM   ANC_ABSENCE_TYPE_REASONS_F tr
JOIN   ANC_ABSENCE_TYPES_F typ ON tr.ABSENCE_TYPE_ID = typ.ABSENCE_TYPE_ID
JOIN   ANC_ABSENCE_REASONS_F rsn ON tr.ABSENCE_REASON_ID = rsn.ABSENCE_REASON_ID
WHERE  SYSDATE BETWEEN tr.EFFECTIVE_START_DATE AND tr.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes

---

## 🔒 Observações

- Tabela de relação entre tipos e motivos de ausência.
- Date-effective: a validade de um motivo para um tipo pode mudar ao longo do tempo.
- Usada pela interface de self-service para filtrar motivos conforme o tipo selecionado.

---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_TYPE_REASONS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsencetyperesonsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
