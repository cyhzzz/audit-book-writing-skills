# Audit Book Writing and Review Skill

A Claude Code skill for writing comprehensive audit books and conducting thorough reviews with systematic quality assurance.

## Overview

This skill provides a systematic workflow for writing audit survey books, practical guides, case analyses, and review materials on topics like financial audit, internal control audit, compliance audit, performance audit, IT audit, internal audit, and government audit. It emphasizes both academic rigor and practical applicability, with a structured 4-round review process.

## Features

- **Structured 7-phase workflow** for audit book writing and review
- **Domain-specific templates** covering 7 major audit areas
- **Standardized writing style** with precise professional language
- **Comprehensive case study templates** with complete elements
- **4-round quality assurance process** (accuracy, coherence, applicability, format)
- **Regulatory citation standards** for audit standards and laws

## Installation

Copy this skill folder to your Claude Code skills directory:

```
~/.claude/skills/audit-book-writing-review/
```

## Trigger Keywords

The skill automatically activates when detecting:
- "审计书籍" (audit books)
- "审计综述" (audit survey/review)
- "审计实务" (audit practice)
- "写书" (write book)
- "审校" (review)
- "审计案例分析" (audit case analysis)
- "内部控制审计" (internal control audit)
- "合规审计" (compliance audit)
- "财务审计" (financial audit)
- "绩效审计" (performance audit)
- "IT审计" (IT audit)
- Mentions of writing audit-related books or conducting audit reviews

## Files

| File | Description |
|------|-------------|
| `SKILL.md` | Main skill definition and quick reference |
| `WORKFLOW.md` | Detailed 7-phase workflow with 4-round review |
| `TEMPLATES.md` | Project file templates (CLAUDE.md, IMPLEMENTATION_PLAN.md) |
| `DOMAINS.md` | Domain-specific audit areas and classifications |

## Supported Audit Domains

- **Financial Audit** (财务审计)
  - Risk-based audit, cycle approach, data analytics
  - Financial statement audit, fraud audit, disclosure audit

- **Internal Control Audit** (内部控制审计)
  - COSO framework, China internal control standards
  - Control deficiency identification, internal control system evaluation

- **Compliance Audit** (合规审计)
  - Regulatory compliance, AML audit, anti-fraud audit
  - Legal and regulatory requirements verification

- **Performance Audit** (绩效审计)
  - 3E audit (economy, efficiency, effectiveness)
  - Government performance audit, project evaluation

- **IT Audit** (IT审计)
  - ITGC, ITAC, cybersecurity audit
  - COBIT framework, ISO 27001, data audit

- **Internal Audit** (内部审计)
  - Risk-based internal audit, consulting audit
  - Operational audit, governance audit

- **Government Audit** (政府审计)
  - Budget execution audit, economic responsibility audit
  - Public investment audit, policy implementation audit

## Workflow Phases

1. **Project Initialization** - Create project structure and templates
2. **Material Collection** - Gather standards, regulations, cases, literature
3. **Outline Development** - Define book structure with 5 parts
4. **Chapter Writing** - Write theory, practice, case, regulatory chapters
5. **Tables and Cases** - Create comparison tables and detailed cases
6. **Quality Assurance and Review** - 4-round review process
7. **Incremental Updates** - Track regulatory changes and update content

## Standard Book Structure

```
# [Book Title]: Theory, Practice, and Cases

## Preface

## Part 1: Theoretical Foundation
### Chapter 1: Audit Overview
### Chapter 2: Theoretical Framework

## Part 2: Practical Operations
### Chapter 3: Audit Planning and Preparation
### Chapter 4: Audit Procedures

## Part 3: Typical Cases
### Chapter 5: Financial Audit Cases
### Chapter 6: Internal Control Audit Cases

## Part 4: Regulatory Interpretation
### Chapter 7: Audit Standards Interpretation
### Chapter 8: Related Laws and Regulations

## Part 5: Emerging Topics
### Chapter 9: Digital Audit
### Chapter 10: Audit Development Trends

## Appendices
## References
```

## Writing Guidelines

- Use **precise professional language** with accurate audit terminology
- Cite **authoritative sources** (audit standards, laws, regulations)
- Every claim needs **supporting evidence or references**
- Balance **academic rigor with practical applicability**
- Maintain **professional objectivity and neutrality**
- Each major section needs **comparison tables and case studies**
- Follow **standard citation formats** for regulations and cases

## 4-Round Review Process

### Round 1: Content Accuracy Review
- ✓ Regulatory accuracy (standard numbers, clauses, effective dates)
- ✓ Case accuracy (company names, dates, amounts, findings)
- ✓ Terminology accuracy (audit, accounting, legal terms)

### Round 2: Logical Coherence Review
- ✓ Chapter logic (hierarchy, transitions, progression)
- ✓ Argumentation (logical chain, supported claims)
- ✓ Consistency (terminology, data, references)

### Round 3: Practical Applicability Review
- ✓ Procedural feasibility (complete steps, actionable)
- ✓ Case representativeness (typical, current)
- ✓ Recommendation value (actionable, practical)

### Round 4: Format Standardization Review
- ✓ Citation format (standards, regulations, cases)
- ✓ Table consistency (titles, columns, formatting)
- ✓ Heading hierarchy (numbering, levels)

## Material Sources

### Primary Sources
- **Audit Standards**: CAS, ISA, Government Audit Standards, Internal Audit Standards
- **Laws and Regulations**: Audit Law, Accounting Law, CPA Law, Securities Law
- **Regulatory Documents**: MOF, CSRC, CBIRC, Audit Office guidance
- **Practical Cases**: Listed company audits, government audit reports, enforcement actions
- **Professional Resources**: Academic textbooks, journals, industry reports

### Key Websites
- CICPA: http://www.cicpa.org.cn/
- National Audit Office: http://www.audit.gov.cn/
- IIA China: http://www.iiachina.org.cn/
- MOF: http://www.mof.gov.cn/
- CSRC: http://www.csrc.gov.cn/

## Quality Dimensions

| Dimension | Description | Key Metrics |
|-----------|-------------|-------------|
| **Accuracy** | Content is error-free | Regulatory accuracy, case accuracy, terminology accuracy |
| **Completeness** | Comprehensive coverage | Complete procedures, complete references, all topics covered |
| **Timeliness** | Current and relevant | Latest standards, recent cases, current practice |
| **Practicality** | Actionable and useful | Feasible procedures, learnable cases, actionable recommendations |
| **Standardization** | Format compliance | Standard citations, consistent terminology, proper formatting |

## Citation Examples

```
# Audit Standards
CAS No. 1101 (2019) - 注册会计师的总体目标和审计工作的基本要求

# Regulations
《中华人民共和国审计法》第XX条

# Cases
XX股份有限公司20XX年度财务报表审计案例

# Academic Papers
张三(20XX)."论文标题"[J].审计研究,Vol.X,No.X:pp-pp.
```

## License

MIT License

## Contributing

This skill is adapted from the medical-imaging-review skill, redesigned for the audit domain with enhanced review processes and practical applicability focus.
