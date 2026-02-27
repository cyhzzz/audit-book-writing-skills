# 7-Phase Audit Book Writing and Review Workflow

## Phase 1: Project Initialization

Create project structure:
```
project_root/
├── CLAUDE.md              # Writing guidelines and terminology
├── IMPLEMENTATION_PLAN.md # Staged execution plan
├── book_draft.md          # Main book manuscript
└── figures/               # Figure placeholders
```

**Actions:**
1. Create `CLAUDE.md` from template (see TEMPLATES.md)
2. Create `IMPLEMENTATION_PLAN.md` with stages
3. Initialize empty `book_draft.md`

## Phase 2: Material Collection

### Data Sources

#### 1. Audit Standards (Primary Sources)

**Chinese Standards:**
- CAS (Chinese Audit Standards) - 注册会计师审计准则
- Government Audit Standards - 政府审计准则
- Internal Audit Standards - 内部审计准则
- Internal Control Standards - 企业内部控制基本规范

**International Standards:**
- ISA (International Standards on Auditing)
- IIA Standards (Institute of Internal Auditors)
- COSO Framework (Internal Control)
- COBIT (IT Audit)

**Collection Strategy:**
```
Source: Official websites
- Ministry of Finance: http://www.mof.gov.cn/
- CICPA: http://www.cicpa.org.cn/
- National Audit Office: http://www.audit.gov.cn/
- IIA China: http://www.iiachina.org.cn/

Types: Standards, implementation guidance, interpretation bulletins
Date: Focus on latest versions and revisions (last 3-5 years)
Format: Official PDF documents, authoritative interpretations
```

**Workflow:**
1. Identify relevant standards for the audit topic
2. Download official standards from authoritative sources
3. Note effective dates and revision history
4. Extract key requirements and provisions
5. Organize by standard number and topic

#### 2. Regulatory Documents

**Regulatory Bodies:**
- Ministry of Finance (财政部) - Accounting and auditing regulations
- CSRC (证监会) - Securities regulation and disclosure requirements
- CBIRC (银保监会) - Banking and insurance supervision
- National Audit Office (审计署) - Government audit regulations
- MOFCOM (商务部) - Enterprise internal control

**Document Types:**
- Laws and Regulations (会计法, 注册会计师法, 审计法, 证券法)
- Administrative Rules (部门规章)
- Regulatory Guidelines (指引, 通知, 规范)
- Enforcement Actions (处罚决定书, 监管函, 通报)

**Collection Workflow:**
1. Search regulatory body websites by topic
2. Identify relevant laws and regulations
3. Download enforcement cases for practical examples
4. Organize by issuing body and effective date
5. Track amendments and revisions

#### 3. Practical Cases

**Case Sources:**
- Listed company annual reports and audit reports
- Government audit reports (审计结果公告)
- Enforcement actions by regulators (行政处罚决定书)
- Professional firm case studies (Big 4 case collections)
- Academic case databases

**Case Selection Criteria:**
- Representativeness (typical scenarios)
- Recency (last 3-5 years preferred)
- Materiality (significant findings or issues)
- Educational value (clear lessons)

**Case Collection Workflow:**
1. Search by audit type and industry
2. Identify cases with complete information
3. Extract key facts: background, process, findings, outcomes
4. Organize by audit domain and topic
5. Create case matrix:

| Case Type | Company | Year | Key Issues | Reference | Source |
|-----------|---------|------|------------|-----------|--------|
| Financial Audit | [Company] | 20XX | [issues] | [citation] | [source] |
| Internal Control | [Company] | 20XX | [issues] | [citation] | [source] |

#### 4. Professional Resources

**Books and Monographs:**
- Academic textbooks (审计学, 审计实务)
- Professional guides (实务操作指南)
- International translations (ISA译本, COSO框架)

**Academic Papers:**
- Journals: 审计研究, 会计研究, 审计月刊, Auditing: A Journal of Practice & Theory
- Conference papers
- Research reports

**Industry Reports:**
- Professional firm annual reports (Big 4趋势报告)
- Industry white papers
- Survey results

