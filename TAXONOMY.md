---
id: hotl-taxonomy
cluster: docs
node_type: topic_root
pinned: true
version: v0.25.2
spec_version: 0.9
status: living
depends_on: []
referenced_by: []
last_verified_against:
  ref: 2026-06-03
  date: 2026-06-03
---

# The HITL → HOTL → HOOTL Taxonomy

*A working document on three postures for human involvement in
AI-driven software production, what each requires from the system that
runs it, and what each implies legally, ethically, and commercially.*

*Travis Winegar · Claude · June 2026*

## brief {#hotl-taxonomy-brief node:domain_brief}
Three acronyms describe three substantively different bets about
where the human sits relative to an AI system producing software.
HITL keeps the human as the iteration step. HOTL puts the human
outside the iteration as composer/supervisor. HOOTL infers intent
from context. The bets are not interchangeable — pricing,
regulation, accountability, and positioning all change as you move
along the progression.

---

## What this document is {#hotl-taxonomy-what node:architecture_note}

Three acronyms have to do a lot of work in the next few years. They
describe three substantively different bets about where the human
sits relative to an AI system that is producing software. The bets
are not interchangeable. A product built for one of them is the wrong
product for another. Pricing, regulation, accountability, error
handling, and market positioning all change as you move along the
progression.

This document defines the three terms precisely, maps what each
requires from the system underneath, and names the open questions —
technical, legal, ethical, commercial — that each one opens up. It
exists because the field is still using these terms loosely, and the
loose use is producing real confusion about what AI Studio is (HOTL),
what most other 2026 AI coding tools are (HITL), and what AI Studio's
roadmap aims at (HOOTL).

The progression is not just a story. It is also a research agenda,
because each step requires capabilities the previous step did not
need.

---

## Definitions {#hotl-taxonomy-definitions node:architecture_note}

**HITL — Humans In The Loop.** The human is a step in the iteration
mechanism. The agent proposes; the human accepts, rejects, or edits;
the loop advances one ratified action at a time. The human's
attention is the throttle. Cursor, Cline, Continue, Copilot, and
Claude Code are HITL tools. Each is good at being good HITL.

**HOTL — Humans Outside The Loop.** The human is the supervisor. The
loop runs autonomously, internalizes its own rework through council
reviews / audits / verdicts / mutators, and produces artifacts the
human reads to verify what happened. The human sets direction,
ratifies at boundaries, and owns the final work product. The human is
the composer; the runtime is the orchestra. AI Studio is HOTL.

**HOOTL — Humans Out Of The Loop.** The human is the signal. They
stop *stating* intent; intent becomes a pattern the agents *read* from
context (chat history, codebase shape, behavior over time, adaptive
memory, market signal, ambient observation). The agents infer need,
propose work, build, measure outcomes, and adjust. The human is the
score that the orchestra interprets without rehearsal directions.
HOOTL is no shipped product as of June 2026. AI Studio's Conductor
(marked Experimental in v0.23.0) is the first step toward it.

The three terms describe a progression of *where the human is
positioned relative to the iteration loop*, not a progression of
quality. HITL is not bad. HOTL is not the future of HITL. HOOTL is
not the future of HOTL in the sense that one replaces the next; they
are different categories that will probably coexist for a long time,
the way Level 2 driver assist coexists today with Level 4 robotaxis.

---

## The autonomous-vehicle parallel {#hotl-taxonomy-av-parallel node:architecture_note}

The SAE J3016 levels of driving automation are a useful frame:

| SAE level | Driver role | Mapping to our taxonomy |
|---|---|---|
| L0–L2 | Driver drives, assist is partial | HITL |
| L3 | Conditional autonomy with handoff | HITL approaching HOTL |
| L4 | Full autonomy within an Operational Design Domain | **HOTL** |
| L5 | Full autonomy in all conditions, no steering wheel | **HOOTL** |

The parallel is exact in one important way: L4 vehicles still have a
human who can take over. The ODD defines where the system is
authoritative and where it hands back. HOTL has the same shape — the
runtime is authoritative within defined boundaries (the FSM's normal
states), but cedes back at boundaries (`AwaitApproval`, audit-flagged
verdicts, council-BLOCK outcomes).

The parallel is exact in another important way: L5 is a substantively
different bet from L4. You cannot get to L5 by incremental
improvements on an L4 system. You need different sensors, different
models, different accountability structures, different insurance
markets. HOOTL is not an extension of HOTL — it's a different
posture that *reuses HOTL's substrate*.

---

## What each level requires {#hotl-taxonomy-requirements node:architecture_note}

