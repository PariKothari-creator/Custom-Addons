from odoo import models, fields
from odoo.http import request

class ResUsers(models.Model):
    _inherit = "res.users"

    timer_enable = fields.Boolean(string="Enable Session Timer", default=True)
    set_time = fields.Integer(string="Idle Time (Minutes)", default=60)


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        res = super().session_info()
        user = request.env.user

        res.update({
            "timer_enable": user.timer_enable,
            "timer_set_time": user.set_time,
        })
        return res