#### 5. Zotero Integration (Reference Management)

**Workflow:**
1. Connect to Zotero API or use Zotero-MCP
2. Browse existing collections by audit topic
3. Export metadata for citation management
4. Organize by: Standards, Regulations, Cases, Books, Papers

### Collection Workflow

**Actions:**
1. **Standards collection** - Identify and download all relevant standards (target: 20-30 standards)
2. **Regulatory collection** - Collect laws and regulations (target: 30-50 documents)
3. **Case collection** - Gather representative cases (target: 20-40 cases)
4. **Literature collection** - Books and papers (target: 30-50 items)
5. **Categorize** materials by audit domain and topic
6. Create material matrix:

| Category | Subcategory | Key Items | Count | Source |
|----------|-------------|-----------|-------|--------|
| Standards | CAS | [list standards] | N | MOF/CICPA |
| Regulations | Securities Law | [list regs] | N | CSRC |
| Cases | Financial Audit | [list cases] | N | Annual Reports |
| Literature | Academic | [list papers] | N | Journals |

7. **Gap analysis** - Identify missing topics or outdated materials
8. **Targeted collection** - Fill gaps with additional searches

## Phase 3: Outline Development

**Actions:**
1. Define book structure based on audit domain and target audience
2. Map materials to chapters and sections
3. Plan comparison tables and case placements
4. Design figure placeholders
5. Create chapter hierarchy:

```
Part 1: Theoretical Foundation (Chapters 1-2)
├── Chapter 1: Audit Overview
│   ├── 1.1 Definition and Classification
│   ├── 1.2 History and Development
│   └── 1.3 Functions and Roles
└── Chapter 2: Theoretical Framework
    ├── 2.1 Audit Concepts
    ├── 2.2 Audit Risk
    └── 2.3 Audit Evidence

Part 2: Practical Operations (Chapters 3-4)
├── Chapter 3: Audit Planning
│   ├── 3.1 Engagement Letter
│   └── 3.2 Risk Assessment
└── Chapter 4: Audit Procedures
    ├── 4.1 Tests of Controls
    └── 4.2 Substantive Procedures

Part 3: Typical Cases (Chapters 5-6)
├── Chapter 5: Financial Audit Cases
│   └── Case Study 5-1: [Company]
└── Chapter 6: Internal Control Cases
    └── Case Study 6-1: [Company]

Part 4: Regulatory Interpretation (Chapters 7-8)
├── Chapter 7: Audit Standards
└── Chapter 8: Related Laws

Part 5: Emerging Topics (Chapters 9-10)
├── Chapter 9: Digital Audit
└── Chapter 10: Development Trends
```

**Output:** Detailed outline in IMPLEMENTATION_PLAN.md

## Phase 4: Chapter Writing

For each major chapter:

**Theory Chapters:**
1. **Write introduction** (1-2 paragraphs on importance)
2. **Define concepts** with authoritative sources
3. **Explain frameworks** with clear structure
4. **Trace development** (historical evolution)
5. **Create comparison table** (schools of thought, approaches)
6. **Add references** to standards and academic sources

**Practice Chapters:**
1. **Write introduction** (purpose and scope)
2. **Describe procedures** step-by-step
3. **Provide templates** and working paper examples
4. **Include quality control points**
5. **Create comparison table** (method comparison, procedure selection)
6. **Add practical tips** from experienced auditors

**Case Chapters:**
1. **Provide background** (company, industry, period)
2. **Describe audit process** (planning, execution, reporting)
3. **Detail key findings** with supporting evidence
4. **Analyze root causes** and implications
5. **Extract lessons** and best practices
6. **Reference relevant standards** and regulations

**Regulatory Chapters:**
1. **Explain background** (why issued, objectives)
2. **Summarize requirements** (key provisions)
3. **Compare with other standards** (domestic/international)
4. **Provide practical application** guidance
5. **Include compliance checklist**
6. **Reference enforcement cases**

**Progress tracking:** Use TodoWrite for each chapter

## Phase 5: Tables and Cases

