from odoo import  models,fields,api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    report_visible = fields.Boolean(string="Reports Visible",config_parameter = 'school_management.report_visible')

    def set_values(self):
        super().set_values()

        group = self.env.ref('school_management.group_report_download')
        users = self.env['res.users'].search([])

        if self.report_visible:
            users.write({'groups_id': [(4,group.id)]})
        else:
            users.write({'groups_id': [(3,group.id)]})
