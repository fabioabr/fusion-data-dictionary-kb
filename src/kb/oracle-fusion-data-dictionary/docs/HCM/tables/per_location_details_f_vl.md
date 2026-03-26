---
id: DOC-HCM-677
doc_type: system-doc
title: "PER_LOCATION_DETAILS_F_VL — View de Detalhes de Localização com Tradução"
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
  - per-locations
  - location-details-vl
  - view-traduzida
  - multilanguage
aliases:
  - PER_LOCATION_DETAILS_F_VL
  - per_location_details_f_vl
  - view-detalhes-localizacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_LOCATION_DETAILS_F_VL

## Visão Geral

**View** que combina os dados da tabela base `PER_LOCATION_DETAILS_F` com as traduções da tabela `PER_LOCATION_DETAILS_F_TL`, apresentando os detalhes de localização já com os campos traduzidos no idioma da sessão do usuário.

> [!note] Sufixo _VL
> O sufixo `_VL` indica **View com Language** — join automático entre a tabela base (_F) e a tabela de tradução (_TL), filtrando pelo idioma da sessão.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Consultas simplificadas** — elimina a necessidade de join manual entre base e TL
- **Relatórios localizados** — dados já no idioma do usuário corrente
- **Integrações com BI/Analytics** — fonte preferida para relatórios OTBI e BIP
- **APIs REST** — muitas APIs HCM utilizam views _VL como fonte de dados

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOCATION_DETAILS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe de localização | — | 🟢 95% |
| 2 | LOCATION_ID | NUMBER(18) | NOT NULL | FK | Referência à localização principal | PER_LOCATIONS | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 5 | TIMEZONE_CODE | VARCHAR2(50) | NULL | Configuração | Código do fuso horário da localização | — | 🟡 75% |
| 6 | LOCATION_DETAILS_NAME | VARCHAR2(360) | NULL | Tradução | Nome traduzido do detalhe de localização | — | 🟡 75% |
| 7 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_locations]] — via `LOCATION_ID` (localizaÃ§Ã£o da visÃ£o traduzida de detalhes)

### Tabelas-filha (FK de saída)
- Nenhuma — views não possuem FKs diretas.

---

## Uso Típico

### Detalhes traduzidos de uma localização ativa
```sql
SELECT vl.LOCATION_DETAILS_ID, vl.LOCATION_DETAILS_NAME,
       vl.TIMEZONE_CODE, vl.DESCRIPTION
FROM   PER_LOCATION_DETAILS_F_VL vl
WHERE  SYSDATE BETWEEN vl.EFFECTIVE_START_DATE AND vl.EFFECTIVE_END_DATE
  AND  vl.LOCATION_ID = :p_location_id;
```

---

## Observações

- Por ser uma view, não aceita DML direto — alterações devem ser feitas via tabelas base.
- O filtro de idioma é aplicado automaticamente com base no `USERENV('LANG')`.
- Preferir esta view em relatórios OTBI para garantir tradução automática.

---

## Referências

- [Oracle Docs — PER_LOCATION_DETAILS_F_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perlocationdetailsfvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