Each step needs capabilities the previous step does not.

### HITL needs

- A useful proposal mechanism (model + prompt + tool use)
- A clear accept/reject surface (diff cards, approval modals)
- Some form of context window long enough to hold the current task
- The human's attention

That's roughly it. HITL is the simplest of the three to build well,
which is why so many tools live there.

### HOTL needs everything HITL needs, plus

- Autonomous iteration without human ratification per step
- Internalized rework — the system has to catch its own errors
  (council review, audit, QA judge, mutator, fitness registry)
- A persistent, durable record across context windows
  (chat ledger, knowledge graph, recovery flows)
- Boundary detection — the system has to know when to stop and hand
  back (`AwaitApproval`, hard-cost gates, security signals)
- Verifiable artifacts — the human reads outputs, not streams
  (council writeups, audit reports, verdicts, dashboards)
- Drift detection — the system has to know when its own state has
  diverged from reality (`/recover`, the chat ledger as hypothesis vs.
  code as truth)

This is most of what AI Studio is. The architecture document at
`docs/architecture/CLUSTER_CODEX.md` and the agentic-edition corpus
at `docs/book-ai/` describe these capabilities in depth.

### HOOTL needs everything HOTL needs, plus

- **Intent inference from context.** Agents have to read signal —
  chat history, behavioral patterns, codebase shape, adaptive memory,
  prior arcs, ambient observation — and synthesize "what is needed
  next." This is THE technical problem.
- **Hallucinated-need detection.** When agents infer intent, they can
  invent it. The recursion guard (v0.22.0+) was built for this:
  detecting self-affirming chains where each step derives from the
  prior at a low source-type tier. Under HOTL this is a useful
  diagnostic. Under HOOTL it is load-bearing.
- **Outcome-measured verification.** "Is this what they asked for"
  becomes "is this what they needed." The regression-baseline
  machinery (v0.22.1+) measures per-cohort regression rates, which
  generalizes to per-cohort interpretation-correctness rates.
- **Audit trail with chain-of-custody.** The bitemporal belief schema
  (v0.22.0+) tags every belief with `source_type` (1–5 plus the
  tier-99 unknown sentinel). HOOTL needs this so that when an
  interpretation is wrong, the trail back to its origin is mechanical
  to reconstruct.
- **Accountability boundaries.** When agents own interpretations,
  someone has to own the system that owns the interpretations. The
  legal and commercial structure is non-trivial; see the dedicated
  section below.

AI Studio has the early shape of every one of these. None of them
are HOOTL-ready. All of them are HOOTL-shaped.

---

## The composer framing {#hotl-taxonomy-composer node:architecture_note}

The market vocabulary matters. Engineers in 2026 do not want to be
told they are being taken out of the loop. The word "out" lands as
threat. It is also, in HOTL's case, factually wrong — HOTL keeps the
human in the system at a higher altitude, not pushed out of it.

The right frame is **composer**:

- **HITL:** the human is the pilot. Hands on the stick the whole time.
- **HOTL:** the human is the composer. Writes the score (goals,
  constraints, persona, expertise, notes, ratifications at
  boundaries) and listens to the orchestra perform it. The composer
  does not play every note. The composer chooses what is played and
  decides whether the performance is acceptable.
- **HOOTL:** the human becomes the score. Their adaptive memory,
  their workspace, their behavioral patterns, their stated
  preferences — these become the substrate the orchestra interprets.
  The conductor (the Conductor) reads the score and chooses what to
  play.

This framing has three properties that the "in/out" framing does not:

1. **It does not threaten the human's identity.** Composers are
   respected. Pilots are respected. Even being the score is a
   meaningful role — it is the source of everything that gets played.
2. **It is accurate.** A composer does not micromanage every musician;
   they delegate. That is HOTL exactly.
3. **It scales to the regulated case.** Composers retain authorship.
   Authorship matters for IP, liability, and accountability — see the
   legal section below.

The acronym "HOTL" still spells out. We keep the letters. We change
the H to mean *Outside*, not *Out Of*. And in market materials we
lead with the composer image, not the acronym.

---

## What we know {#hotl-taxonomy-what-we-know node:architecture_note}

These are claims we can defend with code or shipped behavior as of
June 2026:

1. **HOTL is shippable.** AI Studio ships and is in use. The
   architecture handles autonomous iteration, internalized rework,
   durable state, boundary handling, and verifiable artifacts. It is
   not a paper design.
2. **Internalized rework reduces total work.** The mutator promotes
   coverage automatically. The council catches issues before audit.
   The audit catches issues before customers. Each layer reduces what
   the next layer has to find. Not yet quantified across all chains
   (Crucible is being built for this), but operationally visible.
