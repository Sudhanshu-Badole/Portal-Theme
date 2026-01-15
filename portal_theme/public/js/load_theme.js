function loadUITheme() {
	if (window.frappe && frappe.call) {
		// Desk
		frappe.call({
			method: "portal_theme.api.api.get_active_theme_css",
			callback: (r) => applyCSS(r?.message?.css),
		});
	} else {
		// Portal
		fetch("/api/method/portal_theme.api.api.get_active_theme_css", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"X-Frappe-CSRF-Token": window.csrf_token || "",
			},
		})
			.then((r) => r.json())
			.then((r) => applyCSS(r?.message?.css));
	}
}

function applyCSS(css) {
	if (!css) return;

	let styleTag = document.getElementById("dynamic-ui-theme");
	if (!styleTag) {
		styleTag = document.createElement("style");
		styleTag.id = "dynamic-ui-theme";
		document.head.appendChild(styleTag);
	}
	styleTag.textContent = css;
}

loadUITheme();
