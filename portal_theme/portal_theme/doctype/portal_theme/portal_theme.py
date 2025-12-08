# Copyright (c) 2025, Sudhanshu Badole
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re
from portal_theme.portal_theme.doctype.portal_theme.theme_css_body import css_body


class PortalTheme(Document):

	# ---------------------------------------------------------
	# HOOKS
	# ---------------------------------------------------------

	def on_update(self):
		"""Ensure slug consistency after updating"""
		self.slugify_theme_name()

	def before_save(self):
		all_doc = frappe.db.get_all(self.doctype, filters={"is_active": 1}, fields=['name'])
		for doc in all_doc:
			frappe.db.set_value(self.doctype, doc.name, "is_active", 0)
		self.slugify_theme_name()
		self.generate_css_for_doc()

	# ---------------------------------------------------------
	# SLUG UTILITIES
	# ---------------------------------------------------------

	@staticmethod
	def slugify(value: str) -> str:
		"""Convert a string to a URL/browser safe slug"""
		if not value:
			return ""

		value = value.strip().lower()
		value = re.sub(r"\s+", "-", value)
		value = re.sub(r"[^a-z0-9\-]", "", value)
		value = re.sub(r"-+", "-", value)

		return value.strip("-")

	def slugify_theme_name(self):
		"""Always derive slug from theme_name"""
		if self.theme_name:
			self.slug = self.slugify(self.theme_name)

	# ---------------------------------------------------------
	# CSS GENERATION
	# ---------------------------------------------------------

	def generate_css_for_doc(self):
		"""
		Generates CSS using theme_variables table and stores
		final CSS inside css_content field
		"""
		theme_name = self.theme_name or ""
		slug = self.slugify(theme_name)

		variables = []
		for row in self.get("theme_variables") or []:
			var_name = (row.variable_name or "").strip()
			if not var_name:
				continue

			variables.append({
				"variable_name": var_name,
				"light_value": row.light_value or "",
				"dark_value": row.dark_value or ""
			})

		css_content = self.build_css_content(variables)
		css_content += "\n\n/* Custom CSS Body */\n"
		css_content += css_body or ""

		# Save without updating modified timestamp
		self.db_set("css_content", css_content, update_modified=False)
		self.db_set("slug", slug, update_modified=False)

		frappe.logger("portal_theme").info(
			f"Generated Portal Theme CSS for {theme_name} ({slug})"
		)

	# ---------------------------------------------------------
	# CORE CSS BUILDER
	# ---------------------------------------------------------

	@staticmethod
	def build_css_content(variables):
		"""
		Builds rooted CSS variables for light & dark themes.

		variables format:
		[
			{
				"variable_name": "primary",
				"light_value": "#1e88e5",
				"dark_value": "#0d47a1"
			},
			...
		]
		"""

		def safe_name(name: str) -> str:
			return PortalTheme.slugify(name) if name else ""

		if not variables:
			return ""

		light_lines = []
		dark_lines = []

		for v in variables:
			name = (v.get("variable_name") or "").strip()
			if not name:
				continue

			cname = safe_name(name)
			light_val = v.get("light_value") or ""
			dark_val = v.get("dark_value") or light_val
			dark_mode_text = v.get("light_text") or "#000000"
			light_mode_text = v.get("dark_text") or "#ffffff"

			light_lines.append(f"  --{cname}: {light_val};")
			light_lines.append(f"  --{cname}-text-color: {dark_mode_text};")

			dark_lines.append(f"  --{cname}: {dark_val};")
			dark_lines.append(f"  --{cname}-text-color: {light_mode_text};")

		# Light mode block
		root_block = (
			":root {\n"
			+ "\n".join(light_lines) +
			"\n}\n\n"
		)

		# Dark mode using HTML attribute or class
		dark_attr_block = (
			':root[data-theme="dark"] {\n'
			+ "\n".join(dark_lines) +
			"\n}\n\n"
		)

		# Dark mode via system preference
		indented_dark = "\n".join("    " + line.strip() for line in dark_lines)
		# dark_media_block = (
		# 	"@media (prefers-color-scheme: dark) {\n"
		# 	"  :root {\n"
		# 	+ indented_dark +
		# 	"\n  }\n}\n\n"
		# )
		dark_media_block = ""

		return root_block + dark_attr_block + dark_media_block
