I cannot use comments in test_update_user_profile.out or test_update_user_profile.in,
so I am writing my explanation here, I have used boundary testing, output partition and input partition,
for boundary testing, there was only one thing that had a boundary that needed to be tested for, which is the username
length requirement, so I tested for when the length is at 2 and 20 to see if it works correctly with the requirements.
Then I did output partitioning, I tested for every single possible output except "unknown error", because I do not know
how to trigger unknown error. I also tested for input partitioning, I tested for possible inputs in the menu as well as
in email changing, name changing, and postal code changing. I did not test multiple inputs for address because there is
no requirements for address.
Specifically, in the test_update_user_profile.in file, on line 16 to line 28, I did output partitioning,
and also as much input as I can for possible problems. On line 30-39, I also did the same thing as above.
Line 36 and 38 are for boundary testing.
As of specific requirements, R3-1 is on line 14 of the .in file(The only options are those four),
I also tested an invalid input on line 54. R3-2 was tested on line 42-52,
R3-3 is on line 53(that is a valid US postal code), and finally R3-4 is tested on lines 30-39