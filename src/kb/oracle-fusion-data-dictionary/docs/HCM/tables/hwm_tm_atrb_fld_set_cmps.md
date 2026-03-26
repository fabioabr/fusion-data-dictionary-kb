---
id: DOC-HCM-360
doc_type: system-doc
title: "HWM_TM_ATRB_FLD_SET_CMPS — Componentes de Conjunto de Campos de Atributos"
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
  - time-management
  - atributos
  - conjuntos
  - componentes
aliases:
  - HWM_TM_ATRB_FLD_SET_CMPS
  - hwm_tm_atrb_fld_set_cmps
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_ATRB_FLD_SET_CMPS

## 📌 Visão Geral

Define os componentes que compõem conjuntos de campos de atributos de Time Management, estabelecendo quais campos fazem parte de cada conjunto configurado.



---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Personalização de campos:** Configuração de campos adicionais para captura de informações específicas do negócio.
- **Flexibilidade de interface:** Definição de quais campos são exibidos e obrigatórios por contexto.
- **Referência mestre:** Manutenção de valores válidos para campos de atributo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | FLD_SET_CMP_ID | NUMBER(18) | NOT NULL | PK | Identificador do componente de conjunto | — | 🟡 80% |
| 2 | FLD_SET_ID | NUMBER(18) | NOT NULL | FK | Referência ao conjunto de campos | — | 🟡 80% |
| 3 | ATRB_FLD_ID | NUMBER(18) | NOT NULL | FK | Referência ao campo de atributo | HWM_TM_ATRB_FLDS_B | 🟡 80% |
| 4 | SEQUENCE_NUMBER | NUMBER(9) | NULL | Controle | Ordem do campo no conjunto | — | 🟡 75% |
| 5 | REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o campo é obrigatório (Y/N) | — | 🟡 70% |
| 6 | DISPLAY_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o campo é visível (Y/N) | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.ATRB_FLD_ID, t.SEQUENCE_NUMBER, t.REQUIRED_FLAG, t.DISPLAY_FLAG
FROM   HWM_TM_ATRB_FLD_SET_CMPS t
WHERE  t.FLD_SET_ID = :p_fld_set_id
ORDER BY t.SEQUENCE_NUMBER
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_ATRB_FLD_SET_CMPS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_atrb_fld_set_cmps.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
