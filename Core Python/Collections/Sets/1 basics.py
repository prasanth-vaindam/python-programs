"""
Scenario 2: The Email Campaign Manager
You're building an email marketing tool. You have a list of 50,000 email addresses
from various sources (some lists overlap). Before sending a campaign,
you need to remove all duplicates and also exclude anyone who has previously
unsubscribed (you have a separate list of 5,000 unsubscribed emails).

What data structure(s) would you use and why?

As we are getting emails from different sources some of them might be lists and others sets of
i am trying to eliminate the duplicates by combining all the sources into a Combined_SET
As set will not allow duplicates, however the order is not maintained which not necessary for us as of now
in the second step i am iterating over the list of unsubscribed emails which is also converted to set to remove
duplicates and then if it is present in the Combined_SET i am removing it
"""
import itertools

list1 = ["email1", "email2"]
list2 = ["email2", "email3", "email4"]
list3 = {"email5", "email6"}
unsubscribedList = ["one", "two", "email4"]
unsubscribedListSet = set(unsubscribedList)

combined_set = set(itertools.chain(list1, list2, list3))

for item in unsubscribedListSet:
    if combined_set.__contains__(item):
        combined_set.remove(item)
print(combined_set)


# final_emails = set(itertools.chain(list1, list2, list3)) - set(unsubscribed_emails)
# combined_set = {x for lst in [list1, list2, list3] for x in lst}
