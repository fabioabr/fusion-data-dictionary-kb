---
id: DOC-HCM-332
doc_type: system-doc
title: "HWM_TCD_MAPPING_DTLS — Detalhes de Mapeamento de Time Card"
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
  - time-card
  - mapeamentos
  - detalhes
aliases:
  - HWM_TCD_MAPPING_DTLS
  - hwm_tcd_mapping_dtls
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TCD_MAPPING_DTLS

## 📌 Visão Geral

Armazena os detalhes granulares de cada mapeamento de cartão de ponto, incluindo campo de origem, campo de destino e regras de transformação.



---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Exportação de dados de ponto:** Configuração de como os dados do cartão de ponto são exportados para sistemas externos.
- **Mapeamento de campos:** Definição de correspondência entre campos do time card e sistemas de destino.
- **Integração com Payroll:** Transferência de horas trabalhadas para processamento de folha de pagamento.
- **Integração com Project Costing:** Alocação de horas em projetos para custeio.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | MAPPING_DTL_ID | NUMBER(18) | NOT NULL | PK | Identificador do detalhe de mapeamento | — | 🟡 80% |
| 2 | MAPPING_ID | NUMBER(18) | NOT NULL | FK | Referência ao mapeamento pai | — | 🟡 80% |
| 3 | SOURCE_FIELD | VARCHAR2(240) | NULL | Dados | Campo de origem | — | 🟡 75% |
| 4 | TARGET_FIELD | VARCHAR2(240) | NULL | Dados | Campo de destino | — | 🟡 75% |
| 5 | TRANSFORMATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de transformação aplicada | — | 🟡 70% |
| 6 | SEQUENCE_NUMBER | NUMBER(9) | NULL | Controle | Ordem de processamento | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_tcd_mappings_b]] — via `MAPPING_ID` (mapeamento pai do detalhe de tempo)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.SOURCE_FIELD, t.TARGET_FIELD, t.TRANSFORMATION_TYPE
FROM   HWM_TCD_MAPPING_DTLS t
ORDER BY t.SEQUENCE_NUMBER
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Time Card Export dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_TCD_MAPPING_DTLS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tcd_mapping_dtls.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
