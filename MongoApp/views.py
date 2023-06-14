from django.shortcuts import render
from MongoDBProject.settings import db
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated 
import json
from bson import json_util
print(db,"=============")

# products_col=db['products']
#  - Title (CharField)
#    - Description (TextField)
#    - Selling Price(DecimalField)
#    - Market Price (DecimalField)
#    - Category (CharField)
#    - Image(CharField)
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def addData(request):
    document=[{"Title":"Think and grow rich","Description":"This book gives you an idea of how to make money",
                              "Selling_Price":780.00,"Market_Price":520.00,"Category":"Psycology","image":"image"},
                              {"Title":"watch","Description":"watch","Selling_Price":1350.00,"Market_Price":800.00,"Category":"electonic","image":"image"},
                                {"Title":"Laptop","Description":"Hp Laptop with ryzen","Selling_Price":45000.00,"Market_Price":3200.00,"Category":"electonic","image":"image"}]
    products_col=db['products']
    data=products_col.insert_many(document)
    return JsonResponse({"status":"success","description":"created"})

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getRecords(request):
    title=request.GET.get("title")
    description=request.GET.get("description")
    category=request.GET.get("category")
    data=None
    if title:
        data=db['products'].find_one({"Title":title})
        print(data,"==data===")

        return JsonResponse({"status":"success","data":json.loads(json_util.dumps(data))})
       
    elif description:
        data=db['products'].find({"Description":description})
        return JsonResponse({"status":"success","data":json.loads(json_util.dumps(data))})


    elif category:
        data=db['products'].find({"Category":category})
        return JsonResponse({"status":"success","data":json.loads(json_util.dumps(data))})
    

    else:
        data=db['products'].find()
    
        print(data,"============data=======")

        documents = []
        # if len(data)>=1:
        for document in data:
            print(document,"=====document====")
        # Convert ObjectId fields to string representation
            document['_id'] = str(document['_id'])
            documents.append(document)



        return JsonResponse({"status":"success","data":documents})




    
