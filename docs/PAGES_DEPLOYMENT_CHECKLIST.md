# GitHub Pages Deployment Checklist

GitHub Pages is optional. This checklist keeps deployment static and safe.

## Pre-deployment requirements

- [ ] `docs/index.md` exists.
- [ ] `python scripts/validate_static_status.py .` passes.
- [ ] `python scripts/check_public_safety.py .` passes.
- [ ] CI is green on `main`.
- [ ] `DONATIONS_ACTIVE` remains `NO`.
- [ ] `WALLETS_PUBLISHED` remains `NO`.
- [ ] No real wallet address is published.
- [ ] No private key, seed phrase, or signing material exists in the repository.
- [ ] No beneficiary private information is exposed.

## Recommended GitHub Pages settings

Use the lowest-complexity static deployment:

```text
Source: Deploy from a branch
Branch: main
Folder: /docs
```

Do not add backend services for the initial status page.

## Post-deployment review

After enabling Pages, review the published page for:

- accurate inactive donation status;
- clear safety boundaries;
- working policy links;
- no real wallet addresses;
- no private beneficiary information;
- no return-promise language;
- no trading-fund language.

## Rollback

If the published page contains unsafe content:

1. Disable GitHub Pages or revert the unsafe commit.
2. Confirm `docs/index.md` is safe.
3. Run CI.
4. Re-enable Pages only after review.
