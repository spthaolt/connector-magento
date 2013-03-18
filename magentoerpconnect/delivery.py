# -*- coding: utf-8 -*-
##############################################################################
#
#    Authors: Guewen Baconnier, Sébastien Beau
#    Copyright (C) 2010 BEAU Sébastien
#    Copyright 2011-2013 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm


class delivery_carrier(orm.Model):
    _inherit = "delivery.carrier"

    def _carrier_code(self, cr, uid, ids, name, args, context=None):
        res = {}
        for carrier in self.browse(cr, uid, ids, context=context):
            if not carrier.magento_code:
                res[carrier.id] = False
                continue
            res[carrier.id] = carrier.magento_code.split('_')[0]
        return res

    _columns = {
        'magento_code': fields.char(
            'Magento Carrier Code',
            size=64,
            required=False),
        'magento_tracking_title': fields.char(
            'Magento Tracking Title',
            size=64,
            required=False),
        # in Magento, the delivery method is something like that:
        # tntmodule2_tnt_basic
        # where the first part before the _ is always the carrier code
        # in this example, the carrier code is tntmodule2
        'magento_carrier_code':
            fields.function(_carrier_code,
                            string='Magento Base Carrier Code',
                            size=32,
                            type='char')
    }
