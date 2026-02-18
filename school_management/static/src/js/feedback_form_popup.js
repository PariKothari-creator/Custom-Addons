/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { ListController } from "@web/views/list/list_controller";

patch(ListController.prototype, {
    async openRecord(record) {
        if (this.props.resModel === "students.feedback") {

            this.actionService.doAction({
                type: "ir.actions.act_window",
                res_model: this.props.resModel,
                res_id: record.resId,
                views: [[false, "form"]],
                target: "new",
            });
        } else {

            return super.openRecord(...arguments);
        }
    }
});