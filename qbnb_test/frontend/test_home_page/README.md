No explicit requirements have been defined for the user home page, so basic tests ensuring it links to the correct pages and functions properly as a menu were performed (all in the  `test_home_page.in` file)

Lines `1` - `8` are boilerplate code - creating a user so we may reach the user home page.

- **Test Create Listing Link: `9` - `12`**
	- Attempt to reach the "create listing" page (Option 1)
- **Test Update Listing Link: `13` - `14`**
	- Attempt to reach the "update listing" page (Option 2)
- **Test Update Profile Link: `15` - `16`**
	- Attempt to reach the "update user profile" page (Option 3)
- **Test Invalid Inputs: `17` - `19`**
	- Attempt several invalid inputs (menu should ignore them)
		- Out-of-range number
		- Alphabetical character
		- Blank input
- **Test Exit - `20`: `21`**
	- Attempt to exit / log out (Option 4)