class Star_Cinema:
    __hall_list = []
    
    def entry_hall(self):
         Star_Cinema.__hall_list.append(self)
        
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_lists = []
        self.rows = rows
        self.cols = cols
        self.__hall_no = hall_no
        
        Star_Cinema.entry_hall(self)
    
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_lists.append(show_info)
        
        seats = [[0 for _ in range(self.cols)] for _ in range(self.rows)]      
        self.__seats[id] = seats
         
    def book_seats(self, id, available_seats):
        if id not in self.seats:
            print("Invalid ID")
            return

        for seat in available_seats:
            row, col = seat
            if (row, col) not in self.__seats[id]:
                print(f"Seat ({row}, {col}) is invalid.")
                
            elif self.__seats[id][(row, col)] == 1:
                print(f"Seat ({row}, {col}) is already booked.")
                
            else:
                print(f"Seat ({row}, {col}) has been successfully booked.")
                
    def view_show_list(self):
        print("List of the shows: ")
        if not self.__show_lists:
            print("No shows available.")
            return
        
        for show in self.__show_lists:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid Show_Id")
            return
        
        show_seats = self.__seats[show_id]
        print(f"Available seats for show ID {show_id}:")
        
        for row in range(self.rows):
            for col in range(self.cols):
                if show_seats[row][col] == 0:
                    seat_status = 'Available'
                else:
                    seat_status = 'Booked'
        
        print(f"Seat ({row}, {col}): {seat_status}")
    
hall1 = Hall(5, 5, "H1")
hall1.entry_show("S1", "Movie 1", "12:00 PM")
hall1.entry_show("S2", "Movie 2", "03:00 PM")

while True:
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    
    option = int(input("Enter Option: "))
    
    if option == 1:
       hall1.view_show_list()
        
    elif option == 2:
        show_id = input("Enter Show Id: ")
        hall1.view_available_seats(show_id)
        
    elif option == 3:
        show_id = input("Enter Show Id: ")
        num_of_seats = int(input("Enter number of seats to book: "))
        seats_to_book = []
        
        for _ in range(num_of_seats):
            row = int(input("Enter row number: "))
            col = int(input("Enter col number: "))
            seats_to_book.append(row, col)
        
        hall1.book_seats(show_id, seats_to_book)
        
    elif option == 4:
        print("Exit")
        
    else:
        print("Invalid option")
