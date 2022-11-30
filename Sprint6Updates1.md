# Update Report Made: Nov.29.2022
---

# Allen

### 1. What is the branch he/she worked on (has to be pushed to the repo)
test_booking_frontend

### 2. What is the progress so far
made the files and the function, waiting for frontend development to start writing any test cases


### 3. Any difficulties
N/A


### 4. What is the plan for the days before the deadline.
Write the test cases

# Connor

### 1. What is the branch he/she worked on (has to be pushed to the repo)

`booking_backend` `booking_backend_bugfix`

### 2. What is the progress so far

created and assigned cards on the scrumboard, created the book_listing function, made changes so that it fits the criteria

### 3. Any difficulties

Some of the requirements were misinterpreted and the booking had to be changed to fix them after we noticed

### 4. What is the plan for the days before the deadline.

wait for the other components to finish and then deploy it all with docker

# Haiden

### 1. What is the branch he/she worked on (has to be pushed to the repo)

`backend_testing_haiden`

Planned Branch:

`security_testing_haiden`

### 2. What is the progress so far

- Created cards on scrum board
- Created requirements
- Created backend test cases for the `book_listing()` function

**Requirements:**

- R1: A user can book a listing.
- R2: A user cannot book a listing for his/her listing.
- R3: A user cannot book a listing that costs more than his/her balance.
- R4: A user cannot book a listing that is already booked with the overlapped dates.
- R5: A booked listing will show up on the user's home page.
- R6: User id exists in the database
- R7: Listing id exists in the database
- R8: Price has to be of range [10, 10000].
- R9: Date must be after 2021-01-02 and before 2025-01-02
- R10: User balance is correctly updated upon successful booking

### 3. Any difficulties

Getting error `sqlite3.OperationalError: database is locked` when running pytest.

Error occurs when attempting to create a second booking.

### 4. What is the plan for the days before the deadline.

- Fix error with backend testing
- Create security test cases
- Attend second scrum meeting

# Kennan

### 1. What is the branch he/she worked on (has to be pushed to the repo)
`Make_Booking_Page`

### 2. What is the progress so far
- Created and assigned cards on scrum board
- Make booking page has been created and is accessible through the user home page. Adjusted frontend tests to pass.

### 3. Any difficulties
- An exception is thrown when attempting to book a listing - a bug fix for the backend is in the works (`booking_backend_bugfix` branch).

### 4. What is the plan for the days before the deadline.
1. Pull bugfixes from main once they're merged
2. Update existing code as nessesary until booking page works
3. Create PR for `Make_Booking_Page` branch
4. Start work on "home page displays current bookings" feature (#105)
5. Review any other PRs

![image](Sprint6ScrumBoard1.png)
