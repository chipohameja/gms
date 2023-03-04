# Copyright (c) 2022, Chipo Hameja and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymMember(Document):
	def validate(self):
		self.full_name = f"{self.first_name} {self.last_name}"
	
	def after_insert(self):
		self.create_customer_record()

	def create_customer_record(self):
		customer = frappe.get_doc({
			"doctype": "Customer",
			"customer_name": f"{self.full_name}",
			"customer_type": "Individual",
			"customer_group": "All Customer Groups",
			"territory": "All Territories",
			"email address": f"{self.email}"
		})
		
		customer.insert()
		frappe.db.commit()

		self.customer = customer.name
		self.save()
		frappe.db.commit()
