# Case 328 — GT improvement regression

This folder is a reproducible regression case for `sgs-recharge-advisor`
v1.0.0.

## Result at a glance

| | Historical GT | Skill candidate |
|---|---:|---:|
| Cash | 506.2 CNY | **504.0 CNY** |
| Deterministic yuanbao | 136,100 | **137,300** |
| Difference | — | **-2.2 CNY / +1,200 yuanbao** |

Within the explicitly declared **known-action model**, the candidate is the
finite-search winner.

**Known-action-set optimality:** `PASS`  
**Live-game global optimality:** `NOT_VERIFIED`

## Folder layout

```text
328/
├── README.md
├── CASE_REPORT.md
├── case.json
├── input/
│   ├── aim.txt
│   └── note.pdf
├── baseline/
│   └── gt-reconstructed.md
├── result/
│   ├── plan.md
│   ├── search-result.json
│   └── verify-output.txt
└── tools/
    └── verify_case.py
```

## Source integrity

`input/aim.txt` and `input/note.pdf` are copies of the supplied test inputs.
Their SHA-256 hashes are recorded in `case.json`.

The original historical `gt.md` was not available when this package was
created. `baseline/gt-reconstructed.md` therefore reconstructs **only** the
baseline facts explicitly retained by `aim.txt`; it does not invent missing GT
content.

## Run the checker

```bash
python tools/verify_case.py
```

The checker enumerates the declared action model under the 506.2 CNY budget and
asserts that the best deterministic-yuanbao candidate is:

```text
328 + 128 + 30 + week-card(12) + regular 6
= 504 CNY
= 137,300 deterministic yuanbao
```

See [CASE_REPORT.md](./CASE_REPORT.md) for the reasoning and limitations.
