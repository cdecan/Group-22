All requirements are tested through a single `test_create_listing.in` file.

Lines `1` - `8` are boilerplate code - creating a user so we may create listings under their name.

- **R4-1: Lines `61` - `80`**
	- Input Partition Testing
	- Partitions for Title:
		- Alphanumeric-Only (`TestTitle1`)
		- Non-Alphanumeric (`TestTitle2!`)
		- Space in Middle (`Test Title 3`)
		- Space as Prefix (` TestTitle4`)
		- Space as Suffix (`TestTitle5 `)
- **R4-2: Lines `9` - `16`**
	- Input Boundary Testing
	- Title is max 80 characters; test 80 & 81 characters long. Expect 80 to pass, 81 to fail.
- **R4-3: Lines `17` - `24`**
	- Output Parition Testing
	- Output Partitions: Success, Failure.
	- Test with description of valid length (20-2000 chars), then with description of invalid length (<20 chars).
- **R4-4: Lines `41` - `52`**
	- Input Partition Testing
	- Partitions for Title:
		- Description longer than Title
		- Description same length as Title
		- Description smaller than Title
- **R4-5: Lines `25` - `40`**
	- Input Boundary Testing
	- Price must be within range [10,10000]. Test 9, 10, 10000, 10001. Expect 9 & 10001 to fail, 10 & 10000 to pass
- **R4-6: (Not possible to test through frontend)**
	- Tested using direct back-end access (see `frontend/test_create_listing.py`)
	- Ensure that date upon creation is within allowable range
- **R4-7: (Not possible to test through frontend)**
	- Tested using direct back-end access (see `frontend/test_create_listing.py`)
	- Ensure that owner_email is defined and valid upon creation
- **R4-8:  Lines `53` - `60`**
	- Output Parition Testing
	- Output Partitions: Success, Failure.
	- Attempt to create two listing with the same title; first should pass, second should fail.