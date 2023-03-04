import frappe

@frappe.whitelist()
def create_gym_subscription_item():
    gym_subscription_item = frappe.get_doc({
        "doctype": "Item",
        "item_code": "Gym Membership Subscription",
        "item_group": "Services",
        "stock_uom": "Nos",
        "is_stock_item": 0
    })

    gym_subscription_item.insert()
    frappe.db.commit()

@frappe.whitelist()
def create_gym_membership_subscription_plans():
    gym_membership_subscription_plan_names = ["Weekly", "Monthly", "Yearly"]

    for gym_membership_subscription_plan_name in gym_membership_subscription_plan_names:
        billing_interval = "Week"
        
        if gym_membership_subscription_plan_name == "Monthly":
            billing_interval = "Month"

        elif gym_membership_subscription_plan_name == "Yearly":
            billing_interval = "Year"

        subscription_plan = frappe.get_doc({
            "doctype": "Subscription Plan",
            "plan_name": f"{gym_membership_subscription_plan_name} Gym Membership Subscription Plan",
            "item": "Gym Membership Subscription",
            "price_determination": "Fixed Rate",
            "billing_interval": f"{billing_interval}",
            "billing_interval_count": 1
        })

        subscription_plan.insert()
        frappe.db.commit()
        
        gym_membership_subscription_plan = frappe.get_doc({
            "doctype": "Gym Membership Subscription Plan",
            "plan_name": f"{gym_membership_subscription_plan_name} Plan",
            "interval": f"{gym_membership_subscription_plan_name}",
            "enabled": 1,
            "subscription_plan": f"{subscription_plan.name}"
        })

        gym_membership_subscription_plan.insert()
        frappe.db.commit()