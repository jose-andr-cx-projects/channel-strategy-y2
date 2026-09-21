---
title: "Annex A - Parking Use-Case Mapping"
source_system: confluence
confluence_page_id: "1517912074"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1517912074/Annex+A+-+Parking+Use-Case+Mapping"
confluence_version: "3"
repository_path: "intelligent-front-door/ifd-define/ifd-draft-problem-statement-validation/annex-a-parking-use-case-mapping/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# Annex A - Parking Use-Case Mapping

## 1.1. Purpose

This annex captures the current working mapping between the six priority Parking customer intents and the existing service structure, information needs, support needs and authentication needs.

It is a **Define working artefact**, not a confirmed service model.

The table should be reviewed with service owners and other relevant stakeholders to:

- confirm that the customer intents are meaningful;
- validate the relationship between customer intent and existing Service Offerings;
- identify missing or incorrectly grouped pathways;
- validate information requirements;
- validate authentication and authority requirements;
- validate likely support levels;
- distinguish formal interaction modes from Intelligent Front Door routing behaviours; and
- identify where current organisational language does not align well with customer language.

The detailed source mapping is retained in `IFD-Define usecases.csv`.

---

## 1.2. A1. Priority use-case validation table

[Confluence macro: expand] 4000 Service Offering / working alignment Customer intent / contact reason Interaction mode — current working classification Cross-mode information need Authentication need Support need Why useful for Define Validation note Parking Permitting Apply for or manage a parking permit Apply Which permit applies? Am I eligible? What evidence is required? What does it cost? What happens next? How do I check progress or make changes? Likely required for application or account-linked management; exact rule to validate Routine → Guided High-volume, relatively routine task. Tests self-service routing, eligibility guidance, knowledge structure and authentication. Validate when authentication actually becomes necessary and whether different permit types require materially different routing. Infringement Review Request a review of a fine Comply / Apply-review — to validate Can I request a review? What grounds apply? What evidence is required? What is the timeframe? What happens after submission? How do I check progress or outcome? Identity + infringement details + authority/evidence likely required Guided → Assisted High-volume, judgement-heavy interaction. Tests Guided/Assisted routing, evidence needs, status information and authentication. Apply-review is not currently a formal interaction mode. Confirm whether this should be classified as Comply, Apply or another existing mode rather than creating a new category. Infringement Review / Parking Enforcement — alignment to validate Nominate another driver Comply Am I eligible to nominate? Who can be nominated? What evidence or declaration is required? What is the deadline? What happens after submission? Identity + infringement reference + authority/evidence likely required Routine → Guided Clear transaction with strong identity and evidence requirements. Useful for defining authentication and knowledge rules. Exact Service Offering remains to validate. This use case is particularly useful for testing authority versus identity requirements. Parking Enforcement Report a parking issue Report an Issue What can I report? Is this the right issue type? What location and details are required? Is it urgent? What happens after I report it? Usually low/no authentication initially; contact details may be required by the pathway Routine → Guided Tests issue recognition, context capture, reporting logic and routing. Validate which reports can remain anonymous, what minimum information is required and whether all currently mapped source pathways belong under this intent. Parking Provision / cross-offering knowledge — working alignment Find parking information / understand rules Formal mode to validate What rule applies to my situation? Where does it apply? What can or cannot I do? What exceptions exist? What should I do next? None for general information Routine Strong information architecture and knowledge use case. Tests customer-language content, authoritative information and intent recognition. The source table currently describes this as a Cross-mode information layer . Information Need has already been identified as cross-mode rather than a formal interaction mode, so the underlying interaction mode should be validated separately. Cross-offering navigation General parking enquiry Formal mode depends on identified intent What are you trying to do? Is this about a permit, fine, rule, enforcement issue, an existing request or something else? What is the right next step? None initially; authentication only after the task is identified Guided Diagnostic for situations where customers cannot recognise the correct pathway. Ideal for testing routing questions and front-door logic. Guided navigation across modes describes an IFD behaviour rather than a formal interaction mode. The interaction mode should emerge once the customer's intent has been understood.

---

## 1.3. A2. Current underlying service mappings

The working grid currently connects the six customer intents to a broader set of existing service names and knowledge articles.

These mappings are useful evidence of the current service landscape, but they should **not yet be interpreted as a validated one-to-one service taxonomy**.

### 1.3.1. Apply for or manage a parking permit

Current source mappings include:

