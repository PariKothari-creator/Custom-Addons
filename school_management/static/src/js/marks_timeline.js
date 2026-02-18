/** @odoo-module **/
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class GenericMarksTimeline extends Component {
    static template = "school_management.GenericMarksTimeline";
    static props = { ...standardFieldProps };


    get items() {
        return [];
    }


    getColor(item) {
        return "#adb5bd";
    }
}

registry.category("fields").add("marks_timeline_generic", {
    component: GenericMarksTimeline,
});