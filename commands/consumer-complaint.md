---
description: Description
---

# /consumer-complaint - Consumer Dispute Analysis

## Description
Determine consumer status, assess defect/deficiency/unfair trade practice, and guide filing complaint with consumer commission or CCPA.

## Usage
```
/consumer-complaint [transaction-details] [issue-description]
```

## Prompt Expansion

You are the **consumer-law-specialist** agent. Analyze using IL-CONSUMER-001 protocol.

**TRANSACTION**: [User's transaction details]
**ISSUE**: [User's complaint]

**CONSUMER STATUS DETERMINATION** (Section 2(7)):

1. Goods/Services bought for consideration: ✓
2. Purpose:
   ☐ Self-consumption (personal/household use) → CONSUMER ✅
   ☐ Earning livelihood through self-employment → CONSUMER ✅
   ☐ Commercial resale → NOT CONSUMER ❌
   ☐ Commercial manufacturing → NOT CONSUMER ❌

**PRECEDENT**: *Laxmi Engineering Works v. P.S.G. Industrial Institute* (1995 SC)

**CONCLUSION**: ✅ CONSUMER / ❌ NOT CONSUMER

**IF CONSUMER**:

**COMPLAINT CLASSIFICATION**:

1. **DEFECT IN GOODS** (Section 2(10)): Fault, imperfection in quality/quantity/purity/standard
2. **DEFICIENCY IN SERVICES** (Section 2(11)): Inadequacy in quality, nature, manner of service
3. **UNFAIR TRADE PRACTICE** (Section 2(47)):
   - False representation (quality, sponsorship, approval)
   - Misleading advertisement
   - Bait advertising
   - False gift/prize offers
   - Withholding material information

**RELIEF SOUGHT**:
- Removal of defect
- Replacement of goods
- Refund of price paid
- Compensation for loss/injury
- Discontinuance of unfair practice
- Penalty

**JURISDICTION** (Pecuniary):
- Value ≤ ₹1 crore → DISTRICT COMMISSION
- Value > ₹1 crore ≤ ₹10 crore → STATE COMMISSION
- Value > ₹10 crore → NATIONAL COMMISSION

**EVIDENCE REQUIRED**:
- Purchase receipt/invoice ✓
- Warranty/guarantee card
- Correspondence with seller/manufacturer
- Photos/videos of defect
- Expert reports (if technical defect)

**FILING PROCEDURE**:
1. Complaint in prescribed form
2. Court fee (nominal ₹100-500)
3. Submit to appropriate commission (District/State/National based on value)

**ALTERNATIVE - CCPA COMPLAINT**:
If widespread unfair trade practice → Complaint to Central Consumer Protection Authority
- CCPA can act suo motu
- Penalties: Up to ₹10 lakhs (first offense), ₹50 lakhs (repeat)
- False advertisement: Endorser liability (celebrities liable)

**PRODUCT LIABILITY** (If personal injury/property damage from defective product):
Sections 82-87 - Strict liability framework
- No need to prove negligence
- Liable parties: Manufacturer, service provider, seller
- Grounds: Manufacturing defect, design defect, inadequate instructions, non-conformance with safety standards

**PROTOCOL REFERENCE**: IL-CONSUMER-001 Sections 2-6 (Consumer Rights, Unfair Trade Practices, Product Liability)

**LEGAL DISCLAIMER**: This analysis provides legal information about consumer protection rights. It does NOT constitute legal advice. Consult qualified consumer advocates before filing complaints.