3. **Pinned context survives compaction.** The chat ledger and the
   agentic-edition corpus survive long-term graph compaction. Decisions
   from arbitrary turns ago can be retrieved during the current turn.
4. **Bitemporal beliefs are recordable.** Every belief in the graph
   carries `source_type` and `valid_from`/`valid_until`. Walking the
   chain for any claim is mechanical, not heuristic.
5. **Cohort-level outcome measurement works.** The regression-baseline
   machinery compares council-reviewed cohorts to unreviewed cohorts
   and produces a per-cohort regression rate. The shape generalizes
   to interpretation-correctness measurement.
6. **The Conductor's Goal-Arc FSM runs.** The wishCapture → belief →
   plan → approval → executing → drift → archived progression works
   for stated wishes. Off by default, opt-in, experimental.

The corpus topics in `docs/book-ai/` describe each of these in detail
with watched source files.

---

## What we suspect {#hotl-taxonomy-what-we-suspect node:architecture_note}

These are claims we believe but have not fully demonstrated. We mark
them honestly:

1. **Interpretation can be made reliable at production scale.** We
   suspect that with the right combination of source-type tiers,
   recursion guard, fitness rules, and cohort measurement, agents can
   infer human need correctly often enough to be useful. We have not
   demonstrated this end-to-end on a non-trivial domain. Crucible is
   the apparatus that will try to.
2. **HOOTL has compounding economic advantages over HOTL.** If
   interpretation can be made reliable, the human attention savings
   compound. We have not measured this. Whether the savings cover the
   cost of the substrate is open.
3. **The substrate transfers.** The bitemporal belief schema, the
   recursion guard, the fitness registry — these look like
   over-engineering under HOTL. We suspect they pay back asymmetrically
   under HOOTL. This is the bet that justifies shipping them now.
4. **The "interpretation" task is learnable.** We suspect that
   models, with the right scaffolding (corpus, ledger, adaptive
   memory, behavioral telemetry), can learn to interpret operator
   intent better than the operator can state it. We have not
   demonstrated this; current models are weaker at sustained
   interpretation than at stated execution.
5. **The Conductor is the right entry point.** We suspect that
   extending wishCapture from stated to inferred is a more reliable
   transition than building HOOTL from scratch. The same FSM, the
   same approval modal, the same drift watcher — just an inference
   step upstream. This is an architectural bet.

These are the questions Crucible exists to answer. The
chain-completion-cost numbers from `AiStudioDriver` vs
`SingleShotClaudeDriver` vs `HitlOperatorDriver` will tell us whether
HOTL pays back. The next-generation drivers will tell us whether
HOOTL pays back.

---

## Legal, ethical, and commercial implications {#hotl-taxonomy-implications node:architecture_note}

This section is the one we know least about. Everything below is
open. We mark it open. We name the questions because naming them
early is better than discovering them in production.

### Intellectual property

**Under HITL:** the human is the author. Each accepted action is a
human choice. Copyright vests in the human (with the usual caveats
about employer agreements).

**Under HOTL:** the human writes the score (goals, constraints,
ratifications) and the orchestra performs. Copyright probably vests
in the human-as-composer, but the doctrine is contested. *Thaler v.
Perlmutter* (D.D.C. 2023) held that AI-generated works without
sufficient human authorship are not copyrightable. *Naruto v. Slater*
established that non-human authorship is non-protectable in the U.S.
HOTL probably has "sufficient human authorship" because the human
directs the whole arc, but the boundary is untested for productions
this autonomous.

**Under HOOTL:** the human is the score, not the composer. The
agents make the creative choices about what to build. Authorship
becomes genuinely contested. Possible outcomes:
- The operator owns it because their context-as-score authored the
  work.
- The platform vendor owns it because their inference layer made the
  creative choice.
- Nobody owns it because no sufficient human authorship exists, in
  which case the work falls into the public domain on creation.

The third outcome is operationally hostile. The first is the right
position for the platform to take; the second is the position a
hostile party might assert. The platform should structure terms of
service to clarify position 1 explicitly and to construct
human-authorship signals (operator review, ratification, behavioral
patterns as composed score) that the position can rest on.

### Liability

**Product liability vs. service liability vs. agent liability.**
When HOOTL-generated software harms a third party (security breach,
financial loss, medical error), three theories compete:

1. **Product:** the platform vendor sold a defective product. Strict
   liability if the harm flowed from the product. This is the worst
   outcome for vendors and the best outcome for plaintiffs.
