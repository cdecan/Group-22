No explicit requirements have been defined for the user home page, so basic tests ensuring it links to the correct pages and functions properly as a menu were performed (all in the  `test_home_page.in` file)

Lines `1` - `8` are boilerplate code - creating a user so we may reach the user home page.

- **Rx-1: Create Listing Page must be reachable: Lines `9` - `12`**
	- Attempt to reach the "create listing" page (Option 1)
- **Rx-2: Update Listing Page must be reachable: Lines `13` - `14`**
	- Attempt to reach the "update listing" page (Option 2)
- **Rx-3: Update User Profile Page must be reachable: Lines `15` - `16`**
	- Attempt to reach the "update user profile" page (Option 3)
- **Rx-4: Menu must reject invalid inputs: Lines `17` - `21`**
	- Input Partition Testing
	- Test valid and various invalid inputs;
		- Valid input
		- Out-of-range number
		- Alphabetical character
		- Blank input
- **Rx-5: Must be able to Exit Menu: Lines `22`: `23`**
	- Attempt to exit / log out (Option 4)