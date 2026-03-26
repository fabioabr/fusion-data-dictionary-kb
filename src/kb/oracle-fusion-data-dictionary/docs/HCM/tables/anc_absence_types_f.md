---
id: DOC-HCM-007
doc_type: system-doc
title: "ANC_ABSENCE_TYPES_F — Tipos de Ausência"
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
  - tipos-ausencia
  - absence-types
  - ferias
  - licenca
aliases:
  - ANC_ABSENCE_TYPES_F
  - anc_absence_types_f
  - tipos-ausencia-hcm
  - absence-types
  - anc-abs-types
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_TYPES_F

## 📌 Visão Geral

Armazena os **tipos de ausência** do módulo Absence Management. Cada tipo define uma modalidade de ausência (ex.: férias, licença médica, licença maternidade, falta injustificada) com suas regras de uso, duração e impacto na folha de pagamento.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação de ausências:** Define os tipos disponíveis para solicitação de ausência pelos colaboradores.
- **Regras de negócio:** Cada tipo pode ter configurações de duração mínima/máxima, exigência de certificados, etc.
- **Integração com folha:** Vinculação com elementos de pagamento para cálculo de impacto salarial.
- **Compliance trabalhista:** Tipos alinhados com requisitos legais (CLT, legislações locais).
- **Relatórios de absenteísmo:** Base para análise por tipo de ausência.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de ausência | — | 🟢 95% |
| 2 | ABSENCE_TYPE_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do tipo de ausência | — | 🟢 90% |
| 3 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 90% |
| 4 | ABSENCE_TYPE_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status (A — ativo, I — inativo) | — | 🟢 90% |
| 5 | DURATION_IN_DAYS_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se a duração é medida em dias (Y/N) | — | 🟡 70% |
| 6 | DURATION_IN_HOURS_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se a duração é medida em horas (Y/N) | — | 🟡 70% |
| 7 | CERT_REQUIRED_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se requer certificado/atestado (Y/N) | — | 🟡 70% |
| 8 | RUNNING_TOTAL_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se mantém total acumulado (Y/N) | — | 🟡 65% |
| 9 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 10 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta identificada (tabela de configuração raiz).

### Tabelas-filha (FK de saída)
- [[anc_absence_types_f_tl]] — via `ABSENCE_TYPE_ID` (traducoes multilingue do registro)
- [[anc_absence_type_cate_f]] — via `ABSENCE_TYPE_ID` (associação tipo-categoria)
- [[anc_absence_type_reasons_f]] — via `ABSENCE_TYPE_ID` (associação tipo-motivo)
- [[anc_per_abs_type_entries]] — via `ABSENCE_TYPE_ID` (entradas por tipo)
- [[anc_per_abs_entries]] — via `ABSENCE_TYPE_ID` (ausências registradas)

---

## 📎 Uso Típico

### Tipos de ausência ativos
```sql
SELECT at.ABSENCE_TYPE_ID, at.ABSENCE_TYPE_NAME,
       at.LEGISLATION_CODE, at.CERT_REQUIRED_FLAG
FROM   ANC_ABSENCE_TYPES_F at
WHERE  SYSDATE BETWEEN at.EFFECTIVE_START_DATE AND at.EFFECTIVE_END_DATE
  AND  at.ABSENCE_TYPE_STATUS = 'A';
```

### Filtros comuns
- `ABSENCE_TYPE_STATUS = 'A'` — Tipos ativos
- `LEGISLATION_CODE = 'BR'` — Tipos para legislação brasileira
- `CERT_REQUIRED_FLAG = 'Y'` — Tipos que exigem atestado

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigência.
- Os flags `DURATION_IN_DAYS_FLAG` e `DURATION_IN_HOURS_FLAG` determinam a unidade de medida.
- `CERT_REQUIRED_FLAG = 'Y'` indica que o colaborador deve anexar um certificado/atestado.
- Tipos são associados a categorias via `ANC_ABSENCE_TYPE_CATE_F` e a motivos via `ANC_ABSENCE_TYPE_REASONS_F`.

---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_TYPES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsencetypesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
