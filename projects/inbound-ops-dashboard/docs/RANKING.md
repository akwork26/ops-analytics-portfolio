# Mix-Weighted Performer Ranking

## Why not just rank by units/hour?

Associates process a **mix** of item sizes, and different sizes carry different rate
expectations. If one associate spent the interval on a hard mix (mostly large items) and
another on an easy mix (mostly small), ranking both by raw units/hour unfairly punishes
the first. Managers lose trust in a leaderboard that's really just measuring who got the
easy work.

## The approach: percent-of-target

For each associate, compute a **blended target** from their own actual size mix, then rank
by how close their actual rate came to *that personalized target*.

```
smallShare = smallUnits / (smallUnits + mediumUnits)

target     = smallShare * SMALL_GOAL + (1 - smallShare) * MEDIUM_GOAL
actual     = (smallUnits + mediumUnits) / (smallHours + mediumHours)
pctOfTarget = actual / target
```

- An associate at a 50/50 mix with `SMALL_GOAL = 400` and `MEDIUM_GOAL = 200` gets a
  blended target of `300`.
- `pctOfTarget >= 1.0` → **making rate** → goes in the **Top** list (best first).
- `pctOfTarget < 1.0`  → **missing rate** → goes in the **Bottom** list (worst first).

The two lists are mutually exclusive, so nobody appears twice. If either list is short, a
fallback fills it without creating overlaps.

## Eligibility

To keep the ranking meaningful, an associate must clear a minimum volume for the interval
(e.g. a units threshold *and* having both units and hours recorded). Below that, there
isn't enough signal to rank fairly.

## Lesson learned (reliability)

The goal constants are **inlined inside the ranking function** rather than read from
top-level variables. Early versions hit a load-order bug: a suppressed top-level error
left shared constants `undefined`, which silently broke ranking. Inlining the scalar
constants inside the function that uses them made the ranking robust to load order.

> All numbers above (`400`, `200`, thresholds) are **illustrative placeholders** for this
> public writeup, not real operational targets.
