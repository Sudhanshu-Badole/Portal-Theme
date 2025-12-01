// Copyright (c) 
// For license information, see license.txt

frappe.ui.form.on("Portal Theme", {
    add_variables(frm) {
        frm.clear_table("theme_variables");
        if (!frm.doc.primary && !frm.doc.secondary && !frm.doc.accent && !frm.doc.neutral) {
            frappe.throw("Please select at least one color.");
        }
        generate_color_rows(frm);
    }

});

function generate_color_rows(frm) {

    let colors = [
        { name: "primary", value: frm.doc.primary },
        { name: "secondary", value: frm.doc.secondary },
        { name: "accent", value: frm.doc.accent },
        { name: "neutral", value: frm.doc.neutral }
    ];

    colors.forEach(c => {
        if (!c.value) return;
        
        let exists = (frm.doc.variables || []).some(row => row.variable_name === c.name);
        if (exists) return;
        
        const light = c.value;
        const dark = darkenColor(light, 35);
        const lightText = getContrastText(light);
        const darkText = getContrastText(dark);

        frm.add_child("theme_variables", {
            variable_name: `--${c.name}`,
            light_value: light,
            dark_value: dark,
            light_text: lightText,
            dark_text: darkText
        });
    });
    frm.refresh_field("theme_variables");
}


function darkenColor(hex, percent = 30) {

    if (!hex) return "";

    hex = hex.replace("#", "");

    let r = parseInt(hex.substring(0, 2), 16);
    let g = parseInt(hex.substring(2, 4), 16);
    let b = parseInt(hex.substring(4, 6), 16);

    r = Math.max(0, parseInt(r * (1 - percent / 100)));
    g = Math.max(0, parseInt(g * (1 - percent / 100)));
    b = Math.max(0, parseInt(b * (1 - percent / 100)));

    return "#" +
        r.toString(16).padStart(2, "0") +
        g.toString(16).padStart(2, "0") +
        b.toString(16).padStart(2, "0");
}


function getContrastText(hex) {

    if (!hex) return "#000000";

    hex = hex.replace("#", "");

    let r = parseInt(hex.substring(0, 2), 16);
    let g = parseInt(hex.substring(2, 4), 16);
    let b = parseInt(hex.substring(4, 6), 16);

    let brightness = (r * 299 + g * 587 + b * 114) / 1000;

    return brightness > 128 ? "#000000" : "#FFFFFF";
}
