# Historical GT baseline — reconstructed

> **Status:** reconstructed baseline, not the original `gt.md`.

The original `gt.md` was not available in the current chat/file library when this
case was packaged. This file therefore reconstructs only the historical baseline
facts that are explicitly preserved in `input/aim.txt`.

## Historical cash schedule

| Date | Historical action | Cash (CNY) | Treatment in regression |
|---|---|---:|---|
| 2026-03-28 | `28月卡 + 0.2元` | 28.2 | opaque historical action |
| 2026-03-29 | `12周卡 + 12微信 + 6` | 30 | opaque historical action |
| 2026-03-30 | 30 CNY recharge | 30 | normal 3000 tier |
| 2026-03-31 | 328 CNY recharge | 328 | 32800 tier |
| 2026-04-01 | 30 CNY recharge | 30 | normal 3000 tier |
| 2026-04-02 | 30 CNY recharge | 30 | normal 3000 tier |
| 2026-04-03 | 30 CNY recharge | 30 | normal 3000 tier |
| **Total** |  | **506.2** | |

## Historical deterministic-yuanbao accounting used by the regression

`aim.txt` explicitly preserves the two custom entries as opaque observed actions:

- 2026-03-28 opaque action: **4,200 yuanbao**
- 2026-03-29 opaque action: **6,500 yuanbao**

For the ordinary recharge actions:

- first 30 CNY recharge: 3,000 base + 3,000 first-charge + 3,000 announcement single reward = **9,000**
- next three 30 CNY recharges: each 3,000 base + 3,000 announcement single reward = **18,000 total**
- 328 CNY recharge: 32,800 base + 32,800 first-charge + 32,800 chosen announcement reward = **98,400**

Therefore the historical baseline used in this case is:

```text
4,200
+ 6,500
+ 9,000
+ 18,000
+ 98,400
= 136,100 deterministic yuanbao
```

## Important limitation

The mechanics behind `28月卡`, `0.2元`, `12微信`, and the historical `6元` item
are not established by the current official notice. They are preserved only as
historical observed atoms, exactly as required by the Skill.

They are **not** promoted into reusable actions for the new search.
