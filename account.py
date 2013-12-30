# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp.osv import fields, osv

class account_invoice(osv.osv):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    def _check_invoice_number(self, cr, uid, ids, context=None):
        obj = self.browse(cr, uid, ids[0], context=context)
	if not obj.supplier_invoice_number:
		return True
	list_values = obj.supplier_invoice_number.split('-')
	if obj.supplier_invoice_number.find('-') < 0: 
		return False
	if obj.supplier_invoice_number[4] <> '-': 
		return False
	if len(list_values) <> 2:
		return False
	if len(list_values[0]) <> 4 or len(list_values[1]) <> 8:
		return False
	try:
		int1 = int(list_values[0])
		int2 = int(list_values[1])
	except:
		return False
        return True


    _constraints = [
        (_check_invoice_number, 'Formato de número de factura de proveedor inválido', ['supplier_invoice_number']),
    ]

account_invoice()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
