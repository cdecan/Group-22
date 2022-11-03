All requirements are tested through a single `test_create_listing.in` file.

Lines `1` to `7` are boilerplate code - creating a user so we may create listings under their name.

File is very messy and line numbers are non-final.

- R1:
- R2: Input boundary testing, lines [] - []
	- Title is max 80 characters; test 80 & 81 characters long. Expect 80 to pass, 81 to fail.
- R3: Output parition testing, lines [] - []
	- two output options; success or failure. test with a description of valid length (20-2000 chars), and then a description of invalid length (<20 chars) to yield both outputs.
- R4:
- R5: Input boundary testing [] - []
	- Price must be within range [10,10000]. Test 9, 10, 10000, 10001. Expect 9 & 10001 to fail, 10 & 10000 to pass
- R6:
- R7:
- R8:

github pls

2
createlistingtest@email.com
createlistingtest
ValidPassword#1
ValidPassword#1
1
createlistingtest@email.com
ValidPassword#1
1
80808080808080808080808080808080808080808080808080808080808080808080808080808080
descriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescription
100
1
818181818181818181818181818181818181818181818181818181818181818181818181818181818
descriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescription
100
1
ThisIsAValidAndCoolTitle
ThisDescriptionIsLongEnough
100
1
ThisIsStillAValidTitle
NotLongEnough
100
1
ThisIsAValidTitlePrice1
descriptiondescriptiondescription
9
ThisIsAValidTitlePrice2
descriptiondescriptiondescription
10
ThisIsAValidTitlePrice3
descriptiondescriptiondescription
10000
ThisIsAValidTitlePrice4
descriptiondescriptiondescription
10001
4
3