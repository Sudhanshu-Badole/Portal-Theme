// Copyright (c) 2025, Sudhanshu Badole and contributors
// For license information, please see license.txt

frappe.ui.form.on("Portal Theme", {
    refresh(frm) {
        if (!frm._color_button_added) {
            frm.add_custom_button("Generate Theme", () => {
                open_color_shade_dialog(frm);
            });
            frm._color_button_added = true;
        }
    },
});

function open_color_shade_dialog(frm) {

    let d = new frappe.ui.Dialog({
        title: "Theme Color Generator",
        fields: [
            {
                label: "Color 1",
                fieldname: "c1",
                fieldtype: "Color",
                reqd: true
            },
            {
                label: "Color 2",
                fieldname: "c2",
                fieldtype: "Color",
                reqd: true
            },
            {
                label: "Color 3",
                fieldname: "c3",
                fieldtype: "Color",
                reqd: true
            },
            {
                label: "Color 4",
                fieldname: "c4",
                fieldtype: "Color",
                reqd: true
            },
            {
                label: "Number of Shades (4-8)",
                fieldname: "shade_count",
                fieldtype: "Int",
                default: 5,
                reqd: true,
                description: "Max 3"
            }
        ],
        primary_action_label: "Generate",
        primary_action(values) {

            if (values.shade_count < 3) {
                frappe.msgprint("Shades must be between 1 and 3.");
                return;
            }

            generate_theme_variables(frm, values);
            d.hide();
        }
    });

    d.show();
}

function generate_theme_variables(frm, values) {

    // Fixed 4 color names
    const names = ["primary", "secondary", "accent", "neutral"];
    const baseColors = [values.c1, values.c2, values.c3, values.c4];

    // Clear previous rows
    frm.clear_table("theme_variables");

    let shadeCount = values.shade_count;

    // Calculate shade levels (even spread)
    let steps = [];
    let stepGap = 100 / (shadeCount + 1);
    for (let i = 0; i < shadeCount; i++) {
        steps.push(100 - (i + 1) * stepGap);
    }

    // For each of the 4 colors
    names.forEach((name, index) => {

        let baseColor = baseColors[index];

        steps.forEach((percent, shadeIndex) => {
            let generated = adjustColor(baseColor, percent);

            frm.add_child("theme_variables", {
                variable_name: `--${name}-${(shadeIndex + 1)}00`,
                light_value: generated,
                dark_value: generated
            });
        });
    });

    frm.refresh_field("theme_variables");
    frappe.show_alert("Theme variables generated!",5);
}


// Utility function: darken/lighten color by percent (0-100)
function adjustColor(hex, percent) {

    let num = parseInt(hex.replace("#", ""), 16),
        r = (num >> 16),
        g = (num >> 8) & 0xff,
        b = num & 0xff;

    r = Math.round(r * (percent / 100));
    g = Math.round(g * (percent / 100));
    b = Math.round(b * (percent / 100));

    return "#" + (1 << 24 | (r << 16) | (g << 8) | b)
        .toString(16)
        .slice(1)
        .toUpperCase();
}
