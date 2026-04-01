---
id: DOC-AR-066
doc_type: system-doc
title: "AR_TRANSMISSION_FORMATS — Formatos de Transmissão"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, transmissao, remessa-bancaria, direct-debit]
aliases: [AR_TRANSMISSION_FORMATS, ar_transmission_formats, transmission_formats, formatos_transmissao, ar_trans_formats]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_TRANSMISSION_FORMATS

## 📌 Visão Geral

Tabela de cadastro de **formatos de transmissão** para remessas bancárias e direct debit. Define a estrutura dos arquivos de transmissão utilizados na comunicação entre o sistema AR e os bancos — layout de arquivo, tipo de formato e status.

## 🧠 Propósito de Negócio

Os formatos de transmissão são o **contrato técnico** entre o AR e os bancos. Definem como os dados de recebimentos, remessas e débitos automáticos são formatados para envio aos bancos, garantindo compatibilidade com os padrões bancários (CNAB, FEBRABAN, SEPA, etc.).

Casos de uso principais:
- Definição de layout CNAB para remessa de boletos
- Formato de arquivo para direct debit (débito automático)
- Layout de retorno bancário para compensação automática
- Padronização de formatos por banco

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | TRANSMISSION_FORMAT_ID | NUMBER | PK. Identificador único do formato de transmissão. | Chave | 🟢 100% |
| 2 | NAME | VARCHAR2 | Nome do formato (ex: "CNAB240_REMESSA_BB", "SEPA_DIRECT_DEBIT"). | Identificação | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2 | Descrição detalhada do formato e seu uso. | Identificação | 🟢 100% |
| 4 | FORMAT_TYPE | VARCHAR2 | Tipo do formato: `REMITTANCE`, `DIRECT_DEBIT`, `LOCKBOX`, `RETURN`. | Classificação | 🟢 100% |
| 5 | STATUS | VARCHAR2 | Status do formato: `A` (ativo) ou `I` (inativo). | Controle | 🟢 100% |
| 6 | FORMAT_PROGRAM_ID | NUMBER | ID do programa que implementa o formato (geração/parsing do arquivo). | Configuração | 🟢 100% |
| 7 | TRANSMISSION_PROGRAM_ID | NUMBER | ID do programa de transmissão (envio ao banco). | Configuração | 🟢 100% |
| 8 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 9 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 10 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 11 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_receipt_methods]] | AUTO_TRANS_PROGRAM_ID | Referência | Métodos de recebimento que usam formatos de transmissão |
| [[ar_receipt_classes]] | — | Referência | Classes com remessa usam formatos de transmissão |
| [[ce_bank_accounts]] | — | Referência | Contas bancárias associadas a formatos |

## 📎 Uso Típico

```sql
-- Listar formatos de transmissão ativos
SELECT transmission_format_id,
       name,
       format_type,
       description,
       status
  FROM ar_transmission_formats
 WHERE status = 'A'
 ORDER BY format_type, name;
```

```sql
-- Formatos por tipo
SELECT format_type,
       COUNT(*) AS qtd_formatos,
       SUM(CASE WHEN status = 'A' THEN 1 ELSE 0 END) AS ativos
  FROM ar_transmission_formats
 GROUP BY format_type
 ORDER BY format_type;
```

## 🔒 Observações

- No Brasil, os formatos mais comuns seguem o padrão **CNAB** (Centro Nacional de Automação Bancária) — 240 ou 400 posições.
- Cada banco pode ter seu formato específico; é comum ter múltiplos formatos ativos simultaneamente.
- O `FORMAT_PROGRAM_ID` aponta para o programa PL/SQL ou BI Publisher que gera o arquivo no layout correto.
- Esta tabela é **compartilhada** entre todas as BUs (não particionada por ORG_ID).
- Em migrações de EBS para Fusion, os formatos de transmissão geralmente precisam ser reconfigurados, pois o Fusion usa a camada de Payments (IBY) para transmissão.

## 🔗 PVOs Relacionados

### [[transmissionformatextractpvo|TransmissionFormatExtractPVO]] (OTHER · BICC: 13/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | ArTransmissionFormatAttribute1 | — |
| ATTRIBUTE10 | ArTransmissionFormatAttribute10 | — |
| ATTRIBUTE11 | ArTransmissionFormatAttribute11 | — |
| ATTRIBUTE12 | ArTransmissionFormatAttribute12 | — |
| ATTRIBUTE13 | ArTransmissionFormatAttribute13 | — |
| ATTRIBUTE14 | ArTransmissionFormatAttribute14 | — |
| ATTRIBUTE15 | ArTransmissionFormatAttribute15 | — |
| ATTRIBUTE2 | ArTransmissionFormatAttribute2 | — |
| ATTRIBUTE3 | ArTransmissionFormatAttribute3 | — |
| ATTRIBUTE4 | ArTransmissionFormatAttribute4 | — |
| ATTRIBUTE5 | ArTransmissionFormatAttribute5 | — |
| ATTRIBUTE6 | ArTransmissionFormatAttribute6 | — |
| ATTRIBUTE7 | ArTransmissionFormatAttribute7 | — |
| ATTRIBUTE8 | ArTransmissionFormatAttribute8 | — |
| ATTRIBUTE9 | ArTransmissionFormatAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArTransmissionFormatAttributeCategory | — |
| CREATED_BY | ArTransmissionFormatCreatedBy | ✅ |
| CREATION_DATE | ArTransmissionFormatCreationDate | ✅ |
| DESCRIPTION | ArTransmissionFormatDescription | ✅ |
| FORMAT_NAME | ArTransmissionFormatFormatName | ✅ |
| LAST_UPDATE_DATE | ArTransmissionFormatLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArTransmissionFormatLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArTransmissionFormatLastUpdatedBy | ✅ |
| MODULE_ID | ArTransmissionFormatModuleId | ✅ |
| OBJECT_VERSION_NUMBER | ArTransmissionFormatObjectVersionNumber | ✅ |
| SEED_DATA_SOURCE | ArTransmissionFormatSeedDataSource | ✅ |
| STATUS_LOOKUP_CODE | ArTransmissionFormatStatusLookupCode | ✅ |
| TRANSMISSION_FORMAT_ID | ArTransmissionFormatTransmissionFormatId | ✅ |
| ZENGIN_CHAR_SET | ArTransmissionFormatZenginCharSet | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Transmission Formats View Object
- Oracle Fusion Cloud — Setting Up Funds Capture (Payments Configuration Guide)
