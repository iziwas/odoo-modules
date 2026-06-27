/** @odoo-module **/

import {companyService} from "@web/webclient/company_service";
import {cookie} from "@web/core/browser/cookie";
import {patch} from "@web/core/utils/patch";
import {session} from "@web/session";

patch(companyService, {
    start(env, {user, router, action}) {
        const hashCompanyIds = router.current.hash.cids;
        const shouldSelectAll = !hashCompanyIds && !cookie.get("cids");

        if (shouldSelectAll) {
            const preferred = session.user_companies?.preferred_companies;
            if (preferred?.length > 0) {
                const defaultCompanyId = session.user_companies.current_company;
                const ordered =
                    defaultCompanyId && preferred.includes(defaultCompanyId)
                        ? [defaultCompanyId, ...preferred.filter((id) => id !== defaultCompanyId)]
                        : preferred;
                cookie.set("cids", ordered.join("-"));
            }
        }
        return super.start(env, {user, router, action});
    },
});
