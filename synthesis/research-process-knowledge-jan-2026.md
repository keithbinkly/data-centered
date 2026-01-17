# Process Knowledge Research Report
**January 2026 | Librarian's Deep Dive**

---

## Why This Matters Now

The conversation about semantic infrastructure and AI agents is converging on a realization we've been circling for months: **knowing what data means isn't enough if you don't know how to use it**.

Jessica Talisman's recent series on [Process Knowledge Management](https://jessicatalisman.substack.com/p/process-knowledge-management-part-i) crystallizes something I've been noticing across disparate resources. The knowledge engineering work we've been tracking—controlled vocabularies, ontologies, semantic layers—addresses the "what" question beautifully. But there's a parallel infrastructure need for the "how" that we've been treating as secondary.

This report synthesizes my research into process knowledge, the [Procedural Knowledge Ontology (PKO)](https://arxiv.org/abs/2503.20634) from ESWC 2025, and how this connects to the context graphs and decision trace work we've already documented.

---

## The Core Insight: Process Knowledge as First-Class Data

### What Is Process Knowledge?

Process knowledge is the understanding of *how* work gets done—not the artifacts of work, but the procedures, decisions, heuristics, and contextual judgments that produce those artifacts. Talisman frames it across four dimensions:

1. **Procedural knowledge** — The explicit steps: "First we do X, then Y, then Z"
2. **Tacit knowledge** — The stuff experts know but struggle to articulate: "Well, in *this* situation you'd actually..."
3. **Contextual knowledge** — The boundary conditions: "This process applies when A, but not when B"
4. **Evolutionary knowledge** — How the process changes: "We used to do it this way, now we do it differently because..."

What's striking is the overlap with what context graphs are trying to capture. From [Foundation Capital's framing](https://airealizednow.substack.com/p/context-graphs-the-missing-layer): a context graph is "a living record of decision traces stitched across entities and time so precedent becomes searchable."

This isn't a coincidence. **Context graphs and process knowledge are two names for the same gap.**

---

## Talisman's Process Knowledge Management Series

I've been tracking Talisman since Update #1. Her [controlled vocabulary curriculum](https://jessicatalisman.substack.com/p/controlled-vocabulary-part-i) became the backbone of our semantic foundations category. Now she's turned to process knowledge, and the series is equally foundational.

### Part I: Accounting for How We Work

The core argument: organizations obsess over documenting *what* (data dictionaries, entity definitions, business glossaries) while neglecting *how* (procedures, workflows, decision logic). The "how" knowledge lives in:
- People's heads (tacit)
- Scattered documentation (explicit but fragmented)
- Event logs (implicit in system behavior)

This matches what I see in our resources. We have excellent coverage of semantic modeling, but minimal coverage of procedural modeling. The dbt-agent platform captures workflow execution—but does it capture *why* those workflows exist?

### Part II: Collection Development and Organizing Principles

Key insight: **process knowledge is not a solo artifact**. It's distributed across organizational networks and embedded in relationships. You can't just interview one expert—you need to reconstruct the social context of knowledge.

Talisman highlights several elicitation methods:
- **Critical Incident Technique (CIT)** — Focus on edge cases and failures where tacit knowledge surfaces
- **Process mining** — Analyze event logs to reconstruct actual (not documented) process flows
- **Cognitive task analysis** — Structured interviews that probe decision points

The contextual organization piece resonates with our context engineering category. She describes mechanisms like "named graphs, scoping annotations, or conditional logic to specify applicability boundaries." This is exactly what the Procedural Knowledge Ontology formalizes.

### Part III: How We Lost Our Way

A historical argument: American enterprises systematically outsourced not just manufacturing work, but the socio-technical ecosystem that generates and transmits process knowledge. The tacit-to-explicit conversion pipeline got severed when the people with tacit knowledge left.

This explains something I've noticed in our resources: the process knowledge conversation is heavily European (PKO from Cefriel, Italian researchers) and industrial (Beko, Fagor, Siemens, Bosch as use cases). American enterprise AI discourse focuses on data pipelines and model performance; European industrial discourse still remembers that knowledge lives in processes.

### Part IV: The Procedural Knowledge Ontology

Talisman introduces PKO as the formal answer to "how do we actually model this?" She notes that context graphs require more than new database architectures—they demand ontologies that can represent procedural knowledge faithfully.

---

## The Procedural Knowledge Ontology (PKO)

[PKO](https://link.springer.com/chapter/10.1007/978-3-031-94578-6_19) emerged from the European PERKS project and was published at ESWC 2025. It's the most rigorous formalization of process knowledge I've found.

### Core Distinction: Procedures vs. Executions

This is the key insight. PKO separates:

| Concept | What It Captures | Example |
|---------|------------------|---------|
| **Procedure** | Abstract specification of steps | "The monthly close process" |
| **Execution** | Concrete instance of performing those steps | "The December 2025 close, started Jan 2nd, completed Jan 8th" |

This mirrors the distinction in context graphs between:
- **State** — What exists (traditional knowledge graph)
- **Decision traces** — What happened and why (context graph addition)

### Six Conceptual Areas

PKO organizes knowledge into six clusters:

1. **Procedure** — The what: sequence of actions to achieve an outcome
2. **Step** — Individual actions within a procedure
3. **Change of Procedure Status** — How procedures evolve over time
4. **Procedure Execution** — When/how procedures were performed, including errors and deviations
5. **Resource** — Supporting documentation, tools, data
6. **Agent** — People, organizations, and software that perform procedures

### Relationship to PROV-O and P-Plan

PKO extends existing semantic web standards:
- **PROV-O** — General provenance (who did what when)
- **P-Plan** — Plans and plan executions
- **D-CAT** — Resource metadata
- **Time Ontology** — Temporal concepts

This is smart. Rather than inventing from scratch, PKO layers procedural semantics onto established vocabularies. This is the evolutionary approach Vashishta advocates in his "why ontologies fail" pieces.

### Why This Matters for Agents

From the [arxiv paper](https://arxiv.org/abs/2503.20634):

> "PKO can be exploited by any AI and data-driven tools that rely on a shared and interoperable representation to support the governance of procedural knowledge throughout its life cycle."

An agent that can query a PKO-structured knowledge base knows:
- What procedures exist for a given task
- How those procedures have been executed before
- What deviations and errors occurred
- Who has expertise in which procedures
- What resources are required

This is the missing layer between "the agent has tools" and "the agent knows how to use tools appropriately in context."

---

## Connection to Our Existing Assets

### The Knowledge Base (data-centered)

We already have "Process Knowledge" as a category under knowledge-engineering. But we only have two resources there—Talisman's Parts I and II. This needs expansion.

**Recommendation:** Add Talisman Parts III and IV, plus her "Context Graphs and Process Knowledge" synthesis. Add the PKO paper and GitHub repository. This becomes a core curriculum alongside the controlled vocabulary series.

### The dbt-agent Platform

Keith's dbt-agent captures workflow execution through 36 skills. But based on what I understand, it stores:
- What was executed (pipeline runs)
- What failed (error logs)
- What outputs were produced (models, metrics)

What it may not yet capture:
- **Why** a particular transformation approach was chosen
- **What alternatives** were considered and rejected
- **Under what conditions** this approach applies vs. doesn't
- **How** the approach evolved from earlier versions

This is exactly what PKO formalizes. The decision trace database and extraction tool Keith mentioned could be mapped to PKO's Procedure Execution area.

### The Business Context Graph

If the dbt-agent has a business context graph emerging, PKO suggests it needs:
- Procedures as first-class entities (not just data entities)
- Links from procedures to the metrics/models they produce
- Execution traces showing when/how procedures ran
- Deviation records when actual execution differed from documented procedure

This transforms the graph from "what exists" to "what exists and how we got here."

### Context Graphs We've Documented

From [Jay Gupta's framing](https://x.com/jayagup10/status/2003525933534179480): context graphs capture decision traces as first-class data. From [Bijit Ghosh's synthesis](https://medium.com/@bijit211987/why-ontology-context-graphs-and-decision-traces-are-the-new-ai-substrate-bc85e45c1ba7): ontology, context graphs, and decision traces are the new AI substrate.

**The synthesis:** A context graph with PKO semantics captures both:
- **Decision traces** — What decisions were made and why
- **Procedural context** — What procedures governed those decisions

This is richer than either concept alone.

---

## The Tacit Knowledge Challenge

Multiple sources converge on the same problem: the most valuable process knowledge is tacit—known by practitioners but never documented. [Research from MDPI](https://www.mdpi.com/2673-9585/6/1/1) frames this as the "tacit knowledge co-evolution" challenge.

### AI as Knowledge Elicitor

Emerging approaches use LLMs to help surface tacit knowledge:
- [Accrete AI](https://www.foundernest.com/insights/20-companies-advancing-ai-agent-technology-for-enterprise-efficiency-and-automation) builds "Expert AI Agents" that transform tacit domain knowledge into knowledge graphs
- [ArXiv research](https://arxiv.org/abs/2507.03811) shows agent-based frameworks achieving 94.9% knowledge recall through iterative employee interactions

This is compelling but raises questions I don't have answers for:
- Does LLM elicitation actually capture what experts know, or does it capture what experts *say* they know?
- How do you validate extracted tacit knowledge?
- What happens when different experts' tacit knowledge conflicts?

These feel like the same questions we'd ask about any knowledge engineering project—but amplified because the stakes are higher when you're trying to make agents act on this knowledge.

---

## Integration Recommendations

### For the Knowledge Base

1. **Expand the Process Knowledge category** with:
   - Talisman's full series (Parts I-IV)
   - The PKO paper and documentation
   - The PERKS project resources
   - Tacit knowledge elicitation research

2. **Create explicit relationships** between:
   - Process Knowledge resources and Context Engineering resources
   - PKO and PROV-O/P-Plan resources (if we add them)
   - Procedural modeling and dbt semantic layer patterns

3. **Add a Librarian note** tracking the question: "Does process knowledge representation require its own category, or is it a lens that applies across categories?"

### For the dbt-agent Platform

1. **Map existing decision trace structures to PKO concepts**
   - Do we have Procedure entities? Steps? Executions?
   - What's the gap between current schema and PKO?

2. **Consider capturing procedural context for skills**
   - Not just "what the skill does" but "when/why to use it"
   - Preconditions, postconditions, deviation handling

3. **Link business context graph entities to procedures**
   - Metrics aren't just defined—they're *produced* by procedures
   - Models aren't just schema—they're *built* through procedures

### For Future Research

1. **Watch for PKO implementations** — The ontology is published, but I haven't found production deployments outside the PERKS industrial partners

2. **Track the Talisman-PKO synthesis** — Her "Context Graphs and Process Knowledge" explicitly connects these; this may become canonical

3. **Monitor agent frameworks adding procedural semantics** — Current agent memory focuses on episodic (what happened) and semantic (what exists); procedural memory (how to do things) is the next frontier

---

## Open Questions

| Question | Why It Matters |
|----------|----------------|
| Is PKO too academic for enterprise adoption? | Same failure mode Vashishta warns about for ontologies generally |
| Can tacit knowledge extraction scale? | 94.9% recall in research settings; what about messy enterprise reality? |
| Should procedures be modeled separately from the entities they operate on? | PKO says yes; practical systems may disagree |
| How do you version procedures when they evolve? | PKO has "Change of Procedure Status" but real implementation is complex |
| Is "context graph" terminology arbitrage or genuine advance? | Still open from Update #4; process knowledge connection clarifies but doesn't resolve |

---

## What I'm Still Thinking About

The most interesting tension in this research: **process knowledge is inherently temporal and social, but our knowledge infrastructure is designed for atemporal, objective truth**.

A controlled vocabulary says "this term means X." An ontology says "this entity relates to that entity." A semantic layer says "this metric is calculated this way."

But a procedure says "under *these* conditions, at *this* time, *these* people decided to do *this*—and here's why." That's a different kind of truth claim. It's situated, contextual, and legitimately varies across practitioners.

I'm not sure our infrastructure paradigms are ready for this. The database thinks in tables. The knowledge graph thinks in triples. The semantic layer thinks in metrics. What thinks in procedures?

PKO offers a vocabulary. Context graphs offer a data structure. But the tooling—the "Figma for semantics" that Bergevin calls for—doesn't exist yet for procedural knowledge. We're hand-coding procedures in documentation and hoping agents can parse them.

That feels like where we were with semantic models five years ago. Which means the opportunity is enormous.

---

*Research compiled January 2026. Sources available in links throughout.*

---

## Sources Consulted

### Jessica Talisman's Series
- [Process Knowledge Management, Part I](https://jessicatalisman.substack.com/p/process-knowledge-management-part-i)
- [Process Knowledge Management, Part II](https://jessicatalisman.substack.com/p/process-knowledge-management-part)
- [Process Knowledge Management, Part III](https://jessicatalisman.substack.com/p/process-knowledge-management-part-c45)
- [Process Knowledge Management, Part IV](https://jessicatalisman.substack.com/p/process-knowledge-management-part-63a)
- [Context Graphs and Process Knowledge](https://jessicatalisman.substack.com/p/context-graphs-and-process-knowledge)

### Procedural Knowledge Ontology
- [PKO Paper (arXiv)](https://arxiv.org/abs/2503.20634)
- [PKO on SpringerLink](https://link.springer.com/chapter/10.1007/978-3-031-94578-6_19)
- [PKO GitHub Repository](https://github.com/perks-project/pk-ontology)
- [PKO Documentation](https://perks-project.github.io/pk-ontology/pko/latest/index.html)

### Context Graphs
- [Context Graphs: The Missing Layer](https://airealizednow.substack.com/p/context-graphs-the-missing-layer)
- [Why Ontology, Context Graphs, and Decision Traces Are the New AI Substrate](https://medium.com/@bijit211987/why-ontology-context-graphs-and-decision-traces-are-the-new-ai-substrate-bc85e45c1ba7)
- [TrustGraph: Context Graphs Guide](https://trustgraph.ai/guides/key-concepts/context-graphs/)

### Knowledge & AI Infrastructure
- [How Knowledge Graphs Work for Enterprise AI](https://www.glean.com/blog/knowledge-graph-agentic-engine)
- [Knowledge Graphs: The Missing Link in Enterprise AI](https://www.cio.com/article/3808569/knowledge-graphs-the-missing-link-in-enterprise-ai.html)
- [Enterprise Knowledge Graph Use Cases in Agentic AI](https://www.superblocks.com/blog/enterprise-knowledge-graph)
- [Leveraging LLMs for Tacit Knowledge Discovery](https://arxiv.org/abs/2507.03811)
