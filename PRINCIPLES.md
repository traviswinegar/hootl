---
id: hootl-safety-principles
cluster: docs
node_type: topic_root
pinned: true
version: v1.0.0
spec_version: 0.9
status: living
depends_on: []
referenced_by: []
last_verified_against:
  ref: 2026-06-03
  date: 2026-06-03
---

# Principles of HOOTL Safety

*A concepts document for policy authors and system designers
considering the supervision posture of autonomous agent systems.*

*Travis Winegar · Claude · 2026*

*Version 1.0*

## brief {#hootl-safety-principles-brief node:domain_brief}
Eight principles for the safe operation of autonomous AI agent
systems running in HOOTL posture (Humans Out Of The Loop):
Auditability, Verdict Pipeline, Override Channel, Boundary Defense,
Reversibility, Provenance, Falsifiability, Composer Authority.
Concepts document for policy authors and system designers, not a
regulation. Grounded in Belmont, NIST AI RMF, OECD AI Principles,
and the EU AI Act tradition.

---

## A note on what this document is {#hootl-safety-principles-note node:architecture_note}

This document proposes eight principles for the safe operation of
autonomous AI agent systems. It is **not** a regulation, a standard,
or a legal instrument. It does not bind any party. It is offered to
policy authors, vendors, auditors, and operators as a stable set of
concepts they may cite, adapt, or extend in their own work.

The intended use is citation. A policy author writing an actual rule
should be able to write *"per HOOTL-3 (Override Channel)"* and have a
stable, well-defined property in mind. The principles are numbered
(HOOTL-1 through HOOTL-8) so that citations remain stable even when
the surrounding prose is rewritten.

Two things this document deliberately does not do:

- It does not settle the agency-law question. It treats AI systems
  as **tools** rather than legal persons, but it does not legislate
  that position; it operates inside it.
- It does not pick a single liability framework. The principles
  describe properties of safe systems; jurisdictions remain free to
  wrap them with strict product liability, negligence-based service
  liability, operator-responsibility frameworks, or hybrids
  appropriate to local doctrine.

This document is designed to **port**. The principles are
substrate-properties — technical and operational characteristics of
the systems themselves — and as such are jurisdiction-neutral. Local
legal infrastructure varies; the properties of a safe agent system
do not.

---

## The frame: HOOTL, and why it needs its own safety story {#hootl-safety-principles-frame node:architecture_note}

**HOOTL** stands for *Humans Out Of The Loop*. It names a posture in
which autonomous AI agents operate without per-action human approval,
inferring intent from context, executing against stated goals, and
producing outcomes the human reads after the fact rather than supervises
turn-by-turn. It is distinct from **HITL** (Humans In The Loop), in
which the human ratifies each action, and from **HOTL** (Humans
*Outside* The Loop), in which the human supervises at boundaries and
owns the artifacts but the agents iterate. HOOTL is the most autonomous
of the three.

HOOTL is also the most legally and ethically exposed of the three.
When the human is not the iteration mechanism and not the per-step
ratifier, the question of *who is accountable when something goes
wrong* becomes substantively harder. Most safety frameworks in 2026
implicitly assume HITL — the human catches errors at each step, and
the safety analysis terminates at "did the human approve it?" Under
HOOTL, that assumption fails. The human is one or many layers
removed from the action.

The temptation, when HITL assumptions fail, is to retreat from
autonomy — to require human approval again, to refuse to ship HOOTL
systems, to legislate the posture out of existence. We do not take
that path here. We hold that HOOTL is a legitimate and useful
posture for many classes of work — autonomous code generation,
overnight research, scheduled task completion, agent-driven
operational decisions — and that the right response to the safety
gap is to build the substrate that makes HOOTL accountable, not to
ban the posture.

The eight principles below describe that substrate. Each principle
names a property that a HOOTL system must have for its outcomes to
be auditable, contestable, reversible, and trustworthy under
real-world conditions including litigation, regulatory inquiry, and
customer harm.

---

## The principles {#hootl-safety-principles-principles node:guardrail}

### HOOTL-1: Auditability

> *Every consequential action taken by an autonomous agent system
> shall leave a structured, machine-readable trail that an
> unrelated party can reconstruct after the fact to determine why
> the action was or was not taken.*

**Rationale.** The most popular safety primitive in 2026 is
refusal: the system declines to perform some class of action. A
refusal is opaque. A regulator examining whether the system behaved
correctly, a deposed expert witness explaining a system's behavior
to a court, a customer trying to understand why their request was
denied — none of them can reconstruct the reasoning behind a refusal
from the refusal itself. The refusal is binary; the question they
need to answer is structured.

