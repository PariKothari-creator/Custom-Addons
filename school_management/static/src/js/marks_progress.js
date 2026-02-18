/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { GenericMarksTimeline } from "@school_management/js/marks_timeline";

patch(GenericMarksTimeline.prototype, {
    get items() {
        const fieldName = this.props.name;
        const modelName = this.props.record.resModel;
        const listData = this.props.record.data[fieldName];

        if (listData && listData.records && listData.records.length > 0) {
            return listData.records.map(rec => {

                if (modelName === 'school.student') {
                    return {
                        id: rec.id,
                        label: rec.data.name || 'Exam',
                        status: rec.data.result,
                        mode: 'student_view'
                    };
                }


                if (modelName === 'school.exam') {
                    return {
                        id: rec.id,
                        label: rec.data.subject_id ? rec.data.subject_id[1] : 'Subject',
                        marks: rec.data.marks || 0,
                        mode: 'exam_view'
                    };
                }
            });
        }
        return [];
    },

    getColor(item) {
        if (!item) return "#ccc";


       if (item.mode === 'student_view') {
            return item.status === 'pass' ? "#28a745" : "#dc3545";
        }


        if (item.mode === 'exam_view') {
            console.log(`Checking Marks for ${item.label}:`, item.marks);
            return item.marks >= 30 ? "#28a745" : "#dc3545";
        }

        return "#ccc";
    }
});