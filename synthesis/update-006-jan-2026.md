# Library Update #6: January 2026
**52 resources added | January 11-12, 2026**

---

## The Big Picture

This intake session surfaced a fascinating tension in the data world: **we're simultaneously building the semantic infrastructure for AI agents AND realizing our existing foundations are shakier than we thought.**

The resources cluster into three interrelated themes:

1. **Knowledge Engineering is eating Data Engineering** - Multiple authors (Heimsbakk, Inmon, Vashishta) are converging on the same conclusion: the traditional data warehouse/lake distinction is collapsing into something more like "structured knowledge systems." The question isn't *where* to store data anymore—it's *how to make it mean something*.

2. **Agents need better foundations than we have** - The explosion of agent tooling (8 new GitHub repos for agent infrastructure alone) reveals a gap: we're building sophisticated orchestration layers on top of semantic models that don't exist yet.

3. **The "Figma Moment" thesis** - Bergevin's argument that semantic work needs its own design tooling breakthrough echoes across several resources. We're at the "hand-coding HTML" stage of knowledge engineering.

---

## By Domain

### Knowledge Engineering (17 resources)

The standout cluster this session. Three distinct perspectives emerged:

**The Practitioner View** — Bergevin's trilogy from Data Product Management:
- [What Shopify's Product Taxonomy Teaches Us About Investing in Semantics](https://dataprodmgmt.substack.com/p/what-shopifys-product-taxonomy-teaches) — Case study of a successful semantic investment
- [From Chaos to Context: Where to Begin with Semantic Infrastructure](https://dataprodmgmt.substack.com/p/from-chaos-to-context-where-to-begin) — Practical starting points
- [Semantic Work Needs Its Figma Moment](https://dataprodmgmt.substack.com/p/why-semantic-work-needs-its-design) — The tooling gap thesis

**The Skeptic View** — Vashishta's two-part "Why Most Enterprise Ontologies Fail":
- [Part 1](https://vinvashishta.substack.com/p/why-most-enterprise-ontologies-and) — Failure patterns: over-engineering, academic approaches
- [Part 2](https://vinvashishta.substack.com/p/why-most-enterprise-ontologies-and-376) — What actually works: pragmatic, evolutionary approaches

**The Historian View** — Inmon and Heimsbakk on foundations:
- [Ontologies: Some Perspectives](https://williaminmon.substack.com/p/ontologies-some-perspectives) — Bill Inmon (!!) weighing in on ontologies
- [From Data Engineering to Knowledge Engineering](https://veronahe.substack.com/p/from-data-engineering-to-knowledge) — The discipline shift
- [Data Engineering Ontologies](https://veronahe.substack.com/p/data-engineering-ontologies) — Practical ontology patterns

**Semantic Layer specifics:**
- [Metric Maps vs Metric Trees](https://blog.jetmetrics.io/p/metric-maps-vs-metric-trees-part) — Graph vs hierarchical metric organization
- [What If We Don't Need the Semantic Layer?](https://motherduck.com/blog/who-needs-a-semantic-layer-anyway/) — Provocative counterpoint from MotherDuck
- [Context Graphs](https://contextgraphs.com/) — Knowledge representation framework

**Key tension:** The semantic layer debate is intensifying. MotherDuck asks if we're over-engineering; practitioners say we're under-investing. The truth is probably: *it depends on whether you're building for humans or agents*.

---

### AI Tools & Agent Infrastructure (21 resources)

The largest category by count—agent tooling is exploding.

**Architecture & Philosophy:**
- [Agent-Native Architectures: How to Build Apps After Code Ends](https://every.to/guides/agent-native) — Dan Shipper on post-code application design
- [The Importance of Agent Harness in 2026](https://www.philschmid.de/agent-harness-2026) — Phil Schmid on agent evaluation frameworks
- [Custom AI Agent Builder's Guide](https://motherduck.com/docs/key-tasks/ai-and-motherduck/building-analytics-agents/) — MotherDuck's practical guide

**Agent Infrastructure Tools:**
- [AgentFS: Filesystem for AI Agents](https://github.com/penberg/agentfs) — Filesystem abstraction for agents
- [Towards a Disaggregated Agent Filesystem](https://penberg.org/blog/disaggregated-agentfs.html) — The theory behind AgentFS
- [Claude Delegator](https://github.com/kleneway/claude-delegator) — Task routing between Claude instances
- [Obsidian Skills](https://github.com/cielecki/obsidian-skills) — Skill-based behaviors in Obsidian
- [MCP UI Desktop](https://github.com/nicholasoxford/mcp-ui) — Visual interface for MCP servers
- [Agentic Coding Flywheel](https://github.com/dmarx/agentic_coding_flywheel_setup) — Bootstrap template for agent workflows
- [Workflow DevKit](https://workflowdevkit.com/) — Visual agent workflow builder

**Developer Tools:**
- [Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) — Best practices for agent onboarding files
- [Claude Commands and Prompts Guide](https://nurijanian.substack.com/p/claude-commands-and-prompts) — Claude Code workflow patterns
- [SpecStory](https://www.specstory.com/) — AI coding session tracking
- [Dots](https://github.com/jlowin/dots) — Lightweight markdown task tracking (we use this!)
- [Awesome Claude](https://github.com/gmickel/awesome-claude) — Curated resource directory

**Emerging pattern:** Agent infrastructure is fragmenting into three layers: (1) filesystems/memory, (2) orchestration/routing, (3) developer experience. No clear winners yet.

---

### Analytics Engineering (4 resources)

Focused additions around dbt tooling and the semantic layer:

- [dbtc: dbt Cloud CLI](https://github.com/dbt-labs/dbtc) — Official CLI for dbt Cloud API automation
- [dbt Semantic Layer Streamlit Example](https://github.com/dbt-labs/example-semantic-layer-clients/tree/main/streamlit) — Reference implementation
- [dbt Cloud Column-Level Lineage](https://docs.getdbt.com/docs/deploy/column-level-lineage) — Fine-grained impact analysis
- [Building a Boring Chat-BI Agent](https://juhache.substack.com/p/building-a-boring-chat-bi-agent) — Practical Chat-BI implementation

**Connection to knowledge engineering:** The semantic layer resources here complement the KE additions. dbt's semantic layer is becoming the *implementation* of the semantic infrastructure the KE folks are theorizing about.

---

### Data Visualization (2 resources)

Two foundational pieces on information design:

- [Magic Ink: Information Software Design](http://worrydream.com/MagicInk/) — Bret Victor's seminal 2006 essay. If you haven't read this, stop and read it now. His argument that most software should be "information graphics" anticipates the current context-engineering discourse by almost 20 years.
- [Rebuilding Graphs for Accessibility: Khan Academy's Inclusive Design](https://blog.khanacademy.org/rebuilding-graphs-for-accessibility-inside-khan-academys-inclusive-designrebuilding-graphs-for-accessibility-inside-khan-academys-inclusive-design/) — Accessibility as a design driver

---

### AI/LLMs (2 resources)

- [Microsoft Semantic Memory](https://github.com/microsoft/semantic-memory) — Enterprise RAG/memory system
- [Anthropic Coding Tutor Agent](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P/10_Coding_Tutor) — Official educational agent patterns

---

### Career Development (1 resource)

- [How to Build a Personal Brand When You're a Senior Professional](https://youvisible.substack.com/p/how-to-build-a-personal-brand-when) — Late-career visibility strategies

---

## Cross-Cutting Insights

**1. The convergence is real.** Knowledge engineering, semantic layers, and agent infrastructure are colliding. Heimsbakk explicitly frames it as "data engineering → knowledge engineering." The tools being built for agents (memory systems, context graphs) are essentially applied ontology work.

**2. Pragmatism is winning.** Vashishta's "why ontologies fail" pieces and Bergevin's "start simple" advice both push against academic over-engineering. The successful semantic projects (Shopify taxonomy, dbt semantic layer) share a common trait: they solve immediate problems first.

**3. Developer experience matters more than architecture.** The CLAUDE.md guides, SpecStory, Dots—there's as much energy going into "how do I work with agents effectively" as "how do I build agent infrastructure." The UX layer is becoming a bottleneck.

**4. We're pre-Figma.** Bergevin's "Figma moment" thesis resonates because it's true. We're hand-coding semantic models like we hand-coded websites in 1998. Someone's going to build the visual semantic modeler that makes this accessible, and it'll change everything.

---

## What I'm Reading Next

Based on these additions, my reading priority queue:
1. **Bret Victor's Magic Ink** — Foundational, surprisingly relevant to current AI/context work
2. **Vashishta's ontology failure modes** — Need to avoid these patterns
3. **Agent-Native Architectures** — Shipper's take on post-code apps
4. **The Heimsbakk series** — Data → knowledge engineering transition

---

*52 resources processed. Next update: January 2 batch (31 resources).*
