


$(document).ready(function () {
    frappe.call({
        method: "frappe.client.get",
        args: {
            doctype: "Portal Theme Setting",
            name: "Portal Theme Setting"
        },
        callback: function (r) {
            if (!r.exc && r.message) {
                let s = r.message;

                if (s.enable) {

                    let cssVars = `
                        :root {
                            /* Navbar */
                            --navbar-bg: ${s.navbar_color || "inherit"};
                            --navbar-text: ${s.navbar_text_color || "inherit"};

                            /* Primary Button */
                            --btn-primary-bg: ${s.primary_button_background || "inherit"};
                            --btn-primary-text: ${s.primary_button_text || "inherit"};
                            --btn-primary-hover-bg: ${s.primary_button_hover_background || "inherit"};

                            /* Secondary Button */
                            --btn-secondary-bg: ${s.secondary_button_background || "inherit"};
                            --btn-secondary-text: ${s.secondary_button_text || "inherit"};

                            /* Cards */
                            --card-bg: ${s.card_background_color || "inherit"};
                            --card-header-bg: ${s.card_header_color || "inherit"};
                            --card-header-text: ${s.card_header_text || "inherit"};
                            --card-text: ${s.card_text_color || "inherit"};

                            /* Forms */
                            --form-bg: ${s.form_background_color || "inherit"};
                            --form-text: ${s.form_text_color || "inherit"};

                            /* Portal Background */
                            --portal-bg: ${s.portal_background_color || "inherit"};

                            /* Section Headings */
                            --section-heading: ${s.section_heading_color || "inherit"};

                            /* Labels */
                            --label-text: ${s.label_text_color || "inherit"};
                        }
                    `;

                    let cssRules = `
                        /* Portal Background */
                        html, body {
                            background-color: var(--portal-bg) !important;
                        }
                        .page-container {
                            background-color: var(--portal-bg) !important;
                        }

                        /* Navbar */
                        .navbar {
                            background-color: var(--navbar-bg) !important;
                            color: var(--navbar-text) !important;
                        }
                        .navbar a, .navbar .nav-link {
                            color: var(--navbar-text) !important;
                        }

                        /* Primary Button */
                        .btn.btn-primary,
                        div#driver-popover-item .driver-popover-footer button.btn-primary,
                        div#driver-popover-item .driver-popover-footer button.driver-next-btn {
                            background-color: var(--btn-primary-bg) !important;
                            color: var(--btn-primary-text) !important;
                        }
                        .btn.btn-primary:hover {
                            background-color: var(--btn-primary-hover-bg) !important;
                        }

                        /* Secondary Button */
                        .btn.btn-secondary {
                            background-color: var(--btn-secondary-bg) !important;
                            color: var(--btn-secondary-text) !important;
                        }

                        /* Cards */
                        .card,
                        .card .card-body,
                        .card .card-content,
                        .card p,
                        .card span,
                        .card li,
                        .widget.card-box {
                            background-color: var(--card-bg) !important;
                            color: var(--card-text) !important;
                        }
                        .card .card-header,
                        .card-header {
                            background-color: var(--card-header-bg) !important;
                            color: var(--card-header-text) !important;
                        }

                        /* Forms */
                        .form-control {
                            background-color: var(--form-bg) !important;
                            color: var(--form-text) !important;
                            border-color: #c7c7c7 !important;
                            box-shadow: none !important;
                        }
                        .form-control:focus {
                            outline: none !important;
                            box-shadow: 0 0 0 1px var(--btn-primary-bg, #3498db) !important;
                        }

                        /* Section Headings */
                        h1, h2, h3, h4, h5, h6,
                        .section-head {
                            color: var(--section-heading) !important;
                        }

                        /* Labels */
                        .control-label,
                        .grid-heading-row {
                            color: var(--label-text) !important;
                        }

                        /* Dashboard widget links */
                        .widget.links-widget-box .link-item {
                            color: var(--card-text) !important;
                        }
                    `;

                    let styleTag = document.createElement("style");
                    styleTag.innerHTML = cssVars + cssRules;
                    document.head.appendChild(styleTag);
                }
            }
        }
    });
});
