/** @odoo-module **/

import {companyService} from "@web/webclient/company_service";
import {cookie} from "@web/core/browser/cookie";
import {patch} from "@web/core/utils/patch";
import {session} from "@web/session";

patch(companyService, {   
    start(env, { user, router, action }) {
        const hashCompanyIds = router.current.hash.cids;
        const shouldSelectAll = !hashCompanyIds && !cookie.get("cids");
        
        if (shouldSelectAll) {
            const allCompanyIds = Object.values(session.user_companies.preferred_companies)
                .map(id => parseInt(id));
            
            if (allCompanyIds.length > 0) {
                const cidsHash = allCompanyIds.join("-");
                router.current.hash.cids = cidsHash;
            }
        }
        return super.start(env, { user, router, action });
    },
});