$(function () {
    loadUITheme();
});

function loadUITheme() {
    frappe.call({
        method: "portal_theme.api.get_active_theme_css",
        callback: function (r) {
            if (!r || !r.message || !r.message.css) return;

            const css = r.message.css;
            let styleTag = document.getElementById("dynamic-ui-theme");

            // Create if not exists
            if (!styleTag) {
                styleTag = document.createElement("style");
                styleTag.id = "dynamic-ui-theme";
                document.head.appendChild(styleTag);
            }

            styleTag.textContent = css;
        }
    });
}
