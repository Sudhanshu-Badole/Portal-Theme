# Copyright (c) 2025, Sudhanshu Badole and contributors
# For license information, please see license.txt

from pydoc import doc

import frappe
from frappe.model.document import Document


class ThemeTemplate(Document):
	def before_insert(self):
		if not self.version:
			self.version = frappe.__version__
