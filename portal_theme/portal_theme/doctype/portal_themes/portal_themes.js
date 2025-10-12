// Copyright (c) 2025, Sudhanshu Badole and contributors
// For license information, please see license.txt

frappe.ui.form.on("Portal Themes", {
	refresh(frm) {

	},
    
    after_save: function (frm) {
        window.location.reload();
    },

    enable: function(frm){
        if(frm.doc.enable){
            frm.set_value("status","Active")
        }else{
            frm.set_value("status","Inactive")
        }
    }
});
