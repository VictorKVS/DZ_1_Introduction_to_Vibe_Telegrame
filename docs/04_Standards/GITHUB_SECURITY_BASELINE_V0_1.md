# GitHub Security Baseline v0.1

## Назначение

Чек-лист минимальной безопасной организации репозитория FATHER и будущих дочерних проектов.

## Repository Baseline

- [ ] `README.md`
- [ ] `SECURITY.md`
- [ ] `.gitignore`
- [ ] `.editorconfig`
- [ ] dependency manifest
- [ ] lock file where applicable
- [ ] tests directory
- [ ] CI workflow
- [ ] security scan workflow
- [ ] issue template
- [ ] pull request template
- [ ] release/versioning policy
- [ ] documentation navigation

## Access & Governance

- [ ] repository visibility justified
- [ ] least-privilege collaborators
- [ ] protected default branch where supported
- [ ] pull requests required for significant changes
- [ ] review requirement defined
- [ ] CODEOWNERS for team/high-assurance mode
- [ ] security-sensitive paths have owner/reviewer
- [ ] stale access periodically reviewed

## Secrets

- [ ] no secrets in repository
- [ ] `.env` excluded
- [ ] credentials stored in secret manager/GitHub Secrets or equivalent
- [ ] secret scanning enabled or implemented in CI
- [ ] accidental secret exposure has revoke/rotate procedure

## CI/CD Security

- [ ] lint/quality check
- [ ] unit tests
- [ ] SAST
- [ ] secrets scan
- [ ] SCA/dependency scan
- [ ] license policy check where needed
- [ ] build verification
- [ ] SBOM target
- [ ] container scan where containers exist
- [ ] IaC scan where IaC exists
- [ ] integration tests
- [ ] DAST/API security tests where a running web/API surface exists
- [ ] release security gate

## Supply Chain

- [ ] dependencies pinned/locked where feasible
- [ ] automated dependency update policy defined
- [ ] third-party package provenance considered
- [ ] critical dependency replacement plan exists
- [ ] artifact identity/version recorded
- [ ] generated SBOM retained when enabled

## Secure Development

- [ ] security requirements linked to implementation
- [ ] threat model exists for applicable scope
- [ ] authorization negative tests exist
- [ ] sensitive logging avoided
- [ ] input validation rules covered
- [ ] unsafe defaults prohibited
- [ ] dependency additions trigger review

## Release

- [ ] release has version/tag
- [ ] changelog/release notes
- [ ] critical/high findings reviewed
- [ ] unresolved residual risk recorded
- [ ] rollback path exists
- [ ] deployment secrets/config separated from source
- [ ] monitoring readiness confirmed

## Operations

- [ ] vulnerability review cadence defined
- [ ] patch/update process defined
- [ ] incident reporting path defined
- [ ] logs/alerts available where applicable
- [ ] backup/recovery validated where applicable
- [ ] access review cadence defined

## Gate Rule

`NOT APPLICABLE` допустим только с причиной. Пустой пункт не считается выполненным. Для production/high-assurance профилей критические пункты должны быть подтверждены evidence.
