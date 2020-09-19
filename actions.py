from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json


class ActionValidateCity(Action):
    def name(self):
        return 'action_validateCity'
    
    def run(self, dispatcher, tracker, domain):
        locations = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune",
        "Agra","Ajmer","Aligarh","Allahabad","Amravati","Amritsar","Asansol","Aurangabad",
        "Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar",
        "Bikaner","Bokaro Steel City","Chandigarh","Coimbatore","Cuttack","Dehradun",
        "Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad",
        "Gorakhpur","Gulbarga","Guntur","Gurgaon","Guwahati",
        "Gwalior","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur","Jhansi","Jodhpur",
        "Kannur","Kanpur","Kakinada","Kochi","Kottayam","Kolhapur","Kollam","Kota","Kozhikode","Kurnool","Lucknow","Ludhiana",
        "Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut",
        "Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Palakkad","Patna","Pondicherry","Raipur","Rajkot",
        "Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri",
        "Solapur","Srinagar","Sultanpur","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tiruppur",
        "Ujjain","Vijayapura","Vadodara","Varanasi",
        "Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]
        
        cities_list_lower = [x.lower() for x in locations]
        loc = tracker.get_slot('location')
        
        if loc not in cities_list_lower:
            dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location?")
            return [SlotSet('location_match',"zero"),SlotSet('location',"null")]
        else:
            return [SlotSet('location_match',"one"),SlotSet('location',loc)]
            
class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_restaurant'
        
    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
        zomato = zomatopy.initialize_app(config)
        
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('price')
        
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        
        cuisines_dict={'american':1,'mexican':73,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
        rate_dict={'lesser than Rs. 300':1,'Rs. 300 to 700':2,'more than 700':3}
        budget_index = rate_dict.get(budget)
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
        d = json.loads(results)
        response=""
        count = 0
        
        if d['results_found'] == 0:
            response= "no results"
        else:
            for restaurant in d['restaurants']:
                price = restaurant['restaurant']['average_cost_for_two']
                currency = restaurant['restaurant']['currency']
                if(count<=5):
                    if(currency == 'Rs.'):
                        if(budget_index == 1):
                            # if(price <300):
                            response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with rating as : "+restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
                            count = count+1
                        if(budget_index == 2):
                           # if(price >=300 and price<=700):
                            response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with rating as : "+restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
                            count = count+1
                        if(budget_index == 3):
                           # if(price >700):
                            response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with rating as : "+restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
                            count = count+1
        
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]

class ActionSendEmail(Action):
    def name(self):
        return 'action_sendEmail'
  
    def run(self,dispatcher,tracker,domain):
        config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
        zomato = zomatopy.initialize_app(config)
        
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('price')
        
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        
        cuisines_dict={'american':1,'mexican':73,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
        rate_dict={'lesser than Rs. 300':1,'rs. 300 to 700':2,'more than 700':3}
        budget_index = rate_dict.get(budget)
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
        d = json.loads(results)
        response=""
        count = 0
        
        if d['results_found'] == 0:
            response= "no results"
        else:
            for restaurant in d['restaurants']:
                price = restaurant['restaurant']['average_cost_for_two']
                currency = restaurant['restaurant']['currency']
                if(count<=10):
                    if(currency == 'Rs.'):
                        if(budget_index == 1):
                            if(price <300):
                                response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with rating as : "+restaurant['restaurant']['user_rating']['aggregate_rating']
                                count = count+1
                        if(budget_index == 2):
                           if(price >=300 and price<=700):
                               response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with rating as : "+restaurant['restaurant']['user_rating']['aggregate_rating']
                               count = count+1
                        if(budget_index == 3):
                           if(price >700):
                               response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with rating as : "+restaurant['restaurant']['user_rating']['aggregate_rating']
                               count = count+1
        
        email_id = tracker.get_slot('email_id')
        
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "suraj0prakash@gmail.com"
        receiver_email = email_id
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Restaurant Bot : Query"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        part1 = MIMEText(response, "plain")
        message.attach(part1)
        
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, "Complex@26*")
            server.sendmail(sender_email, receiver_email, message.as_string())
    
from rasa_core_sdk.events import Restarted
class ActionResetSlots(Action):
     def name(self):
        return 'export'

     def run(self, dispatcher, tracker, domain):
        return[Restarted()]
    