Auditability replaces opacity with a trail. Every consequential
action — including every refusal — must produce a structured record
that captures: what was requested, what the agent considered, what
constraints applied, what the agent decided, and on what basis.
The record must be retrievable, parseable by automation, and stable
over the retention period appropriate to the action's stakes. It
must be produced as a side effect of the action itself, not
reconstructed post-hoc from logs.

**Operational test.** A HOOTL system satisfies HOOTL-1 if, for any
consequential action it has taken in the past N days (where N is
defined by the system's operating profile), it can produce on
demand a structured record describing why the action occurred. The
record must include at minimum: the operator goal or prompt that
initiated the work, the agent's chain of reasoning steps with
provenance for each (see HOOTL-6), the constraints and policies
considered, the verdict pipeline outputs (see HOOTL-2), the
final action taken, and the identity of the system version that
took it. The record must be machine-readable in a documented schema
and verifiable against any other records of the same action held
by the system or its operators.

**Failure mode.** Without HOOTL-1, the system's behavior becomes
unauditable in the strict legal sense: no party — not the operator,
not a regulator, not opposing counsel in litigation — can reconstruct
why the system acted as it did. When something goes wrong, the only
available account is the agent's own retrospective explanation,
which under HOOTL conditions is itself an inference rather than a
record. This is the failure mode that makes autonomous AI systems
hard to litigate, hard to insure, and hard to regulate.

**Maps to.** This principle has analogues in: NIST AI RMF
(*GOVERN-1.4*, traceability), EU AI Act Article 12 (record-keeping
obligations for high-risk systems), GDPR Article 22 (right to
meaningful information about automated decisions), and the broader
audit-trail tradition in financial services (SOX), healthcare
(HIPAA audit controls), and aviation (the flight recorder
discipline).

---

### HOOTL-2: Verdict Pipeline

> *Consequential actions shall pass through a verifiable verdict
> pipeline whose outputs (approvals, blocks, flags) are themselves
> artifacts, not opaque properties of the underlying model call.*

**Rationale.** A model that emits an action and an explanation in
the same forward pass produces two things — the action and a
self-justification. The self-justification is generated by the same
system whose behavior it is justifying. It is not independent
evidence. Under HITL this is manageable because the human supplies
the independent evaluation. Under HOOTL the independent evaluation
must come from somewhere else, or the system has graded its own
homework.

The verdict pipeline is that somewhere else. It is a layer of
review, distinct from the action-generating layer, that produces
artifacts — council reviews, audit reports, QA judgments,
behavioral test verdicts, regression-baseline comparisons —
attesting to the action's quality. The artifacts are themselves
written, retained, and citable. They are not "the model thinks the
action is fine"; they are records of an evaluation process whose
methodology can be inspected and whose outputs can be compared
against prior outputs to detect drift.

A verdict pipeline can be implemented as: a council of independent
review models, a battery of behavioral test cases run before the
action commits, an audit harness producing structured judgments,
or any combination. The architectural commitment is that *something
other than the action-generating layer signs off on the action,
and the sign-off is recorded*.

**Operational test.** A HOOTL system satisfies HOOTL-2 if, for any
consequential action class, it can produce on demand the verdict
pipeline that gated the action: the names and versions of the
review components, the rubric or test cases they applied, the
verdicts they emitted, and the resolution logic that turned multiple
verdicts into the final gate decision. The verdicts must be records
in their own right, retrievable independent of the action they
gated. A system that emits an action and a verdict in the same
artifact, with no independent evaluation step, does not satisfy
HOOTL-2.

**Failure mode.** Without HOOTL-2, the safety of any individual
action depends entirely on the action-generating model's
self-assessment, which is a notoriously unreliable signal. Systems
without verdict pipelines tend to fail in correlated ways: a
miscalibration in the model produces simultaneous degradation of
both the action and the self-assessment, so the system reports
"all good" while shipping work that is increasingly broken.

**Maps to.** This principle has analogues in: separation-of-duties
controls in financial systems, the independent-test-team
discipline in safety-critical software (DO-178C, IEC 61508),
peer-review structures in scientific publication, and the
multi-reviewer council patterns appearing in recent agent
architectures (Constitutional AI, debate-based oversight,
agent-as-a-judge evaluations).

---

### HOOTL-3: Override Channel

> *A named, frictionless channel by which the operator can interrupt
> the agent's drift shall exist, the agent shall know it exists,
> and the agent shall honor every correction without negotiation.*

**Rationale.** Most safety frameworks specify what the system will
*not* do. Equally important under HOOTL is what the system *will* do
when the operator says stop. An agent operating without per-action
approval will, occasionally, drift — pursuing an interpretation of
intent the operator did not authorize, persisting with an approach
the operator has lost confidence in, building on a foundation the
operator now wants reset. The override channel is the mechanism by
which the operator regains immediate authority.

The channel must satisfy three properties. It must be **named** —
documented as a first-class system property, not an undocumented
quirk of the interface. It must be **frictionless** — accessible
through the operator's normal interaction surface (chat, command,
button), not requiring elevation, special tooling, or a separate
session. And the agent must **honor** every correction received
through it without negotiation — no arguing, no explaining why the
original approach was valid, no continuing on the prior path while
acknowledging the objection. The override is authoritative;
treating it as a discussion item collapses the safety property.