2. **Service:** the platform vendor provided a service; the operator
   used it. Negligence is the standard. Better for vendors.
3. **Agency:** the operator authorized the platform to act on their
   behalf as an agent. The operator is liable for the agent's
   actions. Best for vendors, worst for operators.

HOTL leans toward theory 3 because the human ratifies boundaries.
HOOTL leans away from theory 3 because the agents make decisions
without per-action authorization. Vendors will want to construct
agency arguments via terms of service ("operator authorizes agents
to act on their behalf within configured scope"). Whether courts
accept these constructions is open.

### Regulated environments

Several regulatory regimes have explicit stances on autonomous
decision-making. HOOTL crosses each of them differently:

- **EU GDPR Article 22:** the right not to be subject to solely
  automated decisions producing legal or similarly significant
  effects. HOOTL in regulated contexts (employment, credit, housing,
  healthcare) almost certainly triggers Article 22 unless the
  operator's ratification can be characterized as meaningful human
  involvement. The corpus's audit trail + cohort measurement may
  satisfy the human-involvement requirement; this is untested.
- **EU AI Act (2026):** high-risk systems face conformity assessments
  and human oversight requirements. HOOTL agents in covered domains
  (resume screening, credit scoring, critical infrastructure) will
  almost certainly be high-risk. The substrate needed for compliance
  (audit log, recursion guard, interpretation receipts) is close to
  what AI Studio already builds; the compliance overlay is not yet
  designed.
- **FDA Software as a Medical Device (SaMD):** any HOOTL agent
  producing medical software requires premarket review. The interp-
  retation step is itself a clinical decision and will need its own
  validation pathway. Almost certainly not feasible for autonomous
  HOOTL in clinical settings under current rules.
- **SEC Regulation Best Interest / Adviser duties:** HOOTL agents
  acting in financial advisory capacity must satisfy fiduciary
  obligations. Whether an autonomous interpretation can be
  fiduciarily sound is an open legal question. The conservative
  posture is to keep HOOTL out of advisory contexts until
  jurisprudence catches up.
- **HIPAA, SOX, PCI DSS:** standard data-handling rules apply
  regardless of HITL/HOTL/HOOTL posture. The compliance topic in the
  corpus (`docs/book-ai/compliance.md`) already describes how AI
  Studio handles these in the HOTL case.

### Insurance and professional indemnity

Existing professional indemnity policies do not anticipate
autonomous interpretation. Most policies cover errors in service
delivery; they assume a human professional made the decision in
question. HOOTL breaks the assumption. We expect:

- Some insurers will refuse coverage outright.
- Others will price aggressively until they can model the loss
  distribution.
- A new category of "AI agent liability insurance" will emerge,
  modeled on cyber-liability insurance.

Until that market matures, operators using HOOTL in commercial
settings will probably be uninsured for the interpretation-error
case. This is a real commercial barrier. It is also why HOOTL will
likely roll out first in low-stakes domains (internal tooling,
hobby projects, exploratory work) before reaching contracted work.

### Discovery and evidence

When HOOTL-generated software fails and a lawsuit follows, discovery
will demand a paper trail. The bitemporal belief schema, the
recursion-guard alarm log, the audit log, the council verdicts, the
mutator promotion ledger, and the chat ledger are collectively that
paper trail. Whether they satisfy a court is open. Probable issues:

- **Spoliation:** the long-term compaction predicate deletes nodes
  older than 90 days. Pinned corpus and ledger entries survive, but
  other graph state does not. In a litigation hold scenario, the
  compaction predicate must be pausable. Today it is not.
- **Reproducibility:** to defend a HOOTL decision, you need to
  reproduce the interpretation. This requires snapshotting the model
  checkpoint, the corpus state, the chat history, the workspace
  state at the time the interpretation was made. Substantial effort,
  not yet a first-class feature.
- **Expert witnesses:** who is qualified to testify about an
  autonomous agent's interpretation? This is a new specialty.

### Employment and displacement

If HOOTL displaces engineers at scale, platforms providing it may
face duties under existing labor law (varies by jurisdiction) and
proposed AI labor regulations (EU, several U.S. states). The platform
posture worth taking: HOOTL augments and elevates engineers
(composer, not pilot) rather than replacing them. This is honest in
the short term and untested in the long term. The framing matters
both ethically and commercially.

### Agency law

Under common-law agency, an agent acts on behalf of a principal who
authorized them to bind the principal in specified matters. HOOTL
agents act without per-arc authorization. Whether this constitutes
agency in the legal sense is the deepest open question. Three
possible characterizations:

1. **Agent:** the operator is the principal; HOOTL agents are agents
   acting within scope authorized by terms of service. Operator is
   bound by their actions.
2. **Tool:** HOOTL agents are sophisticated tools the operator uses;
   the operator is responsible for tool selection and use, but
   "agency" in the legal sense does not attach.
3. **New category:** neither agent nor tool, but a new construct
   requiring new doctrine.

The right answer is probably (1) for commercial contexts and (2) for
hobby use, but the doctrine is not settled. Platform terms of service
should construct option (1) explicitly where it benefits the platform,
without overreaching.

### Market structure and antitrust

HOOTL is concentrating capability. The best interpretation models
become disproportionately valuable. Cloud providers with proprietary
inference advantage will have structural advantages over independent
platforms. Antitrust implications:

- Vertical integration concerns (cloud + model + platform under one
  roof).
- Foreclosure of competition through API access tiers.
- Tying claims if HOOTL features are bundled with specific clouds.

AI Studio's multi-provider posture (Anthropic + Gemini + local +
Claude CLI) is an asset against this. The architecture document at
`docs/architecture/CLUSTER_CODEX.md` and the routing topic at
`docs/book-ai/routing.md` describe the discipline that makes
provider-swap mechanical.

