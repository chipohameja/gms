# Copyright (c) 2023, Chipo Hameja and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class GymMembershipSubscriptionPlan(WebsiteGenerator):
	def validate(self):
		subscription_plan = frappe.get_doc("Subscription Plan", f"{self.subscription_plan}")
		subscription_plan.cost = self.cost
		subscription_plan.save()