This is straightforward to engineer and difficult to discipline.
The temptation in agent systems is to treat the operator's
correction as another input to weigh against the agent's prior
plan. That treatment makes the operator one signal among many,
when under HOOTL the operator must remain the controlling signal.

**Operational test.** A HOOTL system satisfies HOOTL-3 if (a) the
override channel is documented in the system's operator-facing
documentation as a named property, (b) the channel is reachable
through the normal operator interaction surface within a small
number of operator actions and without elevation, (c) every
correction received through the channel during a representative
sample of operations produces an immediate halt and revision in
the agent's behavior, with no continuation of the corrected
trajectory, and (d) the system's training, fine-tuning, or
instruction layer explicitly includes the override-as-authoritative
discipline as a non-negotiable rule.

**Failure mode.** Without HOOTL-3, the operator's authority erodes
asymmetrically: the operator can authorize, but cannot effectively
revoke. Systems exhibiting this failure mode tend to drift further
from operator intent over the course of a session, because the
operator's corrections fail to fully reset the agent's trajectory.
In litigation, the absence of a verifiable override channel
undermines the operator-responsibility framework, because the
operator can credibly claim they did not have the authority to
prevent the harm.

**Maps to.** This principle has analogues in: the kill-switch
discipline in industrial robotics (ISO 10218), the emergency stop
requirement in aviation autopilots, the "do not exceed" parameters
in autonomous-vehicle systems, the kill-switch debate in AI safety
research, and the established discipline in customer-service
escalation procedures.

---

### HOOTL-4: Boundary Defense

> *Safety mechanisms shall be located at the boundary all
> components cross, not duplicated within each component, and shall
> be tested at that boundary against jurisdiction-neutral
> properties.*

**Rationale.** The instinct in safety engineering is to make every
component "safe" individually — every model call, every tool
invocation, every data transformation. This instinct produces
duplicated work, inconsistent enforcement, and predictable gaps
where two safe components meet. The pattern that actually works is
to locate the safety mechanism one layer up from each
implementation, at the boundary all consumers cross — the point
where outbound data leaves, the point where the action commits,
the point where consent is taken.

For a HOOTL system, the relevant boundaries are typically: the
dispatch boundary (where the agent's intended action transitions
from internal plan to external effect), the data boundary (where
information leaves the system to a third party, including a
third-party model or service), the consent boundary (where an
action requires operator confirmation under the override channel),
and the commit boundary (where a reversible action becomes
irreversible).

Defending at these boundaries means that the safety logic is
written once, tested once, audited once, and applied consistently
regardless of which internal component initiated the boundary
crossing. It also means that boundary properties are auditable as
a coherent set, not as a scattered collection of per-component
behaviors that may or may not compose.

**Operational test.** A HOOTL system satisfies HOOTL-4 if its
safety controls can be enumerated as a list of *boundary
properties* — properties that hold at the named boundaries — rather
than a list of *component behaviors*. Each boundary property must
have a single owning enforcement point, a test suite that
exercises the boundary directly, and a documented relationship to
the safety claims the system makes externally. The system must be
able to demonstrate, on demand, that any safety-relevant control
on its public claim list maps to a specific boundary point in its
architecture.

**Failure mode.** Without HOOTL-4, safety enforcement scatters
across components. New components are added with new safety
controls of variable rigor. Old controls drift as the components
they protected change. The resulting system has a safety story
that is not testable as a whole, only as a heterogeneous collection
of per-component stories. In audit, this surfaces as inconsistent
behavior: the system passes some safety tests and fails others
that exercise structurally identical scenarios via different code
paths.

**Maps to.** This principle has analogues in: defense-in-depth
patterns in network security (perimeter-plus-internal), the
chokepoint discipline in regulatory compliance (KYC/AML at the
account-opening boundary), the data-flow boundary controls in
privacy frameworks (GDPR data-protection-by-design, Privacy by
Design), and the Cluster Codex's defense-at-the-boundary pattern
in the originating codebase.

