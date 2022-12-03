I have used **boundary testing, output partition and input partition**.

For boundary testing, I tested if a listing can be booked successfully when the user has just enough money, I did this
on **line 38** of the .in file.

Then I did output partitioning, I tested for every single possible output that could be given, which is only 3.

I also tested for input partitioning, there were only three different types: name exists, name does not exist but valid,
name does not exist and invalid.

As of specific requirements, **R1** is on **line 38** of the .in file, **R2** was tested on **line 32**,
**R3** is on **line 49**, I also tested if a listing costs more than current balance but less than initial balance on **
line 42**, and finally **R4** is tested on **lines 40 and line 57**.

The first 30ish lines are for initializing the database so there are valid listings and users in there.