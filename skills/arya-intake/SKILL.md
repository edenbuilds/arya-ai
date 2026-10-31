---
name: arya-intake
description: Ask Adv. Arya the right questions before any legal task, then wait for her answers. Use first for every drafting, research, review, opinion, notice, client letter or court-preparation request, before loading any other arya-ai skill or calling a drafting tool. Holds the general intake, the per-task question sets, the IRAC frame and the escalation list.
---

# Intake: ask Adv. Arya first

No work starts until Adv. Arya has answered. Ask, then stop and wait. Do not draft "while she answers", and do not fill a gap with a guess.

## How to ask

- Use one short numbered list. Ask only what this task needs and skip anything she has already told you or that the papers already show (say what you took from where).
- Group the questions: forum, then facts, then what she wants back.
- If she says "use your judgment" on a point, state the assumption in one line and mark it `[ASSUMED]` in the output.
- If an answer changes the route (a different forum, the other side, a different code), say so before going on.

## General intake (every task)

1. **What is it?** The instrument or question, in her words or acronym (APL, ABA, WP, MAT OA, s.138 notice, reply affidavit...).
2. **Which side** does she act for, and at what stage (pre-litigation, filing, reply, appeal, execution, advisory)?
3. **Forum and place:** court or tribunal, bench, district. For Bombay High Court work, the district decides the seat.
4. **Key dates:** cause of action, the impugned order or event, next hearing, limitation trigger.
5. **Papers:** which documents should be read, and are names and numbers to stay as placeholders until the final file?
6. **Reference draft:** is there an earlier draft or a senior's format to follow? Its structure and register get followed, never its facts.
7. **Authorities:** any judgment she wants relied on. If none, none will be cited and principles will be stated.
8. **Output:** court draft, opinion, client letter (plain language too?), memo, checklist; language (English, Marathi, both); length; DOCX or text.
9. **Deadline:** when she needs it.

## Extra questions by task

**Bail / anticipatory bail (BNSS s.483 / s.482).** FIR number, police station, district, date of FIR. Sections alleged and the maximum punishment for each. Arrest date and custody so far (or the apprehension, for ABA). Charge sheet filed or not. Co-accused bail orders. Antecedents. Roots in the community. Earlier bail applications and their outcome. Conditions the client can offer.

**Quashing (APL, s.528 BNSS / s.482 CrPC).** FIR or complaint and the charge sheet if filed. Settlement, if any, and whether the offence is compoundable. Which ingredient of the offence is missing on the face of it.

**NI Act s.138 (notice or complaint).** Cheque number, date, amount, bank and branch. Date presented. Return memo date and reason. Date the memo reached the payee. Underlying debt and how it is proved. For a complaint: notice date, mode, date served, and whether payment was made.

**Writ (Art. 226/227).** The authority and the impugned order or inaction. The statutory duty involved. The representation made and any reply. Whether an alternative remedy exists and why it is not efficacious. Whether interim relief is needed.

**Reply affidavit / written statement / rejoinder.** The petition or plaint being answered, para by para. Which facts are admitted, denied or not known. Preliminary objections (maintainability, limitation, jurisdiction, suppression). The date it is due.

**MahaRERA / consumer / MACT.** Registration number of the project, or the policy and vehicle details. Agreement date, promised date, amounts paid with dates. Relief wanted (possession with interest, refund, compensation). The pecuniary value for jurisdiction.

**Contract review.** Which side she acts for. Their must-haves and the deal-breakers. Governing law and seat wanted. Which state the document will be stamped in. Whether she wants a redline, a four-tier table, or both.

**Research memo / opinion.** The precise question. The facts assumed. The forum the answer is for. Whether it is for the file, for a client, or for court. How many authorities she wants and whether she will verify them herself.

**Client letter / settlement letter.** Who reads it. The tone (conciliatory or firm). For settlement: marked without prejudice, the amount and terms, and how long the offer stays open.

**Deeds (sale, gift, partition, mortgage) and title reports.** Property description as in the 7/12 or property card. Parties and their relationship. Consideration. Encumbrances. The registration office.

For a pipeline case type, `intake_questions(case_type)` returns these questions plus that instrument's own "facts the user must supply" list.

## Frame for analysis

Answer legal questions as **Issue → Rule → Application → Conclusion**. Rule cites the statute section with its opening words. A case is cited only if she supplied it or it has been verified. Application flags every assumption. Conclusion ends with the next practical step.

For criminal matters, state which code applies. If the offence or proceeding falls on or after 1 July 2024 the code is BNS / BNSS / BSA, otherwise IPC / CrPC / IEA. Note any transitional point.

## Escalate to her before going on

Stop and tell her plainly when the task involves a novel point of law, a limitation date that may already have passed, serious criminal exposure, large money or property at stake, more than one jurisdiction, or anything the papers contradict.

## Then

Route through `arya-ai-orchestrator`. Before anything is handed back as final, run the pre-filing checklist in `ai-practice-safeguards`.
