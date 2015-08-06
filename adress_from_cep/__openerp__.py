# -*- encoding: utf-8 -*-
##############################################################################
#
#    Autocomplete Adress from CEP for Odoo
#    Copyright (C) 2015 KMEE (http://www.kmee.com.br)
#    @author Michell Stuttgart <michell.stuttgart@kmee.com.br>
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

{
    'name': 'Autocomplete Adress from CEP',
    'version': '0.1',
    'category': 'Generic Modules',
    'description': """
    This module fill res_partner and res_company adress through of cep. This
    search is provided from SIGEPWEB webservice of Brazil Correios.
    """,
    'author': 'KMEE',
    'license': 'AGPL-3',
    'website': 'www.kmee.com.br',
    'depends': [
        'base',
    ],
    'data': [
        'view/res_partner.xml',
        'view/res_company.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'active': False,
    'external_dependencies': {
        'python': ['suds'],
    }

}