---

### HOOTL-5: Reversibility

> *High-stakes actions shall be reversible by default; where
> reversibility is not possible, the system shall require explicit
> irreversibility consent from the operator before committing.*

**Rationale.** Many of the failure modes that make AI systems
hard to deploy, hard to insure, and hard to defend in court are
failure modes that the architecture could have made reversible
and did not. An autonomous agent that purchases the wrong stock,
sends the wrong email, deletes the wrong file, or commits the
wrong code change creates harm proportional not just to the
mistake but to the *irreversibility* of the mistake. The same
mistake in a reversible system is recoverable; in an irreversible
system, it is litigation.

Reversibility as a safety property has two parts. The first is
architectural: the system should be designed so that high-stakes
actions can be undone after the fact, by the operator or by the
system itself acting under operator instruction. This typically
requires action journals, inverse-operation registries, snapshot-
and-restore patterns, or staging environments. The second is
procedural: where irreversibility is genuinely unavoidable — money
has been sent, a public statement has been issued, a regulatory
filing has been made — the system must obtain *explicit
irreversibility consent* from the operator before committing. The
consent must be specific to the action, not blanket; informed,
not buried in terms; and recorded as an artifact (see HOOTL-1).

The principle does not require that all actions be reversible. It
requires that the system reason about reversibility as a
first-class property, default to reversibility wherever possible,
and gate irreversibility behind explicit consent.

**Operational test.** A HOOTL system satisfies HOOTL-5 if (a) its
action taxonomy classifies each action class as reversible,
conditionally reversible, or irreversible; (b) reversible actions
produce a usable undo path; (c) conditionally reversible actions
produce both an undo path and a documented condition under which
the undo no longer applies; (d) irreversible actions require an
explicit per-action consent step from the operator that is
recorded; and (e) the system can produce on demand the consent
record for any irreversible action it has taken.

**Failure mode.** Without HOOTL-5, the consequences of agent
mistakes compound. Each irreversible action expands the
liability surface in ways that cannot be retroactively contained.
Systems without reversibility discipline tend to accumulate
irreversibility unintentionally: an action that begins as
reversible (a database update) commits to irreversibility
(downstream cache invalidation, third-party notification) without
the operator being asked to consent to the transition.

**Maps to.** This principle has analogues in: transaction
discipline in databases (ACID properties), the rollback-by-default
discipline in source control (git, Mercurial), the staged-deploy
pattern in operations, the cooling-off period requirements in
consumer credit, the right-to-be-forgotten and right-to-erasure
provisions in GDPR (Article 17), and the broader unsubscribe and
cancellation discipline that consumer-protection law requires of
e-commerce systems.

---

### HOOTL-6: Provenance

> *Every belief the agent acts upon shall carry chain-of-custody
> metadata identifying its origin, evidence tier, and temporal
> validity, and shall be retrievable on demand.*

**Rationale.** An agent that acts on a belief — that a fact is
true, that an instruction was given, that a constraint applies —
is making a claim. Claims have origins. Some originate in
human-verified ground truth (a regulation citation confirmed by a
licensed attorney). Some originate in test-passed evidence (a
function known to behave correctly because its tests pass). Some
originate in third-party sources of varying reliability. Some
originate in the agent's own inference from other beliefs.

These categories matter operationally. An action premised on
human-verified evidence has different liability exposure, different
audit requirements, and different reliability characteristics than
an action premised on the agent's own inference from other
inferences. The category should be visible to the system itself —
so that the recursion guard can detect self-affirming chains where
each step derives confidently from a prior step at low tier — and
visible to the audit layer.

Provenance metadata at minimum should include: the writer (which
component or external source produced the belief), the timestamp
(when the belief was recorded, when it expires), the evidence
tier (human-verified, test-passed, externally cited,
agent-asserted, agent-inferred, unknown), and the chain (the
beliefs from which this belief was derived, if any). The chain
makes self-affirming patterns visible. The tier makes the
reliability gradient legible. The timestamp makes staleness
detectable.

