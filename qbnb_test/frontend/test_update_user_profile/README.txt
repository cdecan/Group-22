I cannot use comments in test_update_user_profile.out or test_update_user_profile.in,
so I am writing my explanation here, I have used boundary testing, output partition and input partition,
for boundary testing, there was only one thing that had a boundary that needed to be tested for, which is the username
length requirement, so I tested for when the length is at 2 and 20 to see if it works correctly with the requirements.
Then I did output partitioning, I tested for every single possible output except "unknown error", because I do not know
how to trigger unknown error. I also tested for input partitioning, I tested for possible inputs in the menu as well as
in email changing, name changing, and postal code changing. I did not test multiple inputs for address because there is
no requirements for address.