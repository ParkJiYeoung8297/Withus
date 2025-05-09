from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse




class Sub(APIView):
    def get(self,request):
        print("겟으로 호출")
        return render(request,"Withus/main.html")
    # def post(self,request):
    #     profile=request.data.get('profile',None)
    #     #여기에 데이터베이스 확인하는 과정 있어야함
    #     print(profile)
    #     request.session['profile'] = profile  # profile 정보를 세션에 저장 (선택)
    #     return JsonResponse({'success': True})  # HTML 대신 JSON 응답
    
# class Home(APIView):
#     def get(self,request):
#         profile = request.session.get('profile', '익명')  # 세션에서 꺼내기
#         return render(request, "Withus/home.html", context={'profile': profile})
    

    