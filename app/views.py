from django.contrib.auth import get_user_model
from rest_framework import viewsets,status,serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import App,Plan
from rest_framework.permissions import IsAuthenticated
from app.serializers import *



@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_apps': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/app/pk/delete'
    }

    return Response(api_urls)


from app.permissions import IsOwnerOfObject


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_app(request):

    app = AppSerializer(data=request.data)

    # validating for already existing data
    if App.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if app.is_valid():
        app.save()
        return Response(app.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_apps(request):
    app = App.objects.all()
    serializer = AppSerializer(app, many=True)
    return Response(serializer.data)




from rest_framework.exceptions import NotFound




@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@permission_classes([IsOwnerOfObject])
def app_detail(request, pk):
    user = request.user
    """
    Retrieve, update or delete a code app.
    """
    try:
        app = user.app_set.get(pk=pk)
    except App.DoesNotExist:
        raise NotFound("You are not the owner of the app or 404 ")

        # return Response(eror={"Failure": "error"} ,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppSerializer(app)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = AppSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PlanViewSet(request):

    plan = PlanSerializer(data=request.data)

    if plan.is_valid():
        plan.save()
        return Response(plan.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_plans(request):
    plan = Plan.objects.all()
    serializer = PlanSerializer(plan, many=True)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_my_plans(request):
    user = request.user
    plan = Plan.objects.filter(user=user)
    serializer = PlanSerializer(plan, many=True)
    return Response(serializer.data)



@api_view(['GET', 'PUT',])
@permission_classes([IsAuthenticated])
def view_plan_detail(request, pk):
    user = request.user
    """
    Retrieve, update or delete a code app.
    """
    try:
        plan = user.plan_set.get(pk=pk)
    except Plan.DoesNotExist:
        raise NotFound("You are not the owner of the plan or 404 ")

        # return Response(eror={"Failure": "error"} ,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT',])
@permission_classes([IsAuthenticated])
def view_subscription_detail(request, pk):
    user = request.user
    """
    Retrieve, update or delete a code app.
    """
    try:
        subscription = user.plan_set.get(pk=pk)
    except Plan.DoesNotExist:
        raise NotFound("You are not the owner of the subscription or 404 ")

        # return Response(eror={"Failure": "error"} ,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Subscription_detail_Serializer(subscription)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = Subscription_detail_Serializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