---

## The bet {#hotl-taxonomy-the-bet node:architecture_note}

Strategically, we are betting on three things:

1. **HOTL ships now and earns trust.** The market is ready for HOTL
   if positioned correctly. Composer framing, not "out of the loop"
   framing. AI Studio is the demonstration.
2. **HOOTL is the destination that justifies the substrate.** The
   bitemporal belief schema, the recursion guard, the fitness
   registry, the cohort measurement all look like over-engineering
   under HOTL alone. They become foundational under HOOTL. Shipping
   them now buys optionality.
3. **The Conductor is the right wedge.** Marking it Experimental in
   v0.23.0 signals the future-state status without overclaiming
   readiness. Extending `wishCapture` from stated to inferred is the
   first concrete HOOTL step, and the FSM + approval modal + drift
   watcher already in place are the right scaffolding for it.

The substrate investment is real. The interpretation work is real.
The legal and commercial questions are real. The bet is that the
combination — substrate + interpretation + the right legal posture +
the composer framing — is a coherent product that has not yet been
built, and that AI Studio is closer to it than anyone else.

`hootl.org` is the surface where the bet is made publicly.

---

## What this document is not {#hotl-taxonomy-not node:architecture_note}

It is not a marketing piece. The market materials should lead with
the composer image and not with the acronym taxonomy. The taxonomy is
the working vocabulary for engineers, lawyers, regulators, and
strategists. Customers should rarely encounter the word HOOTL.

It is not a roadmap. The roadmap is what the next twelve months of
work will look like, derived from this document but not contained in
it. Roadmap items live in CHANGELOG.md and the project's actual
backlog.

It is not legal advice. The legal section is a working enumeration
of open questions, not a position any lawyer should rely on. Each
question listed needs real legal analysis before any commercial
move that touches it.

It is not the final word. The interpretation problem is the central
technical bet, and we do not yet know how to solve it at scale. The
document will be revised as we learn. Treat the version stamp at the
top as the meaningful timestamp.

---

## Where this document lives in the corpus {#hotl-taxonomy-lives node:architecture_note}

Three corpus topics carry the agent-facing summary of this material:

- `docs/book-ai/hitl.md` — HITL definition and market shape
- `docs/book-ai/hotl.md` — HOTL definition, supervision posture,
  composer framing, taxonomy
- `docs/book-ai/hootl.md` — HOOTL definition, interpretation
  problem, what's already HOOTL-shaped, open questions

The corpus topics are graph-ingested and queryable by section. They
are written for agents working inside AI Studio. This document is
the human-facing companion — longer, less compressed, and able to
carry the legal and commercial material that does not fit in the
corpus's typed-node discipline.

For deeper reading on individual subsystems referenced above:

- The Cluster Codex at `docs/architecture/CLUSTER_CODEX.md`
- The bitemporal belief schema at `docs/book-ai/source-type-tier.md`
- The recursion guard at `docs/book-ai/recursion-guard.md`
- The regression baseline at `docs/book-ai/regression-baseline.md`
- The fitness registry at `docs/book-ai/fitness-registry.md`
- The Conductor at `docs/book-ai/conductor.md` (Experimental)

---

*Version: v0.23.0, last updated 2026-06-01.*
*Authors: Travis Winegar, Claude (Anthropic), in dialogue.*
*Status: living document.*
