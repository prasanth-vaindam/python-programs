"""
Scenario 3: The Restaurant Order System
You're building a restaurant POS system.
Each table can have multiple orders, and each order contains multiple items.
You need to track which items are ordered, their quantities, and be able to
quickly check what's been ordered for any table. Also, the kitchen needs to
see a summary of all items being prepared across all tables.
"""
# tables = {}
# orders = [{"order_id":  {"item_name": "item1", "item_quantity": 2}}]

# tables = [
#         {"table_id": 1, "table_orders": [
#             {
#                 "order_id": 1,
#                 "order_items_and_quantity": [{"item_id": 1,
#                                               "item_name": "idly",
#                                               "item_quantity": 4
#                                               },
#                                              {"item_id": 2,
#                                               "item_name": "dosa",
#                                               "item_quantity": 5
#                                               }]
#             },
#             {
#                 "order_id": 2,
#                 "order_items_and_quantity": [{"item_id": 1,
#                                               "item_name": "idly",
#                                               "item_quantity": 4
#                                               },
#                                              {"item_id": 2,
#                                               "item_name": "dosa",
#                                               "item_quantity": 5
#                                               }]
#             }
#         ]},
#         {"table_id": 2, "table_orders": [
#             {
#                 "order_id": 1,
#                 "order_items_and_quantity": [{"item_id": 1,
#                                               "item_name": "idly",
#                                               "item_quantity": 4
#                                               },
#                                              {"item_id": 2,
#                                               "item_name": "dosa",
#                                               "item_quantity": 5
#                                               }]
#             },
#             {
#                 "order_id": 2,
#                 "order_items_and_quantity": [{"item_id": 1,
#                                               "item_name": "idly",
#                                               "item_quantity": 4
#                                               },
#                                              {"item_id": 2,
#                                               "item_name": "dosa",
#                                               "item_quantity": 5
#                                               }]
#             }
#         ]}
#     ]


# for each table table_id> iterate through List of Orders
# find out > what items(item_name) are order and their quantity (item_quantity)

# for table in tables:
#     for key,value in table:
#         if key == "table_id" and value == "1":
#             print(f"For table {key}")

# class table:
#     order
#
#     class order:
#         items = []

# total_items is probably intended to keep a tally of the various items sold or ordered.

# defaultdict is a subclass of the built-in Python dictionary (dict).
# It is designed to provide a default value for a nonexistent key when accessed.
# This means that if you try to access a key that hasn't been set yet,
# instead of raising a KeyError, it will automatically create a new entry with a
# default value. This greatly simplifies the logic needed when counting items.

# defaultdict is a subclass of the built-in Python dictionary (dict). It is designed to provide a default value for a nonexistent key when accessed. This means that if you try to access a key that hasn't been set yet, instead of raising a KeyError, it will automatically create a new entry with a default value. This greatly simplifies the logic needed when counting items.

