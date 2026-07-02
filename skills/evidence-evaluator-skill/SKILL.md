---
name: evidence-evaluator-skill
description: Assess source credibility and evidence quality using CRAAP test and evidence hierarchies.
---

# Evidence Evaluator Skill

## Purpose
Assess source credibility and evidence quality using CRAAP test and evidence hierarchies.

## Trigger Conditions
Keywords: "evaluate source", "is this credible", "check evidence", "study quality", "reliable source"

## Procedure

### Phase 1: CRAAP Test
**C - Currency**: How recent?
**R - Relevance**: Fits the need?
**A - Authority**: Qualified author? Reputable publisher?
**A - Accuracy**: Verifiable? Sources cited? Peer-reviewed?
**P - Purpose**: Why created? Bias present?

Score each: 0-5 (Weight: R=1.5x, A=2x, A=2x, others=1x)
Total score / 37.5 = Credibility %

###  Phase 2: Evidence Hierarchy
**Rank by epistemic strength**:
1. Systematic reviews & meta-analyses (Highest)
2. Randomized controlled trials
3. Cohort studies
4. Case-control studies
5. Cross-sectional studies
6. Case reports
7. Expert opinion
8. Anecdote (Lowest)

### Phase 3: Study Quality (if applicable)
- **Design**: Appropriate for question?
- **Sample size**: Adequate power?
- **Bias**: Selection, measurement, reporting?
- **Confounds**: Controlled?
- **Statistics**: P-values, effect sizes, CIs?
- **Reproducibility**: Replicable?

### Phase 4: Verdict
- **Credibility**: 90-100% Highly credible / 70-89% Credible / 50-69% Questionable / <50% Not credible
- **Use recommendation**: ✅ Use / ✓ Use with caveats / ⚠️ Verify first / ❌ Don't use

## Tool Access
**Allowed:** Read

## Integration
**Agent**: evidence-evaluator
**Protocols**: THINK-EVIDENCE-001 to 005

## Example
**Input**: Blog post claiming "Coffee causes cancer"

**Output**:
- **CRAAP**: C=3, R=3, A=1 (no qualifications), A=1 (no sources), P=2 (clickbait) = 25% credible
- **Hierarchy**: Anecdote (lowest level)
- **Actual evidence**: WHO meta-analyses show coffee protective against several cancers
- **Verdict**: ❌ Don't use blog post, use systematic reviews instead
