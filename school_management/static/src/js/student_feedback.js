/** @odoo-module **/

import {registry} from "@web/core/registry";
import {Component,useState} from "@odoo/owl";
import {rpc} from "@web/core/network/rpc";
import { user } from "@web/core/user";
import { useService } from "@web/core/utils/hooks";
import { ConfirmationDialog, AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";



class StudentFeedbackClient extends Component{
    static template = "student_feedback.FeedbackForm";
    setup(){
      this.orm = useService("orm");
      this.dialog = useService("dialog")
      console.log(user.userId);
      const today = new Date().toISOString().split("T")[0];
      this.state= useState({
        all_students: [],
        students:[],
        teachers:[],
        classes :[],
        student_id:"",
        teacher_id:user.userId,
        class_id:"",
        feedback_date: today,
        rating:"",
        remarks:""

      });
      this.loadStudents();
    }

    async loadStudents(){

      const classes = await this.orm.searchRead("school.class",[],["id","name"]);
      this.state.classes = classes;

      const students = await this.orm.searchRead("school.student",[],["id","name","class_id"]);
      this.state.all_students = students;

    }


      onClassChange(ev){
      const classId = parseInt(ev.target.value);
      this.state.class_id = classId;

      this.state.students = this.state.all_students.filter(student => {
      return  student.class_id[0] === classId;})
      }

      async submitFeedback(){

      if(!this.state.feedback_date){
      return alert("Please select a Feedback Date");
      }
      if(!this.state.class_id){
      return alert("Please select a Class");
      }
      if(!this.state.student_id){
      return alert("Please select a Student");
      }
      if(!this.state.rating){
      return alert("Please select a Rating");
      }
      if(!this.state.discipline_grade){
      return alert("Please select a Discipline Grade");
      }
      if(!this.state.remarks || this.state.remarks.trim()==""){
      return alert("Please Enter Remark");
      }
       await this.orm.create("students.feedback",[{
         student_id: this.state.student_id,
         teacher_id: this.state.teacher_id,
         rating: this.state.rating,
         remarks: this.state.remarks,
         class_id: this.state.class_id,
         feedback_date: this.state.feedback_date,
         discipline_grade: this.state.discipline_grade
       }]);

      const today = new Date().toISOString().split("T")[0];
       this.state.student_id ="";
       this.state.teacher_id = "";
       this.state.class_id ="";
       this.state.rating="";
       this.state.remarks ="";
       this.state.discipline_grade="";
       this.state.feedback_date= today;

       this.dialog.add(AlertDialog,{
        title: "Success",
        body: "Feedback saved successfully",
        buttons: [ { text: "OK", class: "btn-primary",close:true
       },],
       });
    }
  }
       registry.category("actions").add("student_feedback",StudentFeedbackClient);