# Changelog

All notable changes to this module are documented in this file.

Version format follows the Odoo convention: `{odoo_series}.{major}.{minor}.{patch}`
- **major** : breaking changes (model rename, field removal)
- **minor** : new features (backward compatible)
- **patch** : bug fixes only

---

## [17.0.1.2.0] - 2026-06-27

### Added
- Prioritize the user's default company (`company_id`) in the preferred
  companies list — it is placed first so it appears as the primary active
  company in the interface header

---

## [17.0.1.1.0] - 2026-06-27

### Fixed
- `fields.Many2many` was passing `"user_id"` as the relation (junction table)
  name instead of a proper table name, causing a malformed database schema
- `session_info` now guards against a `KeyError` when `user_companies` is
  absent from the result (portal and public users)
- JavaScript: added null guard on `session.user_companies.preferred_companies`
  to prevent a `TypeError` crash at webclient startup when the key is missing
- JavaScript: replaced direct mutation of `router.current.hash.cids` with
  `cookie.set("cids", ...)` to ensure the value is reliably picked up by
  the original `companyService.start()`

### Added
- Server-side `@api.constrains` on `preferred_company_ids` to reject any
  company outside the user's allowed scope (`company_ids`)
- `write()` override to automatically remove stale preferred companies when
  an administrator revokes a company from the user's allowed list

---

## [17.0.1.0.0] - 2025-11-08

### Added
- Initial release
- `preferred_company_ids` Many2many field on `res.users`
- `ir.http.session_info` override to expose preferred companies in the
  web client session
- JavaScript patch on `companyService` to auto-activate preferred companies
  on login when no session company selection exists
- User preferences view to select preferred companies (restricted to
  allowed companies via domain)
