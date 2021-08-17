from django.shortcuts import render
from django.http import request, HttpResponse

from .models import Property

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create your views here.

# def index(request):
    
def scrappe_view(request):
    url = 'https://www.crexi.com/properties'

    driver = webdriver.Chrome(ChromeDriverManager().install())

    # driver.maximize_window()

    driver.get(url)

    properties = driver.find_elements_by_class_name('property-tile')

    for property in properties:
        price = property.find_element_by_class_name('property-price').text
        name = property.find_element_by_class_name('property-name').text
        details = property.find_element_by_class_name('property-details').text
        address = property.find_element_by_class_name('property-address').text
        logo = property.find_element_by_class_name('ng-star-inserted ').text
        
        property_object = Property()
        property_object.name=name
        property_object.price=price
        property_object.details=details
        property_object.address=address
        property_object.logo=logo
        property_object.save()
        
        # return HttpResponse("saved")
        print(price, name, details, address, logo)
        
        
if __name__ == '__main__':
    scrappe_view()
    
# 7Rw6eLLrjTbZUDGdjH6a