**Required tables:**
- Standards comparison tables (CAS vs ISA, old vs new)
- Procedure comparison tables (methods, approaches, tools)
- Regulation summary tables (key requirements, applicability)
- Case summary tables (background, findings, lessons)

**Case study format:**
- Background (company, industry, period, audit type)
- Objectives (what audit aimed to achieve)
- Process (planning, execution, reporting phases)
- Findings (key issues with evidence)
- Recommendations (actionable suggestions)
- Insights (lessons learned, applicability)

**Figure placeholders:**
- Figure 1: Audit process flowchart
- Figure 2: Risk assessment framework
- Figure 3: Control testing procedures
- Figure 4: Audit report structure
- Figure 5: Standards comparison matrix
- Figure 6: Digital audit technology landscape

## Phase 6: Quality Assurance and Review

### 4-Round Review Process

#### Round 1: Content Accuracy Review

**⚠️ DATA VERIFICATION (CRITICAL STEP)**

**必须执行的验证流程**：

1. **法律法规验证**：
   ```bash
   # 使用Grep在法律法规库中查询
   Grep -pattern "法规名称或关键词" -path="D:\project\审计书籍撰写\法律法规库\*.md" -output_mode="content"
   ```
   - ✓ 法规名称是否准确
   - ✓ 条款号是否存在
   - ✓ 条款内容是否准确引用
   - ✓ 发布日期和生效日期是否正确
   - ❌ 发现编造或错误引用，必须重新查询并修正

2. **统计数据验证**：
   ```bash
   # 使用WebSearch查询并标注来源
   WebSearch "统计数据关键词 年份 官方来源"
   ```
   - ✓ 数据来源是否权威（政府、官方机构）
   - ✓ 数据发布机构是否标注
   - ✓ 数据发布时间是否标注
   - ✓ 来源网址是否标注
   - ⚠️ 无法核实的数据，标注"**[待核实：该数据需要人工核对后补充]**"

3. **案例数据验证**：
   - ✓ 公司名称是否准确
   - ✓ 审计期间是否准确
   - ✓ 金额数据是否准确
   - ✓ 来源于公开可查的审计报告

4. **标准和准则验证**：
   ```bash
   # 查询标准原文
   Grep -pattern "标准号 关键词" -path="D:\project\审计书籍撰写\标准库\*.md"
   ```
   - ✓ 标准号是否准确
   - ✓ 条款号是否存在
   - ✓ 引用内容是否准确

**验证标准**：
- ✅ 所有法律法规引用必须经过法规库验证
- ✅ 所有统计数据必须标注来源网址
- ⚠️ 无法验证的数据必须标注待核实
- ❌ 禁止使用"大约"、"约"、"估计"等模糊表述（除非来源明确使用）

**Regulatory Accuracy:**
- ✓ Standard numbers (CAS No. XXX)
- ✓ Clause citations (Article X, Clause Y)
- ✓ Effective dates (issued date, effective date)
- ✓ Scope of application (who/what it applies to)
- ✓ Amendment history (latest revision)

**Case Accuracy:**
- ✓ Company names (correct legal entity)
- ✓ Dates (audit period, report date)
- ✓ Amounts (financial figures, materiality)
- ✓ Events (timeline of what happened)
- ✓ Findings (accurate representation)

**Terminology Accuracy:**
- ✓ Audit terms (consistent with standards)
- ✓ Accounting terms (follow accounting standards)
- ✓ Legal terms (accurate legal language)
- ✓ Professional jargon (industry-standard usage)

**Common Issues to Check:**
- Confusing CAS with ISA requirements
- Citing outdated standards (before revision)
- Misquoting regulation clauses
- Inaccurate case details
- Inconsistent terminology
- **⚠️ CRITICAL: Fabricated data or references (must be corrected immediately)**

#### Round 2: Logical Coherence Review

**Chapter Logic:**
- ✓ Clear chapter hierarchy (numbering, levels)
- ✓ Smooth transitions (flow between sections)
- ✓ Logical progression (foundation → practice → cases)
- ✓ Balanced content (no sections too short/long)

