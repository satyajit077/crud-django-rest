from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework import generics
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.
# class Home(APIView):
#     def get(self,request):
#         student_objs = Student.objects.all()
#         serializer= StudentSerializer(student_objs , many = True)
#         # return Response({'status':200 ,'message':"Hello This is Satyajit"})
#         return Response({'status':200 , 'Students Details':serializer.data})

# class Home(APIView):
#     # queryset = Student.objects.all()
#     # serializer_class = StudentSerializer
    
#     def get(self,request):
#          query_param = self.request.get('id')
#          data = request.query_params
#          #id = data.get("id", None)
#          student = Student.objects.filter(id=query_param) # Replace 'param_name' with the actual name of your field
#          return Response({'status':200 , 'StudentDetails':student})
#         # return student

    
# class StudentDetailView(generics.RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = 'id'




# class StudentView(generics.RetrieveAPIView,generics.UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get_object(self):
        
        
#         id = self.request.query_params.get('id', None)
#         if id is not None:
#             try:
#                 obj = Student.objects.get(id=id)
#                 return obj
            
#             except Student.DoesNotExist :
#                 raise NotFound('This Id Does not Exist,Please Enter the Valid Id to get Your Information.')
#         else:
#             student_objs = Student.objects.all()
#             serializer= StudentSerializer(student_objs , many = True)
#             return Response({'status':200 , 'Students Details':serializer.data})

            
            # raise NotFound('Id Query Parameter is Required')
            # return None
            # name = self.request.query_params.get('name', None)
            # if name is not None:
            #     obj = Student.objects.get(name=name)
            #     # obj = get_object_or_404(Student,name=name)
            #     return obj
            # else:
            #     raise NotFound('Id Or Name Query Parameter Is Required to Fetch the Student Data.')
            
            # ================================================================================================================#

class StudentView(APIView):
    def get(self, request):
        id = request.query_params.get('id',None)
        if id is not None:
            try:
                queryset = Student.objects.get(id=id)
                serializer = StudentSerializer(queryset)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'message': f'Student with id {id} does not exist. Please enter a valid id.'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=500)
                
        else:
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many=True)
            return Response(serializer.data)
            
        
            
    
  
    
       
    def post(self,request):
        # data = request.data
        # print(data)
        serializer = StudentSerializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors, 'message':"Something Went Wrong..."})

        serializer.save()
        return Response({'status' : 200 ,'StudentDetails' :serializer.data ,'message':"Student data Saved." })



    # def put(self, request):
    #     try: 
    #         # data = request.request.data
    #         # id = data.get("id", None)
            
    #         student_obj = Student.objects.get(id = request.data['id'])
                
    #         # serializer = StudentSerializer(partial=False)
                 
    #         # student_obj = Student.objects.get(id)
                
    #         serializer = StudentSerializer(student_obj,data = request.data,partial=False)
                
    #         if not serializer.is_valid():
    #             print(serializer.errors)
    #             return Response({'status':403,'errors':serializer.errors,'message':'Something Went Wrong...'})
        
    #         serializer.save()
    #         return Response({'status':200 ,'StudentDetails':serializer.data,'message':"Student data Update Successfully"})
            
    #     except Exception as e:
    #             print(e)
    #             return Response({'status':403,'message':' Invalid Id.'})
    
    
    
    def put(self, request):
        id = self.request.query_params.get('id', None)
        if not id:
            return Response({'error': 'ID not provided in query parameter'}, status=400)

        try:
            obj = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Data not found'}, status=404)

        serializer = StudentSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Data updated successfully'})
        else:
            return Response(serializer.errors, status=400)
    







                
    def patch (self,request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_obj,data = request.data,partial=True)
                
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':'Something Went Wrong...'})
        
            serializer.save()
            return Response({'status':200 ,'StudentDetails':serializer.data,'message':"Student data Update Successfully"})
            
        except Exception as e:
                print(e)
                return Response({'status':403,'message':' Invalid Id.'})



    # def delete(self,request):
    #         try:
    #             # id = request.GET.get('id')
    #             # student_obj = Student.objects.get(id = id)
    #             student_obj = Student.objects.get(id = request.data['id'])
    #             student_obj.delete()
    #             return Response({'status':200 , 'message':' Student Data Deleted'})
    #         except Exception as e:
    #             print(e)
    #             return Response({'status':403 , 'message':'invalid id '})
    
    
    
    def delete(self, request):
        id = request.query_params.get('id', None)
    
        if id is None:
            return Response({'error': 'ID is required in the Query parameter to delete the data'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            obj = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({'success': 'Student Data Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

            


