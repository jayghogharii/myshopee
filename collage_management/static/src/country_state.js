odoo.define('website.layout', function (require) {
    'use strict';
    
    var publicWidget = require('web.public.widget');
    
    publicWidget.registry.portalDetails = publicWidget.Widget.extend({
        selector: '.country-state',
        events: {
            'change select[name="country_id"]': '_onCountryChange',
        },
    
        /**
         * @override
         */
        start: function () {
            var def = this._super.apply(this, arguments);
    
            this.$state = this.$('select[name="state_id"]');
            this.$stateOptions = this.$state.filter(':enabled').find('option:not(:first)');
            this._adaptAddressForm();
    
            return def;
        }
});
});