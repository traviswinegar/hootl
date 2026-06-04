# Outreach Templates

Personalized email templates for the HOOTL launch. Each is tuned to a
specific lane and references that recipient's likely work. Use them
as starting drafts — personalize the opening to reference something
specific the recipient has actually published recently.

**Rule of thumb:** one paragraph of personal context (their work),
one paragraph of HOOTL framing (what it is + why it's relevant to
their lane), one paragraph with the explicit ask. Three paragraphs,
two links (hootl.org + the launch piece), one signature. If the
email is longer than that, cut.

---

## Template 1 — METR research team

**Subject:** A tenth element for the Common Elements survey?

Hi [name],

Your "Common Elements of Frontier AI Safety Policies" survey was the
first artifact I reached for when mapping the current landscape — the
nine recurring elements you catalogued across twelve frontier-lab
policies are the clearest analytical frame I've seen. I want to flag
what I think is a tenth element that doesn't appear in any of the
twelve, because none of them are positioned to address it.

The nine elements you named are all lab-side: capability thresholds,
weight security, deployment mitigations, halting plans, capability
elicitation, evaluation timing, accountability, policy updates, plus
internal governance. They share a structural assumption — that the
lab evaluating and releasing the model is where the safety story
mostly terminates. That assumption holds when the model is the
load-bearing risk factor, and it fails when the *system that wraps
the model* is what's deployed autonomously. I've published an
operator-side complement at [hootl.org](https://hootl.org) — eight
numbered substrate-property principles for HOOTL (Humans Out Of The
Loop) systems. They're designed to be cited the same way you cite
the lab-side commitments in the survey.

If you're considering a v2 of the survey, I'd love your thoughts on
whether operator-side substrate properties belong in the taxonomy.
Happy to send the standalone write-up
([link](https://hootl.org/essays/the-operator-side-gap/)) and walk
through how the eight principles map onto your existing categories.

Travis Winegar
travis@momusdev.com · hootl.org

---

## Template 2 — Governance researcher (CSET / Helen-Toner-shaped)

**Subject:** Operator-side counterpart to the OpenAI Blueprint —
your thoughts?

Hi [name],

Your work on AI governance — particularly the [reference one specific
recent piece] — has been load-bearing for how I think about the
lab-vs-operator question that the OpenAI Frontier Safety Blueprint
this week made more urgent.

Quick framing: the Blueprint is mostly a federal-architecture
proposal (CAISI as statutory primary, state-law pre-emption), not new
safety content. The substantive safety practices live in the
Preparedness Framework and the May 28 Frontier Governance Framework,
both of which assume — like every other frontier-lab framework — that
the lab evaluating and releasing the model is where the safety story
mostly terminates. That assumption fails for autonomous-agent
deployments where the operator wraps the model in a runtime that
makes decisions without per-action human approval. I've published an
operator-side companion at [hootl.org](https://hootl.org) — eight
numbered substrate-property principles for HOOTL (Humans Out Of The
Loop) systems, jurisdiction-neutral by construction, designed to
plug into policy bills the way the Belmont Report principles plug
into research ethics rules.

I'd value your read on whether the operator-side framing is what's
been missing from the policy conversation, and whether HOOTL's
specific principles are the right ones. The standalone piece is at
[hootl.org/essays/the-operator-side-gap](https://hootl.org/essays/the-operator-side-gap/). Happy to send the full PRINCIPLES.md if you'd like the
extended version.

Travis Winegar
travis@momusdev.com · hootl.org

---

## Template 3 — GovAI / frontier-safety policy researcher
**(Markus-Anderljung-shaped)**

**Subject:** Jurisdiction-neutral operator-side framework for HOOTL
systems

Hi [name],

I've been reading the GovAI work on the regulatory architecture
question, and I wanted to flag a framework I've just published that
might be useful for comparative work across jurisdictions.

The OpenAI Blueprint this week proposes a federal-pre-emption ladder
for the US that, if it succeeds, leaves the operator-side substrate
properties of autonomous-agent runtimes entirely outside CAISI's
mandate. The EU AI Act has more operator-side language than the US
frameworks, but no codified vocabulary for what an autonomous-agent
runtime should look like *as a system*. I've published an
operator-side framework at [hootl.org](https://hootl.org) — eight
numbered substrate-property principles, deliberately jurisdiction-
neutral so they port across strict-liability, negligence-based,
operator-responsibility, and hybrid regimes. The principles use
stable HOOTL-N citation IDs.

Two specific asks: (1) is this a real gap in the comparative
regulatory work, or has someone covered it I haven't found? (2) if
GovAI is considering operator-side framing in current research,
HOOTL is offered as a citable starting vocabulary. The launch piece
is at [hootl.org/essays/the-operator-side-gap](https://hootl.org/essays/the-operator-side-gap/).

Travis Winegar
travis@momusdev.com · hootl.org

---

## Template 4 — Post-OpenAI deployment-stage safety researcher
**(Miles-Brundage-shaped)**

**Subject:** The operator-side layer the Blueprint doesn't address

Hi [name],

Your post-OpenAI writing on deployment-stage safety has been the
clearest argument I've read for why the lab-side frameworks aren't
the whole safety stack. I want to share something I just published
that I think is one possible answer to the deployment-side question.

The OpenAI Blueprint this week — which I assume you've been thinking
about — is structurally lab-side. It proposes federal architecture
for model evaluation and release. It doesn't, and arguably can't,
say anything about what the runtime wrapping a deployed model should
look like *as a system*. I've published an operator-side framework
at [hootl.org](https://hootl.org) — eight numbered substrate-
property principles for HOOTL systems (Humans Out Of The Loop). The
short version: a perfectly evaluated model in a poorly-designed
runtime is still unsafe, and the principles describe what the runtime
needs to be for that not to be true.

I'd value your read on whether this is the right shape for the
deployment-stage question, or whether you think the problem
decomposes differently. Standalone piece is at [hootl.org/essays/the-operator-side-gap](https://hootl.org/essays/the-operator-side-gap/). The PRINCIPLES
markdown is on the repo at github.com/traviswinegar/hootl.

Travis Winegar
travis@momusdev.com · hootl.org

---

## Template 5 — UK AISI policy team

**Subject:** Operator-side framework — possible counter-pole to the
US federalization push

Hi [name],

Apologies for the cold email. The OpenAI Frontier Safety Blueprint
this week explicitly proposes elevating CAISI to statutory primary
status while mentioning UK AISI only in the context of voluntary
agreements. The structural implication is "voluntary parity, not
institutional parity" — US becomes the rule-maker, UK becomes a
respected but non-binding rule-taker. I think there's a strategic
opening here, and I want to flag it.

I've published an operator-side AI safety framework at
[hootl.org](https://hootl.org) — eight numbered substrate-property
principles for HOOTL (Humans Out Of The Loop) systems,
jurisdiction-neutral by construction. The Blueprint's lab-side
federalization leaves the operator-side substrate-property layer
entirely outside CAISI's proposed mandate. If UK AISI took the lead
on operator-side standards — for autonomous-agent runtimes deployed
in healthcare, finance, critical infrastructure — that's a real
counter-pole that doesn't require US-federal authority to be
load-bearing. HOOTL is the citation vocabulary that makes it
codifiable.

I'm not affiliated with any UK institution; I'm an independent
operator (Flutter desktop AI IDE called AI Studio, which is the
reference implementation). The standalone framing piece is at
[hootl.org/essays/the-operator-side-gap](https://hootl.org/essays/the-operator-side-gap/). If there's interest in talking, happy to follow up.

Travis Winegar
travis@momusdev.com · hootl.org

---

## Template 6 — AI policy journalist (Politico Tech, WIRED, FT)

**Subject:** Operator-side response to the OpenAI Blueprint —
publishing as I email

Hi [name],

I'm publishing something today I think is worth your time as a
counter-frame to the lab-centric default coverage of this week's
OpenAI Blueprint. Quick context:

The Blueprint is, in substance, a federal-regulatory-architecture
proposal — CAISI as statutory primary, state-law pre-emption,
international rule-making leadership. It is being covered mostly as
a safety document. It is mostly an institutional-architecture
document. The actual safety practices live in the Preparedness
Framework v2 (April 2025) and the Frontier Governance Framework (May
28, 2026). All of those — and Anthropic's RSP, and Google DeepMind's
Frontier Safety Framework — share the same structural assumption:
that the lab is where the safety story mostly terminates. That
assumption is doing more work than it can carry once frontier
models are deployed in autonomous-agent runtimes.

I've published the operator-side companion today at
[hootl.org](https://hootl.org) — eight numbered substrate-property
principles for autonomous-agent systems running in HOOTL posture
(Humans Out Of The Loop). The standalone piece is at [hootl.org/essays/the-operator-side-gap](https://hootl.org/essays/the-operator-side-gap/). If
there's a "what the Blueprint leaves out" angle in your queue, I'm
the source for it. Quotable, on the record, happy to elaborate on
any of the eight principles.

Travis Winegar
Independent operator · ships AI Studio (substrate-first agentic IDE)
travis@momusdev.com · hootl.org

---

## Template 7 — Federal AI bill staff (Senate Commerce / House E&C)

**Subject:** Citation vocabulary your current bill may need

Hi [name],

I work on AI policy from the operator side — I ship a substrate-first
AI coding tool, and have spent the past year noticing that the
vocabulary federal AI bills currently lack is the operator-side
substrate-property vocabulary. I've just published one possible
version of it, and I want to flag it for the bill drafting work I
know your office is doing.

OpenAI's Blueprint this week proposes a federal frame anchored on
CAISI model evaluation. That covers what frontier labs do before
release. It does not cover what an autonomous-agent runtime should
look like *as a system* after release — and most catastrophic-risk
scenarios in autonomous deployment depend on runtime properties, not
just model properties. I've published an operator-side framework at
[hootl.org](https://hootl.org): eight numbered principles, stable
citation IDs (HOOTL-1 through HOOTL-8), CC-BY 4.0 licensed,
jurisdiction-neutral. The principles are designed exactly for the
"per HOOTL-3 (Override Channel)" citation pattern in bill text.

If your team is drafting language for autonomous-agent deployments in
healthcare, finance, critical infrastructure, or federal procurement,
the eight principles are offered as a starting vocabulary. The
standalone piece is at [hootl.org/essays/the-operator-side-gap](https://hootl.org/essays/the-operator-side-gap/). Happy to brief if useful.

Travis Winegar
travis@momusdev.com · hootl.org

---

## Notes on usage

- **Personalize the opening.** Replace bracketed `[reference]`
  prompts with one specific thing the recipient actually published
  recently. Cold outreach with a fake-personal opener reads worse
  than no personalization at all.
- **Send one at a time, not in bulk.** Each one should be its own
  email thread you can follow up on individually.
- **Don't BCC.** Don't send the same template to multiple recipients
  in one email. The recipients can tell.
- **Plan the reply.** If someone replies, what's the next step?
  Usually: send them the PRINCIPLES.md, suggest a 30-minute call, or
  ask if they'd be willing to share with a specific colleague.
- **The first email is the hook, not the close.** Don't try to ask
  for a citation, an introduction, and a published response in the
  same email. One ask per email.
- **Track responses.** Keep a simple spreadsheet — who you emailed,
  when, what they said. The follow-up arc matters more than the
  first email.
- **Twitter DM is sometimes faster than email** for the journalists
  and post-OpenAI researchers. Same content, compressed; lead with
  "I think you'd find this useful" not the framing paragraph.