**Argumentation Logic:**
- ✓ Complete logical chain (premise → reasoning → conclusion)
- ✓ Supported claims (every claim has evidence)
- ✓ Valid inferences (no logical fallacies)
- ✓ Clear connections (explicit links between ideas)

**Consistency Check:**
- ✓ Terminology consistency (same terms throughout)
- ✓ Data consistency (numbers match across references)
- ✓ Citation consistency (same citation format)
- ✓ Cross-reference accuracy (references point correctly)

**Common Issues to Check:**
- Contradictory statements in different chapters
- Unclear or missing transitions
- Unsupported assertions
- Inconsistent terminology
- Broken cross-references

#### Round 3: Practical Applicability Review

**Procedural Feasibility:**
- ✓ Complete steps (no missing procedures)
- ✓ Logical sequence (steps in right order)
- ✓ Actionable guidance (clear instructions)
- ✓ Realistic expectations (practical in real audits)

**Case Representativeness:**
- ✓ Typical scenarios (not outliers)
- ✓ Current relevance (not outdated)
- ✓ Complete information (all necessary details)
- ✓ Clear lessons (insights for readers)

**Recommendation Value:**
- ✓ Actionable suggestions (specific, implementable)
- ✓ Practical value (useful for practitioners)
- ✓ Evidence-based (supported by case findings)
- ✓ Responsible recommendations (feasible and appropriate)

**Common Issues to Check:**
- Procedures too theoretical (not practical)
- Cases atypical or outdated
- Recommendations too vague
- Missing implementation guidance
- Unrealistic expectations

#### Round 4: Format Standardization Review

**Citation Format:**
- ✓ Standard references: "CAS No. 1101 - [year]"
- ✓ Regulation citations: "《审计法》第X条"
- ✓ Case citations: "[Company] [Year] audit case"
- ✓ Literature citations: "[Author] ([year]), [Journal]"
- ✓ Consistent style throughout

**Table Consistency:**
- ✓ Table titles (clear and descriptive)
- ✓ Column names (consistent terminology)
- ✓ Formatting (统一的表格样式)
- ✓ Numbering (sequential: Table 1.1, 1.2, etc.)

**Heading Hierarchy:**
- ✓ Part numbering (Part 1, Part 2, etc.)
- ✓ Chapter numbering (Chapter 1, Chapter 2, etc.)
- ✓ Section numbering (1.1, 1.2, 1.2.1, etc.)
- ✓ Clear levels (visual distinction)

**Common Issues to Check:**
- Inconsistent citation formats
- Missing table titles or column names
- Non-uniform table formatting
- Inconsistent heading styles
- Missing figure captions

## Phase 7: Incremental Updates

When new standards, regulations, or cases become available:

1. **Categorize** new materials (standards, regulations, cases)
2. **Update CLAUDE.md** reference sources
3. **Update IMPLEMENTATION_PLAN.md** with new stage
4. **Identify insertion points** in book manuscript
5. **Update chapters** with new content
6. **Add new cases** if significant developments
7. **Update tables** with new data
8. **Expand references** with new sources

**Version control:**
```markdown
## Change Log
### [Date] - v1.1
- Updated Chapter 7 with new CAS No. XXXX [20XX]
- Added Case Study 5-4: [Company] [year] case
- Updated Table 7.1 with standards comparison
- Added references to new regulations: [regulation list]
```

## Special Considerations for Audit Books

### Regulatory Updates
- Track standard revisions (CAS, ISA, etc.)
- Monitor new regulations and amendments
- Update enforcement cases regularly
- Note effective dates and transition provisions

### Practical Relevance
- Balance theory with practice
- Include current and representative cases
- Provide actionable guidance
- Address real-world challenges

### Professional Standards
- Maintain professional objectivity
- Avoid definitive statements (use "generally," "typically")
- Acknowledge professional judgment
- Emphasize compliance requirements

### Reader Considerations
- Target audience definition (practitioners, students, researchers)
- Technical depth appropriate for audience
- Clear explanations of complex topics
- Practical examples and illustrations
