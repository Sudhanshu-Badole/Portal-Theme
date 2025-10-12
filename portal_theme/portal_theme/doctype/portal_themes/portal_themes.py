# Copyright (c) 2025, Sudhanshu Badole and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PortalThemes(Document):

	def validate(self):
		if self.enable:
			self.status = "Active"
		else:
			self.status = "Inactive"

@frappe.whitelist()
def get_active_portal_theme():
    theme = frappe.get_all(
        "Portal Themes",
        filters={"status": "Active"},
        fields="*",
        limit=1
    )
    return theme[0] if theme else {}
