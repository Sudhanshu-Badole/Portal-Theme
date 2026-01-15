import frappe


@frappe.whitelist(allow_guest=True)
def get_active_theme_css():
	"""
	Returns CSS of the currently active Portal Theme
	"""
	theme = frappe.get_value("Portal Theme", filters={"is_active": 1}, fieldname="css_content")

	return {"css": theme or ""}
