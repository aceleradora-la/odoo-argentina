##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _
from odoo.tools.misc import formatLang
from ast import literal_eval

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    checkbook_ids = fields.One2many(
        'account.checkbook',
        'journal_id',
        'Checkbooks',
        auto_join=True,
    )

    #@api.model
    #def create(self, vals):
    #    rec = super(AccountJournal, self).create(vals)
    #    issue_checks = self.env.ref(
    #        'account_check.account_payment_method_issue_check')
    #    outbound_payment_method_line_ids = rec.outbound_payment_method_line_ids.filtered(lambda r: r.payment_method_id.code == issue_checks.code)
    #    #if (issue_checks in rec.outbound_payment_method_line_ids and
    #    if (outbound_payment_method_line_ids and not rec.checkbook_ids):
    #        rec._create_checkbook()
#
 #       return rec

    #def _create_checkbook(self):
    #    """ Create a check sequence for the journal """
    #    for rec in self:
    #        checkbook = rec.checkbook_ids.create({
    #            'journal_id': rec.id,
    #        })
    #        checkbook.state = 'active'

    #@api.model
    #def _enable_issue_check_on_bank_journals(self):
    #    """ Enables issue checks payment method
    #        Called upon module installation via data file.
    #    """
    #    issue_checks = self.env.ref(
    #        'account_check.account_payment_method_issue_check')
    #    domain = [('type', '=', 'bank')]
    #    force_company_id = self._context.get('force_company_id')
    #    if force_company_id:
    #        domain += [('company_id', '=', force_company_id)]
    #    bank_journals = self.search(domain)
    #    for bank_journal in bank_journals:
    #        if not bank_journal.checkbook_ids:
    #            bank_journal._create_checkbook()
    #        bank_journal.write({
    #            'outbound_payment_method_ids': [(4, issue_checks.id, None)],
    #        })

