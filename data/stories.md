## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
	- slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- utter_goodbye
	
## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- utter_goodbye

## Generated Story 2732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "kanpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- utter_goodbye

## Generated Story 3732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- utter_goodbye

## Generated Story 4732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- utter_goodbye

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- utter_goodbye

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export
<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and email_address -->

<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and no email_address -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and no email_address -->





<!-- stories starting with location restaurant_search with complete restaurant_searchation and sent email_address -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
     - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "uyhbkjn@gasf.com"}
    - slot{"email_id": "uyhbkjn@gasf.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Amritsar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Amritsar"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "anurag@asdasd.com"}
    - slot{"email_id": "anurag@asdasd.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Nagpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nagpur"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "699"}
    - slot{"price": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "701"}
    - slot{"price": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"price": "701"}
    - slot{"price": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export
<!-- stories starting with location restaurant_search with complete restaurant_searchation and sent email_address -->


<!-- stories starting with location restaurant_search with complete restaurant_searchation and no sent email_address -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Amritsar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Amritsar"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nagpur"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "699"}
    - slot{"price": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "701"}
    - slot{"price": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"price": "701"}
    - slot{"price": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export
	
<!-- stories starting with location restaurant_search with complete restaurant_searchation and no sent email_address -->


<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and sent email_address -->

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "noida"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_send_email
* send_email{"email_id": "zjiom@gasf.co.in"}
    - slot{"email_id": "zjiom@gasf.co.in"}
    - action_sendEmail
    - utter_email_sent
	- export

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Surat"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Surat"}
    - utter_ask_send_email
* send_email{"email_id": "asdsdad@gasf.com"}
    - slot{"email_id": "asdsdad@gasf.com"}
    - action_sendEmail
    - utter_email_sent
	- export
<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and sent email_address -->

<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and no sent email_address -->

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- export

## Generated Story -277470545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- export
	- export

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* goodbye
    - utter_goodbye
	- export

<!-- ------------------------------------------------------------------------------------------------------------------------------------------ -->
## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
	- slot{"location": "null"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - export

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - export


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
	- slot{"location": "null"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - export


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
	- slot{"location": "null"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - export


## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "uyhbkjn@gasf.com"}
    - slot{"email_id": "uyhbkjn@gasf.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "uyhbkjn@gasf.com"}
    - slot{"email_id": "uyhbkjn@gasf.com"}
    - action_sendEmail
    - utter_email_sent
    - export


## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Nashik"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_send_email
* send_email{"email_id": "asdsdad@gasf.com"}
    - slot{"email_id": "asdsdad@gasf.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Nashik"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_send_email
* send_email{"email_id": "asdsdad@gasf.com"}
    - slot{"email_id": "asdsdad@gasf.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Patna"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Patna"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - export

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - export


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - export


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - export


## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "uyhbkjn@gasf.com"}
    - slot{"email_id": "uyhbkjn@gasf.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "uyhbkjn@gasf.com"}
    - slot{"email_id": "uyhbkjn@gasf.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validateCity
    - slot{"location_match": "zero"}
	- slot{"location": "null"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "299"}
    - slot{"price": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* affirm
    - utter_ask_email_address
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

<!-- condition checkpoints -->

<!-- all the restaurant_searchation in one go -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "299"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

<!-- all restaurant_searchation in one go. -->



<!-- starting with price and location -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"price": "2000"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

<!-- starting with cuisine and price -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validateCity
    - slot{"location_match": "one"}
	- slot{"location": "delhi"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_send_email
* send_email{"email_id": "suraj0prakash@gmail.com"}
    - slot{"email_id": "suraj0prakash@gmail.com"}
    - action_sendEmail
    - utter_email_sent
    - export