- Parking Permit - Parking Permit Application;
- Parking Permit - Medical and Healthcare Parking Permit Application;
- Parking Permit - Community Parking Permit Application;
- Business Permits - Private Parking Agreements & Enforcement Agreements Permit Application; and
- Construction Permit - Construction Parking Permit Application.

This suggests that the customer concept of a **parking permit** can currently span multiple organisational service groups.

### 1.3.2. Request a review of a fine

Current source mappings include:

- Infringement Review - Parking - Incorrect Registration On PRN;
- Infringement Review - Parking: Internal Review;
- Infringement Review - Parking: Point of Distribution;
- Infringement Review - Parking: Repeat Review;
- Infringement Review - Parking: Review - Meter Fault Reported; and
- Parking - Tow Fee - Waiver Or Refund.

The relationship between these pathways and the customer intent **"review my fine"** should be validated rather than assumed.

### 1.3.3. Nominate another driver

Current source mapping:

- Parking Infringement Nomination.

This provides a relatively contained case for testing:

**intent → authority → evidence → authentication → pathway**

### 1.3.4. Report a parking issue

Current source mappings include:

- Parking - Abandoned Vehicles - Bicycle Investigation;
- Request for Parking Officer - High Priority;
- Request for Parking Officer - Low Priority;
- Request for Parking Officer - Ongoing Issues;
- Request for Parking Officer - Private Parking Agreement;
- Court Election - Parking; and
- Court Election - Parking - Point Of Distribution.

The inclusion of court-election pathways within this working group should be specifically reviewed with stakeholders.

It may reflect current organisational or system classification rather than a coherent customer intent.

### 1.3.5. Find parking information / understand rules

The current grid spans multiple expert-enquiry pathways, including:

- finance parking enquiries;
- meter payment enquiries;
- prosecution enquiries;
- infringement nomination enquiries;
- parking enforcement enquiries;
- disability and medical parking permit enquiries;
- reserved parking enquiries;
- residential parking enquiries; and
- zoo employee and miscellaneous parking enquiries.

This reinforces the hypothesis that **information need cuts across multiple service offerings** rather than behaving as a standalone customer transaction.

### 1.3.6. General parking enquiry

The current grid similarly spans resolved enquiries across:

- finance;
- meter payments;
- prosecutions;
- enforcement;
- infringements;
- disabled or medical parking permits;
- reserved parking;
- residential parking; and
- community / miscellaneous permit enquiries.

This makes General Parking Enquiry particularly useful for testing the Intelligent Front Door's ability to move from:

> **ambiguous customer need → intent recognition → appropriate service pathway**

rather than treating "general enquiry" as the destination.

---

## 1.4. A3. Questions for stakeholder refinement

When reviewing the table, focus on the following questions.

### 1.4.1. Customer intent

- Would a customer recognise these six intents?
- Are any materially different intents being grouped together?
- Are any of the six actually organisational categories rather than customer intents?
- Are important intents missing?

### 1.4.2. Service alignment

- Does each intent map to the correct Service Offering?
- Are current CRM/service names obscuring relationships that are obvious from the customer's perspective?
- Are any current mappings present because of system configuration rather than service logic?

### 1.4.3. Information

- What must a customer know before they can select or enter the pathway?
- What information is authoritative?
- Is the same information being repeated across multiple pathways?
- Where does information need to change based on customer context?

### 1.4.4. Support

- Can most customers complete the task routinely?
- What conditions should trigger Guided support?
- What conditions genuinely require Assisted support?
- Are staff currently compensating for poor findability or unclear information?

### 1.4.5. Authentication and authority

- What actually requires authentication?
- At what point is authentication required?
- Is authentication being requested earlier than necessary?
- Where does the service need to establish authority rather than simply identity?
- Which interactions can remain anonymous or low-authentication?

### 1.4.6. Existing pathway

- Once the customer's need is understood, is there already an appropriate pathway?
- Where does routing fail today?
- Where does the underlying pathway itself appear to be the problem rather than the front door?

---

## 1.5. A4. Validation status

**Overall status: Draft — stakeholder validation required**

Do not treat the mappings in this annex as confirmed requirements.

During validation, record changes using:

- **Confirmed**
- **Refine**
- **Remove**
- **Missing**
- **Open question**

The purpose of the exercise is not to make the table complete.

The purpose is to establish whether the emerging Intelligent Front Door model accurately represents the decisions customers need help making **before they enter an existing service pathway**.
