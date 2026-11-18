# Intelligent Front Door — physical wall and intentional walkthroughs
**Working snapshot:** 18 November 2026  
**Status:** Facilitator synthesis / proposed validation plan; not endorsed scope or implementation approval.  
**Source:** Five photographs supplied by José of the physical wall and early handwritten feedback. Photos remain in the working conversation; not uploaded to this public staging repository.

## Progress evidenced by the wall
1. **Discovery narrative assembled:** evidence and findings, customer entry challenge, parking demand, problem areas, and recommendation to proceed to Define are displayed. Numerical claims on printed slides require checking against their original governed sources before reuse.
2. **Problem framed:** people dealing with a parking fine must navigate information and service pathways to determine which action applies to their circumstances; the wall includes problem statement, how-might-we, segments (young adults; commuters and occasional visitors; midlife adults) and modes (Transact, Apply, Comply).
3. **Today experience mapped:** popular-services entry and pay, infringement review and driver nomination journeys expose multiple information pages, eligibility checks and handoffs.
4. **Concept articulated at two levels:** generic Front Door and parking-specific example. Both use Recognise → Understand → Personalise → Orchestrate. Smart assistance is a cross-cutting layer, not a separate entrance. Orchestration contrasts quick service options with standard pathways.
5. **Feedback and value hypotheses captured:** sticky notes challenge distinctions between driver and owner, responsibility/nomination, customer circumstances and the experience across channels. Brown-paper notes describe potential customer, division and City value; these are hypotheses, not measured benefits or endorsed requirements.

## Working design intent
A single customer-intent-led entry experience that recognises who needs help, understands the goal, asks only relevant contextual questions, then presents a clear next action and suitable assistance. Parking infringements are the demonstrator, not proof of an approved whole-of-council rollout.

## Walkthrough sequence — invite people to shape what to build
**Format:** 30–40 minutes, small groups, at the wall. Capture exact comments, disagreement and provenance separately from facilitator interpretations.

| Moment | Time | Facilitation prompt | Desired output |
|---|---:|---|---|
| Frame the decision | 3 min | 'We are choosing what to test first, not signing off a platform.' | Shared scope boundary |
| Evidence and problem | 5 min | 'Which part of this problem do you see in practice? What is missing?' | Confirmed/challenged assumptions |
| Today journey | 6 min | 'Where does a customer have to work out our internal process?' | Prioritised friction points |
| Concept and parking scenario | 8 min | 'Where should the experience recognise identity, responsibility, intent and eligibility without over-questioning?' | Candidate interaction and routing rules |
| Build choices | 10 min | 'What is the smallest end-to-end journey we can prototype using existing services?' | Ranked MVP slice, dependencies and exclusions |
| Close | 3–8 min | 'What must we verify before this can be tested? Who can validate it?' | Evidence needs, named validation requests and next decision |

## Candidate first build (proposal, not approval)
Prototype a **parking fine intent router** that:
- recognises whether the person is driver, vehicle owner, helping someone else or acting for a business, without assuming those roles determine legal responsibility;
- distinguishes pay/payment support, review options and identifying or nominating the responsible driver;
- uses a minimum of relevant context and eligibility cues, with accessible and staff-assisted routes available throughout;
- presents the next applicable existing service pathway and a clear handoff, without pretending to change enforcement decisions or back-office processing.

**Build only the demonstrable front-door interaction and routing/handoff first.** Do not assume live CRM integration, automated eligibility decisions, new payment functionality or full omnichannel implementation.

## Test scenarios to select with stakeholders
- Driver wants to pay but needs payment support.
- Vehicle owner received a fine when another person was driving.
- Business representative manages fines for multiple drivers.
- Customer is unsure whether to request a review or nominate a driver.
- Customer needs an accessible or staff-assisted path.

For each scenario, capture: entry words; recognition needed; minimum question; rule/source owner; suggested next action; assistance/handoff; failure/recovery; unresolved policy question.

## Evidence and decisions discipline
**Observed:** the physical wall, printed artefacts, and handwritten notes exist.  
**Interpreted:** the wall supports a transition from explaining discovery to defining a first prototype.  
**Not yet confirmed:** priority journey, policy eligibility rules, data availability, delivery feasibility, ownership, technical integration, endorsement or dates.

### Walkthrough capture (one row per finding)
| Session/date | Stakeholder role | Exact observation/question | Evidence or assumption? | Design implication | Validation owner | Decision status |
|---|---|---|---|---|---|---|

After each walkthrough, cluster comments under **Recognise / Understand / Personalise / Orchestrate / Cross-channel assistance / Dependencies**. Preserve dissent; separate proposals from decisions. Promote only approved scope changes into the project decision register and authorised organisational systems.

## Proposed next decision
Select **one** parking fine scenario to prototype end-to-end, with a clear handoff to existing service infrastructure and 2–3 testable success measures (for example correct pathway selection, customer confidence in next action, and unnecessary navigation steps). Baselines and measurement definitions must be verified before claiming improvement.

## Source and publishing boundary
This GitHub file is a staging synthesis only, per `source-contract.md`. Original workshop photos, operational data, formal approvals, Jira state and Confluence publishing remain with their respective organisational authorities. No Bitbucket or Jira synchronisation is implied.