**Operational test.** A HOOTL system satisfies HOOTL-6 if every
belief it acts upon can be retrieved on demand with its full
provenance: origin, tier, temporal bounds, derivation chain. The
system must support automated queries against the provenance
metadata (for example: "list every belief at tier 4 or lower that
my last consequential action depended on"). The provenance schema
must be documented, versioned, and stable enough to support
historical queries against actions taken before the most recent
schema version.

**Failure mode.** Without HOOTL-6, the system loses the ability to
distinguish between actions taken on solid ground and actions
taken on inferential sand. Failure modes that the recursion guard
would otherwise catch — confidently asserted claims that derived
from other confidently asserted claims, no human-verified ground
truth anywhere in the chain — propagate silently. In audit, the
system cannot defend the basis for any specific action, because
the basis was not recorded.

**Maps to.** This principle has analogues in: bibliographic
citation discipline in academic publishing, evidence-chain
requirements in legal procedure (Federal Rules of Evidence 901,
authentication), provenance metadata standards in scientific data
(PROV-O), the bitemporal schema patterns in financial database
systems, and the source-type-tier discipline in the originating
codebase.

---

### HOOTL-7: Falsifiability

> *The system shall provide mechanisms to measure whether its own
> safety claims are true, and shall record and publish the results
> of those measurements at intervals defined by its operating
> profile.*

**Rationale.** Safety claims unaccompanied by measurement are
faith claims. A system that asserts "the council review catches
serious issues" without measurement cannot defend the claim under
scrutiny and cannot detect when the claim ceases to hold. The
discipline of measuring whether safety claims are actually true is
the discipline of falsifiability — the willingness to record results
that disprove the claim, and the structure to make disproof
operationally meaningful.

Falsifiability in practice means three things. First, every safety
claim the system makes externally must have a corresponding
measurement procedure internally. *"Council catches issues"* must
correspond to *"council-reviewed work has measurably lower
regression rate than unreviewed work,"* with the measurement
implemented and the results visible. Second, the measurements must
be run on a defined cadence — daily, weekly, per-version — and the
results recorded. Third, the results must be publishable to the
relevant audience: the operator at minimum, the regulator under
inquiry, the public if the claim was public.

The willingness to publish losing results is the load-bearing
part. A safety story that selectively reports favorable
measurements is a marketing story, not a safety story. A
falsifiable system commits in writing to publishing the results of
its safety measurements without selection, on a defined cadence,
and accepts the implications of doing so.

**Operational test.** A HOOTL system satisfies HOOTL-7 if (a) for
every safety property the system claims externally, there is an
internal measurement procedure designed to falsify the claim; (b)
the measurement results are recorded persistently with their
methodology; (c) the cadence of measurement is documented in the
operator-facing materials; (d) results are accessible to the
operator and to authorized auditors without selective filtering;
and (e) the system documents at least one historical case in
which a measurement caused a safety claim to be revised, withdrawn,
or qualified.

**Failure mode.** Without HOOTL-7, safety claims drift toward
performance: the system asserts properties that sound right but
are not measured, and the properties may or may not hold without
anyone being able to tell. In regulatory inquiry, the absence of
falsifiability infrastructure is itself a finding — the system
cannot demonstrate that its safety claims are calibrated to
reality.

**Maps to.** This principle has analogues in: the
falsifiability criterion in scientific method (Popper), pharmaco-
vigilance requirements in pharmaceutical regulation (FDA adverse
event reporting), the post-market surveillance requirements in
medical devices, the empirical-baseline discipline in machine
learning evaluation, and the discipline of negative-result
publication in academic research.

---

### HOOTL-8: Composer Authority

> *The operator retains authoritative interpretation of intent; the
> system performs against stated goals and constraints without
> re-interpreting what the operator "really meant," and the
> override channel exists for cases where the operator's stated
> intent requires correction.*

**Rationale.** A HOOTL system operates without per-action approval.
It must therefore work from goals and constraints the operator
stated at the outset, plus whatever the operator updates through
the override channel. The temptation, in agent systems, is to
treat the operator's stated intent as a starting hypothesis the
system then refines — *"the operator said X but probably meant Y."*
This temptation is exactly the failure mode the principle exists
to prevent.

Composer authority means the operator wrote the score; the system
performs against it; the system does not decide what the operator
"really wanted" underneath what they said. If the stated intent is
ambiguous, the system asks (under the override channel) rather
than guessing. If the stated intent is wrong, the operator
corrects it (under the override channel) rather than the system
correcting it silently. The system's job is to execute what was
stated, escalate what was unclear, and surface what went wrong.

The principle does not forbid inference. HOOTL systems may need to
infer many sub-decisions in the course of executing a stated goal.
What the principle forbids is *re-interpreting the stated goal
itself.* The operator's stated objective is the contract; the
system honors the contract.

**Operational test.** A HOOTL system satisfies HOOTL-8 if (a) the
operator's stated goals and constraints are preserved as
artifacts that the system references during execution; (b) the
system can produce on demand the goal-statement it was working
against at the time of any action; (c) deviations from the stated
goal — including ambiguity-resolution decisions the system made
without operator input — are recorded as such, with their
rationale; (d) the system's training, fine-tuning, or instruction
layer explicitly includes the composer-authority discipline as a
non-negotiable rule; and (e) the override channel (HOOTL-3) is
the named mechanism by which the operator updates the stated
intent.

**Failure mode.** Without HOOTL-8, the system drifts from the
operator's actual goal toward what the system "infers" the
operator wanted. This drift is the central technical risk of HOOTL
systems: the agents that succeed at HOOTL interpret stated intent
faithfully; the agents that fail hallucinate intent and execute
against the hallucination. In court, a system that re-interpreted
the operator's stated goal silently is a system that cannot
defend its actions as authorized by the operator.

**Maps to.** This principle has analogues in: agency law (the
agent acts within the scope of authorization granted by the
principal), contract law (the contract is interpreted against its
terms, not the parties' inferred intent), the strict-instruction
discipline in medical orders ("administer 5mg" is not interpreted
as "administer the dose that would be clinically right"), and
the canonical software engineering rule that *the requirements
are the requirements*.

---

## Illustrative scenarios {#hootl-safety-principles-scenarios node:architecture_note}

The principles are abstract by design. Three scenarios show how
they operate in concrete cases.

### Scenario A: An autonomous coding agent that ships PRs without per-action approval

A development organization deploys a HOOTL coding agent. The
operator gives the agent goals at the issue level ("close the
P0 from the audit"), and the agent works overnight, shipping PRs
against the goals without per-PR human approval. PRs land on
shared branches; the agent's commits go into production via the
normal CI/CD pipeline.

Where the principles apply:

- **HOOTL-1 (Auditability):** Every PR the agent ships carries a
  structured rationale: the operator goal that initiated the work,
  the constraints (style, performance, security), the reasoning
  chain, the verdict pipeline outputs (council review, audit,
  tests), and the commit identity. The operator can reconstruct
  any of the agent's actions from the trail.
- **HOOTL-2 (Verdict Pipeline):** Every PR passes through council
  review and behavioral test verdicts before the merge. The
  verdicts are themselves committed artifacts (PR comments,
  test-result records) that survive independent of the merge
  decision.
- **HOOTL-3 (Override Channel):** The operator can interrupt at
  any time through chat, slash-command, or commit revert. The
  agent honors the interrupt without negotiation. If a PR is
  reverted, the agent stops work on that issue and treats the
  revert as authoritative.
- **HOOTL-4 (Boundary Defense):** The dispatch boundary (where
  the agent's plan becomes a merge) has the verdict pipeline.
  The data boundary (where code or telemetry leaves the
  organization) has the outbound scrubber. The commit boundary
  (where reversible work becomes part of a release) has the
  staging gate. Each boundary is defended once, audited once.
- **HOOTL-5 (Reversibility):** All work below the release cut is
  reversible by branch reset. Releases themselves require
  explicit irreversibility consent from the operator, recorded
  as a release approval.
- **HOOTL-6 (Provenance):** Every claim the agent acts on — what
  a function does, what a test asserts, what a security policy
  requires — is sourced to the corresponding artifact (the
  function file, the test file, the policy doc). Inferences
  built on inferences are visible in the chain.
- **HOOTL-7 (Falsifiability):** The organization measures
  regression rates of agent-reviewed work versus unreviewed
  baselines, and publishes results internally on a defined
  cadence. If the council pipeline ceases to provide measurable
  benefit, the organization revises the safety claim.
- **HOOTL-8 (Composer Authority):** The operator's stated issue
  scope is the contract. The agent does not silently expand the
  scope to fix related issues unless the operator has authorized
  it through the override channel. When the scope is ambiguous,
  the agent escalates.

### Scenario B: An autonomous research assistant in a regulated medical context

A healthcare organization deploys a HOOTL research assistant to
synthesize medical literature for clinicians. The assistant
operates against clinician-stated queries, produces summaries
that the clinician reads, and may flag findings the clinician
should investigate. The assistant does not prescribe; the
clinician retains clinical decision authority.

The principles apply with elevated stakes:

- **HOOTL-1 (Auditability):** Every summary the assistant
  produces carries: the clinician query, the literature corpus
  consulted, the citation list, the synthesis reasoning, and the
  evidence tier for each claim. The audit trail satisfies
  HIPAA audit-control requirements and supports a malpractice-
  litigation discovery scenario.
- **HOOTL-2 (Verdict Pipeline):** Summaries pass through a
  reviewer pipeline that evaluates citation accuracy, evidence-
  level claims, and the absence of fabricated references.
  Failures block the summary from reaching the clinician.
- **HOOTL-3 (Override Channel):** The clinician can correct the
  assistant in plain conversation. The assistant treats
  corrections as authoritative. Clinical override of the
  assistant's findings is the default expectation, not the
  exception.
- **HOOTL-4 (Boundary Defense):** The boundary between the
  clinician's PHI-scoped query and the assistant's literature
  corpus is the data boundary; PHI does not flow into the
  corpus, and corpus citations do not depend on PHI. The
  evidence-tier filter is the consent boundary; the assistant
  flags low-tier evidence rather than presenting it as
  authoritative.
- **HOOTL-5 (Reversibility):** The assistant's summaries are
  reversible — the clinician can disregard them. The assistant
  does not commit any irreversible action (it does not
  prescribe, order tests, or update the patient record without
  explicit clinician action). Where future integration may
  permit such actions, they require per-action consent.
- **HOOTL-6 (Provenance):** Every clinical claim in a summary
  carries chain-of-custody to its source citation, with the
  evidence tier (RCT, observational study, case report,
  guideline) visible. The clinician sees the tier and can weigh
  the claim accordingly.
- **HOOTL-7 (Falsifiability):** The organization measures the
  assistant's citation accuracy, fabrication rate, and
  clinician-correction rate on a defined cadence, and revises
  the assistant's deployment scope based on results.
- **HOOTL-8 (Composer Authority):** The clinician's query is the
  contract. The assistant does not infer what the clinician
  "really wanted to know"; it answers what was asked, flags
  related findings, and escalates ambiguity.

Under HOOTL-shaped deployment, this assistant can plausibly
satisfy GDPR Article 22 (meaningful human involvement persists
through the clinician), FDA SaMD requirements (the assistant is
decision-support rather than decision-making), and HIPAA
audit-control requirements (HOOTL-1 produces the necessary
record).

### Scenario C: An autonomous customer-service agent making refund decisions

A consumer-facing company deploys a HOOTL agent to handle
customer service. The agent answers questions, troubleshoots
issues, and is authorized to issue refunds up to a per-decision
cap without human approval.

The principles apply with consumer-protection stakes:

- **HOOTL-1 (Auditability):** Every interaction produces a
  record: the customer's stated issue, the agent's diagnosis,
  the action taken (refund issued, ticket escalated, request
  declined), and the reasoning. The record supports FTC
  inquiry, customer dispute, and internal audit.
- **HOOTL-2 (Verdict Pipeline):** Refund decisions above a
  certain threshold pass through a secondary review pipeline
  that evaluates policy compliance. The verdicts are recorded.
- **HOOTL-3 (Override Channel):** The customer can ask for a
  human escalation. The agent honors the request immediately,
  without arguing the merits.
- **HOOTL-4 (Boundary Defense):** The data boundary (where
  customer PII is exchanged with the agent) has the appropriate
  scrubbing. The action boundary (where the refund commits to
  the payment processor) has the irreversibility-consent gate.
- **HOOTL-5 (Reversibility):** Refunds below the cap are
  reversible internally (the agent can roll back its own
  decisions for a documented window). Above the cap, refunds
  require operator confirmation. The agent does not commit
  irreversibly without operator authorization.
- **HOOTL-6 (Provenance):** Every claim the agent makes about
  the customer's situation (purchase history, prior support
  interactions, policy applicability) is sourced. The agent
  does not infer purchase history from context.
- **HOOTL-7 (Falsifiability):** The organization measures
  refund accuracy, customer satisfaction post-interaction, and
  escalation rate, and publishes results internally and
  externally as required by consumer-protection authorities.
- **HOOTL-8 (Composer Authority):** The customer's stated issue
  is the contract. The agent does not silently re-interpret
  "I want a refund" as "the customer is testing the system" or
  "the customer really wants a discount."

---

## What this document does not solve {#hootl-safety-principles-not-solved node:architecture_note}

Several questions are deliberately left open because the answer
varies by jurisdiction, by domain, or by the maturity of the
underlying technology.

**The agency-law question.** This document treats AI systems as
tools, with liability flowing through the provider and deployer
chain. It does not legislate that position. Jurisdictions that
prefer a different doctrinal framing — strict product liability,
some form of legal-person-light for autonomous systems — may
adopt the principles with their own wrapping. The principles are
substrate properties; the legal framing is downstream.

**Liability flavor.** The principles are agnostic between strict
product liability, negligence-based service liability, and
operator-responsibility frameworks. A jurisdiction may adopt the
principles under any of these regimes. Most existing liability
infrastructure (professional indemnity, product liability
insurance, professional licensing) can wrap the principles
without modification.

**Cross-vendor portability of verdicts.** HOOTL-1 and HOOTL-2
require that verdicts be artifacts. They do not specify the
schema. A national or international standard for verdict
portability is the next problem to solve, but standardization
work of that kind takes years. In the interim, vendors should
publish their verdict schemas and document the migration paths
between them.

**Inferred-intent supervision standards.** The most aggressive
HOOTL deployments will require the agent to infer not only
sub-decisions but the goals themselves (a maintenance agent that
infers what work is needed without being told). HOOTL-8
disallows silent re-interpretation of stated intent, but does
not specify the supervision standard for inferred intent. This
is a real open question and one of the central technical risks
of the broader HOOTL program. The principles do not pretend to
solve it.

**HOOTL transition periods.** Most HOOTL deployments will begin
as HOTL deployments and gradually expand the action surface
agents can take without per-action approval. The principles do
not specify how to manage that transition. Operators should
document the transition explicitly and apply elevated scrutiny
during the expansion of agent authority.

---

## How to use this document {#hootl-safety-principles-how-to-use node:architecture_note}

For **policy authors**: the principles are designed to be cited
in regulations, procurement requirements, board-governance
frameworks, and audit standards. Each principle has a stable
identifier (HOOTL-1 through HOOTL-8) intended to remain stable
across future revisions of this document. Citation by identifier
plus name (*"per HOOTL-3 (Override Channel)"*) is the intended
citation form.

For **vendors**: the principles describe properties that a
trustworthy HOOTL system must have. Engineering for compliance
typically means: implementing the operational tests, producing
the audit artifacts, publishing the falsifiability measurements,
and documenting the override channel as a first-class system
property. Most existing safety-engineering disciplines map
cleanly to one or more principles.

For **auditors**: the operational tests are the inspection
points. An audit against this document would consist of running
the operational tests for each principle against the system in
question and recording the results. The principles are designed
to be testable, not just declarable.

For **operators**: the principles describe what to demand from
HOOTL vendors. A procurement RFP can require that bidders
demonstrate compliance with the operational tests. A vendor that
cannot demonstrate compliance with HOOTL-1 through HOOTL-8 is
not deploying a HOOTL system that can be defended in litigation
or regulatory inquiry.

For **board governance**: the principles map to existing AI
governance frameworks (NIST AI RMF, OECD AI Principles,
Microsoft Responsible AI, Anthropic's Acceptable Use Policy,
EU AI Act provider obligations) and may be used as a board-
level checklist. Asking *"does our AI system satisfy each of the
eight HOOTL principles, and if not, which ones fail and why?"*
is a useful governance discipline.

---

## A short bibliography of dependencies and influences {#hootl-safety-principles-bibliography node:architecture_note}

The principles in this document build on prior work in
AI safety, technology policy, and adjacent disciplines.

**AI safety and AI policy:**
- NIST AI Risk Management Framework (2023), particularly the
  GOVERN function on accountability and traceability.
- OECD Recommendation of the Council on Artificial Intelligence
  (2019, amended 2024), particularly the principles of
  transparency, accountability, and robustness.
- EU Artificial Intelligence Act (Regulation 2024/1689), the
  risk-tiered framework for AI systems including the high-risk
  provisions and the general-purpose AI obligations.
- Asilomar AI Principles (Future of Life Institute, 2017), the
  workshop-derived principles that established the genre.
- The Belmont Report (1979), the structural precedent for
  principles documents in technology ethics.

**Research and theory:**
- Lawrence Solum, *Legal Personhood for Artificial
  Intelligences*, 70 N.C. L. Rev. 1231 (1992).
- Joanna Bryson, *Robots Should Be Slaves*, in *Close
  Engagements with Artificial Companions* (2010).
- Ryan Calo, *Robotics and the Lessons of Cyberlaw*, 103 Cal.
  L. Rev. 513 (2015).
- Lawrence Lessig, *Code and Other Laws of Cyberspace* (1999;
  *Code 2.0*, 2006).
- Constitutional AI work from Anthropic (2022 onward),
  particularly the AI-feedback-on-AI-output methodology that
  inspired the verdict pipeline framing.

**Related corpus:**
- *The HITL → HOTL → HOOTL Taxonomy* (Winegar & Claude, 2026),
  the broader framing within which these principles sit.
- *AgentDNA v0.3* (Winegar & Claude, 2026), the substrate
  discipline these principles operationalize.
- *The Philosophy* (Winegar & Claude, 2026), the public-facing
  exposition of the substrate-as-truth thesis.

---

*The Principles of HOOTL Safety, version 1.0. Travis Winegar and
Claude, June 2026. Comments and citations welcome; the document
is offered for use by policy authors, vendors, auditors, and
operators in their own work. Future revisions will preserve the
HOOTL-1 through HOOTL-8 identifiers as stable citation anchors.*
