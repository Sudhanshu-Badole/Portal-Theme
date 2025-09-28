# Copyright (c) 2025, Indictrans and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PortalThemeSetting(Document):
	
	def validate(self):
		if self.enable:
			self.status = "Active"
		else:
			self.status = "Inactive"
