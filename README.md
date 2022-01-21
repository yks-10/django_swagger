#TRAIN TICKET BOOKING

#Description
    Created an simple application view the availablity of trains.
    Booking the tickets for the passengers.
    Developed using Django Rest Framework.

#Database Schema 
    User:
        username
        email
        password
       

    Train:
        user
        train_name 
        train_no
        starting_at 
        ending_at 
        created_at 
        d_date 
        updated_at 

    Booking:
        user 
        train_name 
        passenger_name 
       

    
#Setup Instructions 
_setup_
1. Initial setup 
   1. Making a directory for project
   
           mkdir directory_name
   
2. Installation of python 
        downloading from the python.org website.

          sudo apt-get install python3 
                    
3. Django setup
   1. Need to install virtualenv
           
          pip install virtualenv 
      
   2. Django environmental setup 
             
          python -m venv environment_name
          environment_name/scripts/actiavte 
          pip install requirements.txt 
        
   3. Run Server     
      
      To run server 
   
          python manage.py runserver 
   
      To check the necessity of migrations 
         
          python manage.py makemigrations 
      
      To migrate the database   
   
          python manage.py migrate 
   
#API Explanation
   1. registration for the customers. 
         
          http://localhost:8000/api/v1/rest-auth/registration/  
   2. Log in for the customers 
         
          http://localhost:8000/api/v1/rest-auth/login/
          
   3. Password changing 
         
          http://localhost:8000/api/v1/rest-auth/password/change/
      
   4. to see the list of availability of train
      
          http://localhost:8000/api/v1/trains
   5. Viewing the  specific train 
            
          http://localhost:8000/api/v1/trains/1/
      
   6. booking the tickets 
      
          http://localhost:8000/api/v1/trains/1/book/                      
      
           
      

        