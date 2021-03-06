odoo.define('facebase.facebase_js', function (require) {
"use strict";
    var ListController = require('web.ListController');
    var rpc = require('web.rpc');
    ListController.include({
       renderButtons: function($node) {
       this._super.apply(this, arguments);
           if (this.$buttons) {
             this.$buttons.find('.oe_operate_button').click(this.proxy('operate_action'))
             this.$buttons.find('.oe_synchronize_button').click(this.proxy('synchronize_action'))
           }
       },

       operate_action: function () {
            rpc.query({
                model: 'da.facebase',
                method: 'recognition'
            })
       },
       synchronize_action: function () {
            rpc.query({
                model: 'da.facebase',
                method: 'synchronize'
            })
       }
    })
})
