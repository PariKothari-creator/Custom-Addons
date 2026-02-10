/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import "@website_sale/js/website_sale";

publicWidget.registry.WebsiteSale.include({


    _submitForm: function () {

        const params = this.rootProduct;
        const extraQty = $('input[name="additional_qty"]').val();

        if (extraQty) {
            params['additional_qty'] = parseInt(extraQty || 0);
        }

        return this._super.apply(this, arguments);
    },